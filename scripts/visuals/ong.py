from common import *

PG = dict(bg='#f5f2e9', hdr='#b9d3c6', ink='#27403a', sub='#4d6a62', card='#dce9e1', card2='#fffdf7', yel='#f2c744', line='#c9d8cf')
T = 27.0

def t(x, y, s, size=14, fill=None, w='400', anchor='start', mono_=False):
    return (mono if mono_ else sans)(x, y, s, size, fill or PG['ink'], anchor, w)

def sections(w, mob):
    """returns list of (name, height, svg-builder(items_time_fn)) ; builders take (rev) where rev(i, inner) wraps reveal."""
    S = []
    pad = 28 if not mob else 18
    def hero(rev):
        h = 250 if not mob else 270
        o = f'<rect width="{w}" height="{h}" fill="#e6efe9"/>'
        o += rev(0, t(pad, 80, 'Construindo juntos,', 34 if not mob else 25, w='700') + t(pad, 120 if not mob else 108, 'um mundo melhor', 34 if not mob else 25, PG['sub'], '700'))
        o += rev(1, t(pad, 160 if not mob else 140, 'Nossa missão é cuidar das pessoas, promovendo o bem-estar mental e emocional', 15 if not mob else 12.5, PG['sub']) if not mob else t(pad, 140, 'Nossa missão é cuidar das pessoas,', 12.5, PG['sub']) + t(pad, 158, 'promovendo o bem-estar mental e emocional', 12.5, PG['sub']))
        by = 190 if not mob else 190
        o += rev(2, f'<rect x="{pad}" y="{by}" width="92" height="36" rx="18" fill="{PG["yel"]}"/>' + t(pad + 46, by + 23, 'Apoie', 14, PG['ink'], '700', 'middle') +
                 f'<rect x="{pad+104}" y="{by}" width="116" height="36" rx="18" fill="none" stroke="{PG["ink"]}" stroke-opacity="0.45" stroke-width="1.4"/>' + t(pad + 162, by + 23, 'Saiba mais', 14, PG['ink'], '600', 'middle'))
        return o, h
    def saiba(rev):
        h = 230 if not mob else 330
        o = f'<rect width="{w}" height="{h}" fill="{PG["bg"]}"/>'
        qs = ['Quem somos?', 'O que fazemos?', 'Por que fazemos?']
        if not mob:
            cw_ = (w - 2 * pad - 2 * 18) / 3
            for i, q in enumerate(qs):
                x = pad + i * (cw_ + 18)
                o += rev(i, f'<rect x="{x}" y="46" width="{cw_}" height="130" rx="14" fill="{PG["card2"]}" stroke="{PG["line"]}"/>' + t(x + 20, 86, q, 18, w='700') + f'<rect x="{x+20}" y="104" width="{cw_-60}" height="8" rx="4" fill="{PG["line"]}"/><rect x="{x+20}" y="124" width="{cw_-90}" height="8" rx="4" fill="{PG["line"]}"/><rect x="{x+20}" y="144" width="{cw_-70}" height="8" rx="4" fill="{PG["line"]}"/>')
        else:
            for i, q in enumerate(qs):
                y = 28 + i * 98
                o += rev(i, f'<rect x="{pad}" y="{y}" width="{w-2*pad}" height="86" rx="12" fill="{PG["card2"]}" stroke="{PG["line"]}"/>' + t(pad + 16, y + 34, q, 16, w='700') + f'<rect x="{pad+16}" y="{y+48}" width="{w-2*pad-80}" height="7" rx="3.5" fill="{PG["line"]}"/><rect x="{pad+16}" y="{y+64}" width="{w-2*pad-120}" height="7" rx="3.5" fill="{PG["line"]}"/>')
        return o, h
    def serv(rev):
        h = 250 if not mob else 330
        o = f'<rect width="{w}" height="{h}" fill="#eef4f0"/>' + rev(0, t(pad, 50, 'Serviços oferecidos.', 22 if not mob else 19, w='700'))
        names = ['Saúde Mental e Bem-estar', 'Cultura e Arte', 'Ação Social', 'Educação e Prevenção']
        if not mob:
            cw_ = (w - 2 * pad - 3 * 14) / 4
            for i, n in enumerate(names):
                x = pad + i * (cw_ + 14)
                o += rev(i + 1, f'<rect x="{x}" y="76" width="{cw_}" height="130" rx="14" fill="{PG["card2"]}" stroke="{PG["line"]}"/><circle cx="{x+30}" cy="112" r="14" fill="{PG["hdr"]}"/>' + t(x + 18, 160, n, 14 if len(n) < 20 else 13, w='700'))
        else:
            cw_ = (w - 2 * pad - 12) / 2
            for i, n in enumerate(names):
                x = pad + (i % 2) * (cw_ + 12); y = 74 + (i // 2) * 124
                words = n.split(' ', 2) if len(n) > 14 else [n]
                lines = ['Saúde Mental e', 'Bem-estar'] if i == 0 else (['Educação e', 'Prevenção'] if i == 3 else [n])
                inner = f'<rect x="{x}" y="{y}" width="{cw_}" height="110" rx="12" fill="{PG["card2"]}" stroke="{PG["line"]}"/><circle cx="{x+24}" cy="{y+28}" r="12" fill="{PG["hdr"]}"/>'
                for li, ln in enumerate(lines): inner += t(x + 14, y + 70 + li * 17, ln, 13.5, w='700')
                o += rev(i + 1, inner)
        return o, h
    def gal(rev):
        h = 200 if not mob else 230
        o = f'<rect width="{w}" height="{h}" fill="{PG["bg"]}"/>' + rev(0, t(pad, 46, 'Nossa galeria', 22 if not mob else 19, w='700'))
        if not mob:
            iw = (w - 2 * pad - 4 * 12) / 5
            for i in range(5):
                x = pad + i * (iw + 12)
                o += rev(i + 1, f'<rect x="{x}" y="70" width="{iw}" height="100" rx="10" fill="{PG["hdr"] if i % 2 == 0 else PG["card"]}"/><path d="M{x+iw*0.2} 150L{x+iw*0.45} 110L{x+iw*0.65} 135L{x+iw*0.8} 120" stroke="{PG["sub"]}" stroke-opacity="0.5" stroke-width="2" fill="none"/>')
        else:
            iw = (w - 2 * pad - 2 * 8) / 3
            for i in range(5):
                x = pad + (i % 3) * (iw + 8); y = 66 + (i // 3) * 76
                o += rev(i + 1, f'<rect x="{x}" y="{y}" width="{iw}" height="68" rx="8" fill="{PG["hdr"] if i % 2 == 0 else PG["card"]}"/>')
        return o, h
    def vol(rev):
        h = 250 if not mob else 300
        o = f'<rect width="{w}" height="{h}" fill="#eef4f0"/>'
        o += rev(0, t(pad, 46, 'Junte-se a nós e faça a diferença,', 20 if not mob else 15, w='700') + t(pad, 72 if not mob else 66, 'venha ser voluntario.', 20 if not mob else 15, w='700'))
        fx = pad; fw = (w - 2 * pad)
        labs = ['Nome completo', 'Email', 'Número de telefone', 'Mensagem']
        y = 96 if not mob else 86
        for i, lb in enumerate(labs):
            hh = 30 if i < 3 else 30
            o += rev(i + 1, t(fx, y + 11, lb, 11.5, PG['sub']) + f'<rect x="{fx}" y="{y+16}" width="{fw if not mob else fw}" height="{hh-8}" rx="6" fill="{PG["card2"]}" stroke="{PG["line"]}"/>')
            y += 38 if not mob else 40
        o += rev(5, f'<rect x="{fx}" y="{y+2}" width="120" height="34" rx="17" fill="{PG["yel"]}"/>' + t(fx + 60, y + 24, 'Cadastre-se', 13.5, PG['ink'], '700', 'middle'))
        return o, h
    def dep(rev):
        h = 250 if not mob else 250
        o = f'<rect width="{w}" height="{h}" fill="{PG["bg"]}"/>' + rev(0, t(pad, 46, 'Veja nossos depoimentos', 22 if not mob else 18, w='700'))
        cwd = (w - 2 * pad - 2 * 16) / 3 if not mob else (w - 2 * pad)
        for i in range(3):
            x = pad + i * (cwd + 16) if not mob else pad
            if mob and i > 0: continue
            o += rev(i + 1, f'<rect x="{x}" y="72" width="{cwd}" height="130" rx="14" fill="{PG["card2"]}" stroke="{PG["line"]}"/><circle cx="{x+28}" cy="104" r="14" fill="{PG["hdr"]}"/><rect x="{x+54}" y="98" width="{cwd*0.4}" height="8" rx="4" fill="{PG["ink"]}" fill-opacity="0.5"/><rect x="{x+20}" y="132" width="{cwd-40}" height="7" rx="3.5" fill="{PG["line"]}"/><rect x="{x+20}" y="150" width="{cwd-60}" height="7" rx="3.5" fill="{PG["line"]}"/><rect x="{x+20}" y="168" width="{cwd-80}" height="7" rx="3.5" fill="{PG["line"]}"/>')
        o += '<!--dots-->'
        return o, h
    def doe(rev):
        h = 170
        o = f'<rect width="{w}" height="{h}" fill="#f6e9b8"/>'
        o += rev(0, t(pad, 62, 'Doe esperança!', 26 if not mob else 21, w='700') + t(pad, 92, 'Sua doação ajuda a levar atenção psicológica, atividades' if not mob else 'Sua doação ajuda a levar atenção', 13.5 if not mob else 12, PG['sub']) + t(pad, 112, 'culturais e ações sociais para quem mais precisa.' if not mob else 'psicológica, atividades culturais e ações sociais.', 13.5 if not mob else 12, PG['sub']))
        return o, h
    return [('inicio', hero), ('saiba', saiba), ('servicos', serv), ('galeria', gal), ('voluntarie', vol), ('depoimentos', dep), ('ajudar', doe)]

def build(animated=True, mob=False):
    ctx = Ctx(animated)
    if not mob:
        W, VW, VH, H = 1000, 900, 340, 556; vx, vy = 50, 100; pw = 900
    else:
        W, VW, VH, H = 400, 360, 440, 690; vx, vy = 20, 92; pw = 360
    defs = base_defs(W, H, rx=24 if not mob else 18)
    body = [backdrop(ctx, W, H, rx=24 if not mob else 18, aurA=(0.8, 0.3), aurB=(0.1, 0.9))]
    cx = W / 2
    body.append(sans(cx, 42 if not mob else 38, 'SITE ONG PARTILHAR · ESTRUTURA DA PÁGINA', 12 if not mob else 11, C['mint'], 'middle', '700', 3 if not mob else 2))
    body.append(sans(cx, 76 if not mob else 68, 'Da apresentação à doação', 26 if not mob else 22, C['t0'], 'middle', '700'))
    # browser frame
    body.append(f'<rect x="{vx-6}" y="{vy-6+6}" width="{VW+12}" height="{VH+54}" rx="16" fill="#04090d" opacity="0.5"/>')
    body.append(f'<rect x="{vx-6}" y="{vy-6}" width="{VW+12}" height="{VH+54}" rx="16" fill="{C["panel"]}" stroke="{C["line"]}" stroke-width="1.3"/>')
    for i, c_ in enumerate(('#ff5f56', '#ffbd2e', '#27c93f')):
        body.append(f'<circle cx="{vx+14+i*18}" cy="{vy+8}" r="4.5" fill="{c_}" opacity="0.85"/>')
    body.append(mono(vx + VW - 8, vy + 12, 'HTML · CSS · JavaScript', 11, C['t3'], 'end'))
    sy = vy + 26
    body.append(f'<clipPath id="vp"><rect x="{vx}" y="{sy+46}" width="{VW}" height="{VH-46+22}" rx="8"/></clipPath>')
    secs = sections(pw, mob)
    heights = []; ys = []; acc = 0
    # first pass to get heights
    for name, fn in secs:
        _, h = fn(lambda i, inner: '')
        heights.append(h); ys.append(acc); acc += h
    total = acc; view_h = VH - 46 + 22
    maxs = max(0, total - view_h)
    stops = [min(y, maxs) for y in ys]
    hold = 2.6; move = 0.9
    t_stop = [0.8 + i * (hold + move) for i in range(len(secs))]
    ENDRESET = t_stop[-1] + hold + 0.2
    def mk_rev(sec_i):
        def rev(i, inner):
            if not ctx.animated: return f'<g>{inner}</g>'
            a = t_stop[sec_i] + (0.0 if sec_i == 0 else move * 0.55) + 0.12 * i
            v, k = norm_track([(0, 0), (a, 0), (a + 0.4, 1), (ENDRESET - 0.2, 1), (ENDRESET + 0.3, 0)], T)
            tv = ['0 10', '0 10', '0 0', '0 0', '0 0']; kt = [x for x in k]
            return (f'<g opacity="0">{inner}{anim(ctx, "opacity", v, k, T)}</g>')
        return rev
    # nav
    navy = sy
    body.append(f'<rect x="{vx}" y="{navy}" width="{VW}" height="46" fill="{PG["hdr"]}"/>')
    body.append(sans(vx + 20, navy + 29, 'Partilhar', 17, PG['ink'], weight='700'))
    items = [('Início', 0.5), ('Depoimentos', 0.62), ('Serviços', 0.74), ('Voluntarie-se', 0.85)] if not mob else []
    active_of = {0: 0, 1: 0, 2: 2, 3: 2, 4: 3, 5: 1, 6: 4}
    nav_pos = []
    if not mob:
        x = vx + 330
        for i, (lb, _) in enumerate(items):
            w_ = len(lb) * 8.4 + 8
            body.append(sans(x, navy + 29, lb, 14, PG['ink']))
            nav_pos.append((x, w_)); x += w_ + 26
        btn = (x - 6, 'Quero Ajudar')
        body.append(f'<rect x="{x-8}" y="{navy+8}" width="124" height="30" rx="15" fill="{PG["yel"]}"/>' + sans(x + 54, navy + 28, 'Quero Ajudar', 13.5, PG['ink'], 'middle', '700'))
        nav_pos.append((x - 8, 124))
        # underline for active section
        if ctx.animated:
            for ni, (nx, nw) in enumerate(nav_pos):
                wins = [(t_stop[si] - 0.2, t_stop[si] + hold + move - 0.2) for si in range(len(secs)) if active_of[si] == ni]
                v, k = window_track(wins, T)
                if ni < 4:
                    body.append(f'<g opacity="0"><rect x="{nx}" y="{navy+34}" width="{nw-8}" height="3" rx="1.5" fill="{PG["ink"]}"/>{anim(ctx, "opacity", v, k, T, discrete=True)}</g>')
                else:
                    body.append(f'<g opacity="0"><rect x="{nx-3}" y="{navy+5}" width="{nw+6}" height="36" rx="18" fill="none" stroke="{PG["ink"]}" stroke-width="2"/>{anim(ctx, "opacity", v, k, T, discrete=True)}</g>')
    else:
        body.append(f'<rect x="{vx+VW-48}" y="{navy+14}" width="26" height="3" rx="1.5" fill="{PG["ink"]}"/><rect x="{vx+VW-48}" y="{navy+22}" width="26" height="3" rx="1.5" fill="{PG["ink"]}"/><rect x="{vx+VW-48}" y="{navy+30}" width="26" height="3" rx="1.5" fill="{PG["ink"]}"/>')
    # scrolling page
    inner = ''
    for i, (name, fn) in enumerate(secs):
        sv, h = fn(mk_rev(i))
        inner += f'<g transform="translate(0 {ys[i]})">{sv}</g>'
    if ctx.animated:
        pts = [(0, '0 0')]
        for i in range(len(secs)):
            if i > 0: pts.append((t_stop[i] - move, f'0 {-stops[i-1]}'))
            pts.append((t_stop[i], f'0 {-stops[i]}'))
        pts.append((ENDRESET, f'0 {-stops[-1]}')); pts.append((ENDRESET + 0.7, '0 0'))
        v, k = norm_track(pts, T)
        sp = ';'.join([EASE if v[i] != v[i + 1] else '0 0 1 1' for i in range(len(v) - 1)])
        scroll = f'<animateTransform attributeName="transform" type="translate" values="{";".join(v)}" keyTimes="{";".join(f(x) for x in k)}" calcMode="spline" keySplines="{sp}" dur="{f(T)}s" repeatCount="indefinite"/>'
        body.append(f'<g clip-path="url(#vp)"><g transform="translate({vx} {sy+46})"><g>{inner}{scroll}</g></g></g>')
    else:
        scale = view_h / total
        body.append(f'<g clip-path="url(#vp)"><g transform="translate({vx + (VW - pw*scale)/2} {sy+46}) scale({f(scale)})">{inner}</g></g>')
    # progress / section chips under frame
    names = ['Início', 'Saiba mais', 'Serviços', 'Galeria', 'Voluntarie-se', 'Depoimentos', 'Doe esperança']
    cy = vy + VH + 54 + 10
    if not mob:
        x0 = vx
        wchip = (VW) / 7
        for i, n in enumerate(names):
            xx = x0 + i * wchip
            body.append(mono(xx + wchip / 2, cy + 16, f'{i+1} {n}', 11, C['t3'], 'middle'))
            if ctx.animated:
                v, k = window_track([(t_stop[i] - 0.3, t_stop[i] + hold + move - 0.3)], T)
                body.append(f'<g opacity="0"><rect x="{f(xx+6)}" y="{cy}" width="{f(wchip-12)}" height="3" rx="1.5" fill="{C["mint"]}"/>{anim(ctx, "opacity", v, k, T, discrete=True)}</g>')
        body.append(mono(cx, cy + 40, 'esquema do conteúdo encontrado no código; não é uma captura da página', 11, C['t3'], 'middle'))
    else:
        body.append(mono(cx, cy + 14, 'esquema do conteúdo do código · não é captura de tela', 10.5 if False else 11, C['t3'], 'middle'))
        if ctx.animated:
            for i, n in enumerate(names):
                v, k = window_track([(t_stop[i] - 0.3, t_stop[i] + hold + move - 0.3)], T)
                body.append(f'<g opacity="0">{mono(cx, cy + 36, f"{i+1}/7 · {n}", 11.5, C["mint"], "middle", "700")}{anim(ctx, "opacity", v, k, T, discrete=True)}</g>')
    title = 'Site ONG Partilhar: estrutura da página'
    if animated:
        desc = ('Esquema do conteúdo da página, não uma captura de tela. A janela rola em ordem pelas seções: apresentação (Construindo juntos, um mundo melhor, com os botões Apoie e Saiba mais), três perguntas (quem somos, o que fazemos, por que fazemos), '
                'quatro serviços (Saúde Mental e Bem-estar, Cultura e Arte, Ação Social, Educação e Prevenção), galeria com cinco imagens, formulário de voluntariado, três depoimentos e a chamada para doação. O menu destaca a seção atual. O site foi retirado do ar; o código permanece no repositório.')
    else:
        desc = ('Esquema do conteúdo da página, não uma captura de tela, mostrando todas as seções em ordem: apresentação, três perguntas, quatro serviços, galeria com cinco imagens, formulário de voluntariado, três depoimentos e chamada para doação. O site foi retirado do ar; o código permanece no repositório.')
    return svg_doc(W, H, title, desc, defs, body + (['<defs/>'] if False else []))

