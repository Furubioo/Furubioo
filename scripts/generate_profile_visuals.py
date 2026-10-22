from __future__ import annotations

import argparse
from datetime import date, timedelta
from html.parser import HTMLParser
from pathlib import Path
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
USERNAME = "Furubioo"

PALETTES = {
    "light": {
        "background": "#f7fafb",
        "border": "#c8d9df",
        "text": "#17313a",
        "muted": "#526e78",
        "levels": ("#e6eef1", "#c6e8e9", "#8dd5d1", "#2fb6c9", "#147b84"),
    },
    "dark": {
        "background": "#07131a",
        "border": "#29434d",
        "text": "#eef6f9",
        "muted": "#a8c1cb",
        "levels": ("#122832", "#164b58", "#18758a", "#2fb6c9", "#7ee8c1"),
    },
}

MONTHS = ("Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez")

ANIMATIONS = {
    "hero-static.svg": (
        "hero.svg",
        """<g aria-hidden="true">
  <circle cx="998" cy="235" r="3.1" fill="#7ee8c1">
    <animateMotion dur="5s" repeatCount="indefinite" path="M0 0 H27"/>
  </circle>
</g>""",
    ),
    "hero-mobile-static.svg": (
        "hero-mobile.svg",
        """<g aria-hidden="true">
  <circle cx="141" cy="621" r="2.8" fill="#7ee8c1">
    <animateMotion dur="5s" repeatCount="indefinite" path="M0 0 H26"/>
  </circle>
</g>""",
    ),
    "cinema-flow-static.svg": (
        "cinema-flow.svg",
        """<g aria-hidden="true">
  <circle cx="832" cy="272" r="3.5" fill="#8fd3ff">
    <animateMotion dur="9s" repeatCount="indefinite" path="M0 0 V288"/>
  </circle>
</g>""",
    ),
    "cinema-flow-mobile-static.svg": (
        "cinema-flow-mobile.svg",
        """<g aria-hidden="true">
  <circle cx="200" cy="708" r="3.5" fill="#8fd3ff">
    <animateMotion dur="9s" repeatCount="indefinite" path="M0 0 V268"/>
  </circle>
</g>""",
    ),
    "lab-static.svg": (
        "lab.svg",
        """<g aria-hidden="true">
  <circle cx="433" cy="263" r="13" fill="none" stroke="#f0c674" stroke-width="1.5" opacity=".35">
    <animate attributeName="r" values="11;17;11" dur="6s" repeatCount="indefinite"/>
    <animate attributeName="opacity" values=".28;.58;.28" dur="6s" repeatCount="indefinite"/>
  </circle>
</g>""",
    ),
    "lab-mobile-static.svg": (
        "lab-mobile.svg",
        """<g aria-hidden="true">
  <circle cx="61" cy="622" r="12" fill="none" stroke="#f0c674" stroke-width="1.5" opacity=".35">
    <animate attributeName="r" values="10;16;10" dur="6s" repeatCount="indefinite"/>
    <animate attributeName="opacity" values=".28;.58;.28" dur="6s" repeatCount="indefinite"/>
  </circle>
</g>""",
    ),
}


class ContributionParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.levels: dict[date, int] = {}

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag != "td":
            return
        attributes = dict(attrs)
        value = attributes.get("data-date")
        level = attributes.get("data-level")
        if value is None or level is None:
            return
        day = date.fromisoformat(value)
        intensity = int(level)
        if not 0 <= intensity <= 4:
            raise ValueError(f"Invalid contribution level {intensity} for {day}")
        self.levels[day] = intensity


def fetch_calendar(year: int, today: date) -> dict[date, int]:
    url = f"https://github.com/users/{USERNAME}/contributions?to={today.isoformat()}"
    request = Request(url, headers={"User-Agent": "profile-readme-calendar/1.0"})
    with urlopen(request, timeout=30) as response:
        if response.status != 200:
            raise RuntimeError(f"GitHub contribution calendar returned HTTP {response.status}")
        markup = response.read().decode("utf-8", "replace")

    parser = ContributionParser()
    parser.feed(markup)
    expected_days = 366 if date(year, 12, 31).timetuple().tm_yday == 366 else 365
    year_levels = {day: level for day, level in parser.levels.items() if day.year == year}
    if len(year_levels) != expected_days:
        raise RuntimeError(
            f"Expected {expected_days} contribution cells for {year}; received {len(year_levels)}"
        )
    return year_levels


