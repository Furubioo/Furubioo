"""Calendário público de contribuições (animado). Usa só a página pública do GitHub, sem token."""
import re, sys
from datetime import date, timedelta
from urllib.request import Request, urlopen
from common import *

USER = 'Furubioo'
LV = ['#10272f', '#1c5360', '#2a8686', '#4fc1a6', '#7ee8c1']
MES = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']

from html.parser import HTMLParser

class _P(HTMLParser):
    def __init__(self):
        super().__init__(); self.cells = {}; self.tips = {}; self._tip = None
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == 'td' and a.get('data-date') and a.get('data-level') is not None:
            self.cells[a['id'] if a.get('id') else a['data-date']] = (a['data-date'], int(a['data-level']))
        elif tag == 'tool-tip':
            self._tip = a.get('for')
    def handle_data(self, data):
        if self._tip:
            self.tips[self._tip] = data.strip(); self._tip = None

def parse_calendar(html, year):
    p = _P(); p.feed(html)
    data = {}
    for cid, (d, lvl) in p.cells.items():
        m = re.match(r'(\d+) contribution', p.tips.get(cid, ''))
        n = int(m.group(1)) if m else 0
        data[date.fromisoformat(d)] = (lvl, n)
    data = {d: v for d, v in data.items() if d.year == year}
    expected = 366 if date(year, 12, 31).timetuple().tm_yday == 366 else 365
    if len(data) != expected:
        raise RuntimeError(f'esperava {expected} células em {year}, recebi {len(data)}')
    return data

def fetch_calendar(today):
    url = f'https://github.com/users/{USER}/contributions?to={today.isoformat()}'
    req = Request(url, headers={'User-Agent': 'profile-readme-calendar/2.0'})
    with urlopen(req, timeout=30) as r:
        if r.status != 200: raise RuntimeError(f'HTTP {r.status}')
        return parse_calendar(r.read().decode('utf-8', 'replace'), today.year)

def build(animated, mob, data, today):
    ctx = Ctx(animated)
    year = today.year
    jan1 = date(year, 1, 1); start = jan1 - timedelta(days=(jan1.weekday() + 1) % 7)  # domingo
    weeks = []
    d = start
    while d <= date(year, 12, 31):
        weeks.append([d + timedelta(days=i) for i in range(7)]); d += timedelta(days=7)
    if mob:
        weeks = [w for w in weeks if w[-1] >= today - timedelta(days=22 * 7 - 1) and w[0] <= today][-22:]
        cs, gp, W = 11, 3, 400
    else:
        cs, gp, W = 13, 3, 1000
    step = cs + gp
    left = 44 if not mob else 34
    gw = len(weeks) * step
    top = 118 if not mob else 108
    H = (top + 7 * step + 150) if not mob else (top + 7 * step + 236)
    if not mob:
        left = (W - gw - 0) / 2 + 14
    defs = base_defs(W, H, rx=24 if not mob else 18)
    defs += f'<clipPath id="gridclip"><rect x="{f(left-2)}" y="{top-2}" width="{f(gw+4)}" height="{7*step+2}"/></clipPath><linearGradient id="scan" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset="0.5" stop-color="#fff" stop-opacity="0.16"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>'
    body = [backdrop(ctx, W, H, rx=24 if not mob else 18, aurA=(0.8, 0.2), aurB=(0.1, 0.9))]
    pad = 40 if not mob else 24
    body.append(sans(pad, 44, 'ATIVIDADE PÚBLICA · GITHUB', 12 if not mob else 11, C['mint'], weight='700', spacing=3 if not mob else 2))
    body.append(sans(pad, 80 if not mob else 76, 'Contribuições por dia', 24 if not mob else 20, C['t0'], weight='700'))
    body.append(sans(W - pad, 80 if not mob else 76, str(year), 24 if not mob else 20, C['t0'], 'end', '700'))
    if not mob: body.append(mono(W - pad, 44, 'cada coluna é uma semana', 11, C['t3'], 'end'))
    # month labels
    last_m = None
    for ci, w in enumerate(weeks):
        for dd in w:
            if dd.year == year and dd.day <= 7 and dd.month != last_m and (ci == 0 or True):
                if w[0].month == dd.month or dd.day <= 7:
                    pass
        m = next((dd.month for dd in w if dd.year == year and dd.day == 1), None)
        if m is not None or (ci == 0 and mob):
            mm = m if m is not None else w[3].month
            if mm != last_m:
                body.append(mono(left + ci * step, top - 10, MES[mm - 1], 11, C['t2']))
                last_m = mm
    for r, lab in ((1, 'seg'), (3, 'qua'), (5, 'sex')):
        body.append(mono(left - 8, top + r * step + cs - 2, lab, 10.5, C['t3'], 'end'))
    # cells
    peaks = []
    cells = []
    for ci, w in enumerate(weeks):
        col = []
        for ri, dd in enumerate(w):
            x = left + ci * step; y = top + ri * step
            if dd.year != year or dd > today:
                if dd.year == year:
                    col.append(f'<rect x="{f(x)}" y="{f(y)}" width="{cs}" height="{cs}" rx="3" fill="none" stroke="#2f5060" stroke-opacity="0.45" stroke-dasharray="2 2"/>')
                continue
            lvl, n = data.get(dd, (0, 0))
            col.append(f'<rect x="{f(x)}" y="{f(y)}" width="{cs}" height="{cs}" rx="3" fill="{LV[lvl]}"/>')
            if lvl == 4: peaks.append((x, y, dd))
        d_ = ci * 0.03 + 0.02
        if animated:
            col_inner = ''.join(col)
            cells.append(f'<g>{col_inner}<animate attributeName="opacity" values="0;0;1" keyTimes="0;{f(d_/(d_+0.5))};1" dur="{f(d_+0.5)}s" begin="0s" fill="freeze"/></g>')
        else:
            cells.append(f'<g>{"".join(col)}</g>')
    body.append(f'<g clip-path="url(#gridclip)">' + ''.join(cells) + '</g>')
    # sweeping light (loops) + peak pulses + today marker
    if animated:
        wsc = 120
        body.append(f'<g clip-path="url(#gridclip)"><rect x="{f(left-wsc)}" y="{top-4}" width="{wsc}" height="{7*step+8}" fill="url(#scan)">'
                    f'<animateTransform attributeName="transform" type="translate" values="0 0;0 0;{f(gw+wsc)} 0;{f(gw+wsc)} 0" keyTimes="0;0.25;0.65;1" calcMode="spline" keySplines="0 0 1 1;{EASE};0 0 1 1" dur="12s" repeatCount="indefinite" begin="2.5s"/></rect></g>')
        for k, (x, y, dd) in enumerate(peaks):
            b = 3.0 + k * 0.8
            body.append(f'<circle cx="{f(x+cs/2)}" cy="{f(y+cs/2)}" r="{cs/2}" fill="none" stroke="{C["mint"]}" stroke-width="1.6" opacity="0">'
                        f'<animate attributeName="r" values="{cs/2};{cs*1.5};{cs*1.5}" keyTimes="0;0.35;1" dur="5s" begin="{b}s" repeatCount="indefinite"/>'
                        f'<animate attributeName="opacity" values="0.9;0;0" keyTimes="0;0.35;1" dur="5s" begin="{b}s" repeatCount="indefinite"/></circle>')
    # today marker
    for ci, w in enumerate(weeks):
        for ri, dd in enumerate(w):
            if dd == today:
                x = left + ci * step; y = top + ri * step
                body.append(f'<rect x="{f(x-2)}" y="{f(y-2)}" width="{cs+4}" height="{cs+4}" rx="5" fill="none" stroke="{C["t0"]}" stroke-width="1.5"/>')
                lx = x + cs / 2
                body.append(mono(min(lx, W - 60), top + 7 * step + 16, 'hoje', 11, C['t1'], 'middle'))
    # stats (real numbers from the public page)
    vals = [(dd, v) for dd, v in data.items() if dd <= today]
    total = sum(n for _, (l, n) in vals); active = sum(1 for _, (l, n) in vals if l > 0 or n > 0)
    best = max(vals, key=lambda p: p[1][1]) if vals else None
    sy = top + 7 * step + 56 if not mob else top + 7 * step + 50
    tiles = [(f'{total}', 'contribuições públicas em ' + str(year) if not mob else f'contribuições em {year}'), (f'{active}', 'dias com atividade'),
             (f'{best[1][1]}', 'no dia de maior atividade · ' + best[0].strftime('%d/%m') if best else '')]
    if not mob:
        tw = (W - 2 * pad - 2 * 16) / 3
        for i, (num, lab) in enumerate(tiles):
            x = pad + i * (tw + 16)
            body.append(f'<rect x="{f(x)}" y="{sy}" width="{f(tw)}" height="64" rx="14" fill="{C["panel"]}" fill-opacity="0.9" stroke="{C["line"]}"/>')
            body.append(sans(x + 18, sy + 40, num, 28, C['t0'], weight='700') + mono(x + 18 + len(num) * 17 + 14, sy + 38, lab, 11.5, C['t2']))
    else:
        for i, (num, lab) in enumerate(tiles):
            y = sy + i * 56
            body.append(f'<rect x="{pad}" y="{y}" width="{W-2*pad}" height="46" rx="12" fill="{C["panel"]}" fill-opacity="0.9" stroke="{C["line"]}"/>')
            body.append(sans(pad + 14, y + 31, num, 22, C['t0'], weight='700') + mono(pad + 14 + len(num) * 13 + 12, y + 29, lab, 11, C['t2']))
    # legend
    lgx = left + 34
    ly = top + 7 * step + 16
    body.append(mono(lgx, ly, 'menos', 11, C['t3'], 'end'))
    for i in range(5):
        body.append(f'<rect x="{f(lgx+8+i*(cs+4))}" y="{ly-cs+2}" width="{cs}" height="{cs}" rx="3" fill="{LV[i]}"/>')
    body.append(mono(lgx + 14 + 5 * (cs + 4), ly, 'mais', 11, C['t3']))
    title = f'Contribuições públicas de {USER} em {year}'
    desc = (f'Calendário de contribuições públicas no GitHub em {year}{" (últimas 22 semanas)" if mob else ""}. Cada célula é um dia e a cor indica a intensidade. '
            f'{total} contribuições em {active} dias com atividade até {today.strftime("%d/%m/%Y")}.' + (' As colunas aparecem da esquerda para a direita e uma faixa de luz percorre o calendário; os dias de maior atividade pulsam.' if animated else ''))
    return svg_doc(W, H, title, desc, defs, body)

