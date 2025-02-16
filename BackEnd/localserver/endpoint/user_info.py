from fastapi import APIRouter
import json


from BackEnd.localserver.endpoint.models.user_model import User
from BackEnd.logger_cfg.logg_comfig import logger


router_api = APIRouter(prefix="/user")


@router_api.post("/newUser")
async def new_user(data: User):
    print(data)
    with open("data/user/cfg.json", "w") as file:
        json.dump(data, file)


@router_api.get("/getUserInfo")
async def get_user_info():
    try:
        with open("data/user/cfg.json", "r") as file:
            data: None | dict = json.load(file)

        return data
    except FileNotFoundError:
        logger.error("No cfg.json found")
        return None
    except Exception as e:
        logger.error(e)
        return None