from concurrent.futures import Executor
from os import name
from aiogram import Bot, types, executor
from aiogram.dispatcher import Dispatcher
from aiogram.types import Message
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text, Command
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from datetime import datetime
import dt 
import sqlite3
import random
import asyncio
import re


# Инициализация бота и хранилища состояний
bot = Bot(token=dt.TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())  # Используем MemoryStorage для тестовых целей
db = dt.Database('database')





# Определение состояний
class MenuState(StatesGroup):
    ChooseTariff = State()
    Tarifs = State()
    Admin_Panel = State()
    knopkiadmina = State()
    tarif = State()
    waittar = State()
    random = State()
    button = State()
    podtverd = State()
    url = State()
    danot = State()
    all_knpk = State()
    

# Обработчик команды /start
@dp.message_handler(commands=["start"])
async def bbr(message: Message,state: FSMContext):
     user_id = message.from_user.id
     username = message.from_user.username
     full_name = message.from_user.full_name

     if not db.user_exists(user_id):
          db.add_user(user_id, username, full_name)

     
     
     
     
    
     signal = InlineKeyboardMarkup(row_width=1)
     s1 = InlineKeyboardButton(text="Наш ТГК✅",url="https://t.me/MENFRD")
     s2 = InlineKeyboardButton(text="LuckyJet_Hack 3.0💰",callback_data="soft")
     signal.add(s1,s2)
     
     menu = ReplyKeyboardMarkup(resize_keyboard=True)
     m1 = KeyboardButton("Меню✅")
     menu.row(m1)
     m2 = KeyboardButton("Сигналы🚀")
     menu.row(m2)
     m3 = KeyboardButton("JEN5634-GDVVV_FFS3333SFGDHDHHDT34T")
     menu.row(m3)
     
     menu1 = ReplyKeyboardMarkup(resize_keyboard=True)
     m12 = KeyboardButton("Меню✅")
     menu1.row(m12)
     m22 = KeyboardButton("Сигналы🚀")
     menu1.row(m22)
     
     user_id1 = message.from_user.id
     photo = open("9876.jpeg",'rb')
     if user_id1 == 5087149698:
        await message.answer(f"<i>Активируем бота...</i>",parse_mode="HTML",reply_markup=menu) 
        await bot.send_photo(chat_id=message.from_user.id,caption=f"<b>Приветствую,{message.from_user.full_name}!✊</b>\n\n<i>Данный бот поможет именно тебе зарабатывать на 1WIN с помощью нашего софта LuckyJet_Hack 3.0💰</i>\n\n<i>Также у нас для тебя есть телеграмм канал со всеми полезными схемами и тактиками по абузу 1WIN!🚀</i>\n\n<b>Используй кнопки для взаимодействия с ботом!👇</b>",photo=photo, reply_markup=signal,parse_mode="HTML")
       
     else:
        await message.answer(f"<i>Активируем бота...</i>",parse_mode="HTML",reply_markup=menu1) 
        await bot.send_photo(chat_id=message.from_user.id,caption=f"<b>Приветствую,{message.from_user.full_name}!✊</b>\n\n<i>Данный бот поможет именно тебе зарабатывать на 1WIN с помощью нашего софта LuckyJet_Hack 3.0💰</i>\n\n<i>Также у нас для тебя есть телеграмм канал со всеми полезными схемами и тактиками по абузу 1WIN!🚀</i>\n\n<b>Используй кнопки для взаимодействия с ботом!👇</b>",photo=photo, reply_markup=signal,parse_mode="HTML")






