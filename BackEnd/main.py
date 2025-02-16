import webview
import os
from jinja2 import Environment, FileSystemLoader


def render_template(template_name, **context):
    """Генерация HTML через Jinja2"""
    env = Environment(loader=FileSystemLoader("templates"))
    template = env.get_template(template_name)
    output_path = os.path.abspath(f"temp_{template_name}")

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(template.render(context))

    return output_path


# Рендерим HTML
html_file = render_template("index.html", username="Пользователь")

# Запускаем приложение с веб-интерфейсом
webview.create_window("Приложение с веб-интерфейсом", html_file)
webview.start()
