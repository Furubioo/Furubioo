from lib import *

C = dict(bg0='#07131a', bg1='#102f3c', panel='#0a151b', line='#365867', line2='#29434d', blue='#8fd3ff', mint='#7ee8c1',
         amber='#f0c674', t0='#f4f9fb', t1='#a8c1cb', t2='#8aa8b4', t3='#7d9ba7')

def base_defs(W, H, rx=26, grid=26):
    return f'''
<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{C['bg0']}"/><stop offset="1" stop-color="{C['bg1']}"/></linearGradient>
<radialGradient id="auA" cx="0.5" cy="0.5" r="0.5"><stop offset="0" stop-color="#2fb6c9" stop-opacity="0.30"/><stop offset="0.55" stop-color="#2fb6c9" stop-opacity="0.08"/><stop offset="1" stop-color="#2fb6c9" stop-opacity="0"/></radialGradient>
<radialGradient id="auB" cx="0.5" cy="0.5" r="0.5"><stop offset="0" stop-color="#7ee8c1" stop-opacity="0.16"/><stop offset="0.6" stop-color="#7ee8c1" stop-opacity="0.04"/><stop offset="1" stop-color="#7ee8c1" stop-opacity="0"/></radialGradient>
<pattern id="grid" width="{grid}" height="{grid}" patternUnits="userSpaceOnUse"><path d="M{grid} 0H0V{grid}" fill="none" stroke="#b5e4f3" stroke-opacity="0.055"/></pattern>
<clipPath id="card"><rect width="{W}" height="{H}" rx="{rx}"/></clipPath>
<linearGradient id="rim" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#ffffff" stop-opacity="0"/><stop offset="0.5" stop-color="#ffffff" stop-opacity="0.28"/><stop offset="1" stop-color="#ffffff" stop-opacity="0"/></linearGradient>
<radialGradient id="halo" cx="0.5" cy="0.5" r="0.5"><stop offset="0" stop-color="{C['blue']}" stop-opacity="0.55"/><stop offset="1" stop-color="{C['blue']}" stop-opacity="0"/></radialGradient>
<radialGradient id="haloG" cx="0.5" cy="0.5" r="0.5"><stop offset="0" stop-color="{C['mint']}" stop-opacity="0.55"/><stop offset="1" stop-color="{C['mint']}" stop-opacity="0"/></radialGradient>
'''

def backdrop(ctx, W, H, rx=26, grid=26, aurA=(0.72, 0.30), aurB=(0.15, 0.95)):
    """gradient + drifting aurora (2 blobs) + seamless drifting grid. one slow motion layer each."""
    s = [f'<rect width="{W}" height="{H}" rx="{rx}" fill="url(#bg)"/>', '<g clip-path="url(#card)">']
    ax, ay = aurA[0] * W, aurA[1] * H; bx, by = aurB[0] * W, aurB[1] * H
    ra = max(W, H) * 0.55; rb = max(W, H) * 0.42
    s.append(f'<g><ellipse cx="{f(ax)}" cy="{f(ay)}" rx="{f(ra)}" ry="{f(ra*0.7)}" fill="url(#auA)"/>'
             + spline_anim(ctx, None, ['0 0', f'{f(W*0.05)} {f(-H*0.04)}', '0 0'], 28, 'transform', 'translate') + '</g>')
    s.append(f'<g><ellipse cx="{f(bx)}" cy="{f(by)}" rx="{f(rb)}" ry="{f(rb*0.7)}" fill="url(#auB)"/>'
             + spline_anim(ctx, None, ['0 0', f'{f(-W*0.04)} {f(-H*0.05)}', '0 0'], 36, 'transform', 'translate') + '</g>')
    drift = ''
    if ctx.animated:
        drift = f'<animateTransform attributeName="transform" type="translate" from="0 0" to="{grid} 0" dur="42s" repeatCount="indefinite"/>'
    s.append(f'<g><rect x="{-grid}" y="0" width="{W+2*grid}" height="{H}" fill="url(#grid)"/>{drift}</g>')
    s.append('</g>')
    return '\n'.join(s)

def svg_doc(W, H, title, desc, defs, body, extra_attr=''):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-labelledby="t d"{extra_attr}>'
            f'<title id="t">{esc(title)}</title><desc id="d">{esc(desc)}</desc><defs>{defs}</defs>\n' + '\n'.join(body) + '\n</svg>')

def mono(x, y, text, size=11, fill=None, anchor='start', weight='400', spacing=None, extra=''):
    fill = fill or C['t2']
    sp = f' letter-spacing="{spacing}"' if spacing else ''
    return f'<text x="{f(x)}" y="{f(y)}" text-anchor="{anchor}" fill="{fill}" font-family="{MONO}" font-size="{size}" font-weight="{weight}"{sp}{extra}>{esc(text)}</text>'

def sans(x, y, text, size=14, fill=None, anchor='start', weight='400', spacing=None, extra=''):
    fill = fill or C['t0']
    sp = f' letter-spacing="{spacing}"' if spacing else ''
    return f'<text x="{f(x)}" y="{f(y)}" text-anchor="{anchor}" fill="{fill}" font-family="{SANS}" font-size="{size}" font-weight="{weight}"{sp}{extra}>{esc(text)}</text>'

def track_el(ctx, inner, pts, T, static, attr='opacity', discrete=False):
    """wrap in <g>; opacity follows pts (t,value) smoothly; static value used when not animated."""
    if not ctx.animated:
        return f'<g {attr}="{static}">{inner}</g>'
    v, k = norm_track(pts, T)
    return f'<g {attr}="{v[0]}">{inner}{anim(ctx, attr, v, k, T)}</g>'
