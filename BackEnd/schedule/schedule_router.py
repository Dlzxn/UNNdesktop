from fastapi import APIRouter, Cookie, Request
from typing import Optional
from BackEnd.get_info.module_get_info import UnnInfoAboutUser

router_schedule = APIRouter(prefix="/schedule", tags=["schedule"])


@router_schedule.get("{start}:{end}")
async def schedule_get(request: Request, start: str, end: str):
    schedule = UnnInfoAboutUser()
    url = schedule.create_url("s23332", start, end)
    ruz_on = schedule.get_ruz(url)
    if ruz_on:
        return {"ruz": schedule.analyse_ruz(ruz_on)}
    else:
        return {"ruz": None}


