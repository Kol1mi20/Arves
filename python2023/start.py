import logging 
from aiogram import Bot, Dispatcher, executor, types 
import config as cfg 
import markups as nav 
from db import DataBase 
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import Text
 
logging.basicConfig(level=logging.INFO) 

storage = MemoryStorage()
bot = Bot(token=cfg.TOKEN) 
dp = Dispatcher(bot,storage=storage) 
db = DataBase('database') 

async def start9(message: types.Message): 
 if message.chat.type =="private": 
    if not db.user_exists(message.from_user.id): 
      start_command = message.text 
      referrer_id = str(start_command[7:])
      if str(referrer_id) != "":
        if str(referrer_id) != str(message.from_user.id):
          db.add_user(message.from_user.id, referrer_id)
          try:
            await bot.send_message(referrer_id, "По вашей ссылке зарегестрировался новый пользователь!")
          except:
            pass
        else:
          db.add_user(message.from_user.id)
          await bot.send_message(message.from_user.id, "Нельзя регестрироваться по собственной реферальной ссылке!")
      else:
        db.add_user(message.from_user.id)
 
 
    await bot.send_message(message.from_user.id, f"<i><b>MAIN MENU</b></i>\n\n<i><b>{message.from_user.first_name}</b></i>\n<i>/start - <b>обновить</b></i>\n<i><b>Ваш id:</b></i><code>{message.from_user.id}</code>\n\n\n<b>💳Выполнено заданий:</b> 0\n\n\n<b>👥Кол-во рефералов:</b> {db.count_reeferals(message.from_user.id)}\n\n\n💵Заработано на заданиях: 0₽\n💷Заработано на рефералах: 0₽\n🧾Заработано за все время: 0₽\n\n<b>💰Баланс:</b> 0₽\n\n<b>Ваш статус:</b> Обычный\n\n<b>Чтобы получить VIP статус,нужно заработать 2500₽ в боте!</b>\n\n\n<a href ='https://t.me/Arves_Sxem'><i><b>🗣[ПЕРЕЙТИ В КАНАЛ]</b></i></a>\n<a href = 'https://t.me/Arves_Chat'><i><b>🗣[ПЕРЕЙТИ В ЧАТ]</b></i></a>", reply_markup=nav.mainMenu,parse_mode="HTML",disable_web_page_preview=True)