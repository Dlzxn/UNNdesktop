from fastapi import APIRouter
from fastapi.responses import FileResponse

front = APIRouter()

@front.get("/FrontEnd/static/mainstyle.css")
async def mainstyle_css():
    return FileResponse("FrontEnd/static/mainstyle.css")

@front.get("/FrontEnd/img/unn_logo.png")
async def unn_logo():
    return FileResponse("FrontEnd/img/unn_logo.png")

@front.get("/FrontEnd/static/normalize.css")
async def normalize_css():
    return FileResponse("FrontEnd/static/normalize.css")

@front.get("/FrontEnd/img/clouds.png")
async def clouds_png():
    return FileResponse("FrontEnd/img/clouds.png")


@front.get("/static/mainstyle.css")
async def mainstyle_css():
    return FileResponse("FrontEnd/static/mainstyle.css")

@front.get("/FrontEnd/img/profile.svg")
async def profile_svg():
    return FileResponse("FrontEnd/img/profile.svg")


@front.get("/FrontEnd/img/logout.svg")
async def logout_svg():
    return FileResponse("FrontEnd/img/logout.svg")


@front.get("/FrontEnd/img/icon/favicon.ico")
async def favicon_ico():
    return FileResponse("FrontEnd/img/icon/favicon.ico")


@front.get("/static/normalize.css")
async def normalize_css():
    return FileResponse("FrontEnd/static/normalize.css")