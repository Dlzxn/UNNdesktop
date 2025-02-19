from BackEnd.get_info.module_get_info import UnnInfoAboutUser
import asyncio

user = UnnInfoAboutUser()
url = user.create_url("s24380047", "2025.02.17", "2025.02.24")
data = asyncio.run(user.get_ruz(url))
print(user.analyse_ruz(data))