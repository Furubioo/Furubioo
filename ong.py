"""Componentes compartilhados (caixas de camada, brilho de chegada, revelação)."""
from common import *

def reveal(ctx, inner, t_in, T, dy=10, d=0.55, t_out=None):
    if not ctx.animated:
        return f'<g>{inner}</g>'
    t_out = T - 1.3 if t_out is None else t_out
    v, k = norm_track([(0, 0), (t_in, 0), (t_in + d, 1), (t_out, 1), (t_out + 0.6, 0)], T)
    tv = [f'0 {dy}', f'0 {dy}', '0 0', '0 0', f'0 {dy}']
    # transform track (same keyTimes minus final appended)
    kt = k[:-1]; tvals = tv
    tr = (f'<animateTransform attributeName="transform" type="translate" values="{";".join(tvals)}" keyTimes="{";".join(f(x) for x in kt[:len(tvals)-1] + [1.0])}" dur="{f(T)}s" repeatCount="indefinite"/>')
    return f'<g opacity="0">{inner}{anim(ctx, "opacity", v, k, T)}{tr}</g>'

def layer_box(x, y, w, h, title, sub, sub2=None, accent=None):
    s = f'<rect x="{x}" y="{y+5}" width="{w}" height="{h}" rx="11" fill="#050d12" opacity="0.6"/>'
    s += f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="11" fill="#112733" stroke="#335767"/>'
    s += f'<path d="M{x+14} {y+0.8}H{x+w-14}" stroke="url(#rim)" stroke-width="1"/>'
    s += sans(x + 16, y + 20, title, 14, '#eaf4f7', weight='700')
    if sub: s += mono(x + 16, y + 36, sub, 10.5, C['t2'])
    if sub2: s += mono(x + 16, y + 50, sub2, 10.5, C['t2'])
    return s

def glow(ctx, x, y, w, h, times, T, color, rise=0.18, fall=0.8, r=11):
    if not ctx.animated or not times: return ''
    v, k = norm_track(pulse_pts(times, rise, fall), T)
    return (f'<rect x="{x-2}" y="{y-2}" width="{w+4}" height="{h+4}" rx="{r+2}" fill="{color}" fill-opacity="0.12" stroke="{color}" stroke-width="1.9" opacity="0">'
            + anim(ctx, 'opacity', v, k, T) + '</rect>')

def card(x, y, w, h, num, title, sub, accent, sub_size=11):
    s = f'<rect x="{x+6}" y="{y+8}" width="{w}" height="{h}" rx="18" fill="#04090d" opacity="0.55"/>'
    s += f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="18" fill="{C["panel"]}" fill-opacity="0.94" stroke="{C["line"]}" stroke-width="1.3"/>'
    s += f'<path d="M{x+24} {y+0.8}H{x+w-24}" stroke="url(#rim)" stroke-width="1.2"/>'
    s += f'<rect x="{x+22}" y="{y+20}" width="34" height="22" rx="11" fill="none" stroke="{accent}" stroke-opacity="0.75"/>'
    s += mono(x + 39, y + 35.5, num, 11.5, accent, 'middle', '700')
    s += sans(x + 68, y + 37, title, 19, '#eef6f9', weight='700')
    s += mono(x + 22, y + 64, sub, sub_size, C['t2'])
    return s

def token_motion(ctx, d, T, stops, shape, color, glowid, opacity_windows):
    if not ctx.animated: return ''
    mot = motion_stops(d, T, stops, ease=True)
    v, k = window_track(opacity_windows, T)
    return f'<g opacity="0"><circle r="15" fill="url(#{glowid})"/>{shape}{mot}{anim(ctx, "opacity", v, k, T, discrete=True)}</g>'

