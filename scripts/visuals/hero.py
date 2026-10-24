from common import *
from widgets import glow

T = 21.0
SC = [(0.0, 6.9), (7.0, 13.9), (14.0, 20.9)]
TABS = [('Desenvolvimento', 'Sistema de Cinema · Java, React, Spring'), ('Dados', 'pandas · scikit-learn · notebooks'), ('IA', 'interesse · primeiros estudos de classificação')]

def scene_wrap(ctx, inner, a, b, static_on=False):
    if not ctx.animated:
        return f'<g>{inner}</g>' if static_on else ''
    v, k = norm_track([(0, 0), (a, 0), (a + 0.45, 1), (b - 0.45, 1), (b, 0)], T)
    tv = ['0 8', '0 8', '0 0', '0 0', '0 -6']
    kt = k[:-1]; kt[-1] = 1.0 if len(kt) == 5 else kt[-1]
    tr = (f'<animateTransform attributeName="transform" type="translate" values="{";".join(tv)}" keyTimes="{";".join(f(x) for x in kt)}" dur="{f(T)}s" repeatCount="indefinite"/>')
    return f'<g opacity="0">{inner}{anim(ctx, "opacity", v, k, T)}{tr}</g>'

def box(x, y, w, h, title, sub, tsize=14, ssize=11, left=False):
    s = f'<rect x="{x}" y="{y+4}" width="{w}" height="{h}" rx="11" fill="#050d12" opacity="0.6"/>'
    s += f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="11" fill="#112733" stroke="#335767"/>'
    s += f'<path d="M{x+12} {y+0.8}H{x+w-12}" stroke="url(#rim)"/>'
    s += sans(x + (16 if left else w / 2), y + h / 2 - (2 if sub else -5), title, tsize, '#eaf4f7', 'start' if left else 'middle', '700')
    if sub: s += mono(x + w / 2, y + h / 2 + 15, sub, ssize, C['t2'], 'middle')
    return s

def token(ctx, d, stops, shape, window, glowid='halo', ease=True):
    if not ctx.animated: return ''
    mot = motion_stops(d, T, stops, ease=ease)
    v, k = window_track([window], T)
    return f'<g opacity="0"><circle r="14" fill="url(#{glowid})"/>{shape}{mot}{anim(ctx, "opacity", v, k, T, discrete=True)}</g>'

REQ = lambda: f'<path d="M-6.5 -5.5H6.5L0 6Z" fill="{C["blue"]}"/>'
RESP = lambda: f'<circle r="5.5" fill="none" stroke="{C["mint"]}" stroke-width="2.4"/>'


def chip(ctx, x, y, w, h, text, col, a, b=None, size=11.5):
    """pill that appears at a (s) and fades at the end of the scene"""
    inner = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{h/2}" fill="{col}" fill-opacity="0.14" stroke="{col}" stroke-width="1.4"/>' + mono(x + w / 2, y + h / 2 + 4, text, size, col, 'middle', '700')
    if not ctx.animated: return inner
    b = b if b else T - 0.5
    v, k = norm_track([(0, 0), (a, 0), (a + 0.3, 1), (b, 1), (b + 0.4, 0)], T)
    return f'<g opacity="0">{inner}{anim(ctx, "opacity", v, k, T)}</g>'

