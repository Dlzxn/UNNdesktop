import aiohttp
from bottle import response


class UnnInfoAboutUser():

    @staticmethod
    async def get_ruz(url: str):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                return await resp.json()

    @staticmethod
    def create_url(login: str, start: str, end: str) -> str | None:
        try:
            print(f"https://portal.unn.ru/ruzapi/schedule/student/{int(login[1:])-24073692}?start={start}&finish={end}&lng=1")
            return f"https://portal.unn.ru/ruzapi/schedule/student/{int(login[1:])-24073692}?start={start}&finish={end}&lng=1"

        except Exception as e:
            print(e)
            return None

    @staticmethod
    def analyse_ruz(data):
        rasp = {}
        print(len(data))
        rasp = []
        for item in data:
            rasp.append([item["dayOfWeekString"], item["auditorium"], item["building"], item["discipline"],
                              item["kindOfWork"], item["lecturer"], item["beginLesson"], item["endLesson"]])
        print(rasp)
        return rasp
