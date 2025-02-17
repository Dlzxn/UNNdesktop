from fastapi import APIRouter, Response, Form
from fastapi.responses import RedirectResponse
import json


from BackEnd.localserver.endpoint.models.user_model import User
from BackEnd.logger_cfg.logg_comfig import logger


router_api = APIRouter(prefix="/user")


@router_api.post("/newUser")
async def new_user( re: Response, login: str = Form(...)):
    print("Data in str 14", login)
    with open("data/user/cfg.json", "w") as file:
        json.dump(login, file)
    re.set_cookie(key = "login", value = login)
    return RedirectResponse("/", status_code=302)


@router_api.get("/getUserInfo")
async def get_user_info(re: Response):
    try:
        with open("data/user/cfg.json", "r") as file:
            data: None | dict = json.load(file)
            print(f"DATA: {data}")
        try:
            re.set_cookie(key = "login", value = data.login)

        except Exception as e:
            print(e)
        return data
    except FileNotFoundError:
        logger.error("No cfg.json found")
        return None
    except Exception as e:
        logger.error(e)
        return None

