import logging
import sqlite3 
from aiogram import Bot, Dispatcher, executor, types 
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
import asyncio
import re
import random
from html import escape as html_escape
import markdown
import html
from onewindb import DataBase
import knopki as knpk





 
logging.basicConfig(level=logging.INFO) 

storage = MemoryStorage()
bot = Bot(token= "6546815065:AAEeLqcqtqagLnKGdb8gsaVd5QQWnHczEPU") 
dp = Dispatcher(bot,storage=storage) 
db = DataBase('database') 





class OneState(StatesGroup):
  wait_for_galochka = State()
  wait_for_stiker = State()
  wait_for_galoc = State()
  wait_for_rabota = State()
  wait_for_nazad = State()
  wait_for_nazad1 = State()
  wait_for_nazad2 = State()
  wait_for_kol_vo = State()
  wait_for_ghhg = State()
  wait_for_osenka = State()
  wait_for_gafwdss = State()
  wait_for_osenka1 = State()















@dp.message_handler(commands=["start"]) 
async def start(message: types.Message,state: FSMContext):
  if message.chat.type =="private":
      if not db.user_exists(message.from_user.id): 
        start_command = message.text 
        referrer_id = str(start_command[7:])
        if str(referrer_id) != "":
          if str(referrer_id) != str(message.from_user.id):
            db.add_user(message.from_user.id, message.from_user.full_name,message.from_user.username,referrer_id)
            try:
              await bot.send_message(referrer_id, "По вашей ссылке зарегестрировался новый пользователь!")
            except:
              pass
          else:
            db.add_user(message.from_user.id,message.from_user.full_name,message.from_user.username)
            await bot.send_message(message.from_user.id, "Нельзя регистрироваться по собственной реферальной ссылке!")
        else:
          db.add_user(message.from_user.id,message.from_user.full_name,message.from_user.username)
    
     
        

        user_id = message.from_user.id
        conn = sqlite3.connect('database')
        cursor = conn.cursor()
        cursor.execute("SELECT new FROM users WHERE user_id = ?",(user_id,))
        result = cursor.fetchone()
     
        if result[0] == 0:
          await bot.send_message(message.from_user.id,f"Приветствую,<b>{message.from_user.full_name}</b>\n<i>Добро пожаловать в бота <b>SurfPay!</b></i>\n\nМы те,кто <code>платит вам за написание комментариев!</code>\n\nВсе проще простого:\n1.Выбераете платформу\n2.Проходите гайд в боте связанный с выбранной платформой\n3.Начинаете писать комментарии\n4.Получаете свою оплату в пятницу каждой недели\n\n\nПрежде,чем начать сотрудничество,ознакомьтесь с гайдом/инструкции ниже👇👇👇\n\n<a href ='https://telegra.ph/Oznakomitelnyj-gajd-dlya-polzovatelej-telegramm-bota-SurfPay-09-08'><i><b>Основная инструкцией по работе с ботом</b></i></a>\n\n<b>Удачи!</b>",reply_markup=knpk.rep,parse_mode="HTML",disable_web_page_preview=True)
          cursor.execute("UPDATE users SET new = 1 WHERE user_id = ?",(user_id,))
          await state.set_state(OneState.wait_for_galochka)
        if result[0] == 1:
          await bot.send_message(message.from_user.id, f"      <i><b>📝ГЛАВНОЕ МЕНЮ📝     </b></i>\n\n<b>FullName:</b> <code><i>{message.from_user.full_name}</i></code>\n<i><b>ID:</b></i><code>{message.from_user.id}</code>\n\n<i><b>💲Cтавка за 1 приглашение - </b></i> <code>35₽</code>\n     <i><b>💷Вы пригласили:</b></i> <code>0</code>\n\n<b><i>👥Количество рефералов:</i></b> <code>{db.count_reeferals(message.from_user.id)}</code>\n\n<i><b>💰Доступно к выводу:</b></i> <code>{get_user_balance(message.from_user.id)}₽</code>\n\n<b>Не забывай делать скриншоты своих комментариев!</b>\n\n<a href ='https://t.me/Surf_Pay'><i><b>🗣[НОВОСТНОЙ КАНАЛ]</b></i></a>\n<a href = 'https://t.me/SurfPay_Viplat'><i><b>🗣[КАНАЛ С ВЫПЛАТАМИ]</b></i></a>",reply_markup=knpk.menu, parse_mode="HTML",disable_web_page_preview=True)
        conn.commit()
        conn.close()

