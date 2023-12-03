from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton

moknop = ReplyKeyboardMarkup(resize_keyboard=True)
m1 = KeyboardButton("Узнать все подробности о работе✅")
moknop.row(m1)

menu = ReplyKeyboardMarkup(resize_keyboard=True)
mn1 = KeyboardButton("Работа💰")


menu.row(mn1)
mn2 = KeyboardButton("Реферальная программа👥")
m3 = KeyboardButton("💲Вывод средств💲")
menu.row(mn2,m3)


rep = InlineKeyboardMarkup(row_width=1)
r1 = InlineKeyboardButton(text="Я все прочитал(а) и готов к выполнению✅",callback_data="gotovo")
rep.row(r1)


kbkb = ReplyKeyboardMarkup(resize_keyboard=True)
kq1 = KeyboardButton("👌")
kbkb.row(kq1)



lol = ReplyKeyboardMarkup(resize_keyboard=True)
l1 = KeyboardButton("👌")
lol.row(l1)

kol = ReplyKeyboardMarkup(resize_keyboard=True)
k1 = KeyboardButton("Я уже ознакомлен😊")
kol.row(k1)
k2 = KeyboardButton("Ознакомлюсь и вернусь👌")
kol.row(k2)



rabota = ReplyKeyboardMarkup(resize_keyboard=True)
r1 = KeyboardButton("Гайды/инструкции✅")
rabota.row(r1)
r2 = KeyboardButton("Получить текст комментария📝")
rabota.row(r2)
r3 = KeyboardButton("Полезные ссылки🤔")
rabota.row(r3)
r4 = KeyboardButton("Проверить работу💰")
rabota.row(r4) 
r5 = KeyboardButton("Жалобы/предложения🔊")
rabota.row(r5)
r6 = KeyboardButton("Вернуться в меню⬅️")
rabota.row(r6)

dfg = ReplyKeyboardMarkup(resize_keyboard=True)
r63 = KeyboardButton("Назад⬅️")
dfg.row(r63)

hrf = ReplyKeyboardMarkup(resize_keyboard=True)
h1 = KeyboardButton("Жалобу📝")
h2 = KeyboardButton("Предложение📝")
hrf.add(h1,h2)