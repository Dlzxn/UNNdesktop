import uvicorn
from fastapi import FastAPI, Cookie
from fastapi.responses import FileResponse
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from fastapi.responses import RedirectResponse
import aiohttp
from typing import Optional

from BackEnd.localserver.Schedule_.schedule import UnnRequest
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
    return FileResponse("FrontEnd/templates/main_screen.html")


@app.get("/login")
async def login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request, "title": "Main"})



@app.get("schedule/{start_date}:{end_date}")
async def schedule(request: Request, start_date: str, end_date: str, cookies:  Optional[str] = Cookie(None)):
    await UnnRequest.new_format(start_date=start_date, end_date=end_date, login = cookies.login)



# @app.get("/about")
# async def info(request: Request):
#     return templates.TemplateResponse("about.html", {"request": request, "title": "About"})



def start_server():
    uvicorn.run(app, host="0.0.0.0", port=8000)