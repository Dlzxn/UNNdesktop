from typing import TextIO

from fastapi import APIRouter
import json
from BackEnd.localserver.endpoint.models.user_model import User


router_api = APIRouter(prefix="/user")


@router_api.post("/newUser")
async def new_user(data: User):
    with open("data/user/cfg.json", "w") as file:
        json.dump(data, file)


@router_api.get("/getUserInfo")
async def get_user_info():
    with open("data/user/cfg.json", "r") as file:
        data: None | dict = json.load(file)

    return data
