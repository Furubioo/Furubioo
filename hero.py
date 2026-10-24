from common import *

T = 34.5
LEDC = {'vermelho': '#ff8f8f', 'amarelo': '#f0c674', 'azul': '#8fd3ff'}
SLOTS = {'A': (0.4, 11.2), 'B': (11.2, 22.2), 'C': (22.2, 34.0)}

def fx(ctx, inner, a, d=0.3):
    if not ctx.animated: return f'<g>{inner}</g>'
    v, k = norm_track([(0, 0), (a, 0), (a + d, 1), (T - 1.0, 1), (T - 0.5, 0)], T)
    return f'<g opacity="0">{inner}{anim(ctx, "opacity", v, k, T)}</g>'

def win(ctx, inner, wins, static=False):
    if not ctx.animated: return f'<g>{inner}</g>' if static else ''
    v, k = window_track(wins, T)
    return f'<g opacity="0">{inner}{anim(ctx, "opacity", v, k, T, discrete=True)}</g>'

def head(folder, title):
    return mono(28, 44, folder, 11, C['t3']) + sans(28, 70, title, 17, C['t0'], weight='700')

def scene_A(ctx, s, mob):
    out = [head('construcao-compiladores/', 'Lexer → parser')]
    out.append(mono(28, 104, 'examples/input.txt · int main() { … }', 11, C['t3']))
    runs = [
        dict(src='y = x + 5;', toks=[('y', 'ID'), ('=', 'ASSIGN'), ('x', 'ID'), ('+', 'PLUS'), ('5', 'INT_CONST'), (';', 'SEMICOLON')], ok=True, t0=s + 0.4),
        dict(src='y = x + 5   }', toks=[('y', 'ID'), ('=', 'ASSIGN'), ('x', 'ID'), ('+', 'PLUS'), ('5', 'INT_CONST'), ('}', 'RBRACE')], ok=False, t0=s + 5.3)]
    cw, gap = 40, 7
    for ri, r in enumerate(runs):
        t0 = r['t0']; dur = 4.3
        g = [mono(28, 128, r['src'], 17, '#d7e7ec')]
        for i, (tx, ty) in enumerate(r['toks']):
            x = 28 + i * (cw + gap)
            bad = (not r['ok']) and i == 5
            col = C['amber'] if bad else (C['mint'] if ty in ('ASSIGN', 'PLUS', 'SEMICOLON') else C['blue'] if ty in ('ID',) else C['amber'] if ty == 'INT_CONST' else C['t3'])
            col = {'ID': C['blue'], 'ASSIGN': C['mint'], 'PLUS': C['mint'], 'INT_CONST': C['amber'], 'SEMICOLON': C['t3'], 'RBRACE': C['t3']}[ty]
            chip = f'<rect x="{x}" y="142" width="{cw}" height="28" rx="8" fill="#0f2530" stroke="{col}" stroke-opacity="0.85"/>' + mono(x + cw / 2, 161, tx, 14, col, 'middle', '700')
            g.append(fx_run(ctx, chip, t0 + 0.3 + i * 0.25, t0 + dur + 0.4))
        # pointer + readout
        for i, (tx, ty) in enumerate(r['toks']):
            x = 28 + i * (cw + gap) + cw / 2
            ta = t0 + 1.7 + i * 0.4; tb = ta + 0.4 if i < 5 else t0 + dur + 0.5
            last = (i == 5)
            bad = (not r['ok']) and last
            pc = C['amber'] if bad else C['mint']
            ptr = f'<path d="M{x-6} 184L{x+6} 184L{x} 175Z" fill="{pc}"/>'
            lab = mono(28, 206, f'token_atual: TOKEN_{ty}', 11.5, pc, weight='700')
            if bad:
                lab += mono(28, 224, 'esperado: TOKEN_SEMICOLON', 11, C['amber']) + mono(28, 240, 'encontrado: TOKEN_RBRACE', 11, C['amber'])
            g.append(win_run(ctx, ptr + lab, ta, tb))
            if not bad and i < 5 and ctx.animated:
                v, k = norm_track(pulse_pts([ta], 0.1, 0.5), T)
                g.append(f'<rect x="{x - cw/2 - 2}" y="140" width="{cw+4}" height="32" rx="9" fill="none" stroke="{C["mint"]}" stroke-width="1.8" opacity="0">{anim(ctx, "opacity", v, k, T)}</rect>')
        # result
        res_col = C['mint'] if r['ok'] else C['amber']
        res = (f'<rect x="28" y="256" width="{150 if r["ok"] else 190}" height="30" rx="15" fill="{res_col}" fill-opacity="0.15" stroke="{res_col}" stroke-width="1.6"/>'
               + mono(28 + (75 if r['ok'] else 95), 276, 'sucesso' if r['ok'] else 'erro · cita a regra e a linha', 12, res_col, 'middle', '700'))
        g.append(win_run(ctx, res, t0 + dur - 0.1, t0 + dur + 0.4))
        out.append(win_group(ctx, '\n'.join(g), t0 - 0.1, t0 + dur + 0.45, static=(ri == 0 and not ctx.animated)))
    out.append(mono(28, 306, 'lexer: texto → tokens · parser: consome e valida', 11, C['t1']))
    return '\n'.join(out)

def fx_run(ctx, inner, a, b):
    if not ctx.animated: return inner
    v, k = norm_track([(0, 0), (a, 0), (a + 0.25, 1), (b, 1), (b + 0.3, 0)], T)
    return f'<g opacity="0">{inner}{anim(ctx, "opacity", v, k, T)}</g>'

def win_run(ctx, inner, a, b):
    if not ctx.animated: return inner if False else ''
    v, k = window_track([(a, b)], T)
    return f'<g opacity="0">{inner}{anim(ctx, "opacity", v, k, T, discrete=True)}</g>'

def win_group(ctx, inner, a, b, static=False):
    if not ctx.animated: return f'<g>{inner}</g>' if static else ''
    v, k = window_track([(a, b)], T)
    return f'<g opacity="0">{inner}{anim(ctx, "opacity", v, k, T, discrete=True)}</g>'

def scene_B(ctx, s, mob):
    out = [head('fundamentos-hardware/', 'Jogo de memória · Raspberry Pi')]
    out.append(f'<rect x="28" y="88" width="262" height="226" rx="12" fill="#0d241f" stroke="#2f6b5a" stroke-width="1.4"/>')
    leds = [('vermelho', 18, 27, 72), ('amarelo', 23, 17, 160), ('azul', 24, 22, 248)]
    out.append(mono(40, 112, 'LEDs (saída)', 10.5, C['t3']) + mono(40, 252, 'botões (entrada)', 10.5, C['t3']))
    for nm, pl, pb, xx in leds:
        col = LEDC[nm]
        out.append(f'<path d="M{xx} 176V208" stroke="#2f6b5a" stroke-width="1.5"/>')
        out.append(f'<circle cx="{xx}" cy="146" r="16" fill="{col}" fill-opacity="0.10" stroke="{col}" stroke-opacity="0.6" stroke-width="1.6"/>')
        out.append(mono(xx, 180 + 0, f'GPIO {pl}', 10.5, C['t2'], 'middle'))
        out.append(f'<circle cx="{xx}" cy="228" r="13" fill="#0a1b17" stroke="#6f8f9c" stroke-width="1.5"/>')
        out.append(mono(xx, 262, f'GPIO {pb}', 10.5, C['t2'], 'middle'))
    # feedback LEDs
    out.append(f'<circle cx="290" cy="116" r="0"/>')
    out.append(f'<circle cx="190" cy="288" r="8" fill="{C["mint"]}" fill-opacity="0.10" stroke="{C["mint"]}" stroke-opacity="0.6"/>' + mono(204, 292, 'certo · 15', 10.5, C['t2']))
    out.append(f'<circle cx="82" cy="288" r="8" fill="{C["amber"]}" fill-opacity="0.10" stroke="{C["amber"]}" stroke-opacity="0.6"/>' + mono(96, 292, 'errado · 14', 10.5, C['t2']))
    idx = {'vermelho': 0, 'amarelo': 1, 'azul': 2}
    rounds = [dict(t0=s + 0.4, seq=['amarelo', 'azul', 'vermelho'], resp=['amarelo', 'azul', 'vermelho'], ok=True),
              dict(t0=s + 5.6, seq=['vermelho', 'vermelho', 'azul'], resp=['vermelho', 'amarelo', 'azul'], ok=False)]
    for r in rounds:
        t0 = r['t0']
        for j, nm in enumerate(r['seq']):
            a = t0 + 0.3 + j * 0.75
            xx = leds[idx[nm]][3]; col = LEDC[nm]
            out.append(win(ctx, f'<circle cx="{xx}" cy="146" r="40" fill="url(#h{idx[nm]})"/><circle cx="{xx}" cy="146" r="16" fill="{col}"/>' + mono(xx, 114, str(j + 1), 12, C['t0'], 'middle', '700'), [(a, a + 0.55)]))
        for j, nm in enumerate(r['resp']):
            a = t0 + 3.0 + j * 0.6
            xx = leds[idx[nm]][3]; col = LEDC[nm]; bad = (not r['ok']) and j == 1
            out.append(win(ctx, f'<circle cx="{xx}" cy="228" r="8" fill="{col}"/>' + mono(xx, 205, str(j + 1), 12, C['t0'], 'middle', '700'), [(a, a + 0.45)]))
        fb_col = C['mint'] if r['ok'] else C['amber']; fx_ = 190 if r['ok'] else 82
        a = t0 + 4.9
        out.append(win(ctx, f'<circle cx="{fx_}" cy="288" r="26" fill="{fb_col}" fill-opacity="0.25"/><circle cx="{fx_}" cy="288" r="8" fill="{fb_col}"/>', [(a, a + 0.9)]))
    out.append(win(ctx, mono(28, 338, '1 · o jogo mostra 3 cores · 2 · o jogador repete', 10.5, C['t1']), [(s, s + 4.6), (s + 5.2, s + 10.0)], static=True))
    if not ctx.animated:
        xx = leds[1][3]
        out.append(f'<circle cx="{xx}" cy="146" r="40" fill="url(#h1)"/><circle cx="{xx}" cy="146" r="16" fill="{LEDC["amarelo"]}"/>')
        out.append(f'<circle cx="190" cy="288" r="26" fill="{C["mint"]}" fill-opacity="0.25"/><circle cx="190" cy="288" r="8" fill="{C["mint"]}"/>')
    return '\n'.join(out)

def scene_C(ctx, c, mob):
    out = [head('infraestrutura-software/', 'Peterson · exclusão mútua')]
    def sbox(x, label, w):
        return f'<rect x="{x}" y="92" width="{w}" height="28" rx="8" fill="#0c1f29" stroke="#2f5060"/>' + mono(x + 10, 110.5, label, 11, C['t1'])
    out += [sbox(22, 'wants[0]', 92), sbox(122, 'wants[1]', 92), sbox(222, '', 130)]
    def dot(x, wins, st):
        base = f'<circle cx="{x}" cy="106" r="4.5" fill="#3a5461"/>'
        if ctx.animated:
            v, k = window_track(wins, T)
            return base + f'<circle cx="{x}" cy="106" r="4.5" fill="{C["mint"]}" opacity="0">{anim(ctx, "opacity", v, k, T, discrete=True)}</circle>'
        return base + (f'<circle cx="{x}" cy="106" r="4.5" fill="{C["mint"]}"/>' if st else '')
    out += [dot(100, [(c + 0.8, c + 7.0)], True), dot(200, [(c + 3.6, c + 9.9)], True)]
    for txt, wins, col in (('turn = –', [(0, c + 1.7), (c + 10.8, T - 0.01)], C['t3']), ('turn = 1', [(c + 1.7, c + 4.5)], C['amber']), ('turn = 0', [(c + 4.5, c + 10.8)], C['amber'])):
        inner = mono(236, 110.5, txt, 11.5, col, weight='700')
        if ctx.animated: out.append(win(ctx, inner, wins))
        elif txt == 'turn = 0': out.append(inner)
    for yy in (196, 268):
        out.append(f'<path d="M64 {yy}H256" stroke="#29434d" stroke-width="1.5" stroke-dasharray="3 6"/>')
    csx, csy, csw, csh = 262, 160, 98, 144
    out.append(f'<rect x="{csx}" y="{csy}" width="{csw}" height="{csh}" rx="12" fill="#0c1f29" stroke="#335767" stroke-width="1.4"/>')
    out.append(sans(csx + csw / 2, 228, 'seção', 12.5, C['t1'], 'middle', '700') + sans(csx + csw / 2, 244, 'crítica', 12.5, C['t1'], 'middle', '700'))
    for (a, b_, col) in ((c + 3.1, c + 7.0, C['mint']), (c + 8.4, c + 9.9, C['blue'])):
        inner = f'<rect x="{csx}" y="{csy}" width="{csw}" height="{csh}" rx="12" fill="{col}" fill-opacity="0.13" stroke="{col}" stroke-width="1.8"/>'
        if ctx.animated: out.append(win(ctx, inner, [(a, b_)]))
        elif col == C['mint']: out.append(inner)
    dx = 268
    def thread(yy, label, col, tr, in_cs=False):
        circ = f'<circle cx="44" cy="{yy}" r="16" fill="#123241" stroke="{col}" stroke-width="1.8"/>' + mono(44, yy + 4.5, label, 12.5, col, 'middle', '700')
        if not ctx.animated: return f'<g transform="translate({dx if in_cs else 0} 0)">{circ}</g>'
        a0, a1, b0, b1 = tr
        v, k = norm_track([(0, '0 0'), (a0, '0 0'), (a1, f'{dx} 0'), (b0, f'{dx} 0'), (b1, '0 0')], T)
        sp = ';'.join([EASE if v[i] != v[i + 1] else '0 0 1 1' for i in range(len(v) - 1)])
        return f'<g>{circ}<animateTransform attributeName="transform" type="translate" values="{";".join(v)}" keyTimes="{";".join(f(x) for x in k)}" calcMode="spline" keySplines="{sp}" dur="{f(T)}s" repeatCount="indefinite"/></g>'
    out.append(thread(196, 'T0', C['mint'], (c + 2.3, c + 3.1, c + 7.0, c + 7.8), True))
    out.append(thread(268, 'T1', C['blue'], (c + 7.6, c + 8.4, c + 9.9, c + 10.7)))
    ring = f'<circle cx="44" cy="268" r="23" fill="none" stroke="{C["amber"]}" stroke-width="1.6" stroke-dasharray="4 5">' + (f'<animateTransform attributeName="transform" type="rotate" from="0 44 268" to="360 44 268" dur="3s" repeatCount="indefinite"/>' if ctx.animated else '') + '</circle>'
    lab = mono(44, 306, 'sched_yield()', 11, C['amber'], 'middle')
    if ctx.animated: out.append(win(ctx, ring + lab, [(c + 4.5, c + 7.7)]))
    else: out.append(ring + lab)
    caps = [('T0 quer entrar: wants[0] = true', 0.8, 1.7), ('T0 cede (turn = 1) e entra: wants[1] é false', 1.7, 3.6), ('T1 quer entrar: wants[1] = true', 3.6, 4.5),
            ('T1 cede a vez (turn = 0) e aguarda', 4.5, 7.0), ('T0 sai: wants[0] = false · T1 entra', 7.0, 9.9), ('nunca duas threads na seção crítica', 9.9, 11.4)]
    if mob: caps = [(a_.replace('T0 cede (turn = 1) e entra: wants[1] é false', 'T0 cede (turn = 1) e entra'), b1, b2) for a_, b1, b2 in caps]
    for txt, a, b_ in caps:
        inner = mono(190, 336, txt, 11, C['t1'], 'middle')
        if ctx.animated: out.append(win(ctx, inner, [(c + a, c + b_)]))
        elif txt.startswith('T1 cede'): out.append(inner)
    return '\n'.join(out)

def dim_group(ctx, inner, active):
    if not ctx.animated: return f'<g>{inner}</g>'
    a, b = active
    pts = [(0, 0.5), (max(0.01, a - 0.4), 0.5), (a, 1), (b, 1), (b + 0.5, 0.5)] if a - 0.4 > 0 else [(0, 1), (b, 1), (b + 0.5, 0.5)]
    v, k = norm_track(pts, T)
    return f'<g opacity="{v[0]}">{inner}{anim(ctx, "opacity", v, k, T)}</g>'

def build(animated=True, mob=False):
    ctx = Ctx(animated)
    if not mob:
        W, H = 1000, 396; defs = base_defs(W, H, 24)
        body = [backdrop(ctx, W, H, 24, aurA=(0.5, 0.1), aurB=(0.95, 0.9))]
        body.append(f'<path d="M326 30V344M622 30V344" stroke="{C["line2"]}"/>')
        pos = {'A': (4, 0), 'B': (322, 0), 'C': (632, 0)}; foot = 380
    else:
        W, H = 400, 1130; defs = base_defs(W, H, 18)
        body = [backdrop(ctx, W, H, 18, aurA=(0.7, 0.2), aurB=(0.2, 0.9))]
        pos = {'A': (24, 4), 'B': (50, 372), 'C': (10, 744)}
        for yy in (366, 738): body.append(f'<path d="M24 {yy}H376" stroke="{C["line2"]}"/>')
        foot = 1114
    defs += ''.join(f'<radialGradient id="h{i}" cx="0.5" cy="0.5" r="0.5"><stop offset="0" stop-color="{c}" stop-opacity="0.75"/><stop offset="1" stop-color="{c}" stop-opacity="0"/></radialGradient>' for i, c in enumerate(LEDC.values()))
    for key, fn, st in (('A', scene_A, 0.8), ('B', scene_B, 11.6), ('C', scene_C, 22.6)):
        ox, oy = pos[key]
        body.append(f'<g transform="translate({ox} {oy})">{dim_group(ctx, fn(ctx, st, mob), SLOTS[key])}</g>')
    body.append(mono(W / 2, foot, 'ilustrações simplificadas do código do repositório acadêmico' if not mob else 'ilustrações simplificadas · repositório acadêmico', 11, C['t3'], 'middle'))
    title = 'Três estudos do repositório acadêmico: compilador, hardware e concorrência'
    if animated:
        desc = ('Três cenas em sequência, uma em destaque por vez. Compilador em C: o lexer transforma a linha y = x + 5; em tokens e o parser os consome um a um; a primeira execução termina em sucesso e a segunda, sem o ponto e vírgula, termina em erro, com o esperado e o encontrado. '
                'Hardware: um jogo de memória na Raspberry Pi mostra três cores em LEDs (GPIO 18, 23 e 24) e o jogador repete nos botões (GPIO 27, 17 e 22); o acerto acende o LED 15 e o erro acende o LED 14. '
                'Concorrência: no algoritmo de Peterson, a thread T0 cede a vez e entra na seção crítica; T1 cede a vez e aguarda com sched_yield até T0 sair.')
    else:
        desc = ('Três cenas. Compilador em C: a linha y = x + 5; dividida em tokens, consumidos pelo parser até o resultado sucesso. Hardware: jogo de memória na Raspberry Pi com LEDs nos GPIO 18, 23 e 24, botões nos GPIO 27, 17 e 22 e LEDs de feedback 15 (certo) e 14 (errado). '
                'Concorrência: algoritmo de Peterson com wants[0] e wants[1] verdadeiros, turn = 0, T0 na seção crítica e T1 aguardando com sched_yield.')
    return svg_doc(W, H, title, desc, defs, body)

