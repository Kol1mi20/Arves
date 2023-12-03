import logging 
from aiogram import Bot, Dispatcher, executor, types 
import config as cfg 
import markups as nav 
from db import DataBase 
from db1 import DataBase1
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
from aiogram.types import ReplyKeyboardMarkup,KeyboardButton



 
logging.basicConfig(level=logging.INFO) 

storage = MemoryStorage()
bot = Bot(token=cfg.TOKEN) 
dp = Dispatcher(bot,storage=storage) 

class FsState(StatesGroup):
  copy_to_message = State()

saved_messages ={}

@dp.message_handler()
async def command_start_handler(message: types.Message, state: FSMContext):
  user_id = message.from_user.id
  saved_messages[user_id] = await message.copy_to(chat_id=user_id)
  
   
  await message.answer("Сообщение сохранено!")
  
@dp.message_handler(commands=["send_saved_message"])
async def send_saved_message(message: types.Message):
  user_id = message.from_user.id
  if user_id in saved_messages:
    saved_message = saved_messages[user_id]
    await message.answer("Сохраненное сообщение:")
    await bot.copy_message(chat_id=message.chat.id,from_chat_id = user_id,message_id = saved_message.message_id)
  else:
    await message.answer("У вас нет сохраненных сообщений!")




























































if __name__ == "__main__":
  executor.start_polling(dp, skip_updates=True)