@dp.callback_query_handler(text="gotovo", state=OneState.wait_for_galochka)
async def tex765(callback:types.callback_query,  state: FSMContext) -> None: 
  await bot.send_message(callback.from_user.id, f"      <i><b>📝ГЛАВНОЕ МЕНЮ📝     </b></i>\n\n<b>FullName:</b> <code><i>{callback.from_user.full_name}</i></code>\n<i><b>ID:</b></i><code>{callback.from_user.id}</code>\n\n<i><b>💲Cтавка за 1 приглашение - </b></i> <code>35₽</code>\n     <i><b>💷Вы пригласили:</b></i> <code>0</code>\n\n<b><i>👥Количество рефералов:</i></b> <code>{db.count_reeferals(callback.from_user.id)}</code>\n\n<i><b>💰Доступно к выводу:</b></i> <code>{get_user_balance(callback.from_user.id)}₽</code>\n\n<b>Не забывай делать скриншоты своих комментариев!</b>\n\n<a href ='https://t.me/Surf_Pay'><i><b>🗣[НОВОСТНОЙ КАНАЛ]</b></i></a>\n<a href = 'https://t.me/SurfPay_Viplat'><i><b>🗣[КАНАЛ С ВЫПЛАТАМИ]</b></i></a>",reply_markup=knpk.menu, parse_mode="HTML",disable_web_page_preview=True)
  await state.set_state(None)
  
  
@dp.message_handler(Text(equals="Работа💰",ignore_case=True),state=None)
async def rabota(message: types.Message, state: FSMContext) -> None:
  await message.answer(f"<i>Используй кнопки для взаимодействия с ботом👇</i>",parse_mode="HTML",reply_markup=knpk.rabota)
  await state.set_state(OneState.wait_for_rabota)
  #await message.answer("<b>Твой текст,который нужно сохранить,а затем импользовать,как комментарий:</b>\n\n<code>Напиши мне в тг - @qwehar Там все подробно и внятно объясню про Абуз 1WIN</code>\n\n<b>ВНИМАНИЕ!</b>\nЧтобы узнать,как использовать данный комментарий подробно изучи инструкции!\n\nГлавное меню >Гайды для работы✅",parse_mode="HTML")

@dp.message_handler(Text(equals="Гайды/инструкции✅",ignore_case=True),state=OneState.wait_for_rabota)
async def tex765(message: types.Message, state: FSMContext) -> None:
  await message.answer(f"<b>Все гайды так или иначе взаимосвязаны между собой,поэтому нужно изучить Все,чтобы узнать ответы на свои вопросы!</b>\n\n1.<a href = 'https://telegra.ph/Oznakomitelnyj-gajd-dlya-polzovatelej-telegramm-bota-SurfPay-09-08'><i><b>Ознакомительный гайд!</b></i></a>\n\n2.<a href = 'https://telegra.ph/Gajd-na-TikTok-09-10'><i><b>Гайд на TikTok!</b></i></a>\n\n3.<a href = 'https://telegra.ph/Gajd-na-YouTube-Shorts-09-10'><i><b>Гайд на YouTube Shorts!</b></i></a>",parse_mode="HTML",disable_web_page_preview=True,reply_markup=knpk.dfg)
  await state.set_state(OneState.wait_for_nazad)
  
@dp.message_handler(Text(equals="Назад⬅️",ignore_case=True),state=OneState.wait_for_nazad)
async def tex765(message: types.Message, state: FSMContext) -> None:
  await state.reset_state()
  return await rabota(message,state) 


@dp.message_handler(Text(equals="Получить текст комментария📝",ignore_case=True),state=OneState.wait_for_rabota)
async def tex765(message: types.Message, state: FSMContext) -> None:
  await message.answer("<i>Комментарий,который нужно будет оставлять под видео!</i>\n\n<code>Напиши мне в тг - @qweharТам все подробно и внятно объясню про Абуз 1WIN</code>",parse_mode="HTML",reply_markup=knpk.dfg)
  await state.set_state(OneState.wait_for_nazad1)
  
  
@dp.message_handler(Text(equals="Назад⬅️",ignore_case=True),state=OneState.wait_for_nazad1)
async def tex765(message: types.Message, state: FSMContext) -> None:
  await state.reset_state()
  return await rabota(message,state) 
  
  




