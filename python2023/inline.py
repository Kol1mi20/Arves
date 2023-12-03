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

global name1
global name2
global name3
global name4

class fsstate(StatesGroup):
  photo = State()
  audio = State()
  video = State()
  file = State()
  all_files = State()
  desc1 = State()
  desc2 = State()
  desc3 = State()
  knopka = State()
  daornet = State()
  url_knpk = State()
  all_knpk = State()
  podtverdut_rass = State()
  
  
  
  
  
@dp.message_handler(commands=["start"])
async  def start(message: types.Message, state: FSMContext):
  await message.answer("Привет,cначала отправь нам фото,видео,аудио(не текст,текст отправишь позже)!")
  
  
  
@dp.message_handler(lambda message: not message.photo)
async def check_photo1(message: types.Message):
  return await message.reply("Пожалуйста,отправьте только фото,видео или аудио!")

@dp.message_handler(lambda message:  message.photo, content_types=["photo"])
async def load_photo1(message: types.Message, state: FSMContext):
  async with state.proxy() as data:
    data["photo"] = message.photo[0].file_id
    await message.reply("Фотография сохранена!")
    await message.answer("А теперь отправь описание к данной фотографии!")
    await state.set_state(fsstate.desc1)

@dp.message_handler(lambda message: not message.video)
async def check_photo2(message: types.Message):
  return await message.reply("Пожалуйста,отправьте только фото,видео или аудио!")

@dp.message_handler(lambda message:  message.video, content_types=["video"])
async def load_photo2(message: types.Message, state: FSMContext):
  async with state.proxy() as data:
    data["video"] = message.video.file_id
    await message.reply("Видео сохранено!")
    await message.answer("А теперь отправь описание к данному видео!")
    await state.set_state(fsstate.desc2)

@dp.message_handler(lambda message: not message.audio)
async def check_photo3(message: types.Message):
  return await message.reply("Пожалуйста,отправьте только фото,видео или аудио!")

@dp.message_handler(lambda message:  message.audio, content_types=["audio"])
async def load_photo3(message: types.Message, state: FSMContext):
  async with state.proxy() as data:
    data["audio"] = message.audio.file_id
    await message.reply("Аудио-файл сохранен!")
    await message.answer("А теперь отправь описание к данному аудио-файлу!")
    await state.set_state(fsstate.desc3)
    




@dp.message_handler(lambda message:  message.text, state = fsstate.desc1)
async def check_photo5(message: types.Message, state: FSMContext):
   async with state.proxy() as data:
    data["desc"] = message.text
  
   
   await message.answer("Текст для рассылки сохранен!")
    
     
   async with state.proxy() as data:
       await bot.send_photo(chat_id=message.from_user.id,
                            photo=data["photo"],
                            caption=data["desc"])
       await message.answer("Добавить кнопку?",reply_markup=nav.inl)
   await state.set_state(fsstate.knopka)
                            
       
       
    



@dp.message_handler(lambda message:  message.text, state = fsstate.desc2)
async def check_photo7(message: types.Message, state: FSMContext):
  async with state.proxy() as data1:
    data1["desc2"] = message.text
    await message.answer("Текст для рассылки сохранен!") 
    async with state.proxy() as data61:
       await bot.send_video(chat_id=message.from_user.id,
                            video=data61["video"],
                            caption=data61["desc2"])
       await message.answer("Добавить кнопку?",reply_markup=nav.inl)
    await state.set_state(fsstate.knopka)
                            
       
    



@dp.message_handler(lambda message:  message.text, state = fsstate.desc3)
async def check_photo9(message: types.Message, state: FSMContext):
  async with state.proxy() as data5:
    data5["desc"] = message.text
    await message.answer("Текст для рассылки сохранен!") 
    async with state.proxy() as data58:
       await bot.send_audio(chat_id=message.from_user.id,
                            audio=data58["audio"],
                            caption=data58["desc"])
       
       await message.answer("Добавить кнопку?",reply_markup=nav.inl)
    await state.set_state(fsstate.knopka)
    
    
@dp.callback_query_handler(text="add_button", state=fsstate.knopka)
async def inlane(callback: types.CallbackQuery,state: FSMContext):

  await callback.message.answer("Введите текст кнопки!")
  await callback.answer()
  await state.set_state(fsstate.url_knpk)
  
@dp.message_handler(content_types=["text"],state=fsstate.url_knpk)
async def sendall4(message: types.Message,state: FSMContext):
  global jokol
  jokol = message.text
 
  await message.answer("Введите URl для кнопки!")
  await state.set_state(fsstate.all_knpk)
  
@dp.message_handler(content_types=["text"],state=fsstate.all_knpk)
async def sendall4(message: types.Message,state: FSMContext):
  global data58
  global url_knpk
  url_knpk = message.text
  knmnv = InlineKeyboardMarkup(row_width=1)
  knmv1 = InlineKeyboardButton(text=jokol, url=url_knpk)
  knmnv.add(knmv1)
  
  await message.answer("Подтвердить рассылку?", reply_markup=nav.hlfgk)
  await state.set_state(fsstate.podtverdut_rass)
  

  
@dp.callback_query_handler(text="no_button", state=fsstate.knopka)
async def inlane(callback: types.CallbackQuery,state: FSMContext):
  pass      


  
  
 
  
  

  
  

  
  
#@dp.message_handler(content_types=["text"])
#async def rass_text(message: types.Message, state: FSMContext):
  #await state.update_data(url__knpk=message.text)
  #bk = InlineKeyboardMarkup(row_width=1)
 #b1 = InlineKeyboardButton(
    #       text =(await state.get_data()).get("text_knpk"),      
    #       url =(await state.get_data()).get("url__knpk"))
 # bk.add(b1)
  #await message.answer((await state.get_data()).get("text_rass"),reply_markup=bk)
 #await message.answer("Подтвердить рассылку?",reply_markup=nav.hlfgk)
  
  
  
  
 
if __name__ == "__main__":
  executor.start_polling(dp, skip_updates=True)