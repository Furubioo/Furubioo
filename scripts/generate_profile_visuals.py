from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from urllib.error import HTTPError
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
USERNAME = "Furubioo"
REPOSITORIES = (
    ("Site ONG Partilhar", "SiteOngPartilhar"),
    ("Sistema de Cinema", "Sistema-de-Cinema-JAVA-"),
    ("Acervo acadêmico", "registro-academico-ciencia-da-computacao"),
)
BACKGROUND = "#07131a"
PANEL = "#0c1f29"
NODE = "#102a36"
TEXT = "#f4f9fb"
MUTED = "#c2d3da"
LINE = "#52717d"
ACCENT = "#8fd3ff"
FOCUS = "#7ee8c1"
WARM = "#ffe09a"


@dataclass(frozen=True)
class ProjectDates:
    title: str
    repository: str
    first: date
    latest: date


def fetch_json(url: str) -> tuple[object, str | None]:
    request = Request(
        url,
        headers={
            "Accept": "application/vnd.github+json",
            "User-Agent": "furubioo-profile-timeline/1.0",
            "X-GitHub-Api-Version": "2022-11-28",
        },
    )
    try:
        with urlopen(request, timeout=30) as response:
            if response.status != 200:
                raise RuntimeError(f"GitHub API returned HTTP {response.status} for {url}")
            return json.loads(response.read()), response.headers.get("Link")
    except HTTPError as error:
        raise RuntimeError(f"GitHub API returned HTTP {error.code} for {url}") from error


def last_page_url(link_header: str | None) -> str | None:
    if link_header is None:
        return None
    for part in link_header.split(","):
        match = re.match(r"\s*<([^>]+)>\s*;\s*rel=\"last\"", part)
        if match:
            return match.group(1)
    return None


def commit_date(commit: object, repository: str, label: str) -> date:
    try:
        value = commit["commit"]["committer"]["date"]
        return date.fromisoformat(value[:10])
    except (KeyError, TypeError, ValueError) as error:
        raise RuntimeError(f"Missing committer date for {label} in {repository}") from error


def fetch_project_dates() -> list[ProjectDates]:
    dates: list[ProjectDates] = []
    for title, repository in REPOSITORIES:
        url = f"https://api.github.com/repos/{USERNAME}/{repository}/commits?per_page=1"
        newest_page, links = fetch_json(url)
        if not isinstance(newest_page, list) or not newest_page:
            raise RuntimeError(f"No public commits found in {repository}")
        first_url = last_page_url(links)
        oldest_page = fetch_json(first_url)[0] if first_url else newest_page
        if not isinstance(oldest_page, list) or not oldest_page:
            raise RuntimeError(f"Could not read the oldest commit in {repository}")
        dates.append(
            ProjectDates(
                title=title,
                repository=repository,
                first=commit_date(oldest_page[0], repository, "oldest commit"),
                latest=commit_date(newest_page[0], repository, "latest commit"),
            )
        )
    return dates


