from fastapi import APIRouter, Cookie, Request
from fastapi.templating import Jinja2Templates
from typing import Optional


from BackEnd.get_info.module_get_info import UnnInfoAboutUser


templates = Jinja2Templates(directory="templates")


router_schedule = APIRouter(prefix="/schedule", tags=["schedule"])


@router_schedule.get("{start}:{end}")
async def schedule_get(request: Request, start: str, end: str):
    schedule = UnnInfoAboutUser()
    url = schedule.create_url("s23332", start, end)
    ruz_on = schedule.get_ruz(url)
    full_ruz= schedule.analyse_ruz(ruz_on)
    if ruz_on:
        return templates.TemplateResponse("schedule.html", context={"ruz": full_ruz})
    else:
        return {"ruz": None}


