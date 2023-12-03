from aiogram import executor, Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import config as cfg
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup


storage = MemoryStorage()
bot = Bot(cfg.TOKEN)
dp = Dispatcher(bot=bot,
                storage=storage)

def get_keyboard() ->ReplyKeyboardMarkup:
  kb = ReplyKeyboardMarkup(resize_keyboard=True)
  kb.add(KeyboardButton("Начать работу!"))
  
  return kb

def get_cancel() -> ReplyKeyboardMarkup:
  return ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton("/cancel"))


class ClientStateGroup(StatesGroup):
  
  photo = State()
  desc = State()



@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message) -> None:
  await message.answer("Добро пожаловать!",
                       reply_markup=get_keyboard())
  
  
@dp.message_handler(commands=["cancel"], state="*")
async def cmd_start(message: types.Message,state: FSMContext) -> None:
  current_state = await state.get_state()
  if current_state is None:
    return 
  await message.reply("Отменил",
                      reply_markup=get_keyboard()) 
  await state.finish()
  
@dp.message_handler(Text(equals="Начать работу!",ignore_case=True),state=None)
async def start_work(mesage: types.Message) -> None:
  await ClientStateGroup.photo.set()
  await mesage.answer("Сначала отправь нам фотографию",
                      reply_markup=get_cancel())
  
@dp.message_handler(lambda message: not message.photo, state = ClientStateGroup.photo)
async def check_photo(message: types.Message):
  return await message.reply("Это не фото!")
  
@dp.message_handler(lambda message:  message.photo, content_types=["photo"],state = ClientStateGroup.photo)
async def load_photo(message: types.Message, state: FSMContext):
  async with state.proxy() as data:
    data["photo"] = message.photo[0].file_id
  
  await ClientStateGroup.next()
  await message.reply("А теперь отправь нам описание")
  

@dp.message_handler(lambda message:  message.text, state = ClientStateGroup.desc)
async def check_photo(message: types.Message, state: FSMContext):
  async with state.proxy() as data:
    data["desc"] = message.text
  
  
  await message.reply("Ваша фотография сохранена") 
  
  async with state.proxy() as data:
    await bot.send_photo(chat_id=message.from_user.id,
                         photo=data["photo"],
                         caption=data["desc"])
    
    
    await state.finish()
   

  
  
  
  


  
  
 
  





if __name__ == "__main__":
  executor.start_polling(dp,
                         skip_updates=True)