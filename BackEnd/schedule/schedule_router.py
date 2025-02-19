from fastapi import APIRouter, Cookie, Request
from typing import Optional
from BackEnd.localserver.Schedule_.schedule import UnnRequest

router_schedule = APIRouter(prefix="/schedule", tags=["schedule"])


@router_schedule.get()
async def schedule_get(request: Request):
    schedule = UnnRequest()