def render_timeline(dates: list[ProjectDates], updated: date, mobile: bool) -> str:
    if not dates:
        raise ValueError("At least one repository is required to render the timeline")
    earliest = min(project.first for project in dates)
    latest = max(project.latest for project in dates)
    span = max(1, (latest - earliest).days)

    if mobile:
        width, height = 400, 500
        title_size, body_size = 22, 14
        left, right = 28, 360
        row_top, row_step = 136, 112
        label_x = 28
        first_y, last_y = 28, 50
    else:
        width, height = 1200, 450
        title_size, body_size = 28, 22
        left, right = 300, 1120
        row_top, row_step = 132, 78
        label_x = 36
        first_y, last_y = 178, 207

    def position(day: date) -> float:
        return left + ((day - earliest).days / span) * (right - left)

    items = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">',
        f"<title id=\"title\">Linha do tempo dos projetos de {USERNAME}</title>",
        f"<desc id=\"desc\">Primeiro e último commit por repositório, com datas de committer verificadas na API pública do GitHub. Atualizado em {updated.isoformat()}.</desc>",
        f'<rect width="{width}" height="{height}" rx="20" fill="{BACKGROUND}"/>',
        f'<text x="{label_x}" y="48" fill="{TEXT}" font-family="Arial,sans-serif" font-size="{title_size}" font-weight="700">Histórico dos projetos</text>',
        f'<text x="{label_x}" y="78" fill="{MUTED}" font-family="Arial,sans-serif" font-size="{body_size}">Primeiro e último commit · atualizado em {updated.isoformat()}</text>',
    ]

    for index, project in enumerate(dates):
        center_y = row_top + index * row_step
        start_x = position(project.first)
        end_x = position(project.latest)
        if project.latest < project.first:
            raise ValueError(f"Latest commit predates first commit for {project.repository}")
        if end_x - start_x < 14:
            midpoint = (start_x + end_x) / 2
            start_x = midpoint - 7
            end_x = midpoint + 7
        items.extend(
            (
                f'<text x="{label_x}" y="{center_y - 20 if mobile else center_y + 7}" fill="{TEXT}" font-family="Arial,sans-serif" font-size="{body_size}" font-weight="700">{project.title}</text>',
                f'<path d="M{left} {center_y}H{right}" stroke="{LINE}" stroke-width="4"/>',
                f'<path d="M{start_x:.1f} {center_y}H{end_x:.1f}" stroke="{ACCENT}" stroke-width="6" stroke-linecap="round"/>',
                f'<circle cx="{start_x:.1f}" cy="{center_y}" r="9" fill="{FOCUS}" stroke="{TEXT}" stroke-width="2"/>',
                f'<rect x="{end_x - 8:.1f}" y="{center_y - 8}" width="16" height="16" rx="2" fill="{WARM}" stroke="{BACKGROUND}" stroke-width="2"/>',
            )
        )
        if mobile:
            items.append(
                f'<text x="{label_x}" y="{center_y + first_y}" fill="{MUTED}" font-family="Arial,sans-serif" font-size="{body_size}">● {project.first:%d/%m/%Y}</text>'
            )
            items.append(
                f'<text x="{label_x + 176}" y="{center_y + last_y}" fill="{MUTED}" font-family="Arial,sans-serif" font-size="{body_size}">■ {project.latest:%d/%m/%Y}</text>'
            )
        else:
            items.append(
                f'<text x="{left}" y="{center_y + 32}" fill="{MUTED}" font-family="Arial,sans-serif" font-size="{body_size}">● Primeiro: {project.first:%d/%m/%Y}</text>'
            )
            items.append(
                f'<text x="{left + 290}" y="{center_y + 32}" fill="{MUTED}" font-family="Arial,sans-serif" font-size="{body_size}">■ Último: {project.latest:%d/%m/%Y}</text>'
            )

    legend_y = height - 22
    items.extend(
        (
            f'<circle cx="{label_x + 8}" cy="{legend_y - 6}" r="7" fill="{FOCUS}"/>',
            f'<text x="{label_x + 22}" y="{legend_y}" fill="{MUTED}" font-family="Arial,sans-serif" font-size="{body_size}">primeiro commit</text>',
            f'<rect x="{label_x + 190}" y="{legend_y - 13}" width="14" height="14" rx="2" fill="{WARM}"/>',
            f'<text x="{label_x + 212}" y="{legend_y}" fill="{MUTED}" font-family="Arial,sans-serif" font-size="{body_size}">último commit</text>',
            "</svg>",
        )
    )
    return "\n".join(items) + "\n"


