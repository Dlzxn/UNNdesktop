import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse


app = FastAPI()


@app.get("/")
async def main_menu():
    return FileResponse("FrontEnd/templates/main_screen.html")



def start_server():
    uvicorn.run(app, host="0.0.0.0", port=8000)