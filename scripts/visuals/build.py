#!/usr/bin/env python3
"""Gera os SVGs do perfil em ../../assets.

  python3 scripts/visuals/build.py              # tudo (a atividade usa a página pública do GitHub)
  python3 scripts/visuals/build.py --only activity   # só o calendário (usado pelo workflow diário)

Cada composição sai em 4 variantes: desktop/celular x animada/estática.
"""
import sys
from datetime import date
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import hero, cinema, ong, lab, activity

ASSETS = Path(__file__).resolve().parents[2] / 'assets'

def names(base):
    return {(False, True): f'{base}.svg', (False, False): f'{base}-static.svg', (True, True): f'{base}-mobile.svg', (True, False): f'{base}-mobile-static.svg'}

def write(base, build, *extra):
    for (mob, anim), name in names(base).items():
        (ASSETS / name).write_text(build(anim, mob, *extra) + '\n', encoding='utf-8')

def main():
    only = sys.argv[2] if len(sys.argv) > 2 and sys.argv[1] == '--only' else None
    ASSETS.mkdir(exist_ok=True)
    if only in (None, 'activity'):
        today = date.today()
        data = activity.fetch_calendar(today)
        write('github-activity', activity.build, data, today)
    if only is None:
        write('hero', hero.build); write('cinema-flow', cinema.build)
        write('partilhar-overview', ong.build); write('lab', lab.build)
    print('ok:', sorted(p.name for p in ASSETS.glob('*.svg')))

if __name__ == '__main__':
    main()