def animation_motion(
    color: str,
    path: str,
    duration: str,
    radius: int,
    begin: str = "0s",
    opacity: str = "1;1;0;0;1",
    key_times: str = "0;0.76;0.84;0.96;1",
    motion_key_points: str | None = None,
    motion_key_times: str | None = None,
) -> str:
    motion_timing = ""
    if motion_key_points is not None and motion_key_times is not None:
        motion_timing = (
            f' keyPoints="{motion_key_points}" keyTimes="{motion_key_times}" calcMode="linear"'
        )
    return f"""<circle r="{radius}" fill="{color}" stroke="{TEXT}" stroke-width="3" aria-hidden="true">
  <animateMotion path="{path}" dur="{duration}" begin="{begin}"{motion_timing} repeatCount="indefinite"/>
  <animate attributeName="opacity" values="{opacity}" keyTimes="{key_times}" dur="{duration}" begin="{begin}" repeatCount="indefinite"/>
</circle>"""


def targeted_animation(
    element_id: str,
    attribute: str,
    values: str,
    key_times: str,
    duration: str,
    begin: str = "0s",
    calc_mode: str | None = None,
) -> str:
    mode = f' calcMode="{calc_mode}"' if calc_mode else ""
    return (
        f'<animate href="#{element_id}" attributeName="{attribute}" values="{values}" '
        f'keyTimes="{key_times}" dur="{duration}" begin="{begin}"{mode} repeatCount="indefinite"/>'
    )


def hero_animation(mobile: bool) -> str:
    development_path = "M86 342 H104 H156 H174 H226 H244 H296 H314 H366" if mobile else "M680 183 H710 H850 H880 H1020 H1050 H1190 H1220 H1360"
    data_path = "M132 612 H138 H262 H268" if mobile else "M790 458 H820 H1120 H1150"
    cycle = "10s"
    ids = (
        ("development-card", "data-card", "chip-development", "chip-data")
        if mobile
        else ("development-card", "data-card", "chip-development", "chip-data")
    )
    return "\n".join(
        (
            animation_motion(
                FOCUS,
                development_path,
                cycle,
                9 if mobile else 12,
                opacity="1;1;0;0;1",
                key_times="0;.34;.4;.94;1",
                motion_key_points="0;1;1",
                motion_key_times="0;.34;1",
            ),
            animation_motion(
                ACCENT,
                data_path,
                cycle,
                8 if mobile else 11,
                "5s",
                opacity="1;1;0;0;1",
                key_times="0;.34;.4;.94;1",
                motion_key_points="0;1;1",
                motion_key_times="0;.34;1",
            ),
            targeted_animation(ids[0], "stroke-width", "3;4;4;3", "0;.05;.34;1", cycle),
            targeted_animation(ids[1], "stroke-width", "2;2;4;4;2", "0;.44;.5;.84;1", cycle),
            targeted_animation(ids[2], "stroke-width", "3;4;4;3", "0;.05;.34;1", cycle),
            targeted_animation(ids[3], "stroke-width", "2;2;4;4;2", "0;.44;.5;.84;1", cycle),
        )
    )


