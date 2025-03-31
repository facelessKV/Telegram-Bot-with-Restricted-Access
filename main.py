import random
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command, Text
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
import asyncio
import logging

# Импортируем настройки из config.py
from config import BOT_TOKEN, ALLOWED_USERS, DAILY_CODES

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Создаем клавиатуру с кнопкой "Получить код дня"
def get_keyboard():
    kb = [[KeyboardButton(text="Получить код дня")]]
    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    return keyboard

# Обработчик команды /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    user_id = message.from_user.id
    
    # Проверяем, есть ли пользователь в списке разрешенных
    if user_id in ALLOWED_USERS:
        await message.answer(
            "Добро пожаловать! Используйте кнопку ниже для получения кода дня.", 
            reply_markup=get_keyboard()
        )
    else:
        # Если пользователя нет в списке разрешенных
        await message.answer("Нет доступа. Обратитесь к администратору бота.")
        # Логируем попытку несанкционированного доступа
        logging.warning(f"Попытка доступа от неразрешенного пользователя. ID: {user_id}, "
                        f"Имя: {message.from_user.full_name}, Username: @{message.from_user.username}")

# Обработчик нажатия на кнопку "Получить код дня"
@dp.message(Text("Получить код дня"))
async def get_daily_code(message: types.Message):
    user_id = message.from_user.id
    
    # Дополнительная проверка - пользователь все еще в списке разрешенных
    if user_id in ALLOWED_USERS:
        # Выбираем случайную фразу из списка
        random_code = random.choice(DAILY_CODES)
        await message.answer(random_code, reply_markup=get_keyboard())
    else:
        # Если каким-то образом неразрешенный пользователь получил клавиатуру
        await message.answer("Нет доступа. Обратитесь к администратору бота.")

# Запуск бота
async def main():
    # Удаляем все обновления, накопившиеся за время отключения бота
    await bot.delete_webhook(drop_pending_updates=True)
    # Запускаем бота
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())