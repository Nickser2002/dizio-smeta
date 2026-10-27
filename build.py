"""Собирает index.html для GitHub Pages из исходника сметы (того же файла, что публикуется артефактом).

Исходник написан как фрагмент без <html>/<head>: шрифты и стили переносим в <head>, остальное в <body>.
Запуск: python3 build.py <путь к исходнику>
"""
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).parent
src = pathlib.Path(sys.argv[1]).read_text(encoding="utf-8")

style_end = src.index("</style>") + len("</style>")
head_part, body_part = src[:style_end], src[style_end:]
head_part = re.sub(r"<title>.*?</title>\n?", "", head_part)
head_part = re.sub(r'<meta name="claude:[^"]*"[^>]*>\n?', "", head_part)

TITLE = "Смета для DI·ZIO"
DESCRIPTION = "Брендинг и сайт для DI·ZIO: фиксированная цена, состав работ и дополнительные услуги. Студия Flower, flowerteam.ru"
ICON = (
    "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 29 29'%3E%3Crect width='29' height='29' rx='6' fill='%23000'/%3E"
    "%3Cpath fill='%23FFBB00' d='M25.43 14.01l2.6 2.6h-9.69l-2.6-2.6h9.69zM9.69 11.42l2.6 2.6H2.6L0 11.42h9.69zM14.01 25.43l-2.59 2.6v-9.69l2.59-2.6v9.69zM16.61 9.69l-2.6 2.59V2.6L16.61 0v9.69zM20.24 12.28h-3.63l6.92-6.92h3.63l-6.92 6.92zM15.74 20.42v-3.81l6.92 6.92v3.63l-6.92-6.74zM5.36 4.67V1.04l6.92 6.93v3.45L5.36 4.67zM7.79 15.74h3.63l-6.78 6.93H1.04l6.75-6.93zM12.28 14.01l1.73-1.73 1.73 1.73-1.73 1.73-1.73-1.73z'/%3E%3C/svg%3E"
)

page = f"""<!doctype html>
<html lang="ru">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="robots" content="noindex, nofollow">
<meta name="theme-color" content="#000000">
<title>{TITLE}</title>
<meta name="description" content="{DESCRIPTION}">
<meta property="og:type" content="website">
<meta property="og:title" content="{TITLE}">
<meta property="og:description" content="{DESCRIPTION}">
<link rel="icon" href="{ICON}">
{head_part.strip()}
</head>
<body>
{body_part.strip()}
</body>
</html>
"""
(HERE / "index.html").write_text(page, encoding="utf-8")
print("index.html:", len(page), "символов")