def scene_dev(ctx, s, x, y, w, vert, static=False):
    out = []
    names = [('CompraPage', 'React + Vite'), ('Axios', 'src/api/api.js'), ('SessaoController', 'Spring Boot'), ('SessaoRepository', 'Spring Data JPA'), ('H2', 'cinemadb')]
    out.append(mono(x, y + 4, 'SISTEMA DE CINEMA · COMPRA DE INGRESSO (WEB)' if not vert else 'COMPRA DE INGRESSO · WEB', 11, C['t3'], spacing=1.4))
    if not vert:
        bw, bh, gx = 164, 70, 40
        pos = [(x, y + 52), (x + bw + gx, y + 52), (x + 2 * (bw + gx), y + 52), (x + 2 * (bw + gx), y + 196), (x + bw + gx, y + 196)]
    else:
        bw, bh = min(300, w - 20), 40
        pos = [(x + (w - bw) / 2, y + 34 + i * 54) for i in range(5)]
    cs = [(px + bw / 2, py + bh / 2) for px, py in pos]
    for a_, b_ in zip(cs, cs[1:]):
        out.append(f'<path d="M{f(a_[0])} {f(a_[1])}L{f(b_[0])} {f(b_[1])}" stroke="#3f7f95" stroke-width="2"/>')
    d = path_points(cs); L = seg_lengths(cs); tot = L[-1]; fr = [l / tot for l in L]
    dur = tot / 230.0; t0 = s + 0.6; t1 = t0 + dur + 0.5
    out.append(token(ctx, d, [(0, 0), (t0, 0)] + [(t0 + fr[i] * dur, fr[i]) for i in range(1, 5)], REQ(), (t0, t0 + dur + 0.05)))
    out.append(token(ctx, d, [(0, 1), (t1, 1)] + [(t1 + (1 - fr[i]) * dur, fr[i]) for i in range(3, -1, -1)], RESP(), (t1, t1 + dur + 0.05), 'haloG'))
    for i, ((px, py), (n, sb)) in enumerate(zip(pos, names)):
        out.append(box(px, py, bw, bh, n, sb if not vert else None, 15 if not vert else 13, 11.5 if not vert else 11, left=vert))
        if vert: out.append(mono(px + bw - 12, py + bh / 2 + 4, sb, 10.5, C['t2'], 'end'))
        out.append(glow(ctx, px, py, bw, bh, [t0 + fr[i] * dur], T, C['blue'], 0.15, 0.7))
        out.append(glow(ctx, px, py, bw, bh, [t1 + (1 - fr[i]) * dur], T, C['mint'], 0.15, 0.7))
    if not vert:
        out.append(mono(x + bw + gx + bw / 2 + 22, y + 40, 'POST /sessoes/{id}/comprar', 11.5, C['blue'], 'middle'))
        out.append(chip(ctx, x, y + 142, 164, 26, 'linha · coluna · cupom', C['blue'], t0 + 0.2, t0 + dur - 0.2, 11))
        out.append(chip(ctx, x, y + 142, 164, 26, 'bilhete · 200 OK', C['mint'], t1 + dur - 0.2, None, 11.5) if ctx.animated else '')
        out.append(mono(x, y + 296, 'validarCompra → ocuparCadeira → save: a resposta só volta depois que a cadeira é gravada', 11, C['t1']))
        out.append(mono(x, y + 316, 'React + Vite · Axios · Spring Boot · Spring Data JPA · H2', 11, C['t3']))
    else:
        out.append(mono(x + w / 2, y + 34 + 5 * 54 - 2, 'POST /sessoes/{id}/comprar', 11, C['blue'], 'middle'))
        out.append(chip(ctx, x + 6, y + 34 + 5 * 54 + 12, 150, 24, 'linha · coluna · cupom', C['blue'], t0 + 0.2, t0 + dur - 0.2, 10.5))
        out.append(chip(ctx, x + w - 156, y + 34 + 5 * 54 + 12, 150, 24, 'bilhete · 200 OK', C['mint'], t1 + dur - 0.2, None, 11) if ctx.animated else '')
    if not ctx.animated:
        cx_, cy_ = cs[1]; out.append(f'<g transform="translate({f(cx_ + bw/2 + 18 if not vert else cx_)} {f(cy_ if not vert else cy_ - 30)})"><circle r="14" fill="url(#halo)"/>{REQ()}</g>')
        cx_, cy_ = cs[3]; out.append(f'<g transform="translate({f(cx_ - bw/2 - 18 if not vert else cx_)} {f(cy_ if not vert else cy_ + 30)})"><circle r="14" fill="url(#haloG)"/>{RESP()}</g>')
        out.append(chip(ctx, x if not vert else x + 6, y + 142 if not vert else y + 34 + 5 * 54 + 12, 164 if not vert else 150, 26 if not vert else 24, 'linha · coluna · cupom', C['blue'], 0, None, 11))
    return '\n'.join(out)

ROWS = [('engenheira', 3, 'boa', 0, 'pagamento_regular', 1), ('professora', 4, 'boa', 0, 'pagamento_regular', 1), ('comerciante', 2, 'media', 1, 'pagamento_atrasado', 0),
        ('analista', 0, 'boa', 0, 'pagamento_regular', 1), ('autonoma', 1, 'ruim', 2, 'pagamento_atrasado', 0)]
def scene_data(ctx, s, x, y, w, vert, static=False):
    out = [mono(x, y + 4, 'SCORE DE CRÉDITO · VARIÁVEIS CATEGÓRICAS → NÚMEROS' if not vert else 'SCORE DE CRÉDITO · CATEGORIAS', 11, C['t3'], spacing=1.4)]
    rh = 38 if not vert else 34
    cols = [('profissao', 112), ('mix_credito', 118), ('comportamento_pagamento', 190)] if not vert else [('profissao', 94), ('mix_credito', 92), ('comport._pagamento', 148)]
    tw = sum(c[1] for c in cols)
    tx, ty = x, y + 26
    out.append(f'<rect x="{tx}" y="{ty}" width="{tw}" height="{rh*6}" rx="12" fill="#0c1f29" stroke="#2f5060"/>')
    cx = tx
    for ci, (cn, cwid) in enumerate(cols):
        out.append(mono(cx + 12, ty + rh / 2 + 4, cn, 11, C['blue'], weight='700'))
        if ci: out.append(f'<path d="M{cx} {ty}V{ty+rh*6}" stroke="#1d3a47"/>')
        cx += cwid
    out.append(f'<path d="M{tx} {ty+rh}H{tx+tw}" stroke="#2f5060"/>')
    for i, r in enumerate(ROWS):
        cx = tx
        for ci, (cwid) in enumerate([c[1] for c in cols]):
            txtv, code = r[ci * 2], r[ci * 2 + 1]
            yy = ty + rh * (i + 1) + rh / 2 + 4
            t_flip = s + 0.9 + i * 0.28 + ci * 0.9
            a_ = mono(cx + 12, yy, txtv, 12 if not vert else 11.5, C['t1'])
            b_ = mono(cx + 12, yy, str(code), 14, C['mint'], weight='700')
            if ctx.animated:
                v, k = norm_track([(0, 1), (t_flip, 1), (t_flip + 0.22, 0), (T - 0.7, 0), (T - 0.5, 1)], T)
                v2, k2 = norm_track([(0, 0), (t_flip, 0), (t_flip + 0.22, 1), (T - 0.7, 1), (T - 0.5, 0)], T)
                out.append(f'<g opacity="1">{a_}{anim(ctx, "opacity", v, k, T)}</g><g opacity="0">{b_}{anim(ctx, "opacity", v2, k2, T)}</g>')
            else:
                out.append(b_)
            cx += cwid
        if i < 4: out.append(f'<path d="M{tx} {ty+rh*(i+2)}H{tx+tw}" stroke="#1d3a47" stroke-opacity="0.7"/>')
    out.append(mono(tx, ty + rh * 6 + 24, 'LabelEncoder · um código inteiro por categoria', 11.5, C['t1']))
    # split
    if not vert:
        sx0 = tx + tw + 34; sy0 = ty + 8
        out.append(mono(sx0, ty + 14, 'train_test_split', 12, C['blue'], weight='700'))
        out.append(mono(sx0, ty + 32, '75 % treino · 25 % teste', 10.5, C['t2']))
    else:
        sx0 = tx + 10; sy0 = ty + rh * 6 + 56
        out.append(mono(sx0, sy0 - 8, 'train_test_split · 75 % treino · 25 % teste', 11, C['blue'], weight='700'))
    bs, gap = 15, 5
    for n in range(20):
        r, c = divmod(n, 5 if not vert else 10)
        bx = sx0 + c * (bs + gap); by = sy0 + (44 if not vert else 6) + r * (bs + gap)
        test = n >= 15; col = C['amber'] if test else C['blue']
        move = ''
        if test and ctx.animated:
            a0 = (s + 4.6) / T; a1 = (s + 5.4) / T
            dxm = (bs + gap) * 0.9 if not vert else 0; dym = 0 if not vert else (bs + gap) * 0.9
            move = (f'<animateTransform attributeName="transform" type="translate" values="0 0;0 0;{f(dxm)} {f(dym)};{f(dxm)} {f(dym)};0 0" keyTimes="0;{f(a0)};{f(a1)};{f((s+6.6)/T)};1" dur="{f(T)}s" repeatCount="indefinite"/>')
        out.append(f'<rect x="{f(bx)}" y="{f(by)}" width="{bs}" height="{bs}" rx="3.5" fill="{col}" fill-opacity="0.55" stroke="{col}">{move}</rect>')
    ly = (sy0 + 44 + 4 * (bs + gap) + 14) if not vert else (sy0 + 6 + 2 * (bs + gap) + 12)
    out.append(f'<rect x="{sx0}" y="{ly-9}" width="10" height="10" rx="3" fill="{C["blue"]}" fill-opacity="0.6"/>' + mono(sx0 + 16, ly, 'treino', 11, C['t1']) + f'<rect x="{sx0+78}" y="{ly-9}" width="10" height="10" rx="3" fill="{C["amber"]}" fill-opacity="0.6"/>' + mono(sx0 + 94, ly, 'teste', 11, C['t1']))
    return '\n'.join(out)

def scene_ia(ctx, s, x, y, w, vert, static=False):
    out = [mono(x, y + 4, 'CLASSIFICAÇÃO · PREVER score_credito' if not vert else 'CLASSIFICAÇÃO · score_credito', 11, C['t3'], spacing=1.4)]
    steps = ['train_test_split', 'fit', 'predict', 'accuracy_score']
    sw = [128, 52, 78, 120] if not vert else [110, 40, 64, 104]
    gx = 10 if not vert else 6
    sxs = x; row = y + 24
    cxs = []
    for i, (st, wd) in enumerate(zip(steps, sw)):
        col = C['t1']
        out.append(f'<rect x="{f(sxs)}" y="{row}" width="{wd}" height="26" rx="13" fill="#0f2530" stroke="#335767"/>' + mono(sxs + wd / 2, row + 17, st, 11 if not vert else 10.5, C['t1'], 'middle'))
        out.append(glow(ctx, sxs, row, wd, 26, [s + 0.5 + i * 0.7], T, C['mint'], 0.15, 0.9, 13))
        if i < 3: out.append(mono(sxs + wd + gx / 2, row + 17, '›', 13, C['t3'], 'middle'))
        sxs += wd + gx
    track = (w - 190) if not vert else (w - 70)
    items = [('RandomForestClassifier', 0.82844, '0,83'), ('KNeighborsClassifier', 0.7462, '0,75')]
    for i, (nm, val, lab) in enumerate(items):
        yy = y + 84 + i * 78
        out.append(mono(x, yy, nm, 12, C['t1']))
        by = yy + 14
        out.append(f'<rect x="{x}" y="{by}" width="{f(track)}" height="20" rx="10" fill="#0c1f29" stroke="#2f5060"/>')
        wfull = track * val; col = C['mint'] if i == 0 else C['blue']
        if ctx.animated:
            a = s + 3.0 + i * 0.5
            v, k = norm_track([(0, 0), (a, 0), (a + 1.6, wfull), (T - 1.2, wfull), (T - 0.7, 0)], T)
            out.append(f'<rect x="{x}" y="{by}" width="0" height="20" rx="10" fill="{col}">{anim(ctx, "width", v, k, T)}</rect>')
            vv, kk = norm_track([(0, 0), (a + 1.3, 0), (a + 1.7, 1), (T - 1.2, 1), (T - 0.7, 0)], T)
            out.append(f'<g opacity="0">{mono(x + track + 14, by + 16, lab, 18, C["t0"], weight="700")}{anim(ctx, "opacity", vv, kk, T)}</g>')
        else:
            out.append(f'<rect x="{x}" y="{by}" width="{f(wfull)}" height="20" rx="10" fill="{col}"/>' + mono(x + track + 14, by + 16, lab, 18, C['t0'], weight='700'))
    out.append(mono(x, y + 84 + 2 * 78 - 20, 'acurácia no conjunto de teste, como registrada no notebook' if not vert else 'acurácia no conjunto de teste (notebook)', 10.5, C['t2']))
    py_ = y + 84 + 2 * 78 + 14
    out.append(mono(x, py_ + 16, 'RandomForest · 3 novos clientes →', 11.5, C['t1']))
    px = x + (250 if not vert else 0); pyy = py_ if not vert else py_ + 26
    for j, p in enumerate(['Poor', 'Poor', 'Good']):
        col = C['amber'] if p == 'Poor' else C['mint']
        inner = f'<rect x="{px + j*70}" y="{pyy}" width="60" height="26" rx="13" fill="{col}" fill-opacity="0.14" stroke="{col}"/>' + mono(px + j * 70 + 30, pyy + 17, p, 12, col, 'middle', '700')
        if ctx.animated:
            a = s + 5.0 + j * 0.45
            v, k = norm_track([(0, 0), (a, 0), (a + 0.3, 1), (T - 1.2, 1), (T - 0.7, 0)], T)
            out.append(f'<g opacity="0">{inner}{anim(ctx, "opacity", v, k, T)}</g>')
        else:
            out.append(inner)
    out.append(mono(x, py_ + (62 if not vert else 84), 'execução original do notebook (base de 100 mil linhas)' if not vert else 'execução original: base de 100 mil linhas', 10.5, C['t3']))
    return '\n'.join(out)

def build(animated=True, mob=False):
    ctx = Ctx(animated)
    if not mob:
        W, H = 1200, 500
        defs = base_defs(W, H)
        body = [backdrop(ctx, W, H), f'<rect x="1" y="1" width="{W-2}" height="{H-2}" rx="25" fill="none" stroke="url(#rim)" stroke-opacity="0.6"/>']
        body.append(sans(64, 76, 'CIÊNCIA DA COMPUTAÇÃO · UNICAP', 13, C['mint'], weight='700', spacing=3))
        body.append(sans(62, 150, 'Flávio Daniel', 64, C['t0'], weight='700', spacing=-1))
        body.append(sans(64, 190, 'Técnico em Redes de Computadores', 21, C['t1']))
        body.append(mono(64, 236, 'ESTUDOS EM FOCO', 11, C['t3'], spacing=2.4))
        tx, tw, th = 64, 372, 50
        tys = [252, 312, 372]
        px, py, pw, ph = 480, 40, 670, 410
    else:
        W, H = 400, 890
        defs = base_defs(W, H, rx=20, grid=22)
        body = [backdrop(ctx, W, H, rx=20, grid=22), f'<rect x="1" y="1" width="{W-2}" height="{H-2}" rx="19" fill="none" stroke="url(#rim)" stroke-opacity="0.6"/>']
        body.append(sans(24, 44, 'CIÊNCIA DA COMPUTAÇÃO · UNICAP', 11, C['mint'], weight='700', spacing=2))
        body.append(sans(23, 98, 'Flávio Daniel', 46, C['t0'], weight='700', spacing=-0.8))
        body.append(sans(24, 128, 'Técnico em Redes de Computadores', 16, C['t1']))
        body.append(mono(24, 168, 'ESTUDOS EM FOCO', 11, C['t3'], spacing=2.2))
        tx, tw, th = 24, 352, 46
        tys = [182, 236, 290]
        px, py, pw, ph = 8, 354, 384, 450
    # tabs
    for i, (t, sub) in enumerate(TABS):
        ty = tys[i]; a, b = SC[i]
        base = (f'<rect x="{tx}" y="{ty}" width="{tw}" height="{th}" rx="13" fill="#0f2530" stroke="#335767"/>'
                + sans(tx + 18, ty + 21, t, 16, C['t1'], weight='700') + mono(tx + 18, ty + 39 if not mob else ty + 37, sub, 10.5 if not mob else 10.5, C['t3']))
        body.append(base)
        if animated:
            v, k = norm_track([(0, 0), (a, 0), (a + 0.4, 1), (b - 0.3, 1), (b + 0.1, 0)], T)
            hl = (f'<rect x="{tx}" y="{ty}" width="{tw}" height="{th}" rx="13" fill="{C["mint"]}" fill-opacity="0.13" stroke="{C["mint"]}" stroke-width="1.7"/>'
                  f'<circle cx="{tx+tw-20}" cy="{ty+th/2}" r="4" fill="{C["mint"]}"/>')
            if i == 0:
                v, k = norm_track([(0, 1), (b - 0.3, 1), (b + 0.1, 0)], T)
            body.append(f'<g opacity="{v[0]}">{hl}{anim(ctx, "opacity", v, k, T)}</g>')
            # progress
            pv, pk = norm_track([(0, 0), (a, 0), (b - 0.1, tw - 36), (b, 0)], T)
            if i == 0: pv, pk = norm_track([(0, 0), (b - 0.1, tw - 36), (b, 0)], T)
            body.append(f'<rect x="{tx+18}" y="{ty+th-6}" width="0" height="2.5" rx="1.2" fill="{C["mint"]}" opacity="0.8">{anim(ctx, "width", pv, pk, T)}</rect>')
        elif i == 0:
            body.append(f'<rect x="{tx}" y="{ty}" width="{tw}" height="{th}" rx="13" fill="{C["mint"]}" fill-opacity="0.13" stroke="{C["mint"]}" stroke-width="1.7"/><circle cx="{tx+tw-20}" cy="{ty+th/2}" r="4" fill="{C["mint"]}"/>')
    # panel
    body.append(f'<rect x="{px+5}" y="{py+8}" width="{pw}" height="{ph}" rx="18" fill="#04090d" opacity="0.55"/>')
    body.append(f'<rect x="{px}" y="{py}" width="{pw}" height="{ph}" rx="18" fill="{C["panel"]}" fill-opacity="0.94" stroke="{C["line"]}" stroke-width="1.3"/>')
    body.append(f'<path d="M{px+24} {py+0.8}H{px+pw-24}" stroke="url(#rim)" stroke-width="1.2"/>')
    body.append(mono(px + 22, py + 30, 'IDEIAS EM CÓDIGO · 3 EIXOS', 11, C['t3'], spacing=2))
    # panel dots (progress)
    for i in range(3):
        a, b = SC[i]
        dx = px + pw - 24 - (2 - i) * 18; dy = py + 26
        body.append(f'<circle cx="{dx}" cy="{dy}" r="4" fill="#2f5060"/>')
        if animated:
            v, k = norm_track([(0, 0), (a, 0), (a + 0.4, 1), (b - 0.2, 1), (b + 0.1, 0)], T)
            if i == 0: v, k = norm_track([(0, 1), (b - 0.2, 1), (b + 0.1, 0)], T)
            body.append(f'<circle cx="{dx}" cy="{dy}" r="4" fill="{C["mint"]}" opacity="{v[0]}">{anim(ctx, "opacity", v, k, T)}</circle>')
        elif i == 0:
            body.append(f'<circle cx="{dx}" cy="{dy}" r="4" fill="{C["mint"]}"/>')
    ix, iy, iw = (px + 26, py + 52, pw - 52) if not mob else (px + 20, py + 52, pw - 40)
    vert = mob
    body.append(scene_wrap(ctx, scene_dev(ctx, SC[0][0], ix, iy, iw, vert), SC[0][0], SC[0][1], static_on=True))
    body.append(scene_wrap(ctx, scene_data(ctx, SC[1][0], ix, iy, iw, vert), SC[1][0], SC[1][1]))
    body.append(scene_wrap(ctx, scene_ia(ctx, SC[2][0], ix, iy, iw, vert), SC[2][0], SC[2][1]))
    # base ribbon: redes · sistemas · hardware
    by = H - 26
    x0, x1 = (64, W - 64)
    body.append(mono(x0, by - 12, 'BASE TÉCNICA', 11, C['t3'], spacing=2.2))
    body.append(f'<path d="M{x0} {by}H{x1}" stroke="#3f7f95" stroke-width="1.5" stroke-dasharray="2 6" stroke-opacity="0.7"/>')
    for lab, fx in (('redes', 0.18), ('sistemas', 0.5), ('hardware', 0.82)):
        cx = x0 + (x1 - x0) * fx
        body.append(f'<circle cx="{f(cx)}" cy="{by}" r="4.5" fill="#0f2530" stroke="{C["blue"]}" stroke-width="1.5"/>' + mono(cx + 10, by + 4, lab, 11, C['t1']))
    if animated:
        d = f'M{x0},{by} L{x1},{by}'
        body.append(f'<g opacity="1"><circle r="9" fill="url(#halo)"/><rect x="-8" y="-4" width="16" height="8" rx="3" fill="{C["blue"]}"/>'
                    + motion_stops(d, 9.0, [(0, 0), (9.0, 1)], ease=False).replace('calcMode="spline"', 'calcMode="linear"').replace('keySplines="0 0 1 1"', '') .replace(' keySplines=""', '') + '</g>')
    title = 'Flávio Daniel — Ciência da Computação na UNICAP e técnico em Redes de Computadores'
    if animated:
        desc = ('Banner com o nome, a formação e três eixos de estudo que se alternam: Desenvolvimento (a compra de ingresso do Sistema de Cinema, do React ao banco H2), Dados (codificação de variáveis categóricas e divisão treino/teste em um estudo de score de crédito) '
                'e IA (comparação de dois classificadores, Random Forest e KNN, e previsões para novos clientes). Uma faixa inferior indica a base técnica: redes, sistemas e hardware.')
    else:
        desc = ('Banner com o nome, a formação e três eixos de estudo: Desenvolvimento, Dados e IA. O painel mostra o caminho da compra de ingresso do Sistema de Cinema: CompraPage, Axios, SessaoController, SessaoRepository e H2. Uma faixa inferior indica a base técnica: redes, sistemas e hardware.')
    return svg_doc(W, H, title, desc, defs, body)

