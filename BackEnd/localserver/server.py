import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from fastapi.responses import RedirectResponse
import aiohttp


from BackEnd.localserver.endpoint.user_info import router_api
app = FastAPI()
app.include_router(router_api)

templates = Jinja2Templates(directory="FrontEnd/templates")

@app.get("/")
async def main_menu(request: Request):
    async with aiohttp.ClientSession() as session:
        data = await session.get("http://0.0.0.0:8000/user/getUserInfo")
        print("This is data", await data.json())
    if await data.json():
        return RedirectResponse(url="/main")
    else:
        return RedirectResponse(url="/login")

@app.get("/main")
async def main(request: Request):
    return templates.TemplateResponse("main_screen.html", {"request": request, "data": data})


@app.get("/login")
async def login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request, "title": "Main"})



def start_server():
    uvicorn.run(app, host="0.0.0.0", port=8000)