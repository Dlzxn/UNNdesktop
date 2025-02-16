import webview
import os
from jinja2 import Environment, FileSystemLoader


from localserver.server import start_server

webview.create_window("Приложение с веб-интерфейсом", "http://0.0.0.0:8000")
start_server()
webview.start()