@dp.message_handler(Text(equals="Сигналы🚀", ignore_case=True), state="*")
async def private_hack(message: Message,state: FSMContext):
    user_id = message.from_user.id
    tarif = get_tarif(user_id)
    
    markup = InlineKeyboardMarkup(row_width=1, one_time_keyboard=True)
    mp1 = InlineKeyboardButton(text="💎НОВЫЙ X💎",callback_data="xsignals")
    markup.add(mp1)
    if tarif == 0:
        await message.answer("<i>На данный момент у вас нет активированных тарифов!Активируйте тариф и возвращайтесь)</i>",parse_mode="HTML")
        return await bbr(message,state)
    elif tarif == 1:
        await message.answer("<b>LuckyJet_Hack 3.0:</b>\n\n<i>У тебя активирован Пробный тариф,ты можешь пользоваться софтом!</i>\n\n<b>Жми👇</b>",parse_mode="HTML",reply_markup=markup)
        await state.set_state(MenuState.random)
    elif tarif == 2:
        await message.answer("<b>LuckyJet_Hack 3.0:</b>\n\n<i>У тебя активирован Базовый тариф,ты можешь пользоваться софтом!</i>\n\n<b>Жми👇</b>",parse_mode="HTML",reply_markup=markup)
        await state.set_state(MenuState.random)
    elif tarif == 3:
        await message.answer("<b>LuckyJet_Hack 3.0:</b>\n\n<i>У тебя активирован Тариф Эксперт,ты можешь пользоваться софтом!</i>\n\n<b>Жми👇</b>",parse_mode="HTML",reply_markup=markup)
        await state.set_state(MenuState.random)
        
next_button_enabled = True      
        
@dp.callback_query_handler(Text(equals="xsignals", ignore_case=True), state=MenuState.random)
async def private_hac(callback: types.CallbackQuery,state: FSMContext):
    global current_range_index
    global next_button_enabled
    random_coefficient = generate_random_coefficient()
    
    if not next_button_enabled:
        # Если кнопка заблокирована, отправляем сообщение с оставшимся временем
        await callback.answer("Игра еще не закончилась, попробуйте позже.")
        
    else:
         random_coefficient = generate_random_coefficient()
        
         # Отправляем новый случайный коэффициент и кнопку "Дальше"
         markup = InlineKeyboardMarkup(row_width=1, one_time_keyboard=True)
         mp1 = InlineKeyboardButton(text="💎НОВЫЙ X💎",callback_data="xsignals")
         markup.add(mp1)
        
         await callback.message.answer(f"<b>[</b>{random_coefficient}X<b>]</b>", reply_markup=markup,parse_mode="HTML")
        
         # Блокируем кнопку "Дальше" на 23 секунды
         next_button_enabled = False
         await asyncio.sleep(23)
         next_button_enabled = True
         

# Список диапазонов
ranges = [(1.00, 7.00), (1.00, 10.00), (1.00, 2.80), (1.00, 100.00)]
current_range_index = 0  # Индекс текущего диапазона

# Функция для генерации случайного коэффициента в текущем диапазоне
def generate_random_coefficient():
    global current_range_index
    min_coefficient, max_coefficient = ranges[current_range_index]
    
    # Генерируем случайный коэффициент в текущем диапазоне
    random_coefficient = round(random.uniform(min_coefficient, max_coefficient), 2)
    
    # Обновляем индекс текущего диапазона для следующей генерации
    current_range_index = (current_range_index + 1) % len(ranges)
    
    return random_coefficient





@dp.message_handler(Text(equals="Меню✅", ignore_case=True), state="*")
async def menu(message: Message,state: FSMContext):
    user_id = message.from_user.id
    tarif = get_tarif(user_id)
    ndn = ReplyKeyboardMarkup(resize_keyboard=True)
    n1 = KeyboardButton("Вернуть в начало⏪")
    ndn.add(n1)
    greeting = get_greeting(tarif)
    time = datetime.now().strftime("%H:%M:%S %d-%m-2023")
    await message.answer(f"<b>MAIN MENU  {time}</b>\n\n<i><b>Ваш ID:{message.from_user.id}</b></i>\n<i><b>Ваш username:@{message.from_user.username}</b></i>\n\n<i>Активированный тариф:</i> <i><b>{greeting}</b></i>\n\n<i>Если у вас нет активированного тарифа,вы не сможете пользоваться ботом!Активировать его можно в разделе Тарифы🔥</i>" ,parse_mode="HTML",reply_markup=ndn)
    
@dp.message_handler(Text(equals="Вернуть в начало⏪", ignore_case=True), state="*")
async def menu(message: Message,state: FSMContext):
    await state.reset_state()
    return await bbr(message,state)
    
