import logging

# Настройка логгера
logger = logging.getLogger('logger')  # Создаем логгер с именем 'my_logger'
logger.setLevel(logging.DEBUG)  # Устанавливаем уровень логирования, все сообщения от DEBUG и выше будут логироваться

# Создаем обработчик для записи логов в файл
file_handler = logging.FileHandler('logs/app.log')
file_handler.setLevel(logging.DEBUG)  # Логируем все сообщения от DEBUG и выше в файл

# Создаем обработчик для вывода логов в консоль
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)  # Логируем сообщения от INFO и выше в консоль

# Создаем форматтер для логов
formatter = logging.Formatter('%(asctime)s - %(name)s - [%(levelname)s] - %(message)s')
file_handler.setFormatter(formatter)  # Применяем форматтер к обработчику файла
console_handler.setFormatter(formatter)  # Применяем форматтер к обработчику консоли

# Добавляем обработчики к логгеру
logger.addHandler(file_handler)
logger.addHandler(console_handler)

