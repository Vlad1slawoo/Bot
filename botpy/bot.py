import logging
from aiogram import Bot, Dispatcher, executor, types
from cfg import transliterate
import os
logging.basicConfig(level=logging.INFO)
bot = Bot(token=os.environ.get('TOKEN'))
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def greeting (message: types.Message):
    if message.from_user.id == 280704177:
        name = message.from_user.full_name
        logging.info(f'{name} {message.from_user.id} sent{message.text}')
        txt = f'Яррик, выйди с моего бота и не заходи сюда больше'
        await message.reply(txt)
    else:
        name = message.from_user.full_name
        text = f'Здравствуйте, {name}!\nНапишите ваше ФИО для транслитерации в следующем сообщении'
        logging.info(f'{name} {message.from_user.id} sent{message.text}')
        await message.reply(text)

@dp.message_handler()
async def handle_translit(message: types.Message):
    id = message.from_user.id
    name = message.from_user.full_name
    txt = message.text
    logging.info(f'{id=} {name=} sent message:{txt}')
    await message.reply(transliterate(txt))


if __name__ == '__main__':
    executor.start_polling(dp)