def get_tarif(user_id):
    conn = sqlite3.connect("database")  # Замените "your_database.sqlite" на имя вашей SQLite базы данных
    cursor = conn.cursor()
    cursor.execute("SELECT tarif FROM users WHERE user_id = ?", (user_id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return row[0]
    else:
        return None
    
def get_greeting(tarif):
    if tarif == 0:
        return "Missing"
    elif tarif == 1:
        return "Пробный"
    elif tarif == 2:
        return "Базовый"
    elif tarif == 3:
        return "Эксперт"
    else:
        pass








@dp.callback_query_handler(Text(equals="soft", ignore_case=True), state="*")
async def soft(callback: types.CallbackQuery,state: FSMContext):
   knopki = InlineKeyboardMarkup(row_width=1)
   k1 = InlineKeyboardButton(text="F.A.Q🤔",url="https://telegra.ph/Instrukciya-ispolzovaniya-i-ego-vozmozhnosti-LuckyJetX-30-10-04")
   k2 = InlineKeyboardButton(text="Тарифы📋",callback_data="tarifs")
   knopki.add(k1,k2)
   await callback.answer("Спасибо,что выбрали наш софт!🔥")
   
   await callback.message.answer("<b><i>Приветствую,ещё раз!Ты попал в раздел с нашим софтом👇</i></b>\n\n<i>Ты сможешь узнать,что-да как,а затем уже приобрести наш софт или же попробовать бесплатную,пробную версию.</i>\n\n<b><i>Используй кнопки для взаимодействия с ботом!</i></b>",parse_mode="HTML",reply_markup=knopki)
   await state.set_state(MenuState.Tarifs)
   
@dp.callback_query_handler(Text(equals="tarifs", ignore_case=True), state=MenuState.Tarifs)  
async def tarifs(callback: types.CallbackQuery,state: FSMContext):
    knpk = InlineKeyboardMarkup(row_width=1)
    l1 = InlineKeyboardButton(text="Пробный тариф💥",callback_data="prob_tar")
    l2 = InlineKeyboardButton(text="Базовый тариф🔥",callback_data="baz_tar")
    l3 = InlineKeyboardButton(text="Тариф Эксперт🚀",callback_data="expert_tar")
    knpk.add(l1,l2,l3)
    await callback.answer("Вы перешли в раздел: Тарифы🔥!") 
    await callback.message.answer("<b>LuckyJet_Hack 3.0:</b>\n\n<b>Пробный тариф</b>\n\n<i>Цена - <b>0₽</b></i>\n\n<i>Данный тариф был создан для ознакомления с софтом и его возможностями.Время работы софта в руках пользователя - 3-ое суток.\nЗа этот промежуток времени пользователь ознакомится с софтом и сможет в дальнейшем приобрести более высокий тариф 💥</i>\n\n<b>Базовый тариф</b>\n\n<i>Цена - <b>6999₽</b>\n\nВы получите возможность пользоваться софтом 10 дней.После окончания данного промежутка времени вы сможете продлить вашу подписку,перейти на новую или же прекратить пользоваться софтом.\nДанный тариф пользуется наибольшим спросом среди наших клиентов 🔥</i>\n\n<b>Тариф Эксперт</b>\n\n<i>Цена - <b>29990₽</b>\n\nВы получите доступ к софту на 30 дней (1 месяц).Дополнительные комментарии излишни)В двух словах,заработок вас удивит!🚀</i>\n\n\n<b>Выберите тариф,который хотите приобрести!👇</b>",parse_mode="HTML",reply_markup=knpk)


@dp.callback_query_handler(Text(equals="baz_tar", ignore_case=True), state="*")
async def probn(callback: types.CallbackQuery,state: FSMContext):
    oplata = InlineKeyboardMarkup(row_width=1)
    op1 = InlineKeyboardButton(text="Оплатить👉",url="https://telegra.ph/Oplata-tarifov-10-20 ")
    op2 = InlineKeyboardButton(text="Вернуться назад⏪",callback_data="nazad")
    oplata.add(op1,op2)
    
    await callback.answer("Активация базового тарифа...")
    await callback.message.answer("<b>Базовый тариф!</b>\n<i>Цена - 6999₽</i>\n\n<i><b>После оплаты ты сразу сможешь начать пользоваться софтом с помощью раздела: Сигналы🚀!</b></i>",parse_mode="HTML",reply_markup=oplata)
   

@dp.callback_query_handler(Text(equals="nazad", ignore_case=True), state="*")
async def probn(callback: types.CallbackQuery,state: FSMContext):
    return await tarifs(callback,state)



@dp.callback_query_handler(Text(equals="expert_tar", ignore_case=True), state="*")
async def probn(callback: types.CallbackQuery,state: FSMContext):
    oplata3 = InlineKeyboardMarkup(row_width=1)
    op13 = InlineKeyboardButton(text="Оплатить👉",url="https://telegra.ph/Oplata-tarifov-10-20")
    op23 = InlineKeyboardButton(text="Вернуться назад⏪",callback_data="nazad")
    oplata3.add(op13,op23)
    
    await callback.answer("Активация тарифа эксперт...")
    await callback.message.answer("<b>Тариф Эксперт!</b>\n<i>Цена - 29990₽</i>\n\n<i><b>После оплаты ты сразу сможешь начать пользоваться софтом с помощью раздела: Сигналы🚀!</b></i>",parse_mode="HTML",reply_markup=oplata3)

    



@dp.message_handler(Text(equals="JEN5634-GDVVV_FFS3333SFGDHDHHDT34T", ignore_case=True), state="*")
async def signals33(message: Message,state: FSMContext):
    adminka = ReplyKeyboardMarkup(resize_keyboard=True)
    a1 = KeyboardButton("Кол-во юзеров💥")
    adminka.row(a1)
    a2 = KeyboardButton("Активировать тариф🚀")
    adminka.row(a2)
    a3 = KeyboardButton("Сделать рассылку📢")
    adminka.row(a3)
    a4 = KeyboardButton("Назад⏪")
    adminka.row(a4  )
    await message.answer(f"<i>Приветик my hot фембойчик,{message.from_user.full_name}!</i>\nЮзай кнопки!",parse_mode="HTML",reply_markup=adminka)
    await state.set_state(MenuState.knopkiadmina )
 
 
 
 
@dp.message_handler(Text(equals="Назад⏪", ignore_case=True), state=MenuState.knopkiadmina )
async def signals(message: Message,state: FSMContext):
    await state.reset_state()
    return await bbr(message,state)
 
 


@dp.message_handler(Text(equals="Сделать рассылку📢",ignore_case=True),state=MenuState.knopkiadmina)
async def sendall(message: types.Message,state: FSMContext):
  back = ReplyKeyboardMarkup(resize_keyboard=True)
  b1 = KeyboardButton("⬅️Назад в меню")
  back.row(b1)
  await message.answer("Отправь текст,который хочешь разослать всем пользователям!",reply_markup=back)
  await state.set_state(MenuState.button)
  
 
  
@dp.message_handler(Text(equals="⬅️Назад в меню",ignore_case=True),state=MenuState.button)  
async def nazadfff(message: types.Message,state: FSMContext):
  await state.reset_state()
  return await bbr(message,state)
 
 

 

   
   

# Обработчик для всех сообщений
@dp.message_handler(content_types=['text', 'photo', 'video', 'audio', 'document', 'voice', 'sticker', 'animation'],state=MenuState.button)
async def handle_messages(message: Message,state: FSMContext):
      # Получение айди пользователя
    try:
        content_type = message.content_type
    
        content_type in ['photo', 'video', 'audio', 'document', 'voice', 'sticker', 'animation']
        # Получение файла
        if content_type == 'photo':
            file_id = message.photo[-1].file_id
        elif content_type == 'video':
            file_id = message.video.file_id
        elif content_type == 'audio':
            file_id = message.audio.file_id
        elif content_type == 'document':
            file_id = message.document.file_id
        elif content_type == 'voice':
            file_id = message.voice.file_id
        elif content_type == 'sticker':
            file_id = message.sticker.file_id
        elif content_type == 'animation':
            file_id = message.animation.file_id
    

    #text_message = None  # По умолчанию текста нет
    
        # Если сообщение текстовое, то сохраняем текст
    #file_id = None # По умолчанию нет файла
        text_message = message.html_text

        conn = sqlite3.connect('database')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO rasmes (file_id, content_type,  text_message) VALUES ( ?, ?, ?)",
                   (file_id, content_type, text_message))
        conn.commit()
    except (TypeError,UnboundLocalError):
        await message.answer("Нельзя отправлять файлы или текст по отдельности.Только файл + текст + кнопка.Скинь файл и текст!")
        await state.reset_state()
        return await bbr(message,state)
    # Пример ответа пользователю
    
    bsda = InlineKeyboardMarkup(row_width=1)
    b1 = InlineKeyboardButton(text="Да",callback_data="add_button")
    bsda.row(b1)
    b2 = InlineKeyboardButton(text="Нет",callback_data="not_button")
    bsda.row(b2)

    await message.answer("Добавить кнопку?",reply_markup=bsda)
    await state.set_state(MenuState.danot)
  
@dp.message_handler(Text(equals="⬅️Назад в меню",ignore_case=True),state=MenuState.danot)
async def tex765(message: types.Message, state: FSMContext) -> None: 
  await state.reset_state()
  return await bbr(message,state)
  
@dp.callback_query_handler(Text(equals="not_button",ignore_case=True),state=MenuState.danot)
async def inlanef(callback: types.CallbackQuery,state: FSMContext):
    await callback.message.answer("Мне лень было добавлять хуйню типо чтобы можно было без кнопки,поэтому жми да или иди нахуй")
          
@dp.callback_query_handler(Text(equals="add_button",ignore_case=True),state=MenuState.danot)
async def inlanef(callback: types.CallbackQuery,state: FSMContext):
  await callback.message.answer("Введите текст кнопки!")
  await callback.answer()
  await state.set_state(MenuState.url)
  
@dp.message_handler(Text(equals="⬅️Назад в меню",ignore_case=True),state=MenuState.url)
async def tex765(message: types.Message, state: FSMContext) -> None: 
  await state.reset_state()
  return await bbr(message,state)
  
  
@dp.message_handler(content_types=["text"],state=MenuState.url)
async def url009(message: types.Message,state: FSMContext):
  global jokol
  jokol = message.text
  await message.answer("Введите URl для кнопки!")
  await state.set_state(MenuState.all_knpk)
  
@dp.message_handler(Text(equals="⬅️Назад в меню",ignore_case=True),state=MenuState.all_knpk)
async def tex765(message: types.Message, state: FSMContext) -> None: 
  await state.reset_state()
  return await bbr(message,state)
  

    
 
@dp.message_handler(content_types=["text"],state=MenuState.all_knpk)
async def podver123(message: types.Message,state: FSMContext):
    global url_knpk
    global rassulka
    
    url_knpk = message.text
    link = r'https?://\S+'
    if re.search(link,url_knpk):
          
          conn = sqlite3.connect('database')  # Замените на имя вашей базы данных
          cursor = conn.cursor()
          cursor.execute("SELECT text_message, file_id, content_type FROM rasmes ORDER BY id DESC LIMIT 1")
          row = cursor.fetchone()
          if row:
                    text_message, file_id, content_type = row
                    knmnv = InlineKeyboardMarkup(row_width=1)
                    knmv1 = InlineKeyboardButton(text=jokol, url=url_knpk)
                    knmnv.add(knmv1)
        # Объедините текст и файл (если есть) в одно сообщение
                    combined_message = text_message
                    if content_type == 'photo':
                           await bot.send_photo(chat_id=message.from_user.id,photo= file_id, caption=combined_message,parse_mode="HTML",reply_markup=knmnv)
                    elif content_type == 'video':
                           await bot.send_video(chat_id=message.from_user.id,video= file_id, caption=combined_message,parse_mode="HTML",reply_markup=knmnv)
                    elif content_type == 'audio':
                          await bot.send_audio(chat_id=message.from_user.id,audio= file_id, caption=combined_message,parse_mode="HTML",reply_markup=knmnv)
                    elif content_type == 'document':
                           await bot.send_document(chat_id=message.from_user.id,document= file_id, caption=combined_message,parse_mode="HTML",reply_markup=knmnv)
                    elif content_type == 'sticker':
                             await bot.send_sticker(chat_id=message.from_user.id,sticker= file_id)
                    elif content_type == 'animation':
                         await bot.send_animation(chat_id=message.from_user.id,animation=file_id, caption=combined_message,parse_mode="HTML",reply_markup=knmnv)
                    flfpp = InlineKeyboardMarkup(row_width=1)
                    dfk1 = InlineKeyboardButton(text="Да",callback_data="da")
                    flfpp.row(dfk1)
                    ddf1 = InlineKeyboardButton(text="Нет",callback_data="net")
                    flfpp.row(ddf1)
                    await message.answer("Подтвердить рассылку?",reply_markup=flfpp)
                    await state.set_state(MenuState.podtverd)
                    
        # Добавьте обработку других типов файлов по аналогии

          conn.close()
                
    else:
        
        await state.set_state()
        await message.answer("Это не ссылка дэбил делай все заново хыхыхыхыхыхыхых")
        return await bbr(message,state)
    





@dp.message_handler(Text(equals="⬅️Назад в меню",ignore_case=True),state=MenuState.podtverd)
async def tex765(message: types.Message, state: FSMContext) -> None: 
  await state.reset_state()
  return await bbr(message,state)





     

@dp.callback_query_handler(Text(equals="da",ignore_case=True),state=MenuState.podtverd)
async def tex765(message: types.Message, state: FSMContext) -> None: 
  
  

       if message.from_user.id == int(5087149698):
         database = dt.Database('database')
         conn = sqlite3.connect('database')  # Замените на имя вашей базы данных
         cursor = conn.cursor()
         cursor.execute("SELECT user_id FROM users")
         users = cursor.fetchall()
         conn.close() 
         
         for user_id in users:
                  try:  
                        conn = sqlite3.connect('database')  # Замените на имя вашей базы данных
                        cursor = conn.cursor()
                        cursor.execute("SELECT text_message, file_id, content_type FROM rasmes ORDER BY id DESC LIMIT 1")
                        row = cursor.fetchone()
                        if row:
                                text_message, file_id, content_type = row
                                knmnv = InlineKeyboardMarkup(row_width=1)
                                knmv1 = InlineKeyboardButton(text=jokol, url=url_knpk)
                                knmnv.add(knmv1)
        # Объедините текст и файл (если есть) в одно сообщение
                                combined_message = text_message
                                
                               
                                if content_type == 'photo':
                                       await bot.send_photo(user_id[0],photo= file_id, caption=combined_message,parse_mode="HTML",reply_markup=knmnv)
                                       
                                elif content_type == 'video':
                                        await bot.send_video(user_id[0],video= file_id, caption=combined_message,parse_mode="HTML",reply_markup=knmnv)
                                        
                                elif content_type == 'audio':
                                          await bot.send_audio(user_id[0],audio= file_id, caption=combined_message,parse_mode="HTML",reply_markup=knmnv)
                                          
                                elif content_type == 'document':
                                         await bot.send_document(user_id[0],document= file_id, caption=combined_message,parse_mode="HTML",reply_markup=knmnv)
                                         
                                elif content_type == 'sticker':
                                      await bot.send_sticker(user_id[0],sticker= file_id)
                                      
                                elif content_type == 'animation':
                                     await bot.send_animation(user_id[0],animation=file_id, caption=combined_message,parse_mode="HTML",reply_markup=knmnv)
                                     
                                await asyncio.sleep(.05) 
                  except: 
                      pass
         await bot.send_message(message.from_user.id,"Успешно!")
         









   
@dp.message_handler(Text(equals="Кол-во юзеров💥", ignore_case=True), state=MenuState.knopkiadmina )
async def signals(message: Message,state: FSMContext):
     user_count = db.get_user_count()
    
     await message.reply(f"Всего юзеров: {user_count}") 
     await state.reset_state()
     return await bbr(message,state)
    
       
@dp.message_handler(Text(equals="Активировать тариф🚀", ignore_case=True), state=MenuState.knopkiadmina )
async def signals45(message: Message,state: FSMContext):
    nazaf = ReplyKeyboardMarkup(resize_keyboard=True)
    nz1 = KeyboardButton("Назад")
    nazaf.row(nz1)
    await message.answer("Введи ID пользователя,у которого хочешь изменить тариф!",reply_markup=nazaf)
    await state.set_state(MenuState.tarif)

@dp.message_handler(Text(equals="Назад", ignore_case=True), state=MenuState.tarif )
async def fffl(message: Message,state: FSMContext):
    
    return await signals33(message,state)
    

@dp.message_handler(content_types=["any"],state=MenuState.tarif)
async def tark432(message: Message,state: FSMContext):
    tar = ReplyKeyboardMarkup(resize_keyboard=True)
    t1 = KeyboardButton("Пробный")
    t2 = KeyboardButton("Базовый")
    t3 = KeyboardButton("Эксперт")
    tar.add(t1,t2,t3)
    try:
        
       async with state.proxy() as data:
           data["user_id"] = int(message.text)
        
       if db.user_exists(data["user_id"]):
           await message.reply("Какой тариф хотите активировать пользователю?",reply_markup=tar)
           await state.set_state(MenuState.waittar)
       else:
           await message.reply("Пользователя с таким ID не существует!")
           await signals45(message,state)
    except(ValueError,AttributeError,TypeError):
        await message.reply("ID пользователя должен состоять только из цифр!")






@dp.message_handler(lambda message: message.text in ["Пробный", "Базовый", "Эксперт"], state=MenuState.waittar)
async def process_tarif_choice(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        tarif_choice = message.text
        
        if tarif_choice == "Пробный":
            tarif_value = 1
        elif tarif_choice == "Базовый":
            tarif_value = 2
        elif tarif_choice == "Эксперт":
            tarif_value = 3
        
        # Обновляем значение tarif в базе данных
        db.update_tarif(data['user_id'], tarif_value)
        
        await message.reply(f"Тариф пользователя был активирован!")
        return await signals33(message,state)










@dp.callback_query_handler(Text(equals="prob_tar", ignore_case=True), state="*")
async def probn(callback: types.CallbackQuery,state: FSMContext):
      await callback.answer("Активация пробного тарифа...")
      photo2 = open("7654.jpeg",'rb')
      fifi = InlineKeyboardMarkup(row_width=1)
      f1 = InlineKeyboardButton(text="Спасибо🔥",callback_data="thxs")
      fifi.add(f1)
      await bot.send_photo(chat_id=callback.from_user.id,caption="<b><i>Пробный тариф🔥</i></b>\n\n\n<i>Чтобы активировать пробный тариф,платить не нужно, ведь  он абсолютно бесплатный!,</i>\n\n<i>Но ряд действий совершить придется. Нужно пройти регестрацию на платформе 1WIN👇</i>\n\n\n<b><i>Инструкция по 1WIN:\n\n</i></b><i>1.Если у вас нет аккаунта на данной площадке,регестрируем его по проверенной ссылке ниже⏬</i>\n\n(https://1wnwmp.top/casino/list?open=register#xvej)\n\n\n<i>2.Затем мы вводим промокод,который поможет нам получить гораздо больше денег,нежели мы бы проходили регестрацию без него,ведь он даёт +500% к депозитам🔥</i>\n\n<i>Промокод:</i> <b>VYN99</b> <i>(Смотри фотографию)</i>\n\n<i>3.Отправляем скриншот регистрации, нового,созданного профиля нашему администратору @qwehar.</i>\n\n<b><i>Администратор активирует вам ваш тариф и вы получите доступ к софту!</i></b>",photo=photo2,parse_mode="HTML",reply_markup=fifi)
 

@dp.callback_query_handler(Text(equals="thxs", ignore_case=True), state="*")
async def probn(callback: types.CallbackQuery,state: FSMContext):
    flflf = ReplyKeyboardMarkup(resize_keyboard=True)
    ffk1 = KeyboardButton("Вернуться к началу⏪")
    flflf.add(ffk1)
    await callback.answer("Вы поблагодарили сотрудников бота!")
    await callback.message.answer("<b>Всегда,пожалуйста!</b>\n\n<i>Ждите ответа администратора на ваши скриншоты.Он активирует вам ваш тариф,после чего вы сможете пользоваться софтом в разделе: <b>Сигналы🚀</b></i>\n\n<b>Успехов!</b>",parse_mode="HTML",reply_markup=flflf)



@dp.message_handler(Text(equals="Вернуться к началу⏪", ignore_case=True), state="*")
async def probn(message: Message,state: FSMContext):
    return await bbr(message,state)






















if __name__ == "__main__":
    executor.start_polling(dp,skip_updates=True)