import uvicorn
from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def main_menu():
    return {"message": "Hello World"}



def start_server():
    uvicorn.run(app, host="0.0.0.0", port=8000)