def render_calendar(year: int, levels: dict[date, int], palette: dict[str, object]) -> str:
    first_day = date(year, 1, 1)
    last_day = date(year, 12, 31)
    start_day = first_day - timedelta(days=(first_day.weekday() + 1) % 7)
    week_count = (last_day - start_day).days // 7 + 1

    width = 1020
    height = 204
    grid_x = 66
    grid_y = 73
    cell = 10
    gap = 3
    step = cell + gap
    colors = palette["levels"]
    items = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">',
        f"<title id=\"title\">Calendário de contribuições públicas de {year} no GitHub</title>",
        f"<desc id=\"desc\">Calendário anual de contribuições de {USERNAME}. Cada quadrado representa um dia; a intensidade da cor corresponde ao nível público de atividade exibido pelo GitHub. Dados atualizados em {date.today().isoformat()}.</desc>",
        f'<rect width="{width}" height="{height}" rx="18" fill="{palette["background"]}" stroke="{palette["border"]}"/>',
        f'<text x="28" y="31" fill="{palette["muted"]}" font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace" font-size="10" font-weight="700" letter-spacing="2">ATIVIDADE PÚBLICA · GITHUB</text>',
        f'<text x="{width - 28}" y="32" text-anchor="end" fill="{palette["text"]}" font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace" font-size="14" font-weight="700">{year}</text>',
        f'<text x="28" y="51" fill="{palette["text"]}" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, sans-serif" font-size="13">Contribuições por dia · cada coluna corresponde a uma semana</text>',
    ]

    for month in range(1, 13):
        month_day = date(year, month, 1)
        week = (month_day - start_day).days // 7
        items.append(
            f'<text x="{grid_x + week * step}" y="67" fill="{palette["muted"]}" '
            'font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace" '
            f'font-size="9">{MONTHS[month - 1]}</text>'
        )

    for row, label in ((1, "seg"), (3, "qua"), (5, "sex")):
        y = grid_y + row * step + 8
        items.append(
            f'<text x="52" y="{y}" text-anchor="end" fill="{palette["muted"]}" '
            'font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace" '
            f'font-size="8">{label}</text>'
        )

    for week in range(week_count):
        for row in range(7):
            day = start_day + timedelta(days=week * 7 + row)
            level = levels.get(day, 0) if day.year == year else 0
            x = grid_x + week * step
            y = grid_y + row * step
            items.append(
                f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="2" '
                f'fill="{colors[level]}" data-date="{day.isoformat()}" data-level="{level}"/>'
            )

    legend_y = 183
    items.extend(
        (
            f'<text x="{grid_x}" y="{legend_y}" fill="{palette["muted"]}" '
            'font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace" font-size="9">menos</text>',
            f'<text x="{grid_x + 59}" y="{legend_y}" fill="{palette["muted"]}" '
            'font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace" font-size="9">mais</text>',
        )
    )
    for index, color in enumerate(colors):
        x = grid_x + 34 + index * 15
        items.append(f'<rect x="{x}" y="{legend_y - 9}" width="10" height="10" rx="2" fill="{color}"/>')

    items.append("</svg>")
    return "\n".join(items) + "\n"


def render_animated_svg(source: Path, animation: str) -> str:
    svg = source.read_text(encoding="utf-8")
    if svg.count("</svg>") != 1:
        raise RuntimeError(f"Expected one SVG closing tag in {source.relative_to(ROOT)}")
    return svg.replace("</svg>", f"{animation}\n</svg>")


def write_generated_files(rendered: dict[Path, str]) -> None:
    for path, content in rendered.items():
        temporary = path.with_suffix(path.suffix + ".tmp")
        temporary.write_text(content, encoding="utf-8", newline="\n")
        temporary.replace(path)
        print(f"Generated {path.relative_to(ROOT)}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate local profile illustrations.")
    parser.add_argument("--only", choices=("activities", "animations"))
    args = parser.parse_args()

    today = date.today()
    generated: dict[Path, str] = {}

    if args.only != "animations":
        levels = fetch_calendar(today.year, today)
        generated.update(
            {
                path: render_calendar(today.year, levels, palette)
                for path, palette in (
                    (ASSETS / "github-activity.svg", PALETTES["light"]),
                    (ASSETS / "github-activity-dark.svg", PALETTES["dark"]),
                )
            }
        )

    if args.only != "activities":
        for static_name, (animated_name, animation) in ANIMATIONS.items():
            source = ASSETS / static_name
            generated[ASSETS / animated_name] = render_animated_svg(source, animation)

    write_generated_files(generated)


if __name__ == "__main__":
    main()