def cinema_animation(mobile: bool) -> str:
    if mobile:
        route_common = "M200 158 V256 H360 V544 H200 V598 V683"
        web_down = "M0 0 V484"
        web_up = "M0 0 V-484"
        duration = "18s"
    else:
        route_common = "M367 205 V295 V391 V405 H170 H367 H564 H672 V510 H367 V570 V675"
        web_down = "M0 0 V458"
        web_up = "M0 0 V-458"
        duration = "18s"
    radius = 8 if mobile else 13
    tokens = [
        animation_motion(
            FOCUS,
            route_common,
            duration,
            radius,
            opacity="1;1;0;0;1",
            key_times="0;.76;.84;.96;1",
            motion_key_points="0;1;1",
            motion_key_times="0;.76;1",
        )
    ]
    request_origin = (334, 866) if mobile else (1335, 219)
    response_origin = (352, 1343) if mobile else (1358, 665)
    tokens.extend(
        (
            f'<circle class="request-token" cx="{request_origin[0]}" cy="{request_origin[1]}" r="{radius}" fill="{ACCENT}" stroke="{TEXT}" stroke-width="3"><animateMotion path="{web_down}" dur="{duration}" keyPoints="0;0;1;1;1" keyTimes="0;.02;.72;.76;1" calcMode="linear" repeatCount="indefinite"/><animate attributeName="opacity" values="1;1;1;0;0" keyTimes="0;.72;.76;.8;1" dur="{duration}" repeatCount="indefinite"/></circle>',
            f'<rect class="response-token" x="{response_origin[0]}" y="{response_origin[1]}" width="{radius * 2}" height="{radius * 2}" rx="3" fill="{WARM}" stroke="{BACKGROUND}" stroke-width="2"><animateMotion path="{web_up}" dur="{duration}" keyPoints="0;0;1;1;1" keyTimes="0;.48;.78;.82;1" calcMode="linear" repeatCount="indefinite"/><animate attributeName="opacity" values="0;0;1;1;0;0" keyTimes="0;.48;.52;.78;.82;1" dur="{duration}" repeatCount="indefinite"/></rect>',
        )
    )
    if mobile:
        strategy_phases = (
            ("strategy-common", "2;2;4;4;2;2", "0;.39;.40;.43;.44;1"),
            ("strategy-critical", "2;2;4;4;2;2", "0;.50;.51;.54;.55;1"),
            ("strategy-student", "2;2;4;4;2;2", "0;.62;.63;.66;.67;1"),
        )
    else:
        strategy_phases = (
            ("strategy-common", "2;2;4;4;2;2", "0;.29;.30;.34;.35;1"),
            ("strategy-critical", "2;2;4;4;2;2", "0;.42;.43;.47;.48;1"),
            ("strategy-student", "2;2;4;4;2;2", "0;.55;.56;.60;.61;1"),
        )
    for element_id, values, key_times in strategy_phases:
        tokens.append(
            targeted_animation(element_id, "stroke-width", values, key_times, duration)
        )
    return "\n".join(tokens)


def partilhar_animation(mobile: bool) -> str:
    if mobile:
        path = "M40 144 H36 V238 H40 V332 H36 V426 H40 V520 H36 V614 H40 V708 H36"
        duration = "14s"
        ids = (
            "section-home",
            "section-about",
            "section-services",
            "section-gallery",
            "section-volunteer",
            "section-testimonials",
            "section-donations",
        )
    else:
        path = "M103 153 H174 V213 H197 V153 H339 V213 H362 V153 H504 V213 H527 V153 H669 V213 H692 V153 H834 V213 H857 V153 H999 V213 H1022 V153 H1164 V213"
        duration = "14s"
        ids = (
            "section-home",
            "section-about",
            "section-services",
            "section-gallery",
            "section-volunteer",
            "section-testimonials",
            "section-donations",
        )
    animations = [animation_motion(ACCENT, path, duration, 7 if mobile else 9)]
    for index, element_id in enumerate(ids):
        start = max(index * 0.12, 0.01)
        active = start + 0.01
        end = active + 0.07
        reset = end + 0.01
        key_times = f"0;{start:.2f};{active:.2f};{end:.2f};{reset:.2f};1"
        animations.append(
            targeted_animation(
                element_id,
                "stroke-width",
                "2;2;4;4;2;2",
                key_times,
                duration,
            )
        )
    dot_duration = "3s"
    for index in range(1, 4):
        delay = f"{index - 1}s"
        animations.append(
            targeted_animation(
                f"testimonial-dot-{index}",
                "opacity",
                "1;.35;1",
                "0;.5;1",
                dot_duration,
                delay,
            )
        )
    return "\n".join(animations)


