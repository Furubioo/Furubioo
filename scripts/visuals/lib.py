import math

SANS = "-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif"
MONO = "ui-monospace,SFMono-Regular,Menlo,Consolas,'Liberation Mono',monospace"

def f(x):
    s = ('%.5f' % x).rstrip('0').rstrip('.')
    return s if s != '-0' else '0'

def esc(t):
    return t.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

class Ctx:
    def __init__(self, animated=True):
        self.animated = animated
        self.n = 0
    def uid(self, p='i'):
        self.n += 1
        return f'{p}{self.n}'

def anim(ctx, attr, values, times, dur, discrete=False, begin=None, extra=''):
    """SMIL <animate>. values/times: lists. times normalised 0..1, first must be 0."""
    if not ctx.animated:
        return ''
    assert len(values) == len(times), (values, times)
    assert abs(times[0]) < 1e-9, times
    for a, b in zip(times, times[1:]):
        assert b > a - 1e-12, ('keyTimes not increasing', times)
    values = list(values); times = list(times)
    if not discrete and times[-1] < 1 - 1e-9:
        values.append(values[-1]); times.append(1.0)   # SMIL: linear keyTimes must end at 1
    vs = ';'.join(str(v) for v in values)
    ks = ';'.join(f(t) for t in times)
    b = f' begin="{begin}"' if begin is not None else ''
    cm = ' calcMode="discrete"' if discrete else ''
    return (f'<animate attributeName="{attr}" values="{vs}" keyTimes="{ks}"{cm} '
            f'dur="{f(dur)}s" repeatCount="indefinite"{b}{extra}/>')

def window_track(windows, T, on=1, off=0):
    """discrete on/off track. windows = [(t0,t1),...] in seconds within [0,T). returns values,times."""
    ev = []
    for a, b in windows:
        ev.append((a, on)); ev.append((b, off))
    ev.sort()
    vals = [off]; times = [0.0]
    for t, v in ev:
        tn = t / T
        if tn <= times[-1] + 1e-9:
            tn = times[-1] + 1e-4
        if tn >= 1: continue
        vals.append(v); times.append(tn)
    return vals, times

def windowed(ctx, tag_open, inner, windows, T, attr='opacity', on=1, off=0, static_on=False, extra_attrs=''):
    """wrap content in <g> whose opacity follows windows (discrete). static: on/off by static_on."""
    if not ctx.animated:
        o = on if static_on else off
        return f'<g {attr}="{o}"{extra_attrs}>{inner}</g>'
    v, t = window_track(windows, T, on, off)
    return f'<g {attr}="{off}"{extra_attrs}>{inner}{anim(ctx, attr, v, t, T, discrete=True)}</g>'

def fade_track(t_in, d_in, t_out, d_out, T):
    """opacity 0 -> 1 (linear) at t_in, hold, 1 -> 0 at t_out. returns values,times"""
    pts = [(0, 0)]
    pts.append((t_in, 0)); pts.append((t_in + d_in, 1))
    pts.append((t_out, 1)); pts.append((t_out + d_out, 0))
    vals = []; times = []
    for t, v in pts:
        tn = t / T
        if times and tn <= times[-1] + 1e-9: tn = times[-1] + 1e-6
        if tn >= 1: tn = 0.999999
        vals.append(v); times.append(tn)
    return vals, times

def path_points(pts):
    d = f'M{f(pts[0][0])},{f(pts[0][1])}'
    for p in pts[1:]:
        d += f' L{f(p[0])},{f(p[1])}'
    return d

def seg_lengths(pts):
    L = [0.0]
    for a, b in zip(pts, pts[1:]):
        L.append(L[-1] + math.hypot(b[0]-a[0], b[1]-a[1]))
    return L

def point_at(pts, frac):
    L = seg_lengths(pts); tot = L[-1]; d = frac * tot
    for i in range(1, len(L)):
        if d <= L[i] + 1e-9:
            a, b = pts[i-1], pts[i]
            u = (d - L[i-1]) / max(1e-9, (L[i] - L[i-1]))
            return (a[0] + (b[0]-a[0])*u, a[1] + (b[1]-a[1])*u)
    return pts[-1]

def frac_of_point(pts, p):
    """fraction along polyline of the vertex closest to p (p must be on the path)."""
    L = seg_lengths(pts); tot = L[-1]
    best = None
    for i in range(1, len(pts)):
        a, b = pts[i-1], pts[i]
        dx, dy = b[0]-a[0], b[1]-a[1]
        seglen = math.hypot(dx, dy)
        if seglen == 0: continue
        u = ((p[0]-a[0])*dx + (p[1]-a[1])*dy) / (seglen**2)
        u = max(0, min(1, u))
        q = (a[0]+dx*u, a[1]+dy*u)
        dist = math.hypot(q[0]-p[0], q[1]-p[1])
        if best is None or dist < best[0]:
            best = (dist, (L[i-1] + seglen*u) / tot)
    return best[1]

