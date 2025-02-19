import webview
import os
import threading
from jinja2 import Environment, FileSystemLoader


from BackEnd.localserver.server import start_server

webview.create_window("Личный кабинет студента ННГУ", "http://0.0.0.0:8000", width=1200, height=600)
threading.Thread(target = start_server).start()
print("Hello World!")
webview.start()
