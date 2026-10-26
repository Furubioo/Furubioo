"""Faixa de tecnologias: ícones embutidos (sem serviço externo), organizados por grupo."""
import re
from pathlib import Path
from common import *
import content

ICONS = Path(__file__).resolve().parents[2] / 'assets' / 'icons'

def icon_inner(slug, n):
    s = (ICONS / f'{slug}.svg').read_text(encoding='utf-8')
    s = re.sub(r'^\s*<svg[^>]*>', '', s, count=1).replace('</svg>', '')
    for i in set(re.findall(r'id="([^"]+)"', s)):
        s = s.replace(f'id="{i}"', f'id="i{n}{i}"').replace(f'url(#{i})', f'url(#i{n}{i})')
    return s.strip()

def build(animated, mob):
    ctx = Ctx(animated)
    groups = list(content.TECNOLOGIAS.items())
    ts = 56 if not mob else 46
    n_icon = 0
    if not mob:
        W = 1000; pad = 48
        cells = [(pad, 92, groups[0]), (620, 92, groups[1]), (pad, 220, groups[2])]
        extra_xy = (620, 220); H = 350
    else:
        W = 400; pad = 24
        y = 108; cells = []
        for g in groups:
            cells.append((pad, y, g)); y += 28 + ts + 46
        extra_xy = (pad, y); H = y + 100
    defs = base_defs(W, H, rx=24 if not mob else 18)
    body = [backdrop(ctx, W, H, rx=24 if not mob else 18, aurA=(0.85, 0.2), aurB=(0.1, 0.9))]
    body.append(sans(pad, 44, 'TECNOLOGIAS', 12 if not mob else 11, C['mint'], weight='700', spacing=3 if not mob else 2))
    body.append(mono(pad if mob else W - pad, 44 if not mob else 66, 'presentes nos projetos e estudos · não é nível de domínio', 11, C['t3'], 'start' if mob else 'end'))
    k = 0
    for x0, y0, (gname, items) in cells:
        pitch = 88 if not mob else min(88, int(352 / len(items)))
        body.append(mono(x0, y0 - 14, gname, 11, C['t2'], spacing=1.6))
        for i, (slug, label, proof) in enumerate(items):
            x = x0 + i * pitch; y = y0
            icon = (f'<rect x="{x+2}" y="{y+5}" width="{ts}" height="{ts}" rx="{ts*0.23:.1f}" fill="#04090d" opacity="0.55"/>'
                    f'<svg x="{x}" y="{y}" width="{ts}" height="{ts}" viewBox="0 0 256 256">{icon_inner(slug, n_icon)}</svg>')
            n_icon += 1
            lines = label if isinstance(label, tuple) else (label,)
            for li, ln in enumerate(lines):
                icon += mono(x + ts / 2, y + ts + 18 + li * 13, ln, 11 if not mob else 10.5, C['t1'], 'middle')
            if ctx.animated:
                d = 0.3 + k * 0.06
                kt = d / (d + 0.55)
                icon = (f'<g opacity="1">{icon}<animate attributeName="opacity" values="0;0;1" keyTimes="0;{f(kt)};1" dur="{f(d+0.55)}s" begin="0s" fill="freeze"/>'
                        f'<animateTransform attributeName="transform" type="translate" values="0 8;0 8;0 0" keyTimes="0;{f(kt)};1" dur="{f(d+0.55)}s" begin="0s" fill="freeze"/></g>')
            body.append(icon); k += 1
    ex, ey = extra_xy
    body.append(mono(ex, ey - 14, 'TAMBÉM APARECEM', 11, C['t2'], spacing=1.6))
    line, ly = '', ey + 14
    for it in content.TAMBEM:
        if len(line) + len(it) + 3 > (34 if not mob else 40):
            body.append(mono(ex, ly, line.rstrip(' ·'), 12, C['t1'])); line = ''; ly += 22
        line += it + ' · '
    if line: body.append(mono(ex, ly, line.rstrip(' ·'), 12, C['t1']))
    title = 'Tecnologias presentes nos projetos e estudos'
    names = ', '.join((l if isinstance(l, str) else ' '.join(l)) for _, items in groups for _, l, _ in items)
    desc = f'Ícones das tecnologias presentes nos projetos e estudos, em três grupos: linguagens, frameworks e bibliotecas, ferramentas e plataformas. Itens: {names}. Também aparecem: {", ".join(content.TAMBEM)}. A lista descreve o contexto do código, não um nível de domínio.'
    return svg_doc(W, H, title, desc, defs, body)