def lab_animation(mobile: bool) -> str:
    if mobile:
        peterson_scene_duration = "24s"
        panel_id_groups = (
            ("parser", "1;1;0;0;1", "0;.16;.18;.98;1"),
            ("gpio", "0;0;1;1;0;0", "0;.16;.18;.48;.50;1"),
            ("peterson", "0;0;1;1;0;0", "0;.48;.50;.96;.98;1"),
        )
    else:
        peterson_scene_duration = "24s"
        panel_id_groups = (
            ("parser", "1;1;0;0;1", "0;.16;.18;.98;1"),
            ("gpio", "0;0;1;1;0;0", "0;.16;.18;.48;.50;1"),
            ("peterson", "0;0;1;1;0;0", "0;.48;.50;.96;.98;1"),
        )
    animations = []
    for panel_name, values, times in panel_id_groups:
        animations.append(
            f'<animate href="#panel-{panel_name}" attributeName="opacity" values="{values}" keyTimes="{times}" calcMode="discrete" dur="{peterson_scene_duration}" repeatCount="indefinite"/>'
        )

    parser_steps = (
        ("parser-root", ".02", ".05"),
        ("parser-left", ".05", ".08"),
        ("parser-sum", ".08", ".11"),
        ("parser-a", ".11", ".14"),
        ("parser-constant", ".14", ".17"),
    )
    for element_id, start, end in parser_steps:
        start_value, end_value = float(start), float(end)
        animations.append(
            targeted_animation(
                element_id,
                "stroke",
                f"{LINE};{LINE};{FOCUS};{FOCUS};{LINE};{LINE}",
                f"0;{start_value:.2f};{start_value + .01:.2f};{end_value:.2f};{end_value + .01:.2f};1",
                peterson_scene_duration,
            )
        )

    for led_id, values, times in (
        ("led-18", f"{NODE};{NODE};{WARM};{WARM};{NODE};{NODE}", "0;.20;.21;.23;.24;1"),
        ("led-23", f"{NODE};{NODE};{WARM};{WARM};{NODE};{NODE}", "0;.24;.25;.27;.28;1"),
        ("led-24", f"{NODE};{NODE};{WARM};{WARM};{NODE};{NODE}", "0;.28;.29;.31;.32;1"),
    ):
        animations.append(
            targeted_animation(led_id, "fill", values, times, peterson_scene_duration)
        )
    for button_id, start in (("button-27", ".33"), ("button-17", ".37"), ("button-22", ".41")):
        start_value = float(start)
        end_value = start_value + 0.04
        animations.append(
            targeted_animation(
                button_id,
                "fill",
                f"{NODE};{NODE};{WARM};{WARM};{NODE};{NODE}",
                f"0;{start_value:.2f};{start_value + .01:.2f};{end_value:.2f};{end_value + .01:.2f};1",
                peterson_scene_duration,
            )
        )
    animations.append(
        targeted_animation(
            "gpio-correct",
            "stroke-width",
            "2;2;4;4;2;2",
            "0;.44;.45;.46;.47;1",
            peterson_scene_duration,
        )
    )
    animations.append(
        targeted_animation(
            "gpio-incorrect",
            "stroke-width",
            "2;2;4;4;2;2",
            "0;.46;.47;.48;.49;1",
            peterson_scene_duration,
        )
    )

    peterson_state = (
        ("peterson-t0", f"{LINE};{LINE};{FOCUS};{FOCUS};{LINE};{LINE}", "0;.50;.52;.72;.74;1"),
        ("peterson-t1", f"{LINE};{LINE};{LINE};{FOCUS};{FOCUS};{LINE}", "0;.72;.74;.96;.98;1"),
    )
    for element_id, values, times in peterson_state:
        animations.append(
            targeted_animation(element_id, "stroke", values, times, peterson_scene_duration)
        )
    animations.extend(
        (
            targeted_animation(
                "peterson-t0",
                "fill",
                "#12372c;#12372c;#12372c;#102a36;#102a36",
                "0;.72;.74;.98;1",
                peterson_scene_duration,
                calc_mode="discrete",
            ),
            targeted_animation(
                "peterson-t1",
                "fill",
                "#102a36;#102a36;#12372c;#12372c;#102a36",
                "0;.72;.74;.98;1",
                peterson_scene_duration,
                calc_mode="discrete",
            ),
        )
    )
    state_visibility = (
        ("peterson-t0-active", "0;0;1;0;0;0", "peterson-t0-wait", "1;1;0;1;1;1", "0;.50;.52;.72;.74;1"),
        ("peterson-t1-wait", "0;0;1;0;0;0", "peterson-t1-active", "1;1;0;1;1;1", "0;.50;.52;.72;.74;1"),
        ("peterson-t0-critical-note", "0;0;1;0;0;0", "peterson-t0-wait-note", "1;1;0;1;1;1", "0;.50;.52;.72;.74;1"),
        ("peterson-yield", "0;0;1;0;0;0", "peterson-t1-active-note", "1;1;0;1;1;1", "0;.50;.52;.72;.74;1"),
        ("peterson-t1-active", "0;0;0;1;1;0", "peterson-t1-wait", "1;1;1;0;0;1", "0;.72;.74;.96;.98;1"),
        ("peterson-t0-wait", "0;0;0;1;1;0", "peterson-t0-active", "1;1;1;0;0;1", "0;.72;.74;.96;.98;1"),
        ("peterson-t0-wait-note", "0;0;0;1;1;0", "peterson-t0-critical-note", "1;1;1;0;0;1", "0;.72;.74;.96;.98;1"),
        ("peterson-t1-active-note", "0;0;0;1;1;0", "peterson-yield", "1;1;1;0;0;1", "0;.72;.74;.96;.98;1"),
        ("peterson-turn-one", "0;0;0;1;1;0", "peterson-turn-zero", "1;1;1;0;0;1", "0;.72;.74;.96;.98;1"),
    )
    for visible_id, visible_values, hidden_id, hidden_values, key_times in state_visibility:
        animations.append(
            targeted_animation(visible_id, "opacity", visible_values, key_times, peterson_scene_duration, calc_mode="discrete")
        )
        animations.append(
            targeted_animation(hidden_id, "opacity", hidden_values, key_times, peterson_scene_duration, calc_mode="discrete")
        )
    return "\n".join(animations)