@dp.message_handler(Text(equals="Полезные ссылки🤔",ignore_case=True),state=OneState.wait_for_rabota)
async def tex765(message: types.Message, state: FSMContext) -> None:
  await message.answer("Каналы,которые публикуют нужные нам видео:",parse_mode="HTML",reply_markup=knpk.dfg)
  await state.set_state(OneState.wait_for_nazad2)
  

@dp.message_handler(Text(equals="Назад⬅️",ignore_case=True),state=OneState.wait_for_nazad2)
async def tex765(message: types.Message, state: FSMContext) -> None:
  await state.reset_state()
  return await rabota(message,state) 





@dp.message_handler(Text(equals="Проверить работу💰",ignore_case=True),state=OneState.wait_for_rabota)
async def proverka_raboti(message: types.Message, state: FSMContext) -> None:
  await message.answer("<i>Отправь мне все скриншоты твоих комментариев одним файлом!</i>",parse_mode="HTML",reply_markup=knpk.dfg)
  await state.set_state(OneState.wait_for_kol_vo)
  


@dp.message_handler(Text(equals="Назад⬅️",ignore_case=True),state=OneState.wait_for_rabota)
async def proverka_raboti(message: types.Message, state: FSMContext) -> None:
    await state.reset_state()
    return await rabota(message,state) 
  
  
@dp.message_handler(lambda message:  message.photo, content_types=["photo"],state = OneState.wait_for_kol_vo)
async def load_photo(message: types.Message, state: FSMContext):
   await message.answer("<i>Отправь мне приблизительное число комментариев,которое ты написал!</i>",parse_mode="HTML")
   await state.set_state(OneState.wait_for_ghhg)

@dp.message_handler(Text(equals="Назад⬅️",ignore_case=True),state=OneState.wait_for_ghhg)
async def proverka_raboti(message: types.Message, state: FSMContext) -> None:
    await state.reset_state()
    return await rabota(message,state) 

@dp.message_handler(lambda message: not message.photo, state = OneState.wait_for_kol_vo)
async def check_photo(message: types.Message,state: FSMContext):
  await state.reset_state()
  return await proverka_raboti(message,state) 


  
@dp.message_handler(content_types=["any"],state=OneState.wait_for_ghhg)
async def sendall4(message: types.Message,state: FSMContext):
  global chislo
  try:
     chislo = int(message.text)
  except (ValueError,UnboundLocalError,TypeError):
    await state.reset_state()
    await load_photo(message,state)
    return
   

 
    
  
  
  await message.answer("<i>Спасибо за работу!Ваша скриншоты были отправлена на проверку.</i>",parse_mode="HTML")
  await bot.send_message( -1001900257574,f"ID Мастера:{message.from_user.id}\nUsername Мастера:{message.from_user.username}\n\nКол-во возможных комментариев:{chislo}")
  await state.reset_state()
  return await start(message,state)



@dp.message_handler(Text(equals="Назад⬅️",ignore_case=True),state=OneState.wait_for_kol_vo)
async def proverka_raboti(message: types.Message, state: FSMContext) -> None:
    await state.reset_state()
    return await rabota(message,state) 





@dp.message_handler(Text(equals="Жалобы/предложения🔊",ignore_case=True),state=OneState.wait_for_rabota)
async def geref43(message: types.Message, state: FSMContext) -> None:
  await message.answer(f"<b>Как оценишь нашего бота от 1/5?</b>",parse_mode="HTML",reply_markup=knpk.dfg)
  await state.set_state(OneState.wait_for_osenka)
  
@dp.message_handler(Text(equals="Назад⬅️",ignore_case=True),state=OneState.wait_for_osenka)
async def geref43(message: types.Message, state: FSMContext) -> None:
  await state.reset_state()
  return await rabota(message,state) 


@dp.message_handler(content_types=["text"],state=OneState.wait_for_osenka)
async def tex765(message: types.Message, state: FSMContext) -> None:
  global ocenka
  ocenka = int(message.text)
  if ocenka < 1:
    await state.reset_state()
    return await geref43(message,state) 
  if ocenka > 5:
    await state.reset_state()
    return await geref43(message,state) 
  if ocenka == 1 or 2 or 3 or 4 or 5:
    await message.answer("Спасибо за оценку!Что хочешь написать?",parse_mode="HTML",reply_markup=knpk.hrf)
    await state.set_state(OneState.wait_for_gafwdss)


@dp.message_handler(Text(equals="Жалобу📝",ignore_case=True),state=OneState.wait_for_gafwdss)
async def geref667(message: types.Message, state: FSMContext) -> None:
  await message.answer(f"Напиши свою жалобу.Что тебе не понравилось?")
  await state.set_state(OneState.wait_for_osenka1)
  
@dp.message_handler(lambda message:  message.text, content_types=["text"],state = OneState.wait_for_osenka1)
async def geref(message: types.Message, state: FSMContext) -> None: 
  try:
         jaloba = message.text
         await message.answer("Жалоба успешно отрпавлена!") 
         
  except (ValueError,TypeError,UnboundLocalError,UnicodeDecodeError):
    pass
        
  await state.reset_state()
  return await rabota(message,state)

@dp.message_handler(Text(equals="Жалобу📝",ignore_case=True),state=OneState.wait_for_osenka1)
async def geref6err(message: types.Message, state: FSMContext) -> None:
            await state.reset_state()
            return await geref667(message,state)  

@dp.message_handler(Text(equals="Предложение📝",ignore_case=True),state=OneState.wait_for_osenka1)
async def geref6err(message: types.Message, state: FSMContext) -> None:
  await state.reset_state()
  return await geref667(message,state)  



@dp.message_handler(Text(equals="Предложение📝",ignore_case=True),state=OneState.wait_for_gafwdss)
async def geref(message: types.Message, state: FSMContext) -> None:
  await message.answer(f"Напиши идею/предложение для улучшения бота.Что хочешь улучшить/изменить?")
  await state.set_state(OneState.wait_for_osenka1)
  
@dp.message_handler(lambda message:  message.text, content_types=["text"],state = OneState.wait_for_osenka1)
async def geref(message: types.Message, state: FSMContext) -> None:
  try:
      predlojenie = message.text
      await message.answer("Успешно отправленно!")
  except (ValueError,TypeError,UnboundLocalError,UnicodeDecodeError):
    pass
  await state.reset_state()
  return await rabota(message,state)
  
  























@dp.message_handler(Text(equals="Я уже ознакомлен😊",ignore_case=True),state=None)
async def tex765(message: types.Message, state: FSMContext) -> None:
  pass
  
 
 
 
 
@dp.message_handler(Text(equals="Ознакомлюсь и вернусь👌",ignore_case=True),state=None)
async def tex765(message: types.Message, state: FSMContext) -> None: 
  await state.reset_state()
  return await start(message,state)  
  
  
  
  
  
  
  
@dp.message_handler(Text(equals="👌",ignore_case=True),state=OneState.wait_for_galoc)
async def tex765(message: types.Message, state: FSMContext) -> None:
  await state.reset_state()
  return await start(message,state)  
  
  
  
  
  
  
@dp.message_handler(Text(equals="Реферальная программа👥",ignore_case=True),state=None)
async def tex765(message: types.Message, state: FSMContext) -> None:
  await message.answer(f"🤝<i><b>Реферальная программа</b></i>\n\n<i>👥В нашем боте имеется одноуровневая система рефералов:\n\n 1 уровень - 15 % от заработка\n\n✔️Приглашайте новых пользователей и зарабатываете с их заработка!\n\n👁‍🗨Ссылка для привлечения рефералов:</i>\n<code>https://t.me/SurfPay_bot?start={message.from_user.id}</code>",parse_mode="HTML",reply_markup=knpk.kbkb)
  await state.set_state(OneState.wait_for_stiker)
  
@dp.message_handler(Text(equals="👌",ignore_case=True),state=OneState.wait_for_stiker)
async def tex765(message: types.Message, state: FSMContext) -> None:
  await state.reset_state()
  return await start(message,state) 































def get_user_balance(user_id):
    conn = sqlite3.connect('database')
    c = conn.cursor()
    c.execute("SELECT BALANCE FROM users WHERE user_id=?", (user_id,))
    user_balance = c.fetchone()
    conn.close()
    return user_balance[0] if user_balance else 0.0


def update_user_balance(user_id, new_balance):
    conn = sqlite3.connect('database')
    c = conn.cursor()
    c.execute("UPDATE users SET BALANCE=? WHERE user_id=?", (new_balance, user_id))
    conn.commit()
    conn.close()






















































if __name__ == "__main__":
  executor.start_polling(dp, skip_updates=True)