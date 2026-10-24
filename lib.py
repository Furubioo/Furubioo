from common import *
from widgets import reveal, layer_box, glow, card, token_motion

T = 30.0
ERR = lambda: f'<path d="M-5 -5L5 5M5 -5L-5 5" stroke="{C["amber"]}" stroke-width="2.8" stroke-linecap="round"/>'
REQ = lambda: f'<path d="M-6.5 -5.5H6.5L0 6Z" fill="{C["blue"]}"/>'
OK = lambda: f'<circle r="5.5" fill="none" stroke="{C["mint"]}" stroke-width="2.4"/>'

def build(animated=True, mob=False):
    ctx = Ctx(animated)
    if not mob:
        W = 1000; cw = 452; inner = 24; xT, xW = 34, 514; ty = 134; yW = ty
        tsz = 11
    else:
        W = 400; cw = 368; inner = 16; xT, xW = 16, 16; ty = 126; tsz = 10.5
    bw = cw - 2 * inner
    # ------------- layer specs (title, sub, sub2, h)
    T_layers = [('CinemaView · Terminal', 'entrada e apresentação', None, 46), ('CinemaController', 'coordena a compra', None, 46),
                ('Usuario → EstrategiaPreco', 'calcularPrecoFinal(precoBase)', None, 104), ('Sessao · Sala · Bilhete', 'valida e ocupa a cadeira', None, 46),
                ('PersistenciaArquivo', 'filmes.txt · usuarios.txt', None, 46)]
    W_layers = [('ProgramacaoPage', 'React · lista de sessões', None, 46), ('CompraPage', 'React · seleção de cadeira', None, 46), ('Axios · src/api/api.js', 'baseURL localhost:8080', None, 46),
                ('SessaoController', 'POST /sessoes/{id}/comprar', None, 46), ('SessaoRepository', 'Spring Data JPA', None, 46), ('Banco H2', 'cinemadb · cinema.backend', None, 46)]
    gap = 16; top = 84
    def ys(layers):
        y = top; out = []
        for L in layers:
            out.append(y); y += L[3] + gap
        return out, y - gap
    yT_list, endT = ys(T_layers); yW_list, endW = ys(W_layers)
    chT = endT + 52; chW = endW + 52
    if not mob:
        H = 134 + max(chT, chW) + 58; yT = ty; yW = ty
        ch = max(chT, chW); chT = chW = ch
    else:
        yT = ty; yW = ty + chT + 22
        H = yW + chW + 56
    defs = base_defs(W, H, rx=24 if not mob else 18)
    body = [backdrop(ctx, W, H, rx=24 if not mob else 18, aurA=(0.5, 0.2), aurB=(0.9, 0.95))]
    cxm = W / 2
    body.append(sans(cxm, 44 if not mob else 40, 'PROJETO ACADÊMICO · POO · UNICAP', 12 if not mob else 11, C['mint'], 'middle', '700', 3 if not mob else 2))
    body.append(sans(cxm, 84 if not mob else 76, 'Sistema de Cinema', 30 if not mob else 26, C['t0'], 'middle', '700'))
    body.append(sans(cxm, 109 if not mob else 98, 'Duas implementações · o caminho de uma compra de ingresso', 14 if not mob else 12.5, C['t1'], 'middle'))
    body.append(card(xT, yT, cw, chT, '01', 'Terminal · Java', 'cinema-console · MVC · persistência em arquivos', C['blue'], tsz))
    body.append(card(xW, yW, cw, chW, '02', 'Web · React + Vite · Spring Boot' if not mob else 'Web · React · Spring Boot', 'cinema-system · front e back separados', C['mint'], tsz))
    # ---------- terminal layers
    bx = xT + inner; cx = bx + bw / 2
    chip_pos = []
    for i, ((t_, s_, s2, h_), y_) in enumerate(zip(T_layers, yT_list)):
        yy = yT + y_
        if i == 2:
            mb = (f'<rect x="{bx}" y="{yy+5}" width="{bw}" height="{h_}" rx="11" fill="#050d12" opacity="0.6"/><rect x="{bx}" y="{yy}" width="{bw}" height="{h_}" rx="11" fill="#112733" stroke="#335767"/>'
                  + sans(bx + 16, yy + 20, t_, 14, '#eaf4f7', weight='700') + mono(bx + 16, yy + 36, s_, 10.5, C['t2']))
            names = [('PrecoComum', 'precoBase'), ('PrecoCritico', '0'), ('PrecoEstudante', 'precoBase / 2')]
            cwid = [len(n[0]) * 6.4 + 20 for n in names]; g = 8
            sx = bx + (bw - (sum(cwid) + 2 * g)) / 2
            for (n_, o_), w_ in zip(names, cwid):
                mb += f'<rect x="{f(sx)}" y="{yy+46}" width="{f(w_)}" height="24" rx="7" fill="#0c1f29" stroke="#2f5060"/>' + mono(sx + w_ / 2, yy + 62, n_, 10.5 if mob else 11, C['t1'], 'middle')
                chip_pos.append((sx, yy + 46, w_, 24, o_)); sx += w_ + g
            body.append(reveal(ctx, mb, 0.9, T))
        else:
            body.append(reveal(ctx, layer_box(bx, yy, bw, h_, t_, s_), 0.4 + 0.25 * i, T))
    for i in range(4):
        a_ = yT + yT_list[i] + T_layers[i][3]; b_ = yT + yT_list[i + 1]
        body.append(f'<path d="M{f(cx)} {f(a_)}V{f(b_)}" stroke="#3f7f95" stroke-width="2"/>')
    # ---------- web layers
    bx2 = xW + inner; cx2 = bx2 + bw / 2
    for i, ((t_, s_, s2, h_), y_) in enumerate(zip(W_layers, yW_list)):
        body.append(reveal(ctx, layer_box(bx2, yW + y_, bw, h_, t_, s_), 1.0 + 0.25 * i, T))
    for i in range(5):
        a_ = yW + yW_list[i] + 46; b_ = yW + yW_list[i + 1]
        for off in (-14, 14):
            body.append(f'<path d="M{f(cx2+off)} {f(a_)}V{f(b_)}" stroke="{"#3f7f95" if off < 0 else "#3b8f78"}" stroke-width="2"/>')
    # ---------- choreography
    PT = [3.4, 6.8, 10.2]          # terminal passes
    WT = {'ok': 14.6, 'err': 21.0}  # web trips
    # terminal glows & chips
    arrT = [0.0, 0.7, 1.4, 2.3, 3.0]
    for i, ((t_, s_, s2, h_), y_) in enumerate(zip(T_layers, yT_list)):
        body.append(glow(ctx, bx, yT + y_, bw, h_, [b + arrT[i] for b in PT], T, C['mint'] if i == 4 else C['blue']))
    for p, (x_, y_, w_, h_, o_) in enumerate(chip_pos):
        if ctx.animated:
            v, k = norm_track(pulse_pts([PT[p] + 1.5], 0.2, 1.1), T)
            body.append(f'<rect x="{f(x_)}" y="{f(y_)}" width="{f(w_)}" height="{h_}" rx="7" fill="{C["blue"]}" fill-opacity="0.24" stroke="{C["blue"]}" stroke-width="1.8" opacity="0">{anim(ctx, "opacity", v, k, T)}</rect>')
            # output tag under the chip
            vv, kk = norm_track([(0, 0), (PT[p] + 1.7, 0), (PT[p] + 2.0, 1), (PT[p] + 2.9, 1), (PT[p] + 3.2, 0)], T)
            body.append(f'<g opacity="0">{mono(x_ + w_ / 2, y_ + 38, "→ " + o_, 11, C["mint"], "middle", "700")}{anim(ctx, "opacity", vv, kk, T)}</g>')
        elif p == 2:
            body.append(f'<rect x="{f(x_)}" y="{f(y_)}" width="{f(w_)}" height="{h_}" rx="7" fill="{C["blue"]}" fill-opacity="0.24" stroke="{C["blue"]}" stroke-width="1.8"/>' + mono(x_ + w_ / 2, y_ + 38, '→ ' + o_, 11, C['mint'], 'middle', '700'))
    # web glows
    reqt = [0.0, 0.6, 1.2, 1.8, 2.4, 3.0]
    for k_, base in WT.items():
        for i, y_ in enumerate(yW_list):
            if k_ == 'ok':
                body.append(glow(ctx, bx2, yW + y_, bw, 46, [base + reqt[i]], T, C['blue']))
                body.append(glow(ctx, bx2, yW + y_, bw, 46, [base + 3.4 + (5 - i) * 0.6], T, C['mint']))
            else:
                if i <= 3:
                    body.append(glow(ctx, bx2, yW + y_, bw, 46, [base + reqt[i]], T, C['blue']))
                    body.append(glow(ctx, bx2, yW + y_, bw, 46, [base + 2.4 + (3 - i) * 0.6], T, C['amber']))
    # dim overlays
    def dim(x_, y_, w_, h_, pts):
        if not ctx.animated: return ''
        v, k = norm_track(pts, T)
        return f'<rect x="{x_}" y="{y_}" width="{w_}" height="{h_}" rx="18" fill="#06121a" opacity="0">{anim(ctx, "opacity", v, k, T)}</rect>'
    body.append(dim(xW, yW, cw, chW, [(0, 0), (2.8, 0), (3.4, 0.42), (13.8, 0.42), (14.4, 0), (T, 0)]))
    body.append(dim(xT, yT, cw, chT, [(0, 0), (13.8, 0), (14.4, 0.42), (26.0, 0.42), (26.6, 0), (T, 0)]))
    # tokens
    if ctx.animated:
        y0 = yT + yT_list[0] + 23; y1 = yT + yT_list[-1] + 23
        cT = [yT + y_ + h_ / 2 for (t_, s_, s2, h_), y_ in zip(T_layers, yT_list)]
        d = f'M{f(cx)},{f(cT[0])} L{f(cx)},{f(cT[-1])}'; Lt = cT[-1] - cT[0]; frT = [(c - cT[0]) / Lt for c in cT]
        for b in PT:
            stops = [(0, 0.0), (b, 0.0)] + [(b + arrT[i], frT[i]) for i in range(1, 5)] + [(b + 3.3, 1.0)]
            body.append(token_motion(ctx, d, T, stops, f'<circle r="6" fill="{C["blue"]}"/>', C['blue'], 'halo', [(b, b + 3.35)]))
        cW = [yW + y_ + 23 for y_ in yW_list]
        Lw = cW[-1] - cW[0]; frW = [(c - cW[0]) / Lw for c in cW]
        dd = f'M{f(cx2-14)},{f(cW[0])} L{f(cx2-14)},{f(cW[-1])}'; du = f'M{f(cx2+14)},{f(cW[0])} L{f(cx2+14)},{f(cW[-1])}'
        b = WT['ok']
        stops = [(0, 0.0), (b, 0.0)] + [(b + reqt[i], frW[i]) for i in range(1, 6)] + [(b + 3.2, 1.0)]
        body.append(token_motion(ctx, dd, T, stops, REQ(), C['blue'], 'halo', [(b, b + 3.25)]))
        stops = [(0, 1.0), (b + 3.4, 1.0)] + [(b + 3.4 + (5 - i) * 0.6, frW[i]) for i in range(4, -1, -1)] + [(b + 6.8, 0.0)]
        body.append(token_motion(ctx, du, T, stops, OK(), C['mint'], 'haloG', [(b + 3.4, b + 6.85)]))
        b = WT['err']
        stops = [(0, 0.0), (b, 0.0)] + [(b + reqt[i], frW[i]) for i in range(1, 4)] + [(b + 2.0, frW[3])]
        body.append(token_motion(ctx, dd, T, stops, REQ(), C['blue'], 'halo', [(b, b + 2.0)]))
        stops = [(0, frW[3]), (b + 2.4, frW[3])] + [(b + 2.4 + (3 - i) * 0.6, frW[i]) for i in range(2, -1, -1)] + [(b + 4.4, 0.0)]
        body.append(token_motion(ctx, du, T, stops, ERR(), C['amber'], 'halo', [(b + 2.4, b + 4.45)]))
        # error tag at the controller
        vv, kk = norm_track([(0, 0), (b + 1.8, 0), (b + 2.1, 1), (b + 3.6, 1), (b + 4.0, 0)], T)
        ty_c = yW + yW_list[3]
        body.append(f'<g opacity="0">{mono(bx2 + bw - 12, ty_c + 28, "400 · poltrona ocupada", 11, C["amber"], "end", "700")}{anim(ctx, "opacity", vv, kk, T)}</g>')
        vv, kk = norm_track([(0, 0), (WT['ok'] + 5.8, 0), (WT['ok'] + 6.1, 1), (WT['ok'] + 6.9, 1), (WT['ok'] + 7.2, 0)], T)
        body.append(f'<g opacity="0">{mono(bx2 + bw - 12, yW + yW_list[0] + 28, "200 · bilhete", 11, C["mint"], "end", "700")}{anim(ctx, "opacity", vv, kk, T)}</g>')
    else:
        cW = [yW + y_ + 23 for y_ in yW_list]
        body.append(f'<g transform="translate({f(cx2-14)} {f(cW[2]-8)})"><circle r="14" fill="url(#halo)"/>{REQ()}</g>')
        body.append(f'<g transform="translate({f(cx2+14)} {f(cW[3]+8)})"><circle r="14" fill="url(#haloG)"/>{OK()}</g>')
        body.append(f'<g transform="translate({f(cx2+14)} {f(cW[4]+8)})"><circle r="14" fill="url(#halo)"/>{ERR()}</g>')
    # legend + captions
    lg_y = yW + chW - 16
    # three-shape legend (shape + text, not only colour)
    lx = xW + inner
    body.append(f'<g transform="translate({lx+6} {lg_y-4})">{REQ()}</g>' + mono(lx + 20, lg_y, 'requisição', 11, C['t3']))
    body.append(f'<g transform="translate({lx+104} {lg_y-4})">{OK()}</g>' + mono(lx + 118, lg_y, 'resposta ok', 11, C['t3']))
    body.append(f'<g transform="translate({lx+212} {lg_y-4})">{ERR()}</g>' + mono(lx + 226, lg_y, 'erro', 11, C['t3']))
    cap_y = H - 22; capsize = 12 if not mob else 11
    caps = [('terminal · cada passagem usa a estratégia do tipo de usuário', 3.2, 13.8), ('web · compra aceita: a cadeira é gravada e o bilhete volta', 14.4, 20.6), ('web · compra recusada: a validação falha no controller e volta o erro', 21.0, 26.2)]
    if mob:
        caps = [('terminal · uma estratégia de preço por passagem', 3.2, 13.8), ('web · compra aceita: bilhete volta', 14.4, 20.6), ('web · poltrona ocupada: erro no controller', 21.0, 26.2)]
    if ctx.animated:
        for txt, a, b in caps:
            v, k = window_track([(a, b)], T)
            body.append(f'<g opacity="0">{mono(cxm, cap_y, txt, capsize, C["t1"], "middle")}{anim(ctx, "opacity", v, k, T, discrete=True)}</g>')
    else:
        body.append(mono(cxm, cap_y, 'estratégias de preço no terminal · compra aceita ou recusada na web', capsize if not mob else 11, C['t1'], 'middle'))
    title = 'Sistema de Cinema: duas implementações e o caminho de uma compra'
    if animated:
        desc = ('Dois cartões. Terminal em Java: CinemaView, CinemaController, Usuario que delega a EstrategiaPreco (PrecoComum devolve o preço-base, PrecoCritico devolve zero e PrecoEstudante devolve metade), Sessao, Sala e Bilhete, e PersistenciaArquivo em filmes.txt e usuarios.txt. '
                'Web: ProgramacaoPage, CompraPage, Axios, SessaoController, SessaoRepository com Spring Data JPA e banco H2. As camadas aparecem em sequência. Um ponto percorre o terminal três vezes, uma para cada estratégia. Depois, na web, um triângulo (requisição) desce até o banco e um anel (resposta) volta com o bilhete; '
                'em uma segunda compra, a poltrona está ocupada, a validação falha no controller e um X (erro) volta sem chegar ao banco.')
    else:
        desc = ('Dois cartões. Terminal em Java: CinemaView, CinemaController, Usuario com EstrategiaPreco (PrecoComum, PrecoCritico e PrecoEstudante), Sessao, Sala e Bilhete, e PersistenciaArquivo. '
                'Web: ProgramacaoPage, CompraPage, Axios, SessaoController, SessaoRepository e banco H2. Triângulo indica requisição, anel indica resposta ok e X indica erro.')
    return svg_doc(W, H, title, desc, defs, body)

