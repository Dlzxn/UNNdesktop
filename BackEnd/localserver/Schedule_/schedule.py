import asyncio, aiohttp


class UnnRequest:
    """
    Class UnnRequest
    using for get information from API UNN
    """
    def new_format(self, login: str, start_date: str, end_date: str):
        """
        def for generate dynamic URL
        :return: None
        """
        student_number: int = int(login[1:])
        self.format: str = f'https://portal.unn.ru/ruzapi/schedule/student/{student_number-24073692}?start={start_date}&finish={end_date}&lng=1'
        print(f'[INFO] {self.format}')

    async def get_ruz(self):
        """
        def for get info from API UNN
        :return:
        """
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(self.format) as response:
                    print(await response.text(), "fffff")
                    print("RESPONCE")
                    self.json_response = await response.json()
                    self.us = JsonMigration(self.json_response)
        except aiohttp.ClientError as e:
            print(f"[ERROR] Network issue: {e}")
        except Exception as e:
            print(f"[ERROR] JSON Parsing or other issue: {e}")

    @staticmethod
    def get_week_dates():
        """
        def for getting info about start/finish week dates
        :return: None
        """
        # Получаем текущую дату
        today = dt.date.today()

        start_of_week = today - dt.timedelta(days = today.weekday())  # Понедельник текущей недели
        end_of_week = start_of_week + dt.timedelta(days=6)  # Воскресенье текущей недели

        start_date = start_of_week.strftime("%Y.%m.%d")
        end_date = end_of_week.strftime("%Y.%m.%d")

        return start_date, end_date

    async def get_version(self):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get("http://www.unnapi.ru/version") as response:
                    self.unnapi = await response.json()
                    print(self.unnapi)
                    self.version = self.unnapi['version']
                    print(f'[INFO] Version: {self.version}')
        except aiohttp.ClientError as e:
            print(f'[ERROR] Network issue: {e}')
        except Exception as e:
            print(f"[ERROR] other issue(str96): {e}")

    async def mainloop(self):
        """
        create async tasks
        :return:
        """
        task_one: asyncio.Task = asyncio.create_task(self.get_ruz())
        task_two: asyncio.Task = asyncio.create_task(self.get_version())
        await asyncio.gather(task_one, task_two)

    def main(self):
        """
        start asyncio
        :return:
        """
        asyncio.run(self.mainloop())

    def get_next_week_date(self, start_date):
        """
        Вычисляет начало и конец следующей недели от заданной даты и сохраняет в self.

        :param start_date: Дата в формате 'год.месяц.день' (например, '2025.01.15').
        """
        from datetime import datetime, timedelta

        # Преобразуем строку в объект даты
        date_obj = datetime.strptime(start_date, "%Y.%m.%d")

        # Добавляем 7 дней для начала следующей недели
        start_of_next_week = date_obj + timedelta(weeks=1)

        # Считаем конец следующей недели
        end_of_next_week = start_of_next_week + timedelta(days=6)

        # Сохраняем в self
        self.start_date = start_of_next_week.strftime("%Y.%m.%d")
        self.end_date = end_of_next_week.strftime("%Y.%m.%d")

    def get_previous_week_date(self, start_date):
        """
        Вычисляет начало и конец прошлой недели от заданной даты и сохраняет в self.

        :param start_date: Дата в формате 'год.месяц.день' (например, '2025.01.15').
        """
        from datetime import datetime, timedelta

        # Преобразуем строку в объект даты
        date_obj = datetime.strptime(start_date, "%Y.%m.%d")

        # Вычитаем 7 дней для начала предыдущей недели
        start_of_previous_week = date_obj - timedelta(weeks=1)

        # Считаем конец предыдущей недели
        end_of_previous_week = start_of_previous_week + timedelta(days=6)

        # Сохраняем в self
        self.start_date = start_of_previous_week.strftime("%Y.%m.%d")
        self.end_date = end_of_previous_week.strftime("%Y.%m.%d")