def typewriter(ctx, words, x, y, size, fill, caret_fill, cw, T_holder, hold=1.5, tchar=0.075, echar=0.035, gap=0.4, start=0.5, static_idx=0, cid='tw'):
    """returns (svg, defs, total_duration). Words type char by char, hold, erase."""
    sched = []
    t = start
    for w in words:
        n = len(w)
        t0 = t; t1 = t0 + n * tchar; t2 = t1 + hold; t3 = t2 + n * echar
        sched.append((t0, t1, t2, t3)); t = t3 + gap
    T = t
    T_holder.append(T)
    defs = []; out = []
    for i, w in enumerate(words):
        n = len(w); t0, t1, t2, t3 = sched[i]
        cid_i = f'{cid}{i}'
        full = n * cw + 10
        h = size * 1.5
        if ctx.animated:
            ev = [(0.0, 0)]
            for c in range(1, n + 1):
                ev.append((t0 + (c - 1) * tchar, c * cw if c < n else full))
            for k in range(1, n + 1):
                ev.append((t2 + (k - 1) * echar, max(0, (n - k) * cw)))
            ev.append((t3, 0))
            # dedupe times
            vals = []; times = []
            for tt, v in ev:
                tn = tt / T
                if times and tn <= times[-1] + 1e-9: tn = times[-1] + 1e-6
                vals.append(round(v, 2)); times.append(tn)
            wid = anim(ctx, 'width', vals, times, T, discrete=True)
            # caret x follows
            cx_vals = [round(x + (v if v < full else n * cw), 2) for v in vals]
            cx = anim(ctx, 'x', cx_vals, times, T, discrete=True)
            blink = anim(ctx, 'opacity', [1, 0, 1], [0, 0.5, 1.0 - 1e-6], 1.0, discrete=True)  # blink at 1s
            defs.append(f'<clipPath id="{cid_i}"><rect x="{f(x)}" y="{f(y - size)}" width="0" height="{f(h)}">{wid}</rect></clipPath>')
            win_vals, win_times = window_track([(t0, t3 + 0.05)], T)
            win = anim(ctx, 'opacity', win_vals, win_times, T, discrete=True)
            out.append(f'<g opacity="0"><text x="{f(x)}" y="{f(y)}" font-family="{MONO}" font-size="{size}" fill="{fill}" clip-path="url(#{cid_i})">{esc(w)}</text>'
                       f'<rect x="{f(x)}" y="{f(y - size + 2)}" width="{f(cw * 0.55)}" height="{f(size)}" rx="1" fill="{caret_fill}">{cx}{blink}</rect>{win}</g>')
        else:
            if i == static_idx:
                out.append(f'<g><text x="{f(x)}" y="{f(y)}" font-family="{MONO}" font-size="{size}" fill="{fill}">{esc(w)}</text>'
                           f'<rect x="{f(x + n * cw + 2)}" y="{f(y - size + 2)}" width="{f(cw * 0.55)}" height="{f(size)}" rx="1" fill="{caret_fill}"/></g>')
    return '\n'.join(out), '\n'.join(defs), T


# ---------------------------------------------------------------- v2 helpers
EASE = "0.45 0 0.55 1"

def norm_track(pts, T, end_value=None):
    """pts=[(t_sec,value)] -> (values,keyTimes): strictly increasing (min step 1e-4), start 0, end exactly 1."""
    vals, times = [], []
    for t, v in pts:
        tn = max(0.0, t / T)
        if not times:
            tn = 0.0
        elif tn <= times[-1] + 1e-4:
            tn = times[-1] + 1e-4
        if tn >= 1 - 1e-4:
            break
        vals.append(v); times.append(tn)
    vals.append(vals[-1] if end_value is None else end_value); times.append(1.0)
    return vals, times

def pulse_pts(times, rise=0.15, fall=0.8, lo=0, hi=1):
    pts = [(0, lo)]
    last_end = 0.0
    for t in sorted(times):
        t = max(t, last_end + 0.002)
        pts += [(t, lo), (t + rise, hi), (t + rise + fall, lo)]
        last_end = t + rise + fall
    return pts

def motion_stops(path_d, T, stops, ease=True, extra=''):
    """animateMotion following path_d. stops=[(t_sec, fraction)] sorted; holds between non-adjacent equal fractions."""
    kp, kt, splines = [], [], []
    for i, (t, fr) in enumerate(stops):
        tn = t / T
        if kt and tn <= kt[-1] + 1e-4: tn = kt[-1] + 1e-4
        if i == 0:
            tn = 0.0 if tn > 0 else 0.0
        kp.append(fr); kt.append(tn)
    if kt[-1] < 1:
        kp.append(kp[-1]); kt.append(1.0)
    for a, b in zip(kp, kp[1:]):
        splines.append(EASE if (ease and abs(a - b) > 1e-9) else "0 0 1 1")
    return (f'<animateMotion path="{path_d}" dur="{f(T)}s" repeatCount="indefinite" calcMode="spline" '
            f'keyPoints="{";".join(f(x) for x in kp)}" keyTimes="{";".join(f(x) for x in kt)}" '
            f'keySplines="{";".join(splines)}"{extra}/>')

def spline_anim(ctx, tag_attr, values, T, kind='animate', ttype=None, begin=None):
    """smooth back-and-forth (loop) with eased splines. values list closes the loop (first==last)."""
    if not ctx.animated: return ''
    n = len(values)
    kt = [i / (n - 1) for i in range(n)]
    sp = ';'.join([EASE] * (n - 1))
    vs = ';'.join(str(v) for v in values)
    b = f' begin="{begin}"' if begin else ''
    if kind == 'transform':
        return (f'<animateTransform attributeName="transform" type="{ttype}" values="{vs}" keyTimes="{";".join(f(x) for x in kt)}" '
                f'calcMode="spline" keySplines="{sp}" dur="{f(T)}s" repeatCount="indefinite"{b}/>')
    return (f'<animate attributeName="{tag_attr}" values="{vs}" keyTimes="{";".join(f(x) for x in kt)}" '
            f'calcMode="spline" keySplines="{sp}" dur="{f(T)}s" repeatCount="indefinite"{b}/>')
