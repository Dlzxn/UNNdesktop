import webview
import os
from jinja2 import Environment, FileSystemLoader

webview.create_window("Приложение с веб-интерфейсом", "https://dlzxndev.ru/")
webview.start()
