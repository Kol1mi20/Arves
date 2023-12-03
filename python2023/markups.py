from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton



mainMenu = ReplyKeyboardMarkup(resize_keyboard=True)
m1 = KeyboardButton("Заработать💰")
mainMenu.row(m1)
m2 = KeyboardButton("💲Вывод средств💲")
m3 = KeyboardButton("Реферальная программа👥")
mainMenu.row(m2,m3)
m4 = KeyboardButton("❔ FAQ ❔")
m5 = KeyboardButton("Для заказчиков📝")
mainMenu.add(m4,m5)



Admin_Panele = ReplyKeyboardMarkup(resize_keyboard=True)
lk1 = KeyboardButton("Заработать💰")
Admin_Panele.row(lk1)
lk2 = KeyboardButton("💲Вывод средств💲")
lk3 = KeyboardButton("Реферальная программа👥")
Admin_Panele.row(lk2,lk3)
lk4 = KeyboardButton("❔ FAQ ❔")
Admin_Panele.row(lk4)
lk5 = KeyboardButton("Админ-Панель👑")
lk6 = KeyboardButton("Для заказчиков📝")
Admin_Panele.add(lk5,lk6)


admin_menu = ReplyKeyboardMarkup(resize_keyboard=True)
nq1 = KeyboardButton("Редактор заданий📝")
admin_menu.row(nq1)
nq2 = KeyboardButton("Действия с пользователем👥")
nq3 = KeyboardButton("Заявки на выплату💲")
admin_menu.row(nq2,nq3)
nq4 = KeyboardButton("Сделать рассылку📢")
admin_menu.row(nq4)
nq5 = KeyboardButton("⬅️Назад в меню")
admin_menu.row(nq5)







nazad = ReplyKeyboardMarkup(resize_keyboard = True)
btnn = KeyboardButton("⬅️Назад в меню")
nazad.add(btnn)

faq = ReplyKeyboardMarkup(resize_keyboard=True)
f1 = KeyboardButton("😊Да")
f2 = KeyboardButton("😔Нет,я невнимательный")
faq.row(f1,f2)


ref = ReplyKeyboardMarkup(resize_keyboard=True)
ref1 = KeyboardButton("👌")
ref.add(ref1)


viplata = ReplyKeyboardMarkup(resize_keyboard=True)
ek1 = KeyboardButton("⬅️Назад в меню")
viplata.add(ek1)
ek2 = KeyboardButton("Сбербанк")
viplata.add(ek2)
ek3 = KeyboardButton("Тинькофф")
viplata.add(ek3)
ek5 = KeyboardButton("ВТБ")
viplata.add(ek5)
ek6 = KeyboardButton("ЮMoney")
viplata.add(ek6)
ek7 = KeyboardButton("Альфа Банк")
viplata.add(ek7)
ek8 = KeyboardButton("Райффайзен Банк")
viplata.add(ek8)
ek9 = KeyboardButton("МТС Банк")
viplata.add(ek9)
ek10 = KeyboardButton("Банк Открытие")
viplata.add(ek10)
ek11 = KeyboardButton("Газпром Банк")
viplata.add(ek11)
ek12 = KeyboardButton("Совком Банк")
viplata.add(ek12)
ek13 = KeyboardButton("На баланс телефона")
viplata.add(ek13)



rasnaz = ReplyKeyboardMarkup(resize_keyboard=True)
fg1 = KeyboardButton("⬅️Назад в меню")
rasnaz.row(fg1)

nazadd = ReplyKeyboardMarkup(resize_keyboard=True)
nmn1 = KeyboardButton("⬅️Назад в меню")
nazadd.row(nmn1)

danot = ReplyKeyboardMarkup(resize_keyboard=True)
da1 = KeyboardButton("Добавить кнопку✅")
net1 = KeyboardButton("Продолжить без кнопки❌")
danot.add(da1,net1)

inl = InlineKeyboardMarkup(row_width=1)
in1 = InlineKeyboardButton(text="Добавить кнопку",callback_data="add_button")
in2 = InlineKeyboardButton(text="Продолжить без кнопки",callback_data="no_button")
inl.add(in1,in2)

hlfgk = ReplyKeyboardMarkup(resize_keyboard= True)
fw1 = KeyboardButton("Подтвердить✅")
fw2 = KeyboardButton("Отклонить❌")
hlfgk.add(fw1,fw2)

deist = ReplyKeyboardMarkup(resize_keyboard=True)
d1 = KeyboardButton("Действия с администраторами👑")
deist.row(d1)
d3 = KeyboardButton("Изменить баланс пользователю💰")
deist.row(d3)
d4 = KeyboardButton("Кол-во юзеров в боте👥")
deist.row(d4)
d5 = KeyboardButton("⬅️Назад в меню")
deist.row(d5)

naz = ReplyKeyboardMarkup(resize_keyboard=True)
n1 = KeyboardButton("⬅️Назад в меню")
naz.row(n1)

admin_izmenit_id = ReplyKeyboardMarkup(resize_keyboard=True)
adm1 = KeyboardButton("Добавить администратора✅")
admin_izmenit_id.row(adm1)
adm2 = KeyboardButton("Удалить администратора❌")
admin_izmenit_id.row(adm2)
adm3 = KeyboardButton("Список всех администраторов👑")
admin_izmenit_id.row(adm3)
adm4 = KeyboardButton("⬅️Назад в меню")
admin_izmenit_id.row(adm4)




asdsd = ReplyKeyboardMarkup(resize_keyboard=True)
admr4 = KeyboardButton("⬅️Назад в меню")
asdsd.row(admr4)
                      

balance_user = ReplyKeyboardMarkup(resize_keyboard=True)
bl_us = KeyboardButton("Начислить баланс✅")
balance_user.row(bl_us)
bl_us1 = KeyboardButton("Отнять баланс❌")
balance_user.row(bl_us1)
nazss = KeyboardButton("⬅️Назад в меню")
balance_user.row(nazss)



nas = ReplyKeyboardMarkup(resize_keyboard=True)
d54= KeyboardButton("⬅️Назад в меню")
nas.row(d54)

nas1 = ReplyKeyboardMarkup(resize_keyboard=True)
d541= KeyboardButton("⬅️Назад в меню")
nas1.row(d541)

nas21 = ReplyKeyboardMarkup(resize_keyboard=True)
d5412= KeyboardButton("⬅️Назад в меню")
nas21.row(d5412)