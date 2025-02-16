import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request


app = FastAPI()

templates = Jinja2Templates(directory="FrontEnd/templates")

@app.get("/")
async def main_menu(request: Request):
    return templates.TemplateResponse("main_screen.html", {"request": request, "title": "Main"})


def start_server():
    uvicorn.run(app, host="0.0.0.0", port=8000)