ANIMATION_BUILDERS = {
    "hero-static.svg": ("hero.svg", lambda: hero_animation(False)),
    "hero-mobile-static.svg": ("hero-mobile.svg", lambda: hero_animation(True)),
    "cinema-flow-static.svg": ("cinema-flow.svg", lambda: cinema_animation(False)),
    "cinema-flow-mobile-static.svg": ("cinema-flow-mobile.svg", lambda: cinema_animation(True)),
    "partilhar-overview.svg": ("partilhar-overview-animated.svg", lambda: partilhar_animation(False)),
    "partilhar-overview-mobile.svg": (
        "partilhar-overview-mobile-animated.svg",
        lambda: partilhar_animation(True),
    ),
    "lab-static.svg": ("lab.svg", lambda: lab_animation(False)),
    "lab-mobile-static.svg": ("lab-mobile.svg", lambda: lab_animation(True)),
}


def render_animated_svg(source: Path, animation: str) -> str:
    svg = source.read_text(encoding="utf-8")
    if svg.count("</svg>") != 1:
        raise RuntimeError(f"Expected one SVG closing tag in {source.relative_to(ROOT)}")
    return svg.replace("</svg>", f'<g aria-hidden="true">{animation}</g>\n</svg>')


def write_generated_files(rendered: dict[Path, str]) -> None:
    for path, content in rendered.items():
        temporary = path.with_suffix(path.suffix + ".tmp")
        temporary.write_text(content, encoding="utf-8", newline="\n")
        temporary.replace(path)
        print(f"Generated {path.relative_to(ROOT)}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate the profile timeline and animated SVGs.")
    parser.add_argument("--only", choices=("timeline", "animations"))
    args = parser.parse_args()
    generated: dict[Path, str] = {}

    if args.only != "animations":
        projects = fetch_project_dates()
        today = date.today()
        generated[ASSETS / "project-timeline.svg"] = render_timeline(projects, today, mobile=False)
        generated[ASSETS / "project-timeline-mobile.svg"] = render_timeline(projects, today, mobile=True)

    if args.only != "timeline":
        for static_name, (animated_name, builder) in ANIMATION_BUILDERS.items():
            generated[ASSETS / animated_name] = render_animated_svg(
                ASSETS / static_name, builder()
            )

    write_generated_files(generated)


if __name__ == "__main__":
    main()
