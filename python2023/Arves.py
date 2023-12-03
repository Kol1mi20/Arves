import logging
import sqlite3
from aiogram import Bot, Dispatcher, executor, types
import config as cfg
import markups as nav
from db import DataBase
from db1 import DataBase1
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import asyncio
from db2 import Database2
import re
import random
from html import escape as html_escape
import markdown
import html
from datetime import datetime
from aiogram.dispatcher.filters import BoundFilter
import uuid


logging.basicConfig(level=logging.INFO)

storage = MemoryStorage()
bot = Bot(token=cfg.TOKEN)
dp = Dispatcher(bot, storage=storage)
db = DataBase("database")
db1 = DataBase1("database")
db2 = Database2("database")


global jokol
global url_knpk


class Ref_state(StatesGroup):
    waiting_for_stiker_name = State()
    waiting_for_markups_name = State()
    waiting_for_viplata = State()
    waiting_for_Sberbank = State()
    waiting_for_Tinkoff = State()
    waiting_for_QIWI = State()
    waiting_for_Phone_Balance = State()
    admin_panele = State()
    rassilka = State()
    danot = State()
    dfsfsdfs = State()
    text_knopka = State()
    url_KNOPKA = State()
    all_knpk = State()
    podtverdut_rass = State()
    podtverdut_rass1423 = State()
    sber1 = State()
    sber2 = State()
    tinkoff1 = State()
    tinkoff2 = State()
    qiwi1 = State()
    qiw2 = State()
    phone = State()
    another_bank = State()
    bank1 = State()
    zayotnot = State()
    podotkl = State()
    admin_users = State()
    waiting_for_id_admin = State()
    deist_with_admin = State()
    waiting_for_id_admim_delete = State()
    balance = State()
    balance_id = State()
    balance_id_plus = State()
    balance_id_otn = State()
    balance_id_minus = State()
    block_user = State()
    block = State()
    rf_button = State()
    status_zadania = State()
    zadman = State()
    nafaz = State()
    hdao = State()
    balance_id_opopop = State()
    vlfvlfgvl = State()
    waiting_for_VTB = State()
    vtb1 = State()
    ymoney1 = State()
    waiting_for_YMONEY = State()
    alfa1 = State()
    waiting_for_AlfA = State()
    raifzn1 = State()
    waiting_for_raifzn = State()
    mtc1 = State()
    waiting_for_mtc = State()
    otk1 = State()
    waiting_for_otk = State()
    waiting_for_gasprom = State()
    gas1 = State()
    waiting_for_sovb = State()
    sovb = State()


def check_sub_channel(chat_member):
    if chat_member["status"] != "left":
        return True
    else:
        return False


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    global start_command
    if message.chat.type == "private":
        user_channel_status = await bot.get_chat_member(
            chat_id=cfg.CHANNEL_ID, user_id=message.from_user.id
        )

        if user_channel_status["status"] != "left":
            if not db.user_exists(message.from_user.id):
                start_command = message.text
                referrer_id = str(start_command[7:])
                if str(referrer_id) != "":
                    if str(referrer_id) != str(message.from_user.id):
                        db.add_user(
                            message.from_user.id,
                            message.from_user.full_name,
                            message.from_user.username,
                            referrer_id,
                        )
                        try:
                            await bot.send_message(
                                referrer_id,
                                "По вашей ссылке зарегестрировался новый пользователь!",
                            )
                        except:
                            pass
                    else:
                        db.add_user(
                            message.from_user.id,
                            message.from_user.full_name,
                            message.from_user.username,
                        )
                        await bot.send_message(
                            message.from_user.id,
                            "Нельзя регистрироваться по собственной реферальной ссылке!",
                        )
                else:
                    db.add_user(
                        message.from_user.id,
                        message.from_user.full_name,
                        message.from_user.username,
                    )

            time = datetime.now().strftime("%H:%M:%S %d-%m-2023")
            await bot.send_message(
                message.from_user.id,
                f"<i><b>MAIN MENU {time}</b></i>\n\n<i><b>{message.from_user.full_name}</b></i>\n<i>/start - <b>обновить</b></i>\n<i><b>Ваш id:</b></i><code>{message.from_user.id}</code>\n\n\n<b>💳Выполнено заданий:</b> 0\n\n\n<b>👥Кол-во рефералов:</b> {db.count_reeferals(message.from_user.id)}\n\n\n💷Заработано на рефералах: 0₽\n💵Заработано на заданиях: 0₽\n🧾Заработано за все время: 0₽\n\n<b>💰Баланс:</b> {get_user_balance(message.from_user.id)}\n\n\n<a href ='https://t.me/Arves_Money'><i><b>🗣[ПЕРЕЙТИ В КАНАЛ]</b></i></a>\n<a href = 'https://t.me/Arves_Chat'><i><b>🗣[ПЕРЕЙТИ В ЧАТ]</b></i></a>",
                reply_markup=nav.mainMenu,
                parse_mode="HTML",
                disable_web_page_preview=True,
            )

            user_id = message.from_user.id
            conn = sqlite3.connect("database")
            cursor = conn.cursor()
            cursor.execute("SELECT admin FROM users WHERE user_id = ?", (user_id,))
            result = cursor.fetchone()

            if result is not None and result[0] == 1:
                await bot.send_message(
                    message.from_user.id,
                    "Вы авторизовались как администратор!",
                    reply_markup=nav.Admin_Panele,
                )

            else:
                pass
            if message.from_user.id == int(cfg.ADMIN_ID):
                await bot.send_message(
                    message.from_user.id,
                    "Вы авторизовались как администратор!",
                    reply_markup=nav.Admin_Panele,
                )

            else:
                pass
        else:
            button = types.InlineKeyboardMarkup(row_width=1)
            m1 = types.InlineKeyboardButton(
                text="Подписаться", url="https://t.me/Arves_Job"
            )
            m2 = types.InlineKeyboardButton(text="Готово✅", callback_data="готово")
            button.add(m1, m2)
            await bot.send_message(
                message.from_user.id,
                "<i><b>Для доступа к полному функционалу бота подпишитесь на наш канал!</b></i>",
                reply_markup=button,
                parse_mode="HTML",
            )
            if not db.user_exists(message.from_user.id):
                start_command = message.text
                referrer_id = str(start_command[7:])
                if str(referrer_id) != "":
                    if str(referrer_id) != str(message.from_user.id):
                        db.add_user(
                            message.from_user.id,
                            message.from_user.full_name,
                            message.from_user.username,
                            referrer_id,
                        )
                        try:
                            await bot.send_message(
                                referrer_id,
                                "По вашей ссылке зарегестрировался новый пользователь!",
                            )
                        except:
                            pass
                    else:
                        db.add_user(
                            message.from_user.id,
                            message.from_user.full_name,
                            message.from_user.username,
                        )
                        await bot.send_message(
                            message.from_user.id,
                            "Нельзя регистрироваться по собственной реферальной ссылке!",
                        )
                else:
                    db.add_user(
                        message.from_user.id,
                        message.from_user.full_name,
                        message.from_user.username,
                    )


@dp.callback_query_handler(lambda call: True)
async def callback(call: types.CallbackQuery):
    if call.message:
        user_channel_status = await bot.get_chat_member(
            chat_id=cfg.CHANNEL_ID, user_id=call.from_user.id
        )
        time = datetime.now().strftime("%H:%M:%S %d-%m-2023")
        if user_channel_status["status"] != "left":
            await bot.send_message(
                call.from_user.id,
                f"<i><b>MAIN MENU {time}</b></i>\n\n<i><b>{call.from_user.full_name}</b></i>\n<i>/start - <b>обновить</b></i>\n<i><b>Ваш id:</b></i><code>{call.from_user.id}</code>\n\n\n<b>💳Выполнено заданий:</b> 0\n\n\n<b>👥Кол-во рефералов:</b> {db.count_reeferals(call.from_user.id)}\n\n\n💷Заработано на рефералах: 0₽\n💵Заработано на заданиях: 0₽\n🧾Заработано за все время: 0₽\n\n<b>💰Баланс:</b> {get_user_balance(call.from_user.id)}\n\n\n<a href ='https://t.me/Arves_Money'><i><b>🗣[ПЕРЕЙТИ В КАНАЛ]</b></i></a>\n<a href = 'https://t.me/Arves_Chat'><i><b>🗣[ПЕРЕЙТИ В ЧАТ]</b></i></a>",
                reply_markup=nav.mainMenu,
                parse_mode="HTML",
                disable_web_page_preview=True,
            )
        
        else:
            button = types.InlineKeyboardMarkup(row_width=1)
            m1 = types.InlineKeyboardButton(
                text="Подписаться", url="https://t.me/Arves_Job"
            )
            m2 = types.InlineKeyboardButton(text="Готово✅", callback_data="готово")
            button.add(m1, m2)
            await bot.send_message(
                call.from_user.id,
                "<i><b>Вы не подписались на канал,подпишитесь и попробуйте заново!</b></i>",
                reply_markup=button,
                parse_mode="HTML",
            )


class platzak(StatesGroup):
    pipl_mogut = State()
    kolichestvo_users_kotorue_smog = State()
    oplata_za_zadanie_na_odnogo_cheloveka = State()
    itog_if_punkt_one_one = State()
    oplata_if_punkt_one_one = State()
    users_mogut = State()
    verno_two_one = State()
    pobuj_one_punkt_two_one = State()
    time_two_one = State()
    pobuj_one_punkt_two_one = State()
    knpk_two_one = State()
    knopki_for_creators = State()
    knopki_creat = State()
    dalee = State()
    name = State()
    opis = State()
    photo = State()
    instr = State()
    pukts = State()
    
    if_punkt_one = State()
    kolvo_if_punkt_one = State()
    oplata_if_punkt_one = State()
    itog_if_punkt_one = State()
    pay_arv_if_punkt_one = State()
    
    if_punkt_two = State()
    if_punkt_two_two = State()
    kolvo_if_punkt_two = State()
    oplata_if_punkt_two = State()
    itog_if_punkt_two = State()
    pay_arv_if_punkt_two = State()
    
    if_punkt_tri = State()
    if_punkt_tri_two = State()
    if_punkt_tri_tri = State()
    kolvo_if_punkt_tri = State()
    oplata_if_punkt_tri = State()
    itog_if_punkt_tri = State()
    pay_arv_if_punkt_tri = State()
    
    if_punkt_four = State()
    if_punkt_four_two = State()
    if_punkt_four_tri = State()
    if_punkt_four_four = State()
    kolvo_if_punkt_four = State()
    oplata_if_punkt_four = State()
    itog_if_punkt_four = State()
    pay_arv_if_punkt_four = State()
    
    if_punkt_five = State()
    if_punkt_five_two= State()
    if_punkt_five_tri = State()
    if_punkt_five_four = State()
    if_punkt_five_five = State()
    kolvo_if_punkt_five = State()
    oplata_if_punkt_five = State()
    itog_if_punkt_five = State()
    pay_arv_if_punkt_five = State()
    
    if_punkt_six = State()
    if_punkt_six_two= State()
    if_punkt_six_tri = State()
    if_punkt_six_four = State()
    if_punkt_six_five = State()
    if_punkt_six_six = State()
    kolvo_if_punkt_six = State()
    oplata_if_punkt_six = State()
    itog_if_punkt_six = State()
    pay_arv_if_punkt_six = State()
    
    if_punkt_sem = State()
    if_punkt_sem_two= State()
    if_punkt_sem_tri = State()
    if_punkt_sem_four = State()
    if_punkt_sem_five = State()
    if_punkt_sem_six = State()
    if_punkt_sem_seven = State()
    kolvo_if_punkt_sem = State()
    oplata_if_punkt_sem = State()
    itog_if_punkt_sem = State()
    pay_arv_if_punkt_sem = State()
    
    if_punkt_sem = State()
    if_punkt_sem_two= State()
    if_punkt_sem_tri = State()
    if_punkt_sem_four = State()
    if_punkt_sem_five = State()
    if_punkt_sem_six = State()
    if_punkt_sem_seven = State()
    kolvo_if_punkt_sem = State()
    oplata_if_punkt_sem = State()
    itog_if_punkt_sem = State()
    pay_arv_if_punkt_sem = State()
    
    if_punkt_eight = State()
    if_punkt_eight_two= State()
    if_punkt_eight_tri = State()
    if_punkt_eight_four = State()
    if_punkt_eight_five = State()
    if_punkt_eight_six = State()
    if_punkt_eight_seven = State()
    if_punkt_eight_eight = State()
    kolvo_if_punkt_eight = State()
    oplata_if_punkt_eight = State()
    itog_if_punkt_eight = State()
    pay_arv_if_punkt_eight = State()
    
    if_punkt_nine = State()
    if_punkt_nine_two= State()
    if_punkt_nine_tri = State()
    if_punkt_nine_four = State()
    if_punkt_nine_five = State()
    if_punkt_nine_six = State()
    if_punkt_nine_seven = State()
    if_punkt_nine_eight = State()
    if_punkt_nine_nine = State()
    kolvo_if_punkt_nine = State()
    oplata_if_punkt_nine = State()
    itog_if_punkt_nine = State()
    pay_arv_if_punkt_nine = State()
    
    if_punkt_ten = State()
    if_punkt_ten_two= State()
    if_punkt_ten_tri = State()
    if_punkt_ten_four = State()
    if_punkt_ten_five = State()
    if_punkt_ten_six = State()
    if_punkt_ten_seven = State()
    if_punkt_ten_eight = State()
    if_punkt_ten_nine = State()
    if_punkt_ten_ten = State()
    kolvo_if_punkt_ten = State()
    oplata_if_punkt_ten = State()
    itog_if_punkt_ten = State()
    pay_arv_if_punkt_ten = State()
    
    if_punkt_eleven = State()
    if_punkt_eleven_two = State()
    if_punkt_eleven_tri = State()
    if_punkt_eleven_four = State()
    if_punkt_eleven_five = State()
    if_punkt_eleven_six = State()
    if_punkt_eleven_seven = State()
    if_punkt_eleven_eight = State()
    if_punkt_eleven_nine = State()
    if_punkt_eleven_ten = State()
    if_punkt_eleven_eleven = State()
    kolvo_if_punkt_eleven = State()
    oplata_if_punkt_eleven = State()
    itog_if_punkt_eleven = State()
    pay_arv_if_punkt_eleven = State()

    if_punkt_twelve = State()
    if_punkt_twelve_two = State()
    if_punkt_twelve_tri = State()
    if_punkt_twelve_four = State()
    if_punkt_twelve_five = State()
    if_punkt_twelve_six = State()
    if_punkt_twelve_seven = State()
    if_punkt_twelve_eight = State()
    if_punkt_twelve_nine = State()
    if_punkt_twelve_ten = State()
    if_punkt_twelve_eleven = State()
    if_punkt_twelve_twelve = State()
    kolvo_if_punkt_twelve = State()
    oplata_if_punkt_twelve = State()
    itog_if_punkt_twelve = State()
    pay_arv_if_punkt_twelve = State()
    
    if_punkt_thirteen = State()
    if_punkt_thirteen_two = State()
    if_punkt_thirteen_tri = State()
    if_punkt_thirteen_four = State()
    if_punkt_thirteen_five = State()
    if_punkt_thirteen_six = State()
    if_punkt_thirteen_seven = State()
    if_punkt_thirteen_eight = State()
    if_punkt_thirteen_nine = State()
    if_punkt_thirteen_ten = State()
    if_punkt_thirteen_eleven = State()
    if_punkt_thirteen_twelve = State()
    if_punkt_thirteen_thirteen = State()
    kolvo_if_punkt_thirteen = State()
    oplata_if_punkt_thirteen = State()
    itog_if_punkt_thirteen = State()
    pay_arv_if_punkt_thirteen = State()
    
    if_punkt_fourteen = State()
    if_punkt_fourteen_two = State()
    if_punkt_fourteen_tri = State()
    if_punkt_fourteen_four = State()
    if_punkt_fourteen_five = State()
    if_punkt_fourteen_six = State()
    if_punkt_fourteen_seven = State()
    if_punkt_fourteen_eight = State()
    if_punkt_fourteen_nine = State()
    if_punkt_fourteen_ten = State()
    if_punkt_fourteen_eleven = State()
    if_punkt_fourteen_twelve = State()
    if_punkt_fourteen_thirteen = State()
    if_punkt_fourteen_fourteen = State()
    kolvo_if_punkt_fourteen = State()
    oplata_if_punkt_fourteen = State()
    itog_if_punkt_fourteen = State()
    pay_arv_if_punkt_fourteen = State()
    
    if_punkt_fifteen = State()
    if_punkt_fifteen_two = State()
    if_punkt_fifteen_tri = State()
    if_punkt_fifteen_four = State()
    if_punkt_fifteen_five = State()
    if_punkt_fifteen_six = State()
    if_punkt_fifteen_seven = State()
    if_punkt_fifteen_eight = State()
    if_punkt_fifteen_nine = State()
    if_punkt_fifteen_ten = State()
    if_punkt_fifteen_eleven = State()
    if_punkt_fifteen_twelve = State()
    if_punkt_fifteen_thirteen = State()
    if_punkt_fifteen_fourteen = State()
    if_punkt_fifteen_fifteen = State()
    kolvo_if_punkt_fifteen = State()
    oplata_if_punkt_fifteen = State()
    itog_if_punkt_fifteen = State()
    pay_arv_if_punkt_fifteen = State()
        
    if_punkt_sixteen = State()
    if_punkt_sixteen_two = State()
    if_punkt_sixteen_tri = State()
    if_punkt_sixteen_four = State()
    if_punkt_sixteen_five = State()
    if_punkt_sixteen_six = State()
    if_punkt_sixteen_seven = State()
    if_punkt_sixteen_eight = State()
    if_punkt_sixteen_nine = State()
    if_punkt_sixteen_ten = State()
    if_punkt_sixteen_eleven = State()
    if_punkt_sixteen_twelve = State()
    if_punkt_sixteen_thirteen = State()
    if_punkt_sixteen_fourteen = State()
    if_punkt_sixteen_fifteen = State()
    if_punkt_sixteen_sixteen = State()
    kolvo_if_punkt_sixteen = State()
    oplata_if_punkt_sixteen = State()
    itog_if_punkt_sixteen = State()
    pay_arv_if_punkt_sixteen = State()

    if_punkt_seventeen = State()
    if_punkt_seventeen_two = State()
    if_punkt_seventeen_tri = State()
    if_punkt_seventeen_four = State()
    if_punkt_seventeen_five = State()
    if_punkt_seventeen_six = State()
    if_punkt_seventeen_seven = State()
    if_punkt_seventeen_eight = State()
    if_punkt_seventeen_nine = State()
    if_punkt_seventeen_ten = State()
    if_punkt_seventeen_eleven = State()
    if_punkt_seventeen_twelve = State()
    if_punkt_seventeen_thirteen = State()
    if_punkt_seventeen_fourteen = State()
    if_punkt_seventeen_fifteen = State()
    if_punkt_seventeen_sixteen = State()
    if_punkt_seventeen_seventeen = State()
    kolvo_if_punkt_seventeen = State()
    oplata_if_punkt_seventeen = State()
    itog_if_punkt_seventeen = State()
    pay_arv_if_punkt_seventeen = State()

    if_punkt_eighteen = State()
    if_punkt_eighteen_two = State()
    if_punkt_eighteen_tri = State()
    if_punkt_eighteen_four = State()
    if_punkt_eighteen_five = State()
    if_punkt_eighteen_six = State()
    if_punkt_eighteen_seven = State()
    if_punkt_eighteen_eight = State()
    if_punkt_eighteen_nine = State()
    if_punkt_eighteen_ten = State()
    if_punkt_eighteen_eleven = State()
    if_punkt_eighteen_twelve = State()
    if_punkt_eighteen_thirteen = State()
    if_punkt_eighteen_fourteen = State()
    if_punkt_eighteen_fifteen = State()
    if_punkt_eighteen_sixteen = State()
    if_punkt_eighteen_seventeen = State()
    if_punkt_eighteen_eighteen = State()
    kolvo_if_punkt_eighteen = State()
    oplata_if_punkt_eighteen = State()
    itog_if_punkt_eighteen = State()
    pay_arv_if_punkt_eighteen = State()

    if_punkt_nineteen = State()
    if_punkt_nineteen_two = State()
    if_punkt_nineteen_tri = State()
    if_punkt_nineteen_four = State()
    if_punkt_nineteen_five = State()
    if_punkt_nineteen_six = State()
    if_punkt_nineteen_seven = State()
    if_punkt_nineteen_eight = State()
    if_punkt_nineteen_nine = State()
    if_punkt_nineteen_ten = State()
    if_punkt_nineteen_eleven = State()
    if_punkt_nineteen_twelve = State()
    if_punkt_nineteen_thirteen = State()
    if_punkt_nineteen_fourteen = State()
    if_punkt_nineteen_fifteen = State()
    if_punkt_nineteen_sixteen = State()
    if_punkt_nineteen_seventeen = State()
    if_punkt_nineteen_eighteen = State()
    if_punkt_nineteen_nineteen = State()
    kolvo_if_punkt_nineteen = State()
    oplata_if_punkt_nineteen = State()
    itog_if_punkt_nineteen = State()
    pay_arv_if_punkt_nineteen = State()

    if_punkt_twenty = State()
    if_punkt_twenty_two = State()
    if_punkt_twenty_tri = State()
    if_punkt_twenty_four = State()
    if_punkt_twenty_five = State()
    if_punkt_twenty_six = State()
    if_punkt_twenty_seven = State()
    if_punkt_twenty_eight = State()
    if_punkt_twenty_nine = State()
    if_punkt_twenty_ten = State()
    if_punkt_twenty_eleven = State()
    if_punkt_twenty_twelve = State()
    if_punkt_twenty_thirteen = State()
    if_punkt_twenty_fourteen = State()
    if_punkt_twenty_fifteen = State()
    if_punkt_twenty_sixteen = State()
    if_punkt_twenty_seventeen = State()
    if_punkt_twenty_eighteen = State()
    if_punkt_twenty_nineteen = State()
    if_punkt_twenty_twenty = State()
    kolvo_if_punkt_twenty = State()
    oplata_if_punkt_twenty = State()
    itog_if_punkt_twenty = State()
    pay_arv_if_punkt_twenty = State()
    
    if_punkt_twenty_one = State()
    if_punkt_twenty_one_two = State()
    if_punkt_twenty_one_tri = State()
    if_punkt_twenty_one_four = State()
    if_punkt_twenty_one_five = State()
    if_punkt_twenty_one_six = State()
    if_punkt_twenty_one_seven = State()
    if_punkt_twenty_one_eight = State()
    if_punkt_twenty_one_nine = State()
    if_punkt_twenty_one_ten = State()
    if_punkt_twenty_one_eleven = State()
    if_punkt_twenty_one_twelve = State()
    if_punkt_twenty_one_thirteen = State()
    if_punkt_twenty_one_fourteen = State()
    if_punkt_twenty_one_fifteen = State()
    if_punkt_twenty_one_sixteen = State()
    if_punkt_twenty_one_seventeen = State()
    if_punkt_twenty_one_eighteen = State()
    if_punkt_twenty_one_nineteen = State()
    if_punkt_twenty_one_twenty = State()
    if_punkt_twenty_one_twenty_one = State()
    kolvo_if_punkt_twenty_one = State()
    oplata_if_punkt_twenty_one = State()
    itog_if_punkt_twenty_one = State()
    pay_arv_if_punkt_twenty_one = State()

    if_punkt_twenty_two = State()
    if_punkt_twenty_two_two = State()
    if_punkt_twenty_two_tri = State()
    if_punkt_twenty_two_four = State()
    if_punkt_twenty_two_five = State()
    if_punkt_twenty_two_six = State()
    if_punkt_twenty_two_seven = State()
    if_punkt_twenty_two_eight = State()
    if_punkt_twenty_two_nine = State()
    if_punkt_twenty_two_ten = State()
    if_punkt_twenty_two_eleven = State()
    if_punkt_twenty_two_twelve = State()
    if_punkt_twenty_two_thirteen = State()
    if_punkt_twenty_two_fourteen = State()
    if_punkt_twenty_two_fifteen = State()
    if_punkt_twenty_two_sixteen = State()
    if_punkt_twenty_two_seventeen = State()
    if_punkt_twenty_two_eighteen = State()
    if_punkt_twenty_two_nineteen = State()
    if_punkt_twenty_two_twenty = State()
    if_punkt_twenty_two_twenty_one = State()
    if_punkt_twenty_two_twenty_two = State()
    kolvo_if_punkt_twenty_two = State()
    oplata_if_punkt_twenty_two = State()
    itog_if_punkt_twenty_two = State()
    pay_arv_if_punkt_twenty_two = State()

    if_punkt_twenty_three = State()
    if_punkt_twenty_three_two = State()
    if_punkt_twenty_three_tri = State()
    if_punkt_twenty_three_four = State()
    if_punkt_twenty_three_five = State()
    if_punkt_twenty_three_six = State()
    if_punkt_twenty_three_seven = State()
    if_punkt_twenty_three_eight = State()
    if_punkt_twenty_three_nine = State()
    if_punkt_twenty_three_ten = State()
    if_punkt_twenty_three_eleven = State()
    if_punkt_twenty_three_twelve = State()
    if_punkt_twenty_three_thirteen = State()
    if_punkt_twenty_three_fourteen = State()
    if_punkt_twenty_three_fifteen = State()
    if_punkt_twenty_three_sixteen = State()
    if_punkt_twenty_three_seventeen = State()
    if_punkt_twenty_three_eighteen = State()
    if_punkt_twenty_three_nineteen = State()
    if_punkt_twenty_three_twenty = State()
    if_punkt_twenty_three_twenty_one = State()
    if_punkt_twenty_three_twenty_two = State()
    if_punkt_twenty_three_twenty_three = State()
    kolvo_if_punkt_twenty_three = State()
    oplata_if_punkt_twenty_three = State()
    itog_if_punkt_twenty_three = State()
    pay_arv_if_punkt_twenty_three = State()

    if_punkt_twenty_four = State()
    if_punkt_twenty_four_two = State()
    if_punkt_twenty_four_tri = State()
    if_punkt_twenty_four_four = State()
    if_punkt_twenty_four_five = State()
    if_punkt_twenty_four_six = State()
    if_punkt_twenty_four_seven = State()
    if_punkt_twenty_four_eight = State()
    if_punkt_twenty_four_nine = State()
    if_punkt_twenty_four_ten = State()
    if_punkt_twenty_four_eleven = State()
    if_punkt_twenty_four_twelve = State()
    if_punkt_twenty_four_thirteen = State()
    if_punkt_twenty_four_fourteen = State()
    if_punkt_twenty_four_fifteen = State()
    if_punkt_twenty_four_sixteen = State()
    if_punkt_twenty_four_seventeen = State()
    if_punkt_twenty_four_eighteen = State()
    if_punkt_twenty_four_nineteen = State()
    if_punkt_twenty_four_twenty = State()
    if_punkt_twenty_four_twenty_one = State()
    if_punkt_twenty_four_twenty_two = State()
    if_punkt_twenty_four_twenty_three = State()
    if_punkt_twenty_four_twenty_four = State()
    kolvo_if_punkt_twenty_four = State()
    oplata_if_punkt_twenty_four = State()
    itog_if_punkt_twenty_four = State()
    pay_arv_if_punkt_twenty_four = State()

    if_punkt_twenty_five = State()
    if_punkt_twenty_five_two = State()
    if_punkt_twenty_five_tri = State()
    if_punkt_twenty_five_four = State()
    if_punkt_twenty_five_five = State()
    if_punkt_twenty_five_six = State()
    if_punkt_twenty_five_seven = State()
    if_punkt_twenty_five_eight = State()
    if_punkt_twenty_five_nine = State()
    if_punkt_twenty_five_ten = State()
    if_punkt_twenty_five_eleven = State()
    if_punkt_twenty_five_twelve = State()
    if_punkt_twenty_five_thirteen = State()
    if_punkt_twenty_five_fourteen = State()
    if_punkt_twenty_five_fifteen = State()
    if_punkt_twenty_five_sixteen = State()
    if_punkt_twenty_five_seventeen = State()
    if_punkt_twenty_five_eighteen = State()
    if_punkt_twenty_five_nineteen = State()
    if_punkt_twenty_five_twenty = State()
    if_punkt_twenty_five_twenty_one = State()
    if_punkt_twenty_five_twenty_two = State()
    if_punkt_twenty_five_twenty_three = State()
    if_punkt_twenty_five_twenty_four = State()
    if_punkt_twenty_five_twenty_five = State()
    kolvo_if_punkt_twenty_five = State()
    oplata_if_punkt_twenty_five = State()
    itog_if_punkt_twenty_five = State()
    pay_arv_if_punkt_twenty_five = State()
    knpk = State()
    pobuj_one_punkt = State()
    verno = State()
    time = State()
    knpk_one_2 = State()
    knpk_one_3 = State()
    knpk_one_4 = State()
    knpk_one_5 = State()
    knpk_one_6 = State()
    knpk_one_7 = State()

















@dp.message_handler(Text(equals="Для заказчиков📝", ignore_case=True), state=None)
async def tadm454(message: types.Message, state: FSMContext) -> None:
    pravila = InlineKeyboardMarkup(row_width=1)
    p1 = InlineKeyboardButton(
        text="Праивла и условия❗",
        url="https://telegra.ph/ARVESPravila-i-usloviya-raboty-v-roli-zakazchika-11-11",
    )
    pravila.row(p1)
    p2 = InlineKeyboardButton(text="Ознакомился✅", callback_data="dalee")
    pravila.row(p2)

    zadania = ReplyKeyboardMarkup(resize_keyboard=True)

    n5 = KeyboardButton("⬅️Назад в меню")
    zadania.row(n5)
    await message.answer(
        f"<i><u>Arves</u> стал <b>первым</b> интернет-интсрументом,чьи услуги на рынке <u>микро-бирж</u> стали <b>самыми выгодными</b> в СНГ!</i>",
        parse_mode="HTML",
        reply_markup=zadania,
    )
    await message.answer(
        f"<i>Перед началом работы в роли заказчика,пожалуйста,ознакомься с правилами и условиями работы!</i>",
        parse_mode="HTML",
        reply_markup=pravila,
    )
    await state.set_state(platzak.dalee)


@dp.callback_query_handler(Text(equals="dalee"), state=platzak.dalee)
async def dalee2(callback: types.CallbackQuery, state: FSMContext) -> None:
    knopki_for_creators = ReplyKeyboardMarkup(resize_keyboard=True)
    knpk1 = KeyboardButton("Создать задание✏️")
    knopki_for_creators.row(knpk1)
    knpk2 = KeyboardButton("Мои задания📝")
    knopki_for_creators.row(knpk2)
    knpk3 = KeyboardButton("⬅️Назад в меню")
    knopki_for_creators.row(knpk3)
    
    time = datetime.now().strftime("%H:%M:%S %d-%m-2023")
    await callback.message.answer(
        f"<i><b>CREATOR'S MENU💡 \n{time}</b></i>\n\n<i><b>{callback.from_user.full_name}</b></i>\n<i><b>Ваш id:</b></i><code>{callback.from_user.id}</code>\n\n<b>📄Заданий опубликовано:</b> 0\n\n🟢Заданий в работе: 0\n🟢Выполненных заданий: 0\n🔴Заблокированных заданий: 0₽\n\n<b>💰Потрачено на задания</b>:0",parse_mode="HTML",disable_web_page_preview=True,reply_markup=knopki_for_creators
    )
    await state.set_state(platzak.knopki_for_creators)
@dp.message_handler(Text(equals="⬅️Назад в меню"), state=platzak.dalee)
async def dalee(message: types.Message, state: FSMContext) -> None:
    await state.reset_state()
    await start(message)
    
@dp.message_handler(Text(equals="⬅️Назад в меню"), state=platzak.knopki_for_creators)
async def dalee(message: types.Message, state: FSMContext) -> None:
    await state.reset_state()
    await start(message)
       
@dp.message_handler(Text(equals="Мои задания📝"), state=platzak.knopki_for_creators)
async def dalee(message: types.Message, state: FSMContext) -> None:
    myzadania = ReplyKeyboardMarkup(resize_keyboard=True)
    m1 = KeyboardButton("Задания в работе🟢")
    myzadania.row(m1)
    m2 = KeyboardButton("Отложенные задания🕒")
    myzadania.add(m2)
    m3 = KeyboardButton("Задания на модерации👌")
    myzadania.row(m3)
    m4 = KeyboardButton("⬅️Назад в меню")
    myzadania.row(m4)
    await message.answer("This button is dont work.Please again later!",reply_markup=myzadania)
    await state.set_state(platzak.knopki_creat)
    
@dp.message_handler(Text(equals="Задания в работе🟢"), state=platzak.knopki_creat)
async def dalee(message: types.Message, state: FSMContext) -> None: 
    pass   
    
@dp.message_handler(Text(equals="Отложенные задания🕒"), state=platzak.knopki_creat)
async def dalee(message: types.Message, state: FSMContext) -> None: 
    pass   
    
@dp.message_handler(Text(equals="⬅️Назад в меню"), state=platzak.knopki_creat)
async def dalee456(message: types.Message, state: FSMContext) -> None: 
    knopki_for_creators = ReplyKeyboardMarkup(resize_keyboard=True)
    knpk1 = KeyboardButton("Создать задание✏️")
    knopki_for_creators.row(knpk1)
    knpk2 = KeyboardButton("Мои задания📝")
    knopki_for_creators.row(knpk2)
    knpk3 = KeyboardButton("⬅️Назад в меню")
    knopki_for_creators.row(knpk3)
    
    time = datetime.now().strftime("%H:%M:%S %d-%m-2023")
    await message.answer(
        f"<i><b>CREATOR'S MENU💡 \n{time}</b></i>\n\n<i><b>{message.from_user.full_name}</b></i>\n<i><b>Ваш id:</b></i><code>{message.from_user.id}</code>\n\n<b>📄Заданий опубликовано:</b> 0\n\n🟢Заданий в работе: 0\n🟢Выполненных заданий: 0\n🔴Заблокированных заданий: 0₽\n\n<b>💰Потрачено на задания</b>:0",parse_mode="HTML",disable_web_page_preview=True,reply_markup=knopki_for_creators
    )
    await state.set_state(platzak.knopki_for_creators)
    
    
    
    
@dp.message_handler(Text(equals="Создать задание✏️"), state=platzak.knopki_for_creators)
async def dalee545343(message: types.Message, state: FSMContext) -> None: 
    #await bot.send_message(chat_id=message.from_user.id,text="Готовим базу данных 0%...") 
    #await asyncio.sleep(0.10)  
    #await bot.edit_message_text(text="Готовим базу данных 28%...", chat_id=message.chat.id, message_id=message.message_id -1)
    #await asyncio.sleep(0.10)  
    #await bot.edit_message_text(chat_id=message.from_user.id,message_id=message.message_id -1 ,text="d")
    #await asyncio.sleep(0.10)  
    #await bot.edit_message_text(chat_id=message.from_user.id,message_id=message.message_id -1,text="Готовим базу данных 46%...")
    #await asyncio.sleep(0.10) 
    #await bot.edit_message_text(chat_id=message.from_user.id,message_id=message.message_id -1,text="Готовим базу данных 88%...")
    #await asyncio.sleep(1.89)
    #await bot.edit_message_text(chat_id=message.from_user.id,message_id=message.message_id -1,text="База данных готова для работы✅")
    nazad_name = ReplyKeyboardMarkup(resize_keyboard=True)
    naz_name1 = KeyboardButton("⬅️Назад в меню")
    nazad_name.row(naz_name1)
    await message.answer("<i>Введите название вашего задания!</i>\n<u><i>Длина не более <b>27</b> символов!</i></u>",parse_mode="HTML",reply_markup=nazad_name)
    await state.set_state(platzak.name)
    
    
@dp.message_handler(Text(equals="⬅️Назад в меню"), state=platzak.name)
async def dalee(message: types.Message, state: FSMContext) -> None:
    knopki_for_creators = ReplyKeyboardMarkup(resize_keyboard=True)
    knpk1 = KeyboardButton("Создать задание✏️")
    knopki_for_creators.row(knpk1)
    knpk2 = KeyboardButton("Мои задания📝")
    knopki_for_creators.row(knpk2)
    knpk3 = KeyboardButton("⬅️Назад в меню")
    knopki_for_creators.row(knpk3)
    
    time = datetime.now().strftime("%H:%M:%S %d-%m-2023")
    await message.answer(
        f"<i><b>CREATOR'S MENU💡 \n{time}</b></i>\n\n<i><b>{message.from_user.full_name}</b></i>\n<i><b>Ваш id:</b></i><code>{message.from_user.id}</code>\n\n<b>📄Заданий опубликовано:</b> 0\n\n🟢Заданий в работе: 0\n🟢Выполненных заданий: 0\n🔴Заблокированных заданий: 0₽\n\n<b>💰Потрачено на задания</b>:0",parse_mode="HTML",disable_web_page_preview=True,reply_markup=knopki_for_creators
    )
    await state.set_state(platzak.knopki_for_creators)    
    

    
@dp.message_handler(content_types=['text'], state=platzak.name)
async def name_for_task(message: types.Message, state: FSMContext) -> None:
    global name
    name = message.html_text
    if len(name) > 27:
        await message.answer("<i><u>Ваше название более 27 символов!</u></i>",parse_mode="HTML")
        await state.set_state(platzak.name)
        await dalee545343(message, state)

    else:
        
        potential_number = str(uuid.uuid4().hex[:30])
        indeficat_namber = potential_number
        username = message.from_user.username
        user_id = message.from_user.id
        
        async with state.proxy() as data:
            data['indeficat_namber'] = indeficat_namber
        
        otloj = ReplyKeyboardMarkup(resize_keyboard=True)
        
        ot1 = KeyboardButton("⬅️Назад")
        otloj.row(ot1)
        await message.reply("<i>Название сохранено!</i>", parse_mode="HTML",reply_markup=otloj)
        conn = sqlite3.connect("database")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO tasks (indeficat_namber,username,user_id,name) VALUES (?,?,?,?)",(indeficat_namber,username,user_id,name))
        conn.commit()
        await message.answer(
            "<i>Отправь  описание своего задания!</i>\n<i><u>Длина не более 405 символов!</u></i>",parse_mode="HTML"
        )
        await state.set_state(platzak.opis
                              ) 
@dp.message_handler(Text(equals="⬅️Назад",ignore_case=True),state=platzak.opis)
async def kgkkgk(message: types.Message,state: FSMContext):
    await dalee456(message,state)
    await state.set_state(platzak.knopki_creat)      
        
def check_unique_number(number):
    conn = sqlite3.connect("database")
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM tasks WHERE indeficat_namber = ?", (number,))
    count = cursor.fetchone()[0]
    conn.close()
    return count == 0
    
@dp.message_handler(content_types=['text'], state=platzak.opis)
async def dalee_ffkskfsdkf4543(message: types.Message, state: FSMContext) -> None:  
    global opis
    opis = message.html_text
    if len(opis) > 405:
        await message.answer("<i><u>Ваше описание превышает допустимую длину!</u></i>",parse_mode="HTML")
        await state.set_state(platzak.opis)
        await name_for_task(message,state)
    else:
        async with state.proxy() as data:
            indeficat_namber = data['indeficat_namber']

        # Обновляем строку в базе данных
        conn = sqlite3.connect("database")
        cursor = conn.cursor()
        cursor.execute("UPDATE tasks SET about = ? WHERE indeficat_namber = ?", (opis, indeficat_namber))
        conn.commit()
        otloj = ReplyKeyboardMarkup(resize_keyboard=True)
        ot = KeyboardButton("Отложить задвние⏳")
        otloj.row(ot)
        ot1 = KeyboardButton("⬅️Назад")
        otloj.row(ot1)
        await message.reply("<i>Описание сохранено!</i>",parse_mode="HTML",reply_markup=otloj)
        await message.answer("<i><u>Отправь фото для твоего задания(обложка)!</u></i>",parse_mode="HTML")
        await state.set_state(platzak.photo)
        
@dp.message_handler(Text(equals="⬅️Назад",ignore_case=True),state=platzak.photo)
async def kgkkgk(message: types.Message,state: FSMContext):
    await dalee545343(message,state)
    await state.set_state(platzak.name)
        
@dp.message_handler(content_types=['photo'], state=platzak.photo)
async def dalee656454454353(message: types.Message, state: FSMContext) -> None:
    global gl_photo
    gl_photo = message.photo
    file_id = gl_photo[-1].file_id

    # Сохраняем file_id в состоянии
    async with state.proxy() as data:
        data['file_id'] = file_id
    
    conn = sqlite3.connect("database")
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET photo = ? WHERE indeficat_namber = ?", (file_id, data['indeficat_namber']))
    conn.commit()
    conn.close()
    otloj = ReplyKeyboardMarkup(resize_keyboard=True)
    ot = KeyboardButton("Отложить задание⏳")
    otloj.row(ot)
    ot1 = KeyboardButton("⬅️Назад в меню")
    otloj.row(ot1)
    await message.reply("<i>Фото сохранено!</i>",parse_mode="HTML",reply_markup=otloj)
    instr = InlineKeyboardMarkup(row_width=1)
    in1 = InlineKeyboardButton(text="Написать инструкцию⚙️",url="https://telegra.ph")
    instr.add(in1)
    await message.answer("<i>Отправь ссылку на статью с инструкцией!</i>",parse_mode="HTML",reply_markup=instr)
    await state.set_state(platzak.instr)
    

@dp.message_handler(Text(equals="⬅️Назад",ignore_case=True),state=platzak.instr)
async def kgkkgk(message: types.Message,state: FSMContext):
    await dalee_ffkskfsdkf4543(message,state)
    await state.set_state(platzak.opis)
    
  
  
  
@dp.message_handler(Text(equals="Отложить задание⏳",ignore_case=True),state=platzak.instr)
async def kgkkgk(message: types.Message,state: FSMContext):
    pass
  
  
  
  
  
  
  
  
  
  
  
  
  
       
    
    
    
    

@dp.message_handler(content_types=['text'], state=platzak.instr)
async def dalee(message: types.Message, state: FSMContext) -> None:  
    global instr
    instr = message.html_text
    link = r"https?://\S+"
    
    async with state.proxy() as data:
        file_id = data['file_id']
        indeficat_namber = data['indeficat_namber']
    if re.search(link, instr):
        conn = sqlite3.connect("database")
        cursor = conn.cursor()
        cursor.execute("UPDATE tasks SET instr = ? WHERE indeficat_namber = ?", (instr, indeficat_namber))
        conn.commit()
        conn.close()
        otloj = ReplyKeyboardMarkup(resize_keyboard=True)
        ot = KeyboardButton("Отложить задвние⏳")
        otloj.row(ot)
        ot1 = KeyboardButton("⬅️Назад в меню")
        otloj.row(ot1)
        await message.reply("<i>Инструкция сохранена!</i>",parse_mode="HTML",reply_markup=otloj)
        await message.answer("<i>Введите кол-во пуктов,при выполнении которых исполнитель сможет выполнить задание!</i>\n<i><u>Не менее 1 пунтка,не более 10 пунктов!</u></i>",parse_mode="HTML")
        await state.set_state(platzak.pukts)
    else:
        await message.reply("<i>Это не ссылка!</i>",parse_mode="HTML")
        await state.set_state(platzak.instr)
        instr = InlineKeyboardMarkup(row_width=1)
        in1 = InlineKeyboardButton(text="Написать инструкцию⚙️",url="https://telegra.ph")
        instr.add(in1)
        await message.answer("<i>Отправь ссылку на статью с инструкцией!</i>",parse_mode="HTML",reply_markup=instr)
     
     
@dp.message_handler(Text(equals="⬅️Назад",ignore_case=True),state=platzak.pukts)
async def kgkkgk(message: types.Message,state: FSMContext):
    await dalee_ffkskfsdkf4543(message,state)
    await state.set_state(platzak.opis)
    
  
  
  
@dp.message_handler(Text(equals="Отложить задание⏳",ignore_case=True),state=platzak.instr)
async def kgkkgk(message: types.Message,state: FSMContext):
    pass

    
    
       
@dp.message_handler(content_types=['text'], state=platzak.pukts)
async def dalee(message: types.Message, state: FSMContext) -> None: 
    global punkts
    punkts = (int(message.html_text))
    if punkts > 10:
        await message.reply("<i><u>Не более 15 пунктов!</u></i>",parse_mode="HTML") 
        await state.set_state(platzak.pukts) 
        await message.answer("<i>Введите кол-во пуктов,при выполнении которых исполнитель сможет выполнить задание!</i>\n<i><u>Не менее 1 пунтка,не более 25 пунктов!</u></i>",parse_mode="HTML")
    elif punkts < 1:
        await message.reply("<i><u>Не менее 1 пункта!</u></i>",parse_mode="HTML") 
        await state.set_state(platzak.pukts) 
        await message.answer("<i>Введите кол-во пуктов,при выполнении которых исполнитель сможет выполнить задание!</i>\n<i><u>Не менее 1 пунтка,не более 25 пунктов!</u></i>",parse_mode="HTML")

    elif punkts == 1:
        await message.answer("<i>Объясните <u>нужные Вам действия</u> со стороны исполнителя при выполнении <u>единственного пункта</u> вашего задания!</i>",parse_mode="HTML") 
        await state.set_state(platzak.if_punkt_one) 

    async with state.proxy() as data:
        indeficat_namber = data['indeficat_namber']

    # Обновляем строку в базе данных, добавляя значение punkts
    conn = sqlite3.connect("database")
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET punkts = ? WHERE indeficat_namber = ?", (punkts, indeficat_namber))
    conn.commit()
    conn.close()
    
@dp.message_handler(content_types = ["text"], state = platzak.if_punkt_one) 
async def punkt1(message: types. Message, state: FSMContext):
    knpk = ReplyKeyboardMarkup(resize_keyboard=True)
    k1 = KeyboardButton("photo")
    knpk.row(k1)
    k2 = KeyboardButton("video")
    knpk.row(k2)
    k3 = KeyboardButton("voice")
    knpk.row(k3)
    k4 = KeyboardButton("audio")
    knpk.row(k4)
    k5 = KeyboardButton("file(photo,video...)")  
    knpk.row(k5)
    k6 = KeyboardButton("document(.docx)")
    knpk.row(k6)
    k7 = KeyboardButton("sticker")
    knpk.row(k7)
    k8 = KeyboardButton("animation")
    knpk.row(k8)
    k9 = KeyboardButton("text(link,plain text...)")
    knpk.row(k9)  
    k10 = KeyboardButton("missing(accept all)")
    knpk.row(k10)
    k11 = KeyboardButton("geolocation(In development...)")
    knpk.row(k11)
    
    global punkt_one_about
    punkt_one_about = message.html_text
    async with state.proxy() as data:
        indeficat_namber = data['indeficat_namber']

        # Обновляем строку в базе данных, добавляя значение one_first_message
        conn = sqlite3.connect("database")
        cursor = conn.cursor()
        cursor.execute("UPDATE tasks SET one_first_message = ? WHERE indeficat_namber = ?", (punkt_one_about, indeficat_namber))
        conn.commit()
        conn.close()
        
    await message.reply("<i>Какую информацию вы ждете от пользователя?</i>\n<i><u>Используйте кнопки!</u></i>",parse_mode="HTML",reply_markup=knpk) 
    await state.set_state(platzak.knpk) 
    
@dp.message_handler(Text(equals="photo"), state = platzak.knpk) 
async def punkt1(message: types. Message, state: FSMContext):
    otloj = ReplyKeyboardMarkup(resize_keyboard=True)
    ot = KeyboardButton("Отложить задвние⏳")
    otloj.row(ot)
    ot1 = KeyboardButton("⬅️Назад в меню")
    otloj.row(ot1)
    await message.answer("<i><u>Введите текст,который будет побуждать исполнителя отправить вам информацию данного типа!</u></i>\n<b>Например:</b>\n<i>ОТПРАВЬТЕ СКРИНШОТ САЙТА</i>\n<i>ОТПРАВЬТЕ СКРИНШОТ ВАШЕЙ ПОДПИСКИ...</i>",parse_mode="HTML",reply_markup=otloj) 
    await state.set_state(platzak.pobuj_one_punkt)
    
    async with state.proxy() as data:
        indeficat_namber = data['indeficat_namber']

    # Обновляем строку в базе данных, добавляя значение one_informas
    conn = sqlite3.connect("database")
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET one_informas = ? WHERE indeficat_namber = ?", ("photo", indeficat_namber))
    conn.commit()
    conn.close()
    
@dp.message_handler(content_types=["text"], state = platzak.pobuj_one_punkt) 
async def punkt1(message: types. Message, state: FSMContext):
    global pobuj
    pobuj = message.text
    async with state.proxy() as data:
        indeficat_namber = data['indeficat_namber']

        # Обновляем строку в базе данных, добавляя значение one_first_message
        conn = sqlite3.connect("database")
        cursor = conn.cursor()
        cursor.execute("UPDATE tasks SET one_second_message = ? WHERE indeficat_namber = ?", (pobuj, indeficat_namber))
        conn.commit()
        conn.close()
        otloj = ReplyKeyboardMarkup(resize_keyboard=True)
        ot = KeyboardButton("Отложить задвние⏳")
        otloj.row(ot)
        ot1 = KeyboardButton("⬅️Назад в меню")
        otloj.row(ot1)
    await message.answer("<i>Сколько времени дается на выполнение данного пункта?</i>\n<b>В минутах!</b>",parse_mode="HTML",reply_markup=otloj)
    await state.set_state(platzak.time)
    #await message.answer(f"<b>Сообщения,которые бот отправит исполнителю при 1 пункте:</b>\n\n<b>first:</b>\n\n{punkt_one_about}\n\n<b>second:</b>\n\n{pobuj}\n\n<b>Ожидаемая информация от пользователя:<i><u>Photo</u></i></b>",parse_mode="HTML")
    #await message.answer("<b>Все верно?</b>",parse_mode="HTML")
    #await state.set_state(platzak.verno)
    
@dp.message_handler(content_types=["text"], state = platzak.time) 
async def punkt1(message: types. Message, state: FSMContext):  
    
    try:
        danot = ReplyKeyboardMarkup(resize_keyboard=True)
        d1 = KeyboardButton("Да,продолжить✅")
        danot.row(d1)
        d2 = KeyboardButton("Нет,изменить❌")
        danot.row(d2)
        time = int(message.text)
        async with state.proxy() as data:
            indeficat_namber = data['indeficat_namber']

        # Обновляем строку в базе данных, добавляя значение one_first_message
        conn = sqlite3.connect("database")
        cursor = conn.cursor()
        cursor.execute("UPDATE tasks SET time_one_one = ? WHERE indeficat_namber = ?", (time, indeficat_namber))
        conn.commit()
        conn.close()
        otloj = ReplyKeyboardMarkup(resize_keyboard=True)
        ot = KeyboardButton("Отложить задвние⏳")
        otloj.row(ot)
        ot1 = KeyboardButton("⬅️Назад в меню")
        otloj.row(ot1)  
        await message.answer(f"<b>Сообщения,которые бот отправит исполнителю при 1 пункте:</b>\n\n<b>first:</b>\n\n{punkt_one_about}\n\n<b>second:</b>\n\n{pobuj}\n\n<b>Ожидаемая информация от пользователя:<i><u>Photo</u></i></b>\n<b>Время на выполнение данного пункта:</b><i><u>{time} минут(а)</u></i>",parse_mode="HTML",reply_markup=otloj)
        await message.answer("<b>Все верно?</b>",parse_mode="HTML",reply_markup=danot)
        await state.set_state(platzak.verno)
    except ValueError:
        await message.reply("<b>Введи число!</b>",parse_mode="HTML")
    
    
    
    
    
    

@dp.message_handler(Text(equals="Да,продолжить✅"), state = platzak.verno) 
async def punkt1(message: types. Message, state: FSMContext):
      await oplata_za_zadanie_na_odnogo_cheloveka(message,state)
      await state.set_state(platzak.oplata_za_zadanie_na_odnogo_cheloveka)

@dp.message_handler(Text(equals="Нет,изменить❌"), state = platzak.verno) 
async def punkt1(message: types. Message, state: FSMContext):
        await message. answer("<i>Объясните <u>нужные Вам действия</u> со стороны исполнителя при выполнении <u>единственного пункта</u> вашего задания!</i>",parse_mode="HTML") 
        await state.set_state(platzak.if_punkt_one) 

    
@dp.message_handler(Text(equals="video"), state = platzak.knpk) 
async def punkt1(message: types. Message, state: FSMContext):
    otloj = ReplyKeyboardMarkup(resize_keyboard=True)
    ot = KeyboardButton("Отложить задвние⏳")
    otloj.row(ot)
    ot1 = KeyboardButton("⬅️Назад в меню")
    otloj.row(ot1)
    await message.answer("<i><u>Введите текст,который будет побуждать исполнителя отправить вам информацию данного типа!</u></i>\n<b>Например:</b>\n<i>ОТПРАВЬТЕ СКАЧАННОЕ ВИДЕО</i>\n<i>ОТПРАВЬТЕ ЗАПИСЬ ЭКРАНА...</i>",parse_mode="HTML",reply_markup=otloj) 
    await state.set_state(platzak.pobuj_one_punkt)
    
    
    
@dp.message_handler(content_types=["text"], state = platzak.pobuj_one_punkt) 
async def punkt1(message: types. Message, state: FSMContext):
    global pobuj
    pobuj = message.text
    async with state.proxy() as data:
        indeficat_namber = data['indeficat_namber']

    # Обновляем строку в базе данных, добавляя значение one_informas
    conn = sqlite3.connect("database")
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET one_informas = ? WHERE indeficat_namber = ?", ("video", indeficat_namber))
    conn.commit()
    conn.close()
    otloj = ReplyKeyboardMarkup(resize_keyboard=True)
    ot = KeyboardButton("Отложить задвние⏳")
    otloj.row(ot)
    ot1 = KeyboardButton("⬅️Назад в меню")
    otloj.row(ot1)
    await message.answer("<i>Сколько времени дается на выполнение данного пункта?</i>\n<b>В минутах!</b>",parse_mode="HTML",reply_markup=otloj)
    await state.set_state(platzak.time)
    #await message.answer(f"<b>Сообщения,которые бот отправит исполнителю при 1 пункте:</b>\n\n<b>first:</b>\n\n{punkt_one_about}\n\n<b>second:</b>\n\n{pobuj}\n\n<b>Ожидаемая информация от пользователя:<i><u>Photo</u></i></b>",parse_mode="HTML")
    #await message.answer("<b>Все верно?</b>",parse_mode="HTML")
    #await state.set_state(platzak.verno)
    
@dp.message_handler(content_types=["text"], state = platzak.time) 
async def punkt1(message: types. Message, state: FSMContext):  
    try:
        danot = ReplyKeyboardMarkup(resize_keyboard=True)
        d1 = KeyboardButton("Да,продолжить✅")
        danot.row(d1)
        d2 = KeyboardButton("Нет,изменить❌")
        danot.row(d2)
        time = int(message.text)  
        async with state.proxy() as data:
            indeficat_namber = data['indeficat_namber']

        # Обновляем строку в базе данных, добавляя значение one_first_message
        conn = sqlite3.connect("database")
        cursor = conn.cursor()
        cursor.execute("UPDATE tasks SET time_one_one = ? WHERE indeficat_namber = ?", (time, indeficat_namber))
        conn.commit()
        conn.close()  
        otloj = ReplyKeyboardMarkup(resize_keyboard=True)
        ot = KeyboardButton("Отложить задвние⏳")
        otloj.row(ot)
        ot1 = KeyboardButton("⬅️Назад в меню")
        otloj.row(ot1)
        await message.answer(f"<b>Сообщения,которые бот отправит исполнителю при 1 пункте:</b>\n\n<b>first:</b>\n\n{punkt_one_about}\n\n<b>second:</b>\n\n{pobuj}\n\n<b>Ожидаемая информация от пользователя:<i><u>Photo</u></i></b>\n<b>Время на выполнение данного пункта:</b><i><u>{time} минут(а)</u></i>",parse_mode="HTML",reply_markup=otloj)
        await message.answer("<b>Все верно?</b>",parse_mode="HTML",reply_markup=danot)
        await state.set_state(platzak.verno)
    except ValueError:
        await message.reply("<b>Введи число!</b>",parse_mode="HTML")
    
    
    
    
    
    

@dp.message_handler(Text(equals="Да,продолжить✅"), state = platzak.verno) 
async def punkt1(message: types. Message, state: FSMContext):
      await oplata_za_zadanie_na_odnogo_cheloveka(message,state)
      await state.set_state(platzak.oplata_za_zadanie_na_odnogo_cheloveka)

@dp.message_handler(Text(equals="Нет,изменить❌"), state = platzak.verno) 
async def punkt1(message: types. Message, state: FSMContext):
       await message. answer("<i>Объясните <u>нужные Вам действия</u> со стороны исполнителя при выполнении <u>единственного пункта</u> вашего задания!</i>",parse_mode="HTML") 
       await state.set_state(platzak.if_punkt_one) 

    
    
    
    
    
    
    
    
    
    
    
    
    
        
    
@dp.message_handler(Text(equals="voice"), state = platzak.knpk) 
async def punkt1(message: types. Message, state: FSMContext):
    otloj = ReplyKeyboardMarkup(resize_keyboard=True)
    ot = KeyboardButton("Отложить задвние⏳")
    otloj.row(ot)
    ot1 = KeyboardButton("⬅️Назад в меню")
    otloj.row(ot1)
    await message.answer("<i><u>Введите текст,который будет побуждать исполнителя отправить вам информацию данного типа!</u></i>\n<b>Например:</b>\n<i>ОТПРАВЬТЕ ГОЛОСОВОЕ</i>\n<i>ОТПРАВЬТЕ ГС,ГДЕ ПОЕТЕ ПЕСЕНКУ...</i>",parse_mode="HTML",reply_markup=otloj) 
    await state.set_state(platzak.pobuj_one_punkt)
    
    
    
@dp.message_handler(content_types=["text"], state = platzak.pobuj_one_punkt) 
async def punkt1(message: types. Message, state: FSMContext):
    global pobuj
    pobuj = message.text
    async with state.proxy() as data:
        indeficat_namber = data['indeficat_namber']

    # Обновляем строку в базе данных, добавляя значение one_informas
    conn = sqlite3.connect("database")
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET one_informas = ? WHERE indeficat_namber = ?", ("voice", indeficat_namber))
    conn.commit()
    conn.close()
    otloj = ReplyKeyboardMarkup(resize_keyboard=True)
    ot = KeyboardButton("Отложить задвние⏳")
    otloj.row(ot)
    ot1 = KeyboardButton("⬅️Назад в меню")
    otloj.row(ot1)
    await message.answer("<i>Сколько времени дается на выполнение данного пункта?</i>\n<b>В минутах!</b>",parse_mode="HTML",reply_markup=otloj)
    await state.set_state(platzak.time)
    #await message.answer(f"<b>Сообщения,которые бот отправит исполнителю при 1 пункте:</b>\n\n<b>first:</b>\n\n{punkt_one_about}\n\n<b>second:</b>\n\n{pobuj}\n\n<b>Ожидаемая информация от пользователя:<i><u>Photo</u></i></b>",parse_mode="HTML")
    #await message.answer("<b>Все верно?</b>",parse_mode="HTML")
    #await state.set_state(platzak.verno)
    
@dp.message_handler(content_types=["text"], state = platzak.time) 
async def punkt1(message: types. Message, state: FSMContext):  
    try:
        danot = ReplyKeyboardMarkup(resize_keyboard=True)
        d1 = KeyboardButton("Да,продолжить✅")
        danot.row(d1)
        d2 = KeyboardButton("Нет,изменить❌")
        danot.row(d2)
        time = int(message.text)  
        async with state.proxy() as data:
            indeficat_namber = data['indeficat_namber']

        # Обновляем строку в базе данных, добавляя значение one_first_message
        conn = sqlite3.connect("database")
        cursor = conn.cursor()
        cursor.execute("UPDATE tasks SET time_one_one = ? WHERE indeficat_namber = ?", (time, indeficat_namber))
        conn.commit()
        conn.close()
        otloj = ReplyKeyboardMarkup(resize_keyboard=True)
        ot = KeyboardButton("Отложить задвние⏳")
        otloj.row(ot)
        ot1 = KeyboardButton("⬅️Назад в меню")
        otloj.row(ot1)  
        await message.answer(f"<b>Сообщения,которые бот отправит исполнителю при 1 пункте:</b>\n\n<b>first:</b>\n\n{punkt_one_about}\n\n<b>second:</b>\n\n{pobuj}\n\n<b>Ожидаемая информация от пользователя:<i><u>voice</u></i></b>\n<b>Время на выполнение данного пункта:</b><i><u>{time} минут(а)</u></i>",parse_mode="HTML",reply_markup=otloj)
        await message.answer("<b>Все верно?</b>",parse_mode="HTML",reply_markup=danot)
        await state.set_state(platzak.verno)
    except ValueError:
        await message.reply("<b>Введи число!</b>",parse_mode="HTML")
    
    
    
    
    
    

@dp.message_handler(Text(equals="Да,продолжить✅"), state = platzak.verno) 
async def punkt1(message: types. Message, state: FSMContext):
      await oplata_za_zadanie_na_odnogo_cheloveka(message,state)
      await state.set_state(platzak.oplata_za_zadanie_na_odnogo_cheloveka)

@dp.message_handler(Text(equals="Нет,изменить❌"), state = platzak.verno) 
async def punkt1(message: types. Message, state: FSMContext):
       await message. answer("<i>Объясните <u>нужные Вам действия</u> со стороны исполнителя при выполнении <u>единственного пункта</u> вашего задания!</i>",parse_mode="HTML") 
       await state.set_state(platzak.if_punkt_one) 

@dp.message_handler(Text(equals="audio"), state = platzak.knpk) 
async def punkt1(message: types. Message, state: FSMContext):
    otloj = ReplyKeyboardMarkup(resize_keyboard=True)
    ot = KeyboardButton("Отложить задвние⏳")
    otloj.row(ot)
    ot1 = KeyboardButton("⬅️Назад в меню")
    otloj.row(ot1)
    await message.answer("<i><u>Введите текст,который будет побуждать исполнителя отправить вам информацию данного типа!</u></i>\n<b>Например:</b>\n<i>ОТПРАВЬТЕ ПЕСЕНКУ</i>\n<i>ОТПРАВЬТЕ ЗАПИСЬ РАЗГОВОРА...</i>",parse_mode="HTML",reply_markup=otloj) 
    await state.set_state(platzak.pobuj_one_punkt)
    
    
    
@dp.message_handler(content_types=["text"], state = platzak.pobuj_one_punkt) 
async def punkt1(message: types. Message, state: FSMContext):
    global pobuj
    pobuj = message.text
    async with state.proxy() as data:
        indeficat_namber = data['indeficat_namber']

    # Обновляем строку в базе данных, добавляя значение one_informas
    conn = sqlite3.connect("database")
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET one_informas = ? WHERE indeficat_namber = ?", ("audio", indeficat_namber))
    conn.commit()
    conn.close()
    otloj = ReplyKeyboardMarkup(resize_keyboard=True)
    ot = KeyboardButton("Отложить задвние⏳")
    otloj.row(ot)
    ot1 = KeyboardButton("⬅️Назад в меню")
    otloj.row(ot1)
    await message.answer("<i>Сколько времени дается на выполнение данного пункта?</i>\n<b>В минутах!</b>",parse_mode="HTML",reply_markup=otloj)
    await state.set_state(platzak.time)
    #await message.answer(f"<b>Сообщения,которые бот отправит исполнителю при 1 пункте:</b>\n\n<b>first:</b>\n\n{punkt_one_about}\n\n<b>second:</b>\n\n{pobuj}\n\n<b>Ожидаемая информация от пользователя:<i><u>Photo</u></i></b>",parse_mode="HTML")
    #await message.answer("<b>Все верно?</b>",parse_mode="HTML")
    #await state.set_state(platzak.verno)
    
@dp.message_handler(content_types=["text"], state = platzak.time) 
async def punkt1(message: types. Message, state: FSMContext):  
    try:
        danot = ReplyKeyboardMarkup(resize_keyboard=True)
        d1 = KeyboardButton("Да,продолжить✅")
        danot.row(d1)
        d2 = KeyboardButton("Нет,изменить❌")
        danot.row(d2)
        time = int(message.text) 
        async with state.proxy() as data:
            indeficat_namber = data['indeficat_namber']

        # Обновляем строку в базе данных, добавляя значение one_first_message
        conn = sqlite3.connect("database")
        cursor = conn.cursor()
        cursor.execute("UPDATE tasks SET time_one_one = ? WHERE indeficat_namber = ?", (time, indeficat_namber))
        conn.commit()
        conn.close()   
        otloj = ReplyKeyboardMarkup(resize_keyboard=True)
        ot = KeyboardButton("Отложить задвние⏳")
        otloj.row(ot)
        ot1 = KeyboardButton("⬅️Назад в меню")
        otloj.row(ot1)
        await message.answer(f"<b>Сообщения,которые бот отправит исполнителю при 1 пункте:</b>\n\n<b>first:</b>\n\n{punkt_one_about}\n\n<b>second:</b>\n\n{pobuj}\n\n<b>Ожидаемая информация от пользователя:<i><u>audio</u></i></b>\n<b>Время на выполнение данного пункта:</b><i><u>{time} минут(а)</u></i>",parse_mode="HTML",reply_markup=otloj)
        await message.answer("<b>Все верно?</b>",parse_mode="HTML",reply_markup=danot)
        await state.set_state(platzak.verno)
    except ValueError:
        await message.reply("<b>Введи число!</b>",parse_mode="HTML")
    
    
    
    
    
    

@dp.message_handler(Text(equals="Да,продолжить✅"), state = platzak.verno) 
async def punkt1(message: types. Message, state: FSMContext):
      await oplata_za_zadanie_na_odnogo_cheloveka(message,state)
      await state.set_state(platzak.oplata_za_zadanie_na_odnogo_cheloveka)

@dp.message_handler(Text(equals="Нет,изменить❌"), state = platzak.verno) 
async def punkt1(message: types. Message, state: FSMContext):
       await message. answer("<i>Объясните <u>нужные Вам действия</u> со стороны исполнителя при выполнении <u>единственного пункта</u> вашего задания!</i>",parse_mode="HTML") 
       await state.set_state(platzak.if_punkt_one) 
   
   

@dp.message_handler(Text(equals="file(photo,video...)"), state = platzak.knpk) 
async def punkt1(message: types. Message, state: FSMContext):
    otloj = ReplyKeyboardMarkup(resize_keyboard=True)
    ot = KeyboardButton("Отложить задвние⏳")
    otloj.row(ot)
    ot1 = KeyboardButton("⬅️Назад в меню")
    otloj.row(ot1)
    await message.answer("<i><u>Введите текст,который будет побуждать исполнителя отправить вам информацию данного типа!</u></i>\n<b>Например:</b>\n<i>ОТПРАВЬТЕ ФОТО В ФОРМАТЕ ФАЙЛА</i>\n<i>ОТПРАВЬТЕ СКРИНШОТ ВАШЕЙ ПОДПИСКИ В ФОРМАТЕ ФАЙЛА...</i>",parse_mode="HTML",reply_markup=otloj) 
    await state.set_state(platzak.pobuj_one_punkt)
    
   
    
@dp.message_handler(content_types=["text"], state = platzak.pobuj_one_punkt) 
async def punkt1(message: types. Message, state: FSMContext):
    global pobuj
    pobuj = message.text
    async with state.proxy() as data:
        indeficat_namber = data['indeficat_namber']

    # Обновляем строку в базе данных, добавляя значение one_informas
    conn = sqlite3.connect("database")
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET one_informas = ? WHERE indeficat_namber = ?", ("file", indeficat_namber))
    conn.commit()
    conn.close()
    otloj = ReplyKeyboardMarkup(resize_keyboard=True)
    ot = KeyboardButton("Отложить задвние⏳")
    otloj.row(ot)
    ot1 = KeyboardButton("⬅️Назад в меню")
    otloj.row(ot1)
    await message.answer("<i>Сколько времени дается на выполнение данного пункта?</i>\n<b>В минутах!</b>",parse_mode="HTML",reply_markup=otloj)
    await state.set_state(platzak.time)
    #await message.answer(f"<b>Сообщения,которые бот отправит исполнителю при 1 пункте:</b>\n\n<b>first:</b>\n\n{punkt_one_about}\n\n<b>second:</b>\n\n{pobuj}\n\n<b>Ожидаемая информация от пользователя:<i><u>Photo</u></i></b>",parse_mode="HTML")
    #await message.answer("<b>Все верно?</b>",parse_mode="HTML")
    #await state.set_state(platzak.verno)
    
@dp.message_handler(content_types=["text"], state = platzak.time) 
async def punkt1(message: types. Message, state: FSMContext):  
    try:
        danot = ReplyKeyboardMarkup(resize_keyboard=True)
        d1 = KeyboardButton("Да,продолжить✅")
        danot.row(d1)
        d2 = KeyboardButton("Нет,изменить❌")
        danot.row(d2)
        time = int(message.text)
        async with state.proxy() as data:
            indeficat_namber = data['indeficat_namber']

        # Обновляем строку в базе данных, добавляя значение one_first_message
        conn = sqlite3.connect("database")
        cursor = conn.cursor()
        cursor.execute("UPDATE tasks SET time_one_one = ? WHERE indeficat_namber = ?", (time, indeficat_namber))
        conn.commit()
        conn.close()  
        otloj = ReplyKeyboardMarkup(resize_keyboard=True)
        ot = KeyboardButton("Отложить задвние⏳")
        otloj.row(ot)
        ot1 = KeyboardButton("⬅️Назад в меню")
        otloj.row(ot1)
        await message.answer(f"<b>Сообщения,которые бот отправит исполнителю при 1 пункте:</b>\n\n<b>first:</b>\n\n{punkt_one_about}\n\n<b>second:</b>\n\n{pobuj}\n\n<b>Ожидаемая информация от пользователя:<i><u>file</u></i></b>\n<b>Время на выполнение данного пункта:</b><i><u>{time} минут(а)</u></i>",parse_mode="HTML",reply_markup=otloj)
        await message.answer("<b>Все верно?</b>",parse_mode="HTML",reply_markup=danot)
        await state.set_state(platzak.verno)
    except ValueError:
        await message.reply("<b>Введи число!</b>",parse_mode="HTML")
    
    
    
    
    
    

@dp.message_handler(Text(equals="Да,продолжить✅"), state = platzak.verno) 
async def punkt1(message: types. Message, state: FSMContext):
      await oplata_za_zadanie_na_odnogo_cheloveka(message,state)
      await state.set_state(platzak.oplata_za_zadanie_na_odnogo_cheloveka)

@dp.message_handler(Text(equals="Нет,изменить❌"), state = platzak.verno) 
async def punkt1(message: types. Message, state: FSMContext):
       await message. answer("<i>Объясните <u>нужные Вам действия</u> со стороны исполнителя при выполнении <u>единственного пункта</u> вашего задания!</i>",parse_mode="HTML") 
       await state.set_state(platzak.if_punkt_one) 
   
   
@dp.message_handler(Text(equals="document(.docx)"), state = platzak.knpk) 
async def punkt1(message: types. Message, state: FSMContext):
    otloj = ReplyKeyboardMarkup(resize_keyboard=True)
    ot = KeyboardButton("Отложить задвние⏳")
    otloj.row(ot)
    ot1 = KeyboardButton("⬅️Назад в меню")
    otloj.row(ot1)
    await message.answer("<i><u>Введите текст,который будет побуждать исполнителя отправить вам информацию данного типа!</u></i>\n<b>Например:</b>\n<i>ОТПРАВЬТЕ ДОКУМЕНТ</i>\n<i>ОТПРАВЬТЕ ДОКУМЕНТ,КОТОРЫЙ СКАЧАЛИ...</i>",parse_mode="HTML",reply_markup=otloj) 
    await state.set_state(platzak.pobuj_one_punkt)
    
    
    
@dp.message_handler(content_types=["text"], state = platzak.pobuj_one_punkt) 
async def punkt1(message: types. Message, state: FSMContext):
    global pobuj
    pobuj = message.text
    async with state.proxy() as data:
        indeficat_namber = data['indeficat_namber']

    # Обновляем строку в базе данных, добавляя значение one_informas
    conn = sqlite3.connect("database")
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET one_informas = ? WHERE indeficat_namber = ?", ("document", indeficat_namber))
    conn.commit()
    conn.close()
    otloj = ReplyKeyboardMarkup(resize_keyboard=True)
    ot = KeyboardButton("Отложить задвние⏳")
    otloj.row(ot)
    ot1 = KeyboardButton("⬅️Назад в меню")
    otloj.row(ot1)
    await message.answer("<i>Сколько времени дается на выполнение данного пункта?</i>\n<b>В минутах!</b>",parse_mode="HTML",reply_markup=otloj)
    await state.set_state(platzak.time)
    #await message.answer(f"<b>Сообщения,которые бот отправит исполнителю при 1 пункте:</b>\n\n<b>first:</b>\n\n{punkt_one_about}\n\n<b>second:</b>\n\n{pobuj}\n\n<b>Ожидаемая информация от пользователя:<i><u>Photo</u></i></b>",parse_mode="HTML")
    #await message.answer("<b>Все верно?</b>",parse_mode="HTML")
    #await state.set_state(platzak.verno)
    
@dp.message_handler(content_types=["text"], state = platzak.time) 
async def punkt1(message: types. Message, state: FSMContext):  
    try:
        danot = ReplyKeyboardMarkup(resize_keyboard=True)
        d1 = KeyboardButton("Да,продолжить✅")
        danot.row(d1)
        d2 = KeyboardButton("Нет,изменить❌")
        danot.row(d2)
        time = int(message.text)
        async with state.proxy() as data:
            indeficat_namber = data['indeficat_namber']

        # Обновляем строку в базе данных, добавляя значение one_first_message
        conn = sqlite3.connect("database")
        cursor = conn.cursor()
        cursor.execute("UPDATE tasks SET time_one_one = ? WHERE indeficat_namber = ?", (time, indeficat_namber))
        conn.commit()
        conn.close()
        otloj = ReplyKeyboardMarkup(resize_keyboard=True)
        ot = KeyboardButton("Отложить задвние⏳")
        otloj.row(ot)
        ot1 = KeyboardButton("⬅️Назад в меню")
        otloj.row(ot1)  
        await message.answer(f"<b>Сообщения,которые бот отправит исполнителю при 1 пункте:</b>\n\n<b>first:</b>\n\n{punkt_one_about}\n\n<b>second:</b>\n\n{pobuj}\n\n<b>Ожидаемая информация от пользователя:<i><u>document</u></i></b>\n<b>Время на выполнение данного пункта:</b><i><u>{time} минут(а)</u></i>",parse_mode="HTML",reply_markup=otloj)
        await message.answer("<b>Все верно?</b>",parse_mode="HTML",reply_markup=danot)
        await state.set_state(platzak.verno)
    except ValueError:
        await message.reply("<b>Введи число!</b>",parse_mode="HTML")
    
    
    
    
    
    

@dp.message_handler(Text(equals="Да,продолжить✅"), state = platzak.verno) 
async def punkt1(message: types. Message, state: FSMContext):
      await oplata_za_zadanie_na_odnogo_cheloveka(message,state)
      await state.set_state(platzak.oplata_za_zadanie_na_odnogo_cheloveka)
      
      

@dp.message_handler(Text(equals="Нет,изменить❌"), state = platzak.verno) 
async def punkt1(message: types. Message, state: FSMContext):
       await message. answer("<i>Объясните <u>нужные Вам действия</u> со стороны исполнителя при выполнении <u>единственного пункта</u> вашего задания!</i>",parse_mode="HTML") 
       await state.set_state(platzak.if_punkt_one) 

@dp.message_handler(Text(equals="sticker"), state = platzak.knpk) 
async def punkt1(message: types. Message, state: FSMContext):
    otloj = ReplyKeyboardMarkup(resize_keyboard=True)
    ot = KeyboardButton("Отложить задвние⏳")
    otloj.row(ot)
    ot1 = KeyboardButton("⬅️Назад в меню")
    otloj.row(ot1)
    await message.answer("<i><u>Введите текст,который будет побуждать исполнителя отправить вам информацию данного типа!</u></i>\n<b>Например:</b>\n<i>ОТПРАВЬТЕ STICKER</i>\n<i>ОТПРАВЬТЕ СТИКЕР,КОТОРЫЙ ВЫ СОЗДАЛИ...</i>",parse_mode="HTML",reply_markup=otloj) 
    await state.set_state(platzak.pobuj_one_punkt)
    
   
    
@dp.message_handler(content_types=["text"], state = platzak.pobuj_one_punkt) 
async def punkt1(message: types. Message, state: FSMContext):
    global pobuj
    pobuj = message.text
    async with state.proxy() as data:
        indeficat_namber = data['indeficat_namber']

    # Обновляем строку в базе данных, добавляя значение one_informas
    conn = sqlite3.connect("database")
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET one_informas = ? WHERE indeficat_namber = ?", ("document", indeficat_namber))
    conn.commit()
    conn.close()
    otloj = ReplyKeyboardMarkup(resize_keyboard=True)
    ot = KeyboardButton("Отложить задвние⏳")
    otloj.row(ot)
    ot1 = KeyboardButton("⬅️Назад в меню")
    otloj.row(ot1)
    await message.answer("<i>Сколько времени дается на выполнение данного пункта?</i>\n<b>В минутах!</b>",parse_mode="HTML",reply_markup=otloj)
    await state.set_state(platzak.time)
    #await message.answer(f"<b>Сообщения,которые бот отправит исполнителю при 1 пункте:</b>\n\n<b>first:</b>\n\n{punkt_one_about}\n\n<b>second:</b>\n\n{pobuj}\n\n<b>Ожидаемая информация от пользователя:<i><u>Photo</u></i></b>",parse_mode="HTML")
    #await message.answer("<b>Все верно?</b>",parse_mode="HTML")
    #await state.set_state(platzak.verno)
    
@dp.message_handler(content_types=["text"], state = platzak.time) 
async def punkt1(message: types. Message, state: FSMContext):  
    try:
        danot = ReplyKeyboardMarkup(resize_keyboard=True)
        d1 = KeyboardButton("Да,продолжить✅")
        danot.row(d1)
        d2 = KeyboardButton("Нет,изменить❌")
        danot.row(d2)
        time = int(message.text)
        async with state.proxy() as data:
            indeficat_namber = data['indeficat_namber']

        # Обновляем строку в базе данных, добавляя значение one_first_message
        conn = sqlite3.connect("database")
        cursor = conn.cursor()
        cursor.execute("UPDATE tasks SET time_one_one = ? WHERE indeficat_namber = ?", (time, indeficat_namber))
        conn.commit()
        conn.close()
        otloj = ReplyKeyboardMarkup(resize_keyboard=True)
        ot = KeyboardButton("Отложить задвние⏳")
        otloj.row(ot)
        ot1 = KeyboardButton("⬅️Назад в меню")
        otloj.row(ot1)    
        await message.answer(f"<b>Сообщения,которые бот отправит исполнителю при 1 пункте:</b>\n\n<b>first:</b>\n\n{punkt_one_about}\n\n<b>second:</b>\n\n{pobuj}\n\n<b>Ожидаемая информация от пользователя:<i><u>sticker</u></i></b>\n<b>Время на выполнение данного пункта:</b><i><u>{time} минут(а)</u></i>",parse_mode="HTML",reply_markup=otloj)
        await message.answer("<b>Все верно?</b>",parse_mode="HTML",reply_markup=danot)
        await state.set_state(platzak.verno)
    except ValueError:
        await message.reply("<b>Введи число!</b>",parse_mode="HTML")
    
    
    
    
    
    

@dp.message_handler(Text(equals="Да,продолжить✅"), state = platzak.verno) 
async def punkt1(message: types. Message, state: FSMContext):
      await oplata_za_zadanie_na_odnogo_cheloveka(message,state)
      await state.set_state(platzak.oplata_za_zadanie_na_odnogo_cheloveka)

@dp.message_handler(Text(equals="Нет,изменить❌"), state = platzak.verno) 
async def punkt1(message: types. Message, state: FSMContext):
        otloj = ReplyKeyboardMarkup(resize_keyboard=True)
        ot = KeyboardButton("Отложить задвние⏳")
        otloj.row(ot)
        ot1 = KeyboardButton("⬅️Назад в меню")
        otloj.row(ot1)
        await message. answer("<i>Объясните <u>нужные Вам действия</u> со стороны исполнителя при выполнении <u>единственного пункта</u> вашего задания!</i>",parse_mode="HTML",reply_markup=otloj) 
        await state.set_state(platzak.if_punkt_one) 

@dp.message_handler(Text(equals="animation"), state = platzak.knpk) 
async def punkt1(message: types. Message, state: FSMContext):
    otloj = ReplyKeyboardMarkup(resize_keyboard=True)
    ot = KeyboardButton("Отложить задвние⏳")
    otloj.row(ot)
    ot1 = KeyboardButton("⬅️Назад в меню")
    otloj.row(ot1)
    await message.answer("<i><u>Введите текст,который будет побуждать исполнителя отправить вам информацию данного типа!</u></i>\n<b>Например:</b>\n<i>ОТПРАВЬТЕ АНИМАЮ</i>\n<i>ОТПРАВЬТЕ СКАЧАННУЮ ВАМИ АНИМАЦИЮ...</i>",parse_mode="HTML",reply_markup=otloj) 
    await state.set_state(platzak.pobuj_one_punkt)
    
    
    
@dp.message_handler(content_types=["text"], state = platzak.pobuj_one_punkt) 
async def punkt1(message: types. Message, state: FSMContext):
    global pobuj
    pobuj = message.text
    async with state.proxy() as data:
        indeficat_namber = data['indeficat_namber']

    # Обновляем строку в базе данных, добавляя значение one_informas
    conn = sqlite3.connect("database")
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET one_informas = ? WHERE indeficat_namber = ?", ("document", indeficat_namber))
    conn.commit()
    conn.close()
    otloj = ReplyKeyboardMarkup(resize_keyboard=True)
    ot = KeyboardButton("Отложить задвние⏳")
    otloj.row(ot)
    ot1 = KeyboardButton("⬅️Назад в меню")
    otloj.row(ot1)
    await message.answer("<i>Сколько времени дается на выполнение данного пункта?</i>\n<b>В минутах!</b>",parse_mode="HTML",reply_markup=otloj)
    await state.set_state(platzak.time)
    #await message.answer(f"<b>Сообщения,которые бот отправит исполнителю при 1 пункте:</b>\n\n<b>first:</b>\n\n{punkt_one_about}\n\n<b>second:</b>\n\n{pobuj}\n\n<b>Ожидаемая информация от пользователя:<i><u>Photo</u></i></b>",parse_mode="HTML")
    #await message.answer("<b>Все верно?</b>",parse_mode="HTML")
    #await state.set_state(platzak.verno)
    
@dp.message_handler(content_types=["text"], state = platzak.time) 
async def punkt1(message: types. Message, state: FSMContext):  
    try:
        danot = ReplyKeyboardMarkup(resize_keyboard=True)
        d1 = KeyboardButton("Да,продолжить✅")
        danot.row(d1)
        d2 = KeyboardButton("Нет,изменить❌")
        danot.row(d2)
        time = int(message.text)
        async with state.proxy() as data:
            indeficat_namber = data['indeficat_namber']

        # Обновляем строку в базе данных, добавляя значение one_first_message
        conn = sqlite3.connect("database")
        cursor = conn.cursor()
        cursor.execute("UPDATE tasks SET time_one_one = ? WHERE indeficat_namber = ?", (time, indeficat_namber))
        conn.commit()
        conn.close()
        otloj = ReplyKeyboardMarkup(resize_keyboard=True)
        ot = KeyboardButton("Отложить задвние⏳")
        otloj.row(ot)
        ot1 = KeyboardButton("⬅️Назад в меню")
        otloj.row(ot1)
        await message.answer(f"<b>Сообщения,которые бот отправит исполнителю при 1 пункте:</b>\n\n<b>first:</b>\n\n{punkt_one_about}\n\n<b>second:</b>\n\n{pobuj}\n\n<b>Ожидаемая информация от пользователя:<i><u>animation</u></i></b>\n<b>Время на выполнение данного пункта:</b><i><u>{time} минут(а)</u></i>",parse_mode="HTML",reply_markup=otloj)
        await message.answer("<b>Все верно?</b>",parse_mode="HTML",reply_markup=danot)
        await state.set_state(platzak.verno)
    except ValueError:
         await message.reply("<b>Введи число!</b>",parse_mode="HTML")
    
    
    
    
    
    

@dp.message_handler(Text(equals="Да,продолжить✅"), state = platzak.verno) 
async def punkt1(message: types. Message, state: FSMContext):
      await oplata_za_zadanie_na_odnogo_cheloveka(message,state)
      await state.set_state(platzak.oplata_za_zadanie_na_odnogo_cheloveka)

@dp.message_handler(Text(equals="Нет,изменить❌"), state = platzak.verno) 
async def punkt1(message: types. Message, state: FSMContext):
       otloj = ReplyKeyboardMarkup(resize_keyboard=True)
       ot = KeyboardButton("Отложить задвние⏳")
       otloj.row(ot)
       ot1 = KeyboardButton("⬅️Назад в меню")
       otloj.row(ot1)
       await message. answer("<i>Объясните <u>нужные Вам действия</u> со стороны исполнителя при выполнении <u>единственного пункта</u> вашего задания!</i>",parse_mode="HTML",reply_markup=otloj) 
       await state.set_state(platzak.if_punkt_one) 
 
    
@dp.message_handler(Text(equals="text(link,plain text...)"), state = platzak.knpk) 
async def punkt1(message: types. Message, state: FSMContext):
    otloj = ReplyKeyboardMarkup(resize_keyboard=True)
    ot = KeyboardButton("Отложить задвние⏳")
    otloj.row(ot)
    ot1 = KeyboardButton("⬅️Назад в меню")
    otloj.row(ot1)
    await message.answer("<i><u>Введите текст,который будет побуждать исполнителя отправить вам информацию данного типа!</u></i>\n<b>Например:</b>\n<i>ОТПРАВЬТЕ ССЫЛКУ НА САЙТ</i>\n<i>ОТПРАВЬТЕ СТИХ,КОТОРЫЙ ВЫ ПРИДУМАЛИ...</i>",parse_mode="HTML",reply_markup=otloj) 
    await state.set_state(platzak.pobuj_one_punkt)
    
    
@dp.message_handler(content_types=["text"], state = platzak.pobuj_one_punkt) 
async def punkt1(message: types. Message, state: FSMContext):
    global pobuj
    pobuj = message.text
    async with state.proxy() as data:
        indeficat_namber = data['indeficat_namber']

    # Обновляем строку в базе данных, добавляя значение one_informas
    conn = sqlite3.connect("database")
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET one_informas = ? WHERE indeficat_namber = ?", ("text", indeficat_namber))
    conn.commit()
    conn.close()
    otloj = ReplyKeyboardMarkup(resize_keyboard=True)
    ot = KeyboardButton("Отложить задвние⏳")
    otloj.row(ot)
    ot1 = KeyboardButton("⬅️Назад в меню")
    otloj.row(ot1)
    await message.answer("<i>Сколько времени дается на выполнение данного пункта?</i>\n<b>В минутах!</b>",parse_mode="HTML",reply_markup=otloj)
    await state.set_state(platzak.time)
    #await message.answer(f"<b>Сообщения,которые бот отправит исполнителю при 1 пункте:</b>\n\n<b>first:</b>\n\n{punkt_one_about}\n\n<b>second:</b>\n\n{pobuj}\n\n<b>Ожидаемая информация от пользователя:<i><u>Photo</u></i></b>",parse_mode="HTML")
    #await message.answer("<b>Все верно?</b>",parse_mode="HTML")
    #await state.set_state(platzak.verno)
    
@dp.message_handler(content_types=["text"], state = platzak.time) 
async def punkt1(message: types. Message, state: FSMContext):  
    try:
        danot = ReplyKeyboardMarkup(resize_keyboard=True)
        d1 = KeyboardButton("Да,продолжить✅")
        danot.row(d1)
        d2 = KeyboardButton("Нет,изменить❌")
        danot.row(d2)
        time = int(message.text)
        async with state.proxy() as data:
            indeficat_namber = data['indeficat_namber']

        # Обновляем строку в базе данных, добавляя значение one_first_message
        conn = sqlite3.connect("database")
        cursor = conn.cursor()
        cursor.execute("UPDATE tasks SET time_one_one = ? WHERE indeficat_namber = ?", (time, indeficat_namber))
        conn.commit()
        conn.close() 
        otloj = ReplyKeyboardMarkup(resize_keyboard=True)
        ot = KeyboardButton("Отложить задвние⏳")
        otloj.row(ot)
        ot1 = KeyboardButton("⬅️Назад в меню")
        otloj.row(ot1)   
        await message.answer(f"<b>Сообщения,которые бот отправит исполнителю при 1 пункте:</b>\n\n<b>first:</b>\n\n{punkt_one_about}\n\n<b>second:</b>\n\n{pobuj}\n\n<b>Ожидаемая информация от пользователя:<i><u>text</u></i></b>\n<b>Время на выполнение данного пункта:</b><i><u>{time} минут(а)</u></i>",parse_mode="HTML",reply_markup=otloj)
        await message.answer("<b>Все верно?</b>",parse_mode="HTML",reply_markup=danot)
        await state.set_state(platzak.verno)
    except ValueError:
        await message.reply("<b>Введи число!</b>",parse_mode="HTML")
    
    
    
    
    
    

@dp.message_handler(Text(equals="Да,продолжить✅"), state = platzak.verno) 
async def punkt1(message: types. Message, state: FSMContext):
      await oplata_za_zadanie_na_odnogo_cheloveka(message,state)
      await state.set_state(platzak.oplata_za_zadanie_na_odnogo_cheloveka)

@dp.message_handler(Text(equals="Нет,изменить❌"), state = platzak.verno) 
async def punkt1(message: types. Message, state: FSMContext):
        await message. answer("<i>Объясните <u>нужные Вам действия</u> со стороны исполнителя при выполнении <u>единственного пункта</u> вашего задания!</i>",parse_mode="HTML") 
        await state.set_state(platzak.if_punkt_one)      
       
    
@dp.message_handler(Text(equals="missing(accept all)"), state = platzak.knpk) 
async def punkt1(message: types. Message, state: FSMContext):
    otloj = ReplyKeyboardMarkup(resize_keyboard=True)
    ot = KeyboardButton("Отложить задвние⏳")
    otloj.row(ot)
    ot1 = KeyboardButton("⬅️Назад в меню")
    otloj.row(ot1)
    await message.answer("<i><u>Введите текст,который будет побуждать исполнителя отправить вам информацию нужного вам типа!</u></i>",parse_mode="HTML",reply_markup=otloj) 
    await state.set_state(platzak.pobuj_one_punkt)
    
    
    
@dp.message_handler(content_types=["text"], state = platzak.pobuj_one_punkt) 
async def punkt1(message: types. Message, state: FSMContext):
    global pobuj
    pobuj = message.text
    async with state.proxy() as data:
        indeficat_namber = data['indeficat_namber']

    # Обновляем строку в базе данных, добавляя значение one_informas
    conn = sqlite3.connect("database")
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET one_informas = ? WHERE indeficat_namber = ?", ("accept all", indeficat_namber))
    conn.commit()
    conn.close()
    otloj = ReplyKeyboardMarkup(resize_keyboard=True)
    ot = KeyboardButton("Отложить задвние⏳")
    otloj.row(ot)
    ot1 = KeyboardButton("⬅️Назад в меню")
    otloj.row(ot1)
    await message.answer("<i>Сколько времени дается на выполнение данного пункта?</i>\n<b>В минутах!</b>",parse_mode="HTML",reply_markup=otloj)
    await state.set_state(platzak.time)
    #await message.answer(f"<b>Сообщения,которые бот отправит исполнителю при 1 пункте:</b>\n\n<b>first:</b>\n\n{punkt_one_about}\n\n<b>second:</b>\n\n{pobuj}\n\n<b>Ожидаемая информация от пользователя:<i><u>Photo</u></i></b>",parse_mode="HTML")
    #await message.answer("<b>Все верно?</b>",parse_mode="HTML")
    #await state.set_state(platzak.verno)
    
@dp.message_handler(content_types=["text"], state = platzak.time) 
async def punkt1(message: types. Message, state: FSMContext):  
    try:
        danot = ReplyKeyboardMarkup(resize_keyboard=True)
        d1 = KeyboardButton("Да,продолжить✅")
        danot.row(d1)
        d2 = KeyboardButton("Нет,изменить❌")
        danot.row(d2)
        time = int(message.text)
        async with state.proxy() as data:
            indeficat_namber = data['indeficat_namber']

        # Обновляем строку в базе данных, добавляя значение one_first_message
        conn = sqlite3.connect("database")
        cursor = conn.cursor()
        cursor.execute("UPDATE tasks SET time_one_one = ? WHERE indeficat_namber = ?", (time, indeficat_namber))
        conn.commit()
        conn.close()
        otloj = ReplyKeyboardMarkup(resize_keyboard=True)
        ot = KeyboardButton("Отложить задвние⏳")
        otloj.row(ot)
        ot1 = KeyboardButton("⬅️Назад в меню")
        otloj.row(ot1)   
        await message.answer(f"<b>Сообщения,которые бот отправит исполнителю при 1 пункте:</b>\n\n<b>first:</b>\n\n{punkt_one_about}\n\n<b>second:</b>\n\n{pobuj}\n\n<b>Ожидаемая информация от пользователя:<i><u>accept all</u></i></b>\n<b>Время на выполнение данного пункта:</b><i><u>{time} минут(а)</u></i>",parse_mode="HTML",reply_markup=otloj)
        await message.answer("<b>Все верно?</b>",parse_mode="HTML",reply_markup=danot)
        await state.set_state(platzak.verno)
    except ValueError:
        await message.reply("<b>Введи число!</b>",parse_mode="HTML")
    
    
    
    
    
    

@dp.message_handler(Text(equals="Да,продолжить✅"), state = platzak.verno) 
async def punkt1(message: types. Message, state: FSMContext):
      await oplata_za_zadanie_na_odnogo_cheloveka(message,state)
      await state.set_state(platzak.oplata_za_zadanie_na_odnogo_cheloveka)

@dp.message_handler(Text(equals="Нет,изменить❌"), state = platzak.verno) 
async def punkt1(message: types. Message, state: FSMContext):
       await message. answer("<i>Объясните <u>нужные Вам действия</u> со стороны исполнителя при выполнении <u>единственного пункта</u> вашего задания!</i>",parse_mode="HTML") 
       await state.set_state(platzak.if_punkt_one)     
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

@dp.message_handler(content_types = ["text"], state = platzak.oplata_za_zadanie_na_odnogo_cheloveka) 
async def oplata_za_zadanie_na_odnogo_cheloveka(message: types. Message, state: FSMContext):
    otloj = ReplyKeyboardMarkup(resize_keyboard=True)
    ot = KeyboardButton("Отложить задвние⏳")
    otloj.row(ot)
    ot1 = KeyboardButton("⬅️Назад в меню")
    otloj.row(ot1)
    await message.answer("<u><i>Введите оплату за выполненное исполнителем задание!</i></u>",parse_mode="HTML",reply_markup=otloj)
    await state.set_state(platzak.kolichestvo_users_kotorue_smog)

@dp.message_handler(content_types = ["text"], state = platzak.kolichestvo_users_kotorue_smog) 
async def punkt1(message: types. Message, state: FSMContext):
    try: 
        otloj = ReplyKeyboardMarkup(resize_keyboard=True)
        ot = KeyboardButton("Отложить задвние⏳")
        otloj.row(ot)
        ot1 = KeyboardButton("⬅️Назад в меню")
        otloj.row(ot1)
        global oplata_punkt14343
        oplata_punkt14343 = int(message.text)
        await message.answer("<u><i>Введите кол-во пользователей,которые смогут выполнить задание!От 1...</i></u>",parse_mode="HTML",reply_markup=otloj)
        await state.set_state(platzak.pipl_mogut)     
    except ValueError:
        await message.answer("<b>Введи число!</b>",parse_mode="HTML")
        
        
        
@dp.message_handler(content_types = ["text"], state = platzak.pipl_mogut) 
async def punkt1(message: types. Message, state: FSMContext):
    try:
        otloj = ReplyKeyboardMarkup(resize_keyboard=True)
        ot = KeyboardButton("Отложить задвние⏳")
        otloj.row(ot)
        ot1 = KeyboardButton("⬅️Назад в меню")
        otloj.row(ot1)
        global kolix
        kolix = int(message.text)
        await state.set_state(platzak.users_mogut)
    except ValueError:
        await message.answer("<b>Введи число!</b>",parse_mode="HTML",reply_markup=otloj)

@dp.message_handler(content_types = ["text"], state = platzak.users_mogut) 
async def punkt1(message: types. Message, state: FSMContext):
    pass   
    
    
    
    
    
    
    if punkts == 2:
        await message.answer("<i>Объясните <u>нужные Вам действия</u> со стороны исполнителя при выполнении <u>1 пункта</u> вашего задания!</i>",parse_mode="HTML") 
        await state.set_state(platzak.if_punkt_two) 



    if punkts == 3:
        await message. answer("<i>Объясните <u>нужные Вам действия</u> со стороны исполнителя при выполнении <u>1 пункта!</u></i>",parse_mode="HTML") 
        await state.set_state(platzak.if_punkt_two)
         
    
    if punkts == 4:
        await message. answer("<i>Объясните <u>нужные Вам действия</u> со стороны исполнителя при выполнении <u>1 пункта!</u></i>",parse_mode="HTML") 
        await state.set_state(platzak.if_punkt_four) 

    if punkts == 5:
        await message. answer("Объясните нужные действия исполнителю при 1 пункте!") 
        await state.set_state(platzak.if_punkt_five) 
    
    if punkts == 6:
        await message. answer("Объясните нужные действия исполнителю при 1 пункте!") 
        await state.set_state(platzak.if_punkt_six) 







    




@dp.message_handler(Text(equals="Админ-Панель👑", ignore_case=True), state=None)
async def tadm454(message: types.Message, state: FSMContext) -> None:
    if not message.from_user.id == int(cfg.ADMIN_ID):
        await state.reset_state()
    if message.from_user.id == int(cfg.ADMIN_ID):
        await message.answer(
            f"Привет,@{message.from_user.username}!Ты администратор)Используй кнопки для управления ботом!",
            reply_markup=nav.admin_menu,
        )
        await state.set_state(Ref_state.admin_panele)


@dp.message_handler(
    Text(equals="Действия с пользователем👥", ignore_case=True),
    state=Ref_state.admin_panele,
)
async def te534(message: types.Message, state: FSMContext) -> None:
    await message.answer(
        f"<i>Привет,@{message.from_user.username}!</i>\nВыбери действие,которое хочешь выполнить с каким-либо пользователем!",
        parse_mode="HTML",
        reply_markup=nav.deist,
    )
    await state.set_state(Ref_state.admin_users)


@dp.message_handler(
    Text(equals="⬅️Назад в меню", ignore_case=True), state=Ref_state.admin_users
)
async def nazadfff(message: types.Message, state: FSMContext):
    await state.reset_state()
    return await tadm454(message, state)


@dp.message_handler(
    Text(equals="Кол-во юзеров в боте👥", ignore_case=True), state=Ref_state.admin_users
)
async def tex765(message: types.Message, state: FSMContext) -> None:
    users_count = await get_users()

    await message.answer(
        f"<i><b>Количество пользователей в боте: {users_count}</b></i>",
        parse_mode="HTML",
        reply_markup=nav.nas21,
    )

    await state.set_state(Ref_state.nafaz)


@dp.message_handler(
    Text(equals="⬅️Назад в меню", ignore_case=True), state=Ref_state.nafaz
)
async def nazadfff(message: types.Message, state: FSMContext):
    await state.set_state(Ref_state.admin_panele)
    return await te534(message, state)


async def get_users():
    conn = sqlite3.connect("database")
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM users")
    users_count = cursor.fetchone()[0]

    conn.close()
    return users_count


@dp.message_handler(
    Text(equals="Действия с администраторами👑", ignore_case=True),
    state=Ref_state.admin_users,
)
async def adpny345523(message: types.Message, state: FSMContext):
    await message.answer("Кнопки ниже⬇️", reply_markup=nav.admin_izmenit_id)
    await state.set_state(Ref_state.deist_with_admin)


@dp.message_handler(
    Text(equals="Добавить администратора✅", ignore_case=True),
    state=Ref_state.deist_with_admin,
)
async def admin_users(message: types.Message, state: FSMContext):
    await message.answer(
        "Введите ID пользователя,которого вы хотите сделать админом!",
        reply_markup=nav.naz,
    )
    await state.set_state(Ref_state.waiting_for_id_admin)


@dp.message_handler(
    Text(equals="⬅️Назад в меню", ignore_case=True),
    state=Ref_state.waiting_for_id_admin,
)
async def nazadfff(message: types.Message, state: FSMContext):
    await state.set_state(Ref_state.deist_with_admin)
    return await adpny345523(message, state)


@dp.message_handler(
    Text(equals="⬅️Назад в меню", ignore_case=True), state=Ref_state.deist_with_admin
)
async def nazadfff(message: types.Message, state: FSMContext):
    await state.set_state(Ref_state.admin_panele)
    return await te534(message, state)


@dp.message_handler(
    Text(equals="⬅️Назад в меню", ignore_case=True),
    state=Ref_state.waiting_for_id_admin,
)
async def nazadfff(message: types.Message, state: FSMContext):
    await state.set_state(Ref_state.admin_panele)
    return await adpny345523(message, state)


@dp.message_handler(content_types=["text"], state=Ref_state.waiting_for_id_admin)
async def sendall4(message: types.Message, state: FSMContext):
    user_id = message.text
    conn = sqlite3.connect("database")
    cursor = conn.cursor()
    cursor.execute("SELECT user_id FROM users WHERE user_id = ?", (user_id,))
    result = cursor.fetchone()
    if result is not None:
        cursor.execute("UPDATE users SET admin = 1 WHERE user_id = ?", (user_id,))
        conn.commit()
        conn.close()
        await message.answer("Админ успешно добавлен!")

    else:
        await message.answer("Такого ID не существует!")
        await state.set_state(Ref_state.deist_with_admin)
        return await admin_users(message, state)


@dp.message_handler(
    Text(equals="Удалить администратора❌", ignore_case=True),
    state=Ref_state.deist_with_admin,
)
async def nagtg564(message: types.Message, state: FSMContext):
    await message.answer(
        "Введите ID пользователя,у которого вы хотите отнять статус админа!",
        reply_markup=nav.naz,
    )
    await state.set_state(Ref_state.waiting_for_id_admim_delete)


@dp.message_handler(
    Text(equals="⬅️Назад в меню", ignore_case=True),
    state=Ref_state.waiting_for_id_admim_delete,
)
async def nazadfff(message: types.Message, state: FSMContext):
    await state.set_state(Ref_state.deist_with_admin)
    return await adpny345523(message, state)


@dp.message_handler(content_types=["text"], state=Ref_state.waiting_for_id_admim_delete)
async def sendall4(message: types.Message, state: FSMContext):
    user_id = message.text
    conn = sqlite3.connect("database")
    cursor = conn.cursor()
    cursor.execute("SELECT user_id FROM users WHERE user_id = ?", (user_id,))
    result = cursor.fetchone()
    if result is not None:
        cursor.execute("UPDATE users SET admin = 0 WHERE user_id = ?", (user_id,))
        conn.commit()
        conn.close()
        await message.answer("Админ успешно удален!")

    else:
        await message.answer("Такого ID не существует!")
        await state.set_state(Ref_state.deist_with_admin)
        return await nagtg564(message, state)


@dp.message_handler(
    Text(equals="Список всех администраторов👑", ignore_case=True),
    state=Ref_state.deist_with_admin,
)
async def nazadfff(message: types.Message, state: FSMContext):
    admin_users = get_admin_users()
    if admin_users:
        admin_info = "\n".join(admin_users)
        await message.answer(
            f"<b>Список всех админов,кроме вас:</b>\n\n{admin_info}",
            parse_mode="HTML",
            reply_markup=nav.asdsd,
        )
    else:
        await message.answer("Кроме вас администраторов нет!", reply_markup=nav.asdsd)

    await state.set_state(Ref_state.hdao)


@dp.message_handler(
    Text(equals="⬅️Назад в меню", ignore_case=True),
    state=Ref_state.hdao,
)
async def nazadfff(message: types.Message, state: FSMContext):
    await state.set_state(Ref_state.deist_with_admin)
    return await adpny345523(message, state)


def get_admin_users():
    conn = sqlite3.connect("database")
    cursor = conn.cursor()
    cursor.execute("SELECT full_name,username,user_id FROM users WHERE admin = 1")
    admin_users = cursor.fetchall()

    admins_info = [
        f"{index}.  Имя: {full_name}\n     Username: {username}\n     ID: {user_id}\n"
        for index, (full_name, username, user_id) in enumerate(admin_users, start=1)
    ]

    return admins_info


@dp.message_handler(
    Text(equals="Изменить баланс пользователю💰", ignore_case=True),
    state=Ref_state.admin_users,
)
async def kol434f(message: types.Message, state: FSMContext):
    await message.answer("Кнопки ниже⬇️", reply_markup=nav.balance_user)
    await state.set_state(Ref_state.balance)


@dp.message_handler(
    Text(equals="⬅️Назад в меню", ignore_case=True),
    state=Ref_state.balance,
)
async def nazadfff(message: types.Message, state: FSMContext):
    await state.set_state(Ref_state.admin_panele)
    return await te534(message, state)


@dp.message_handler(
    Text(equals="Начислить баланс✅", ignore_case=True), state=Ref_state.balance
)
async def na66546464(message: types.Message, state: FSMContext):
    await message.answer(
        "Введи айди пользователя,которому хочешь добавить баланс!", reply_markup=nav.nas
    )
    await state.set_state(Ref_state.balance_id)


@dp.message_handler(
    Text(equals="⬅️Назад в меню", ignore_case=True),
    state=Ref_state.balance_id,
)
async def nazadfff(message: types.Message, state: FSMContext):
    await state.set_state(Ref_state.admin_users)
    return await kol434f(message, state)


@dp.message_handler(content_types=["text"], state=Ref_state.balance_id)
async def process_user_id(message: types.Message, state: FSMContext):
    global user_id_to_change1
    user_id_to_change1 = message.text
    conn = sqlite3.connect("database")
    cursor = conn.cursor()
    cursor.execute("SELECT BALANCE FROM users WHERE user_id=?", (user_id_to_change1,))
    user_balance = cursor.fetchone()
    conn.commit()
    try:
        await message.reply(
            f"<i><b>💰Баланс юзера: {user_balance[0]}</b></i>\n\n<b><i>Введите сумму,которую хотите начислить пользователю!</i></b>",
            parse_mode="HTML",
        )
        await state.set_state(Ref_state.balance_id_plus)
    except TypeError:
        pass


@dp.message_handler(
    Text(equals="⬅️Назад в меню", ignore_case=True),
    state=Ref_state.balance_id_plus,
)
async def nazadfff(message: types.Message, state: FSMContext):
    await state.set_state(Ref_state.admin_users)
    return await kol434f(message, state)


@dp.message_handler(content_types=["text"], state=Ref_state.balance_id_plus)
async def process_user_id(message: types.Message, state: FSMContext):
    try:
        amount = float(message.text)
        user_id_to_change = user_id_to_change1
        conn = sqlite3.connect("database")
        cursor = conn.cursor()
        cursor.execute(
            "SELECT BALANCE FROM users WHERE user_id=?", (user_id_to_change,)
        )
        user_balance = cursor.fetchone()[0]
        new_balance = user_balance + amount
        cursor.execute(
            "UPDATE users SET BALANCE=? WHERE user_id=?",
            (new_balance, user_id_to_change),
        )
        conn.commit()
        await message.reply(
            f"<b><i>Баланс успешно обновлен!</i></b>\n\n<b><i>💰Новый баланс: {new_balance}</i></b>",
            parse_mode="HTML",
        )
        await state.set_state(Ref_state.balance_id_opopop)
    except ValueError:
        pass


@dp.message_handler(
    Text(equals="⬅️Назад в меню", ignore_case=True),
    state=Ref_state.balance_id_opopop,
)
async def nazadfff(message: types.Message, state: FSMContext):
    await state.set_state(Ref_state.admin_users)
    return await kol434f(message, state)


@dp.message_handler(
    Text(equals="Отнять баланс❌", ignore_case=True), state=Ref_state.balance
)
async def nazadfff(message: types.Message, state: FSMContext):
    await message.answer(
        "Введи айди пользователя,у которого хочешь отнять баланс!", reply_markup=nav.nas
    )
    await state.set_state(Ref_state.balance_id_otn)


@dp.message_handler(
    Text(equals="⬅️Назад в меню", ignore_case=True),
    state=Ref_state.balance_id_otn,
)
async def nazadfff(message: types.Message, state: FSMContext):
    await state.set_state(Ref_state.admin_users)
    return await kol434f(message, state)


@dp.message_handler(
    Text(equals="⬅️Назад в меню", ignore_case=True),
    state=Ref_state.balance,
)
async def nazadfff(message: types.Message, state: FSMContext):
    await state.set_state(Ref_state.deist_with_admin)
    return await adpny345523(message, state)


@dp.message_handler(content_types=["text"], state=Ref_state.balance_id_otn)
async def process_user_id(message: types.Message, state: FSMContext):
    try:
        global user_id_to_change5
        user_id_to_change5 = message.text
        conn = sqlite3.connect("database")
        cursor = conn.cursor()
        cursor.execute(
            "SELECT BALANCE FROM users WHERE user_id=?", (user_id_to_change5,)
        )
        user_balance = cursor.fetchone()
        conn.commit()
        await message.reply(
            f"<i><b>💰Баланс юзера: {user_balance[0]}</b></i>\n\n<b><i>Введите сумму,которую хотите отнять у пользователя!</i></b>",
            parse_mode="HTML",
        )
        await state.set_state(Ref_state.balance_id_minus)
    except TypeError:
        pass


@dp.message_handler(content_types=["text"], state=Ref_state.balance_id_minus)
async def process_user_id(message: types.Message, state: FSMContext):
    try:
        user_id_to_change = user_id_to_change5
        conn = sqlite3.connect("database")
        cursor = conn.cursor()
        cursor.execute(
            "SELECT BALANCE FROM users WHERE user_id=?", (user_id_to_change,)
        )
        user_balance = cursor.fetchone()[0]
        amount = float(message.text)
        new_balance = user_balance - amount
        if new_balance < 0:
            await message.reply("Невозможно провести операцию!")

        else:
            cursor.execute(
                "UPDATE users SET BALANCE=? WHERE user_id=?",
                (new_balance, user_id_to_change),
            )
            conn.commit()
            await message.reply(
                f"<b><i>Баланс успешно обновлен!</i></b>\n\n<b><i>💰Новый баланс: {new_balance}</i></b>",
                parse_mode="HTML",
            )
            await state.set_state(Ref_state.vlfvlfgvl)
    except ValueError:
        pass


@dp.message_handler(
    Text(equals="⬅️Назад в меню", ignore_case=True),
    state=Ref_state.vlfvlfgvl,
)
async def nazadfff(message: types.Message, state: FSMContext):
    await state.set_state(Ref_state.admin_users)
    return await kol434f(message, state)


@dp.message_handler(
    Text(equals="⬅️Назад в меню", ignore_case=True), state=Ref_state.balance
)
async def nazadfff(message: types.Message, state: FSMContext):
    await state.set_state(Ref_state.admin_panele)
    return await tex765(message, state)


@dp.message_handler(content_types=["text"], state=Ref_state.block_user)
async def process_user_id(message: types.Message, state: FSMContext):
    if message.text == "⬅️Назад в меню":
        await state.set_state(Ref_state.admin_panele)
        return await tex765(message, state)
    user_id_to_block = message.text
    conn = sqlite3.connect("database")
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE users SET ban_user_bot=1 WHERE USER_ID=?", (user_id_to_block,)
    )
    conn.commit()
    await message.reply(
        f"<b>Пользователь с ID <code>{user_id_to_block}</code> успешно заблокирован!</b>",
        parse_mode="HTML",
    )
    await state.set_state(Ref_state.admin_panele)
    return await tex765(message, state)


# ----------------------------------------------------------------------------------------------------------#
# ----------------------------------------------------------------------------------------------------------#
# ----------------------------------------------------------------------------------------------------------#
# ----------------------------------------------------------------------------------------------------------#
# ----------------------------------------------------------------------------------------------------------#
# ----------------------------------------------------------------------------------------------------------#
# ----------------------------------------------------------------------------------------------------------#
# ----------------------------------------------------------------------------------------------------------#
# ----------------------------------------------------------------------------------------------------------#
@dp.message_handler(
    Text(equals="Редактор заданий📝", ignore_case=True), state=Ref_state.admin_panele
)
async def redactor_tasks(message: types.Message, state: FSMContext) -> None:
    zadman = ReplyKeyboardMarkup(resize_keyboard=True)
    zam1 = KeyboardButton("Задания📝")
    zadman.row(zam1)
    zam2 = KeyboardButton("ГЕО Заданий🌍")
    zadman.row(zam2)
    zam3 = KeyboardButton("Filters заданий⚙️")
    zadman.row(zam3)
    zam4 = KeyboardButton("⬅️Назад в меню")
    zadman.row(zam4)
    await message.answer(f"Используй кнопки👇", reply_markup=zadman)
    await state.set_state(Ref_state.zadman)


class ZADANIA(StatesGroup):
    zadania = State()
    name = State()
    opisanie = State()
    photo = State()
    insruction = State()
    punkts = State()


@dp.message_handler(Text(equals="Задания📝", ignore_case=True), state=Ref_state.zadman)
async def geo_tasks34(message: types.Message, state: FSMContext) -> None:
    zadania_markup = ReplyKeyboardMarkup(resize_keyboard=True)
    zad1 = KeyboardButton(text="Добавить задание✅")
    zadania_markup.row(zad1)
    zad2 = KeyboardButton(text="Удалить задание❌")
    zadania_markup.row(zad2)
    zad3 = KeyboardButton(text="⬅️Назад в меню")
    zadania_markup.row(zad3)
    await message.answer(
        f"<b>Привет,@{message.from_user.username})Используй кнопки!</b>",
        parse_mode="HTML",
        reply_markup=zadania_markup,
    )
    await state.set_state(ZADANIA.zadania)


@dp.message_handler(
    Text(equals="Добавить задание✅", ignore_case=True), state=ZADANIA.zadania
)
async def name_for_task(message: types.Message, state: FSMContext) -> None:
    fsdf = ReplyKeyboardMarkup(resize_keyboard=True)
    zad35 = KeyboardButton(text="⬅️Назад в меню")
    fsdf.row(zad35)
    await message.answer(
        "<b>ЕСЛИ ВЫ ДОПУСТИЛИ КАКУЮ-ЛИБО ОШИБКУ В ПРЕДОСТАВЛЕНИИ ИНФОРМАЦИИ О ЗАДАНИИ,ИЗМЕНИТЬ ЕЕ ВЫ СМОЖЕТЕ В САМОМ КОНЦЕ!</b>",
        parse_mode="HTML",
    )
    await message.answer(
        "<b>Введите название вашего задания!\nДо 27 символов!</b>",
        parse_mode="HTML",
        reply_markup=fsdf,
    )
    await state.set_state(ZADANIA.name)


@dp.message_handler(content_types=["text"], state=ZADANIA.name)
async def geo_tasks34(message: types.Message, state: FSMContext) -> None:
    global imya
    imya = message.text
    if len(imya) > 27:
        await message.answer("Ваше название более 27 символов!")
        await state.set_state(ZADANIA.zadania)
        await name_for_task(message, state)

    else:
        await message.reply("<i>Название сохранено!</i>", parse_mode="HTML")
        user_id = message.from_user.id
        username = message.from_user.username
        # conn = sqlite3.connect("database")
        # cursor = conn.cursor()
        # cursor.execute(
        # "INSERT INTO tasks (username,user_id,imya) VALUES (?,?,?)",
        #  (username,user_id,imya,),
        # )
        # conn.commit()
        await message.answer(
            "Отправь краткое описание своего задания!(до 405 символов)"
        )
        await state.set_state(ZADANIA.opisanie)


@dp.message_handler(content_types=["text"], state=ZADANIA.opisanie)
async def geo_tasks34(message: types.Message, state: FSMContext) -> None:
    global opisanie
    opisanie = message.text
    if len(opisanie) > 405:
        await state.set_state(ZADANIA.opisanie)
        await message.answer("Ваше описание более 405 символов!")
        await message.answer(
            "Отправь краткое описание своего задания!(до 405 символов)"
        )
    else:
        await message.answer("Отправь обложку(фото) твоего задания!")
        await state.set_state(ZADANIA.photo)


@dp.message_handler(content_types=["photo"], state=ZADANIA.photo)
async def geo_tasks34(message: types.Message, state: FSMContext) -> None:
    global photo
    photo = message.photo
    await message.answer(
        "Напиши инструкцию по выполнению задания на <https://telegra.ph> и отправь ее!"
    )
    await state.set_state(ZADANIA.insruction)


@dp.message_handler(content_types=["text"], state=ZADANIA.insruction)
async def geo_tasks34(message: types.Message, state: FSMContext) -> None:
    global instruction
    instruction = message.text
    link = r"https?://\S+"
    if re.search(link, instruction):
        await message.answer(
            "Укажи количество пунтов(от 1 до 25),которые должен выполнить пользователь,чтобы выполнить задание правильно!"
        )
        await state.set_state(ZADANIA.punkts)
    else:
        await state.set_state(ZADANIA.insruction)
        await message.reply("Это не ссылка!")
        await message.answer(
            "Напиши инструкцию по выполнению задания на <https://telegra.ph> и отправь ее!"
        )


user_responses = {}


@dp.message_handler(
    lambda message: message.text.isdigit() and 1 <= int(message.text) <= 25,
    state=ZADANIA.punkts,
)
async def handle_user_input(message: types.Message, state: FSMContext):
    pass


@dp.message_handler(
    Text(equals="Удалить задание❌", ignore_case=True), state=Ref_state.zadman
)
async def geo_tasks34(message: types.Message, state: FSMContext) -> None:
    pass


@dp.message_handler(
    Text(equals="⬅️Назад в меню", ignore_case=True), state=Ref_state.zadman
)
async def geo_tasks34(message: types.Message, state: FSMContext) -> None:
    pass


class Filters(StatesGroup):
    Filters = State()
    Filters_add = State()
    Filters_konez = State()
    Filters_konez1 = State()
    Filters_delete = State()


@dp.message_handler(
    Text(equals="Filters заданий⚙️", ignore_case=True), state=Ref_state.zadman
)
async def geo_tasks34(message: types.Message, state: FSMContext) -> None:
    flfd = ReplyKeyboardMarkup(resize_keyboard=True)
    am3 = KeyboardButton("Добавить Filter✅")
    flfd.row(am3)
    am4 = KeyboardButton("Удалить Filters❌")
    flfd.row(am4)
    am5 = KeyboardButton("Все Filters📝")
    flfd.row(am5)
    am6 = KeyboardButton("⬅️Назад в меню")
    flfd.row(am6)
    await message.answer(
        f"<i>Привет,используй кнопки!</i>", parse_mode="HTML", reply_markup=flfd
    )
    await state.set_state(Filters.Filters)


@dp.message_handler(
    Text(equals="⬅️Назад в меню", ignore_case=True), state=Filters.Filters
)
async def tex765(message: types.Message, state: FSMContext) -> None:
    await state.set_state(Ref_state.admin_panele)
    await redactor_tasks(message, state)


@dp.message_handler(
    Text(equals="Добавить Filter✅", ignore_case=True), state=Filters.Filters
)
async def geo_tasks1(message: types.Message, state: FSMContext) -> None:
    werty = ReplyKeyboardMarkup(resize_keyboard=True)
    am5 = KeyboardButton("⬅️Назад в меню")
    werty.row(am5)
    await message.answer(
        f"<i>Привет,отправь</i> <b>Filter</b>,<i>который хочешь добавить!</i>",
        parse_mode="HTML",
        reply_markup=werty,
    )
    await state.set_state(Filters.Filters_add)


@dp.message_handler(
    Text(equals="⬅️Назад в меню", ignore_case=True), state=Filters.Filters_add
)
async def tex765(message: types.Message, state: FSMContext) -> None:
    await state.set_state(Ref_state.zadman)
    await geo_tasks34(message, state)


@dp.message_handler(content_types=["text"], state=Filters.Filters_add)
async def geo_reload(message: types.Message, state: FSMContext) -> None:
    new_country_name = message.text
    if message.text == "⬅️Назад в меню":
        await state.set_state(Ref_state.zadman)
        await geo_tasks1(message, state)
    else:  # Проверяем, не существует ли уже такой страны в базе данных
        conn = sqlite3.connect("database")
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM filters WHERE name=?", (new_country_name,))
        existing_country = cursor.fetchone()

        if existing_country:
            await message.answer(
                f"<i>Filter:</i> <b>{new_country_name}</b> <i>уже существует в базе данных!</i>",
                parse_mode="HTML",
            )
            await message.answer(
                "<i>Отправьте</i> <b>Filter</b><i>,который хотите добавить!</i>",
                parse_mode="HTML",
            )

            await state.set_state(Filters.Filters_add)
        else:
            # Сохраняем новую страну в базе данных
            cursor.execute("INSERT INTO filters (name) VALUES (?)", (new_country_name,))
            conn.commit()
            await message.answer(
                f"<i>Filter:</i> <b>{new_country_name}</b> <i>успешно добавлен в базу данных!</i>",
                parse_mode="HTML",
            )
            await state.set_state(Filters.Filters_konez)


@dp.message_handler(
    Text(equals="⬅️Назад в меню", ignore_case=True), state=Filters.Filters_konez
)
async def tex765(message: types.Message, state: FSMContext) -> None:
    await state.set_state(Ref_state.zadman)
    await geo_tasks34(message, state)


@dp.message_handler(
    Text(equals="Удалить Filters❌", ignore_case=True), state=Filters.Filters
)
async def geo_tasks66(message: types.Message, state: FSMContext) -> None:
    werty = ReplyKeyboardMarkup(resize_keyboard=True)
    am5 = KeyboardButton("⬅️Назад в меню")
    werty.row(am5)
    await message.answer(
        f"<i>Привет,отправь</i> <b>Filter</b>,<i>который хочешь удалить!</i>",
        parse_mode="HTML",
        reply_markup=werty,
    )
    await state.set_state(Filters.Filters_delete)


@dp.message_handler(
    Text(equals="⬅️Назад в меню", ignore_case=True), state=Filters.Filters
)
async def tex765(message: types.Message, state: FSMContext) -> None:
    await state.set_state(Ref_state.zadman)
    await geo_tasks34(message, state)


@dp.message_handler(
    Text(equals="⬅️Назад в меню", ignore_case=True), state=Filters.Filters_delete
)
async def tex765(message: types.Message, state: FSMContext) -> None:
    await state.set_state(Ref_state.zadman)
    await geo_tasks34(message, state)


@dp.message_handler(content_types=["text"], state=Filters.Filters_delete)
async def geo_dkladsl(message: types.Message, state: FSMContext) -> None:
    country_to_delete1 = message.text
    if country_to_delete1 == "⬅️Назад в меню":
        await state.set_state(Ref_state.zadman)
        await geo_tasks66(message, state)
    else:
        conn = sqlite3.connect("database")
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM filters WHERE name=?", (country_to_delete1,))
        existing_country = cursor.fetchone()

        if not existing_country:
            await message.answer(
                f"<i>Filter:</i> <b>{country_to_delete1}</b> <i>не существует в базе данных!</i>",
                parse_mode="HTML",
            )
            await message.answer(
                f"<i>Отправь</i> <b>Filter</b>,<i>который хочешь удалить!</i>",
                parse_mode="HTML",
            )

            await state.set_state(Filters.Filters_delete)
        else:
            # Удаляем страну из базы данных
            cursor.execute("DELETE FROM filters WHERE name=?", (country_to_delete1,))
            conn.commit()
            await message.answer(
                f"<i>Filter:</i> <b>{country_to_delete1}</b> <i>успешно удален из базы данных!</i>",
                parse_mode="HTML",
            )
            await state.set_state(Filters.Filters_konez1)


@dp.message_handler(
    Text(equals="⬅️Назад в меню", ignore_case=True), state=Filters.Filters_konez1
)
async def tex765(message: types.Message, state: FSMContext) -> None:
    await state.set_state(Ref_state.zadman)
    await geo_tasks34(message, state)


@dp.message_handler(
    Text(equals="⬅️Назад в меню", ignore_case=True), state=Ref_state.zadman
)
async def tex765(message: types.Message, state: FSMContext) -> None:
    await state.set_state(Ref_state.zadman)
    await tadm454(message, state)


@dp.message_handler(
    Text(equals="Все Filters📝", ignore_case=True), state=Filters.Filters
)
async def geo_tasks(message: types.Message, state: FSMContext) -> None:
    conn = sqlite3.connect("database")  # Подставьте сюда вашу базу данных
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM filters")
    geos = cursor.fetchall()
    conn.close()

    deqswd = ReplyKeyboardMarkup(resize_keyboard=True)
    d1 = KeyboardButton("⬅️Назад в меню")
    deqswd.row(d1)

    if geos:
        geo_list = "\n".join(
            [f"   {index + 1}. {geo[0]}" for index, geo in enumerate(geos)]
        )

        await message.answer(
            f"<b>Список доступных Filters:</b>\n{geo_list}",
            parse_mode="HTML",
            reply_markup=deqswd,
        )
    else:
        await message.answer(
            "Нет доступных Filters в базе данных!", reply_markup=deqswd
        )


@dp.message_handler(
    Text(equals="⬅️Назад в меню", ignore_case=True), state=Filters.Filters
)
async def tex765(message: types.Message, state: FSMContext) -> None:
    await state.set_state(Ref_state.zadman)
    await geo_tasks34(message, state)


@dp.message_handler(
    Text(equals="⬅️Назад в меню", ignore_case=True), state=Ref_state.zadman
)
async def geo_tasks(message: types.Message, state: FSMContext) -> None:
    await state.reset_state()
    await redactor_tasks(message, state)


@dp.message_handler(
    Text(equals="⬅️Назад в меню", ignore_case=True), state=Ref_state.zadman
)
async def tex765(message: types.Message, state: FSMContext) -> None:
    await state.reset_state()
    await tadm454(message, state)


class Tasks(StatesGroup):
    geo = State()
    geo_add = State()
    geo_delete = State()
    geo_konez = State()
    geo_konez1 = State()


@dp.message_handler(
    Text(equals="ГЕО Заданий🌍", ignore_case=True), state=Ref_state.zadman
)
async def geo_tasks(message: types.Message, state: FSMContext) -> None:
    flfd = ReplyKeyboardMarkup(resize_keyboard=True)
    am3 = KeyboardButton("Добавить ГЕО✅")
    flfd.row(am3)
    am4 = KeyboardButton("Удалить ГЕО❌")
    flfd.row(am4)
    am5 = KeyboardButton("Все ГЕО📝")
    flfd.row(am5)
    am6 = KeyboardButton("⬅️Назад в меню")
    flfd.row(am6)
    await message.answer(
        f"<i>Привет,используй кнопки!</i>", parse_mode="HTML", reply_markup=flfd
    )
    await state.set_state(Tasks.geo)

    conn = sqlite3.connect("database")
    cursor = conn.cursor()
    cursor.execute(
        """
CREATE TABLE IF NOT EXISTS countries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT
)
"""
    )
    conn.commit()


@dp.message_handler(Text(equals="Все ГЕО📝", ignore_case=True), state=Tasks.geo)
async def tex765(message: types.Message, state: FSMContext) -> None:
    conn = sqlite3.connect("database")  # Подставьте сюда вашу базу данных
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM countries")
    geos = cursor.fetchall()
    conn.close()

    deqswd = ReplyKeyboardMarkup(resize_keyboard=True)
    d1 = KeyboardButton("⬅️Назад в меню")
    deqswd.row(d1)

    if geos:
        geo_list = "\n".join(
            [f"   {index + 1}. {geo[0]}" for index, geo in enumerate(geos)]
        )

        await message.answer(
            f"<b>Список доступных гео:</b>\n{geo_list}", parse_mode="HTML"
        )
    else:
        await message.answer("Нет доступных гео в базе данных!", reply_markup=deqswd)
    deqswd = ReplyKeyboardMarkup(resize_keyboard=True)
    d1 = KeyboardButton("⬅️Назад в меню")
    deqswd.row(d1)


@dp.message_handler(Text(equals="Добавить ГЕО✅", ignore_case=True), state=Tasks.geo)
async def tex765(message: types.Message, state: FSMContext) -> None:
    werty = ReplyKeyboardMarkup(resize_keyboard=True)
    am5 = KeyboardButton("⬅️Назад в меню")
    werty.row(am5)
    await message.answer(
        f"<i>Привет,отправь</i> <b>ГЕО</b>,<i>который хочешь добавить!</i>",
        parse_mode="HTML",
        reply_markup=werty,
    )
    await state.set_state(Tasks.geo_add)


@dp.message_handler(Text(equals="⬅️Назад в меню", ignore_case=True), state=Tasks.geo)
async def tex765(message: types.Message, state: FSMContext) -> None:
    await state.set_state(Ref_state.admin_panele)
    await redactor_tasks(message, state)


@dp.message_handler(
    Text(equals="⬅️Назад в меню", ignore_case=True), state=Tasks.geo_add
)
async def tex765(message: types.Message, state: FSMContext) -> None:
    await state.set_state(Ref_state.zadman)
    await geo_tasks(message, state)


@dp.message_handler(content_types=["text"], state=Tasks.geo_add)
async def geo_reload(message: types.Message, state: FSMContext) -> None:
    new_country_name = message.text
    if message.text == "⬅️Назад в меню":
        await state.set_state(Ref_state.zadman)
        await geo_tasks(message, state)
    else:  # Проверяем, не существует ли уже такой страны в базе данных
        conn = sqlite3.connect("database")
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM countries WHERE name=?", (new_country_name,))
        existing_country = cursor.fetchone()

        if existing_country:
            await message.answer(
                f"<i>ГЕО:</i> <b>{new_country_name}</b> <i>уже существует в базе данных!</i>",
                parse_mode="HTML",
            )
            await message.answer(
                "<i>Отправьте</i> <b>ГЕО</b><i>,которое хотите добавить!</i>",
                parse_mode="HTML",
            )

            await state.set_state(Tasks.geo_add)
        else:
            # Сохраняем новую страну в базе данных
            cursor.execute(
                "INSERT INTO countries (name) VALUES (?)", (new_country_name,)
            )
            conn.commit()
            await message.answer(
                f"<i>ГЕО:</i> <b>{new_country_name}</b> <i>успешно добавлено в базу данных!</i>",
                parse_mode="HTML",
            )
            await state.set_state(Tasks.geo_konez1)


@dp.message_handler(
    Text(equals="⬅️Назад в меню", ignore_case=True), state=Tasks.geo_konez1
)
async def tex765(message: types.Message, state: FSMContext) -> None:
    await state.set_state(Ref_state.zadman)
    await geo_tasks(message, state)


@dp.message_handler(Text(equals="Удалить ГЕО❌", ignore_case=True), state=Tasks.geo)
async def tex765(message: types.Message, state: FSMContext) -> None:
    werty = ReplyKeyboardMarkup(resize_keyboard=True)
    am5 = KeyboardButton("⬅️Назад в меню")
    werty.row(am5)
    await message.answer(
        f"<i>Привет,отправь</i> <b>ГЕО</b>,<i>который хочешь удалить!</i>",
        parse_mode="HTML",
        reply_markup=werty,
    )
    await state.set_state(Tasks.geo_delete)


@dp.message_handler(content_types=["text"], state=Tasks.geo_delete)
async def geo_dkladsl(message: types.Message, state: FSMContext) -> None:
    country_to_delete = message.text
    if country_to_delete == "⬅️Назад в меню":
        await state.set_state(Ref_state.zadman)
        await geo_tasks(message, state)
    else:
        conn = sqlite3.connect("database")
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM countries WHERE name=?", (country_to_delete,))
        existing_country = cursor.fetchone()

        if not existing_country:
            await message.answer(
                f"<i>ГЕО:</i> <b>{country_to_delete}</b> <i>не существует в базе данных!</i>",
                parse_mode="HTML",
            )
            await message.answer(
                f"<i>Отправь</i> <b>ГЕО</b>,<i>который хочешь удалить!</i>",
                parse_mode="HTML",
            )

            await state.set_state(Tasks.geo_delete)
        else:
            # Удаляем страну из базы данных
            cursor.execute("DELETE FROM countries WHERE name=?", (country_to_delete,))
            conn.commit()
            await message.answer(
                f"<i>ГЕО:</i> <b>{country_to_delete}</b> <i>успешно удален из базы данных!</i>",
                parse_mode="HTML",
            )
            await state.set_state(Tasks.geo_konez)


@dp.message_handler(
    Text(equals="⬅️Назад в меню", ignore_case=True), state=Tasks.geo_konez
)
async def tex765(message: types.Message, state: FSMContext) -> None:
    await state.set_state(Ref_state.zadman)
    await geo_tasks(message, state)


# ----------------------------------------------------------------------------------------------------------#
# ----------------------------------------------------------------------------------------------------------#
# ----------------------------------------------------------------------------------------------------------#
# ----------------------------------------------------------------------------------------------------------#
# ----------------------------------------------------------------------------------------------------------#
# ----------------------------------------------------------------------------------------------------------#
# ----------------------------------------------------------------------------------------------------------#
# ----------------------------------------------------------------------------------------------------------#
# ----------------------------------------------------------------------------------------------------------#
@dp.message_handler(
    Text(equals="Заявки на выплату💲", ignore_case=True), state=Ref_state.admin_panele
)
async def tex765(message: types.Message, state: FSMContext) -> None:
    mark = types.ReplyKeyboardMarkup(resize_keyboard=True)
    mk1 = types.KeyboardButton("Отправить заявку✅")
    mark.row(mk1)
    mk2 = types.KeyboardButton("Обработаю позже❌")
    mark.row(mk2)
    await message.answer(
        f"<i>Привет,@{message.from_user.username}!</i>\n\nВ этом разделе ты будешь обрабатывать все заявки на выплату денежных средств от пользователей данного бота!\n\n<i>Не ошибись с реквезитами,да и в целом,будь внимателен)</i>",
        parse_mode="HTML",
        reply_markup=mark,
    )
    await message.answer(f"<i>Отправить новую заявку?</i>", parse_mode="HTML")
    await state.set_state(Ref_state.zayotnot)
    # oldest_application = get_oldest_application()
    # if oldest_application:
    # user_id = message.from_user.id
    # req = oldest_application[2]
    # await send_application_with_confirm_button(user_id,req)


@dp.message_handler(
    Text(equals="Обработаю позже❌", ignore_case=True), state=Ref_state.zayotnot
)
async def nazadfff(message: types.Message, state: FSMContext):
    await state.reset_state()
    return await tadm454(message, state)


@dp.message_handler(
    Text(equals="Отправить заявку✅", ignore_case=True), state=Ref_state.zayotnot
)
async def naz667(message: types.Message, state: FSMContext):
    oldest_application = get_oldest_application()
    if oldest_application:
        user_id = message.from_user.id
        req = oldest_application[2]

        markup = types.InlineKeyboardMarkup()
        confirm_button = types.InlineKeyboardButton(
            text="Подтвердить", callback_data="confirm"
        )
        reject_button = types.InlineKeyboardButton(
            text="Отклонить", callback_data="reject"
        )
        markup.row(confirm_button, reject_button)
        await bot.send_message(
            chat_id=user_id, text=req, parse_mode="HTML", reply_markup=markup
        )
        # await send_application_with_confirm_button(user_id,req)
        await state.set_state(Ref_state.podotkl)
    else:
        await message.answer("Нет заявок для обработки!")
        await state.set_state(Ref_state.zayotnot)


@dp.callback_query_handler(text="confirm", state=Ref_state.podotkl)
async def inlane(callback: types.CallbackQuery, state: FSMContext):
    user_id = callback.from_user.id
    application_id = callback.message.message_id
    application_text = callback.message.text
    conn = sqlite3.connect("database")
    cursor = conn.cursor()
    cursor.execute(
        "DELETE FROM Requests WHERE id = (SELECT id FROM Requests ORDER BY id ASC LIMIT 1)"
    )
    conn.commit()
    conn.close()
    await bot.delete_message(
        chat_id=callback.message.chat.id, message_id=application_id
    )
    response_text = "Вы обработали заявку!"
    await bot.send_message(chat_id=user_id, text=response_text)
    await state.set_state(Ref_state.zayotnot)


@dp.callback_query_handler(text="reject", state=Ref_state.podotkl)
async def inlane(callback: types.CallbackQuery, state: FSMContext):
    user_id = callback.from_user.id
    application_id = callback.message.message_id
    application_text = callback.message.text
    conn = sqlite3.connect("database")
    cursor = conn.cursor()
    cursor.execute(
        "DELETE FROM Requests WHERE id = (SELECT id FROM Requests ORDER BY id ASC LIMIT 1)"
    )
    conn.commit()
    conn.close()
    await bot.delete_message(
        chat_id=callback.message.chat.id, message_id=application_id
    )
    response_text = "Вы отклонили заявку!"
    await bot.send_message(chat_id=user_id, text=response_text)
    await state.set_state(Ref_state.zayotnot)


# ----------------------------------------------------------------------------------------------------------#
# ----------------------------------------------------------------------------------------------------------#
# ----------------------------------------------------------------------------------------------------------#
# ----------------------------------------------------------------------------------------------------------#
# ----------------------------------------------------------------------------------------------------------#
# ----------------------------------------------------------------------------------------------------------#
# ----------------------------------------------------------------------------------------------------------#
# ----------------------------------------------------------------------------------------------------------#
# ----------------------------------------------------------------------------------------------------------#


raspilka_text = ""  # Переменная для хранения текста рассылки

# ... (ваш остальной код)


@dp.message_handler(
    Text(equals="Сделать рассылку📢", ignore_case=True), state=Ref_state.admin_panele
)
async def sendall(message: types.Message, state: FSMContext):
    back = ReplyKeyboardMarkup(resize_keyboard=True)
    b1 = KeyboardButton("⬅️Назад в меню")
    back.row(b1)
    await message.answer(
        "Отправь текст, который хочешь разослать всем пользователям!", reply_markup=back
    )
    await state.set_state(Ref_state.rassilka)


@dp.message_handler(
    Text(equals="⬅️Назад в меню", ignore_case=True), state=Ref_state.rassilka
)
async def nazadfff(message: types.Message, state: FSMContext):
    await state.reset_state()
    return await start(message)


@dp.message_handler(
    content_types=[
        "text",
        "photo",
        "video",
        "audio",
        "document",
        "voice",
        "sticker",
        "animation",
    ],
    state=Ref_state.rassilka,
)
@dp.message_handler(state=Ref_state.rassilka)
async def handle_messages(message: types.Message, state: FSMContext):
    text_message = message.text
    file_id = None
    content_type = "text"

    if message.content_type in [
        "photo",
        "text",
        "video",
        "audio",
        "document",
        "voice",
        "sticker",
        "animation",
    ]:
        content_type = message.content_type

        if content_type == "photo":
            file_id = message.photo[-1].file_id
        elif content_type == "video":
            file_id = message.video.file_id
        elif content_type == "audio":
            file_id = message.audio.file_id
        elif content_type == "document":
            file_id = message.document.file_id
        elif content_type == "voice":
            file_id = message.voice.file_id
        elif content_type == "sticker":
            file_id = message.sticker.file_id
        elif content_type == "animation":
            file_id = message.animation.file_id
        elif content_type == "text":
            file_id = None
    # Добавьте проверку на отсутствие текста и файлов
    if not text_message and not file_id:
        await message.answer("ERROR")
        await state.reset_state()
        return await start(message)

    conn = sqlite3.connect("database")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO rasmes (file_id, content_type, text_message) VALUES (?, ?, ?)",
        (file_id, content_type, text_message),
    )
    conn.commit()

    # Далее идет код для добавления кнопки...

    bsda = InlineKeyboardMarkup(row_width=1)
    b1 = InlineKeyboardButton(text="Да", callback_data="add_button")
    bsda.row(b1)
    b2 = InlineKeyboardButton(text="Нет", callback_data="not_button")
    bsda.row(b2)

    await message.answer("Добавить кнопку?", reply_markup=bsda)
    await state.set_state(Ref_state.danot)


@dp.message_handler(
    Text(equals="⬅️Назад в меню", ignore_case=True), state=Ref_state.danot
)
async def tex765(message: types.Message, state: FSMContext) -> None:
    await state.reset_state()
    return await start(message)


@dp.callback_query_handler(
    Text(equals="not_button", ignore_case=True), state=Ref_state.danot
)
async def inlanef(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer()
    flfpp = InlineKeyboardMarkup(row_width=1)
    dfk1 = InlineKeyboardButton(text="Да", callback_data="dat")
    flfpp.row(dfk1)
    ddf1 = InlineKeyboardButton(text="Нет", callback_data="net")
    flfpp.row(ddf1)
    await callback.message.answer("Подтвердить рассылку?", reply_markup=flfpp)
    await state.set_state(Ref_state.podtverdut_rass)


@dp.callback_query_handler(
    Text(equals="add_button", ignore_case=True), state=Ref_state.danot
)
async def inlanef(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer("Введите текст кнопки!")
    await callback.answer()
    await state.set_state(Ref_state.url_KNOPKA)


@dp.message_handler(
    Text(equals="⬅️Назад в меню", ignore_case=True), state=Ref_state.url_KNOPKA
)
async def tex765(message: types.Message, state: FSMContext) -> None:
    await state.reset_state()
    return await start(message)


@dp.message_handler(content_types=["text"], state=Ref_state.url_KNOPKA)
async def url009(message: types.Message, state: FSMContext):
    global raspilka_text
    raspilka_text = message.text
    await message.answer("Введите URL для кнопки!")
    await state.set_state(Ref_state.all_knpk)


@dp.message_handler(
    Text(equals="⬅️Назад в меню", ignore_case=True), state=Ref_state.all_knpk
)
async def tex765(message: types.Message, state: FSMContext) -> None:
    await state.reset_state()
    return await start(message)


@dp.message_handler(content_types=["text"], state=Ref_state.all_knpk)
async def podver123(message: types.Message, state: FSMContext):
    global url_knpk

    url_knpk = message.text
    link = r"https?://\S+"
    if re.search(link, url_knpk):
        conn = sqlite3.connect("database")
        cursor = conn.cursor()
        cursor.execute(
            "SELECT text_message, file_id, content_type FROM rasmes ORDER BY id DESC LIMIT 1"
        )
        row = cursor.fetchone()
        if row:
            text_message, file_id, content_type = row
            knmnv = InlineKeyboardMarkup(row_width=1)
            knmv1 = InlineKeyboardButton(text=raspilka_text, url=url_knpk)
            knmnv.add(knmv1)

            if content_type == "photo":
                await bot.send_photo(
                    chat_id=message.from_user.id,
                    photo=file_id,
                    caption=text_message,
                    parse_mode="HTML",
                    reply_markup=knmnv,
                )
            elif content_type == "video":
                await bot.send_video(
                    chat_id=message.from_user.id,
                    video=file_id,
                    caption=text_message,
                    parse_mode="HTML",
                    reply_markup=knmnv,
                )
            elif content_type == "audio":
                await bot.send_audio(
                    chat_id=message.from_user.id,
                    audio=file_id,
                    caption=text_message,
                    parse_mode="HTML",
                    reply_markup=knmnv,
                )
            elif content_type == "document":
                await bot.send_document(
                    chat_id=message.from_user.id,
                    document=file_id,
                    caption=text_message,
                    parse_mode="HTML",
                    reply_markup=knmnv,
                )
            elif content_type == "sticker":
                await bot.send_sticker(
                    chat_id=message.from_user.id, sticker=file_id, reply_markup=knmnv
                )
            elif content_type == "animation":
                await bot.send_animation(
                    chat_id=message.from_user.id,
                    animation=file_id,
                    caption=text_message,
                    parse_mode="HTML",
                    reply_markup=knmnv,
                )
            elif content_type == "text":
                await bot.send_message(
                    chat_id=message.from_user.id,
                    text=text_message,
                    parse_mode="HTML",
                    reply_markup=knmnv,
                )
        flfpp = InlineKeyboardMarkup(row_width=1)
        dfk1 = InlineKeyboardButton(text="Да", callback_data="da")
        flfpp.row(dfk1)
        ddf1 = InlineKeyboardButton(text="Нет", callback_data="net")
        flfpp.row(ddf1)
        await message.answer("Подтвердить рассылку?", reply_markup=flfpp)
        await state.set_state(Ref_state.podtverdut_rass)

    else:
        await state.set_state()
        await message.answer(
            "Это не ссылка. Пожалуйста, начните сначала и введите правильную ссылку."
        )
        return await start(message)


@dp.callback_query_handler(
    Text(equals="net", ignore_case=True), state=Ref_state.podtverdut_rass
)
async def tex765(callback: types.CallbackQuery, state: FSMContext) -> None:
    await callback.message.answer("Рассылка отменена!")
    await state.set_state(Ref_state.dfsfsdfs)


@dp.message_handler(
    Text(equals="⬅️Назад в меню", ignore_case=True), state=Ref_state.dfsfsdfs
)
async def tex765(message: types.Message, state: FSMContext) -> None:
    await state.reset_state()
    return await start(message)


@dp.callback_query_handler(
    Text(equals="dat", ignore_case=True), state=Ref_state.podtverdut_rass
)
async def tex765(callback: types.CallbackQuery, state: FSMContext) -> None:
    if callback.from_user.id == 5087149698:  # Проверьте ваш ID
        database = DataBase("database")
        conn = sqlite3.connect("database")
        cursor = conn.cursor()
        cursor.execute("SELECT user_id FROM users")
        users = cursor.fetchall()
        conn.close()

        for user_id in users:
            try:
                conn = sqlite3.connect("database")
                cursor = conn.cursor()
                cursor.execute(
                    "SELECT content_type, text_message, file_id FROM rasmes ORDER BY id DESC LIMIT 1"
                )
                row = cursor.fetchone()

                if row:
                    content_type, text_message, file_id = row

                    if content_type == "photo":
                        await bot.send_photo(
                            user_id[0],
                            photo=file_id,
                            caption=text_message,
                            parse_mode="HTML",
                        )
                    elif content_type == "video":
                        await bot.send_video(
                            user_id[0],
                            video=file_id,
                            caption=text_message,
                            parse_mode="HTML",
                        )
                    elif content_type == "audio":
                        await bot.send_audio(
                            user_id[0],
                            audio=file_id,
                            caption=text_message,
                            parse_mode="HTML",
                        )
                    elif content_type == "document":
                        await bot.send_document(
                            user_id[0],
                            document=file_id,
                            caption=text_message,
                            parse_mode="HTML",
                        )
                    elif content_type == "sticker":
                        await bot.send_sticker(user_id[0], sticker=file_id)
                    elif content_type == "animation":
                        await bot.send_animation(
                            user_id[0],
                            animation=file_id,
                            caption=text_message,
                            parse_mode="HTML",
                        )
                    elif content_type == "text":
                        await bot.send_message(
                            user_id[0],
                            text=text_message,
                            parse_mode="HTML",
                        )

                    await asyncio.sleep(0.05)

            except Exception as e:
                print(e)

        await bot.send_message(callback.from_user.id, "Рассылка завершена успешно!")


@dp.callback_query_handler(
    Text(equals="da", ignore_case=True), state=Ref_state.podtverdut_rass
)
async def tex765(callback: types.CallbackQuery, state: FSMContext) -> None:
    if callback.from_user.id == 5087149698:  # Проверьте ваш ID
        database = DataBase("database")
        conn = sqlite3.connect("database")
        cursor = conn.cursor()
        cursor.execute("SELECT user_id FROM users")
        users = cursor.fetchall()
        conn.close()

        for user_id in users:
            try:
                conn = sqlite3.connect("database")
                cursor = conn.cursor()
                cursor.execute(
                    "SELECT content_type, text_message, file_id FROM rasmes ORDER BY id DESC LIMIT 1"
                )
                row = cursor.fetchone()

                if row:
                    content_type, text_message, file_id = row
                    knmnv = InlineKeyboardMarkup(row_width=1)
                    knmv1 = InlineKeyboardButton(text=raspilka_text, url=url_knpk)
                    knmnv.add(knmv1)

                    if content_type == "photo":
                        await bot.send_photo(
                            user_id[0],
                            photo=file_id,
                            caption=text_message,
                            parse_mode="HTML",
                            reply_markup=knmnv,
                        )
                    elif content_type == "video":
                        await bot.send_video(
                            user_id[0],
                            video=file_id,
                            caption=text_message,
                            parse_mode="HTML",
                            reply_markup=knmnv,
                        )
                    elif content_type == "audio":
                        await bot.send_audio(
                            user_id[0],
                            audio=file_id,
                            caption=text_message,
                            parse_mode="HTML",
                            reply_markup=knmnv,
                        )
                    elif content_type == "document":
                        await bot.send_document(
                            user_id[0],
                            document=file_id,
                            caption=text_message,
                            parse_mode="HTML",
                            reply_markup=knmnv,
                        )
                    elif content_type == "sticker":
                        await bot.send_sticker(user_id[0], sticker=file_id)
                    elif content_type == "animation":
                        await bot.send_animation(
                            user_id[0],
                            animation=file_id,
                            caption=text_message,
                            parse_mode="HTML",
                            reply_markup=knmnv,
                        )
                    elif content_type == "text":
                        await bot.send_message(
                            user_id[0],
                            text=text_message,
                            parse_mode="HTML",
                            reply_markup=knmnv,
                        )

                    await asyncio.sleep(0.05)

            except Exception as e:
                print(e)

        await bot.send_message(callback.from_user.id, "Рассылка завершена успешно!")


@dp.message_handler(
    Text(equals="⬅️Назад в меню", ignore_case=True), state=Ref_state.podtverdut_rass
)
async def tex765(message: types.Message, state: FSMContext) -> None:
    await state.reset_state()
    return await start(message)


# ----------------------------------------------------------------------------------------------------------#
# ----------------------------------------------------------------------------------------------------------#
# ----------------------------------------------------------------------------------------------------------#
# ----------------------------------------------------------------------------------------------------------#
# ----------------------------------------------------------------------------------------------------------#


@dp.message_handler(
    Text(equals="⬅️Назад в меню", ignore_case=True), state=Ref_state.admin_panele
)
async def tex765(message: types.Message, state: FSMContext) -> None:
    await state.reset_state()
    return await start(message)


@dp.message_handler(Text(equals="Заработать💰", ignore_case=True), state=None)
async def start_work(message: types.Message, state: FSMContext) -> None:
    markup = InlineKeyboardMarkup(row_width=1)
    m1 = InlineKeyboardButton(text="Россия🇷🇺", callback_data="counry1")
    markup.add(m1)
    await message.answer(
        "Приветствую!В данном разделе ты сможешь зарабатывать реальные деньги выполняя задания💰",
        reply_markup=nav.nas21,
    )
    await message.answer("Выбери страну для работы👇", reply_markup=markup)
    await state.set_state(Ref_state.rf_button)


@dp.message_handler(
    Text(equals="⬅️Назад в меню", ignore_case=True), state=Ref_state.rf_button
)
async def start_work(message: types.Message, state: FSMContext) -> None:
    await state.reset_state()
    return await start(message)


@dp.callback_query_handler(text="counry1", state=Ref_state.rf_button)
async def zarabotati(query: types.CallbackQuery, state: FSMContext):
    markdow = InlineKeyboardMarkup(row_width=1)
    mk1 = InlineKeyboardButton(text="Дорогие💰", callback_data="some_money")
    mk2 = InlineKeyboardButton(text="Дешевые💴", callback_data="need_money")
    markdow.add(mk1, mk2)
    await bot.edit_message_text(
        chat_id=query.message.chat.id,
        message_id=query.message.message_id,
        text="Выберите статус заданий👇",
        reply_markup=markdow,
    )
    await state.set_state(Ref_state.status_zadania)


@dp.message_handler(
    Text(equals="⬅️Назад в меню", ignore_case=True), state=Ref_state.status_zadania
)
async def start_work(message: types.Message, state: FSMContext) -> None:
    await state.reset_state()
    return await start(message)


@dp.message_handler(Text(equals="Реферальная программа👥", ignore_case=True), state=None)
async def start_work(message: types.Message, state: FSMContext) -> None:
    await message.answer(
        f"🤝<i><b>Реферальная программа</b></i>\n\n<i>👥В нашем боте имеется одноуровневая система рефералов:\n\n 1 уровень - 15 % от заработка\n\n✔️Приглашайте новых пользователей и зарабатываете с их заработка!\n\n👁‍🗨Ссылка для привлечения рефералов:</i>\n<code>https://t.me/arvesjob_bot?start={message.from_user.id}</code>",
        parse_mode="HTML",
        reply_markup=nav.ref,
    )
    await state.set_state(Ref_state.waiting_for_stiker_name)


@dp.message_handler(
    Text(equals="👌", ignore_case=True), state=Ref_state.waiting_for_stiker_name
)
async def sticker_menu_ref55(message: types.Message, state: FSMContext) -> None:
    await state.reset_state()
    return await start(message)


kb = InlineKeyboardMarkup(row_width=1)
kb.add(InlineKeyboardButton(text="Связаться", url="https://t.me/AnastasiaNMN"))


@dp.message_handler(Text(equals="❔ FAQ ❔", ignore_case=True), state=None)
async def tex4(message: types.Message, state: FSMContext) -> None:
    await message.answer(
        "<a href = 'https://telegra.ph/FAQ-ARVES-10--Otvety-na-samye-chastye-voprosy-06-25'><i><b>Основная инструкция по работе с ботом</b></i></a>\n\n<b>Основные команды бота:</b>\n/start- перезагрузка бота\n/stop - остановка бота (полезно,если бот начал дублировать сообщения)\n/help - ссылка на основную инструкцию",
        parse_mode="HTML",
        reply_markup=nav.faq,
    )
    await state.set_state(Ref_state.waiting_for_markups_name)


@dp.message_handler(
    Text(equals="😊Да", ignore_case=True), state=Ref_state.waiting_for_markups_name
)
async def sticker_menu_ref91(message: types.Message, state: FSMContext) -> None:
    await state.reset_state()
    return await start(message)


@dp.message_handler(
    Text(equals="😔Нет,я невнимательный", ignore_case=True),
    state=Ref_state.waiting_for_markups_name,
)
async def sticker_menu_ref90(message: types.Message, state: FSMContext) -> None:
    await message.answer("Аккаунт технической поддержки!", reply_markup=kb)
    await state.reset_state()
    return await start(message)


@dp.message_handler(Text(equals="💲Вывод средств💲", ignore_case=True), state=None)
async def hrgh76675(message: types.Message, state: FSMContext) -> None:
    await message.answer(
        "❗❗❗<b>ВНИМАНИЕ</b>❗❗❗\n\n ВЫВОД ДЕНЕЖНЫХ СРЕДСТВ ПРОИСХОДИТ <b>ТОЛЬКО НА КАРТЫ РОССИЙСКИХ БАНКОВ!!!</b>\n\nВыберите <b>банк</b> или <b>платформу</b>",
        parse_mode="HTML",
        reply_markup=nav.viplata,
    )
    await state.set_state(Ref_state.waiting_for_viplata)


@dp.message_handler(
    Text(equals="⬅️Назад в меню", ignore_case=True), state=Ref_state.waiting_for_viplata
)
async def sticker_menu_ref00(message: types.Message, state: FSMContext) -> None:
    await state.reset_state()
    return await start(message)


@dp.message_handler(
    Text(equals="Сбербанк", ignore_case=True), state=Ref_state.waiting_for_viplata
)
async def sticker_menu_ref9(message: types.Message, state: FSMContext) -> None:
    viplik = ReplyKeyboardMarkup(resize_keyboard=True)
    vi1 = KeyboardButton("⬅️Назад в меню")
    viplik.add(vi1)
    await message.answer(
        "<i><b>Сбербанк</b></i>\n\n<i>Напиши <b>номер карты</b> или <b>номер телефона</b>, привязанный к карте</i>\n\n<b>Если введенные вами данные коректны,бот отправит сообщение,если же нет,то и сообщения не будет!!!</b>",
        reply_markup=viplik,
        parse_mode="HTML",
    )
    await state.set_state(Ref_state.waiting_for_Sberbank)


@dp.message_handler(
    Text(equals="⬅️Назад в меню", ignore_case=True),
    state=Ref_state.waiting_for_Sberbank,
)
async def tex765(message: types.Message, state: FSMContext) -> None:
    await state.reset_state()
    return await hrgh76675(message, state)


@dp.message_handler(content_types=["text"], state=Ref_state.waiting_for_Sberbank)
async def sber(message: types.Message, state: FSMContext):
    global recvis
    card_pattern = r"\b\d{4}[- ]?\d{4}[- ]?\d{4}[- ]?\d{4}\b"
    phone_pattern = r"\b(?:\+7|8)?[- (]?\d{3}[- )]?\d{3}[- ]?\d{2}[- ]?\d{2}\b"

    recvis = message.text
    if re.search(card_pattern, recvis):
        await message.reply("Данные банковской карты обновленны!")
        await message.answer(
            f"<code><i>💳Сбербанк</i></code>\n\n<b>📃по номеру карты:</b>\n  <code>{message.text}</code>\n\n<i>Минимальный вывод: <code>350₽</code></i>\n\n<b>Введите сумму,которую хотите вывести!</b>",
            parse_mode="HTML",
        )
        await state.set_state(Ref_state.sber1)
    if re.search(phone_pattern, recvis):
        await message.reply("Данные номера телефона обновленны!")
        await message.answer(
            f"<code><i>💳Сбербанк</i></code>\n\n<b>📃по номеру телефона:</b>\n  <code>{message.text}</code>\n\n<i>Минимальный вывод: <code>350₽</code></i>\n\n<b>Введите сумму,которую хотите вывести!</b>",
            parse_mode="HTML",
        )
        await state.set_state(Ref_state.sber1)
    else:
        pass


@dp.message_handler(content_types=["text"], state=Ref_state.sber1)
async def sber(message: types.Message, state: FSMContext):
    global recvis
    if message.text == "⬅️Назад в меню":
        await state.reset_state()
        return await hrgh76675(message, state)
    try:
        user_id = message.from_user.id
        user_balance = get_user_balance(user_id)
        amount_to_withdraw = float(message.text)
    except (UnboundLocalError, ValueError):
        await message.answer("Введите сумму,которую желаете вывести!")
        return sber

    if amount_to_withdraw >= 350.0:
        if user_balance >= amount_to_withdraw:
            new_balance = user_balance - amount_to_withdraw
            update_user_balance(user_id, new_balance)
            await message.answer(
                f"<b>Заявка на сумму {amount_to_withdraw}₽ отправленна на модерацию!</b>\n<b>Ожидаемое время выплаты: 14 дней!</b>",
                parse_mode="HTML",
            )
            user_id1 = message.from_user.id
            request = f"<b>Новая заявка!</b>\n\n<i>Имя пользователя:</i> {message.from_user.full_name}\n\n<i>ID пользователя:</i>{message.from_user.id}\n\n<i>Username пользователя:</i> @{message.from_user.username}\n\n<i>Реквизиты:</i> {recvis}\n<i>Банк: Сбербанк</i> \n\n<i>Сумма вывода:</i> <code>{amount_to_withdraw}₽</code>\n\n<i>💰Баланс:</i> {new_balance}₽"
            save_zayavk(user_id1, request)
            await state.reset_state()
            return await start(message)
        else:
            await message.answer(
                f"<b>На вашем балансе недостаточно средств!\n\nМинимальный вывод:350₽\n\n💰Доступно для вывода:{user_balance}₽</b>",
                parse_mode="HTML",
            )
    else:
        await message.answer(
            "<b>Минимальная сумма вывода:</b> <code>350₽</code>", parse_mode="HTML"
        )


@dp.message_handler(
    Text(equals="⬅️Назад в меню", ignore_case=True), state=Ref_state.sber1
)
async def tex765(message: types.Message, state: FSMContext) -> None:
    await state.reset_state()
    return await hrgh76675(message, state)


async def add_withdraw_request(user_id, username, bank, amount):
    conn = sqlite3.connect("database")
    c = conn.cursor()
    c.execute(
        "INSERT INTO users (user_id,username,bank,amount,status) VALUES (?,?,?,?,?)",
        (user_id, username, bank, amount, "pending"),
    )
    conn.commit()
    conn.close()


def get_withdraw_requests():
    conn = sqlite3.connect("database")
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE status=?", ("pending",))
    withdraw_request = c.fetchall()
    conn.close()
    return withdraw_request


def approve_withdraw_request(request_id):
    conn = sqlite3.connect("database")
    c = conn.cursor()
    c.execute("UPDATE users SET status=? WHERE request_id=?", ("approved", request_id))
    conn.commit()
    conn.close()


def reject_withdraw_request(request_id):
    conn = sqlite3.connect("database")
    c = conn.cursor()
    c.execute("UPDATE users SET status=? WHERE request_id=?", ("rejected", request_id))
    conn.commit()
    conn.close()


def get_user_balance(user_id):
    conn = sqlite3.connect("database")
    c = conn.cursor()
    c.execute("SELECT BALANCE FROM users WHERE user_id=?", (user_id,))
    user_balance = c.fetchone()
    conn.close()
    return user_balance[0] if user_balance else 0.0


def update_user_balance(user_id, new_balance):
    conn = sqlite3.connect("database")
    c = conn.cursor()
    c.execute("UPDATE users SET BALANCE=? WHERE user_id=?", (new_balance, user_id))
    conn.commit()
    conn.close()


@dp.message_handler(
    Text(equals="Тинькофф", ignore_case=True), state=Ref_state.waiting_for_viplata
)
async def sticker_menu_ref1(message: types.Message, state: FSMContext) -> None:
    tinnaz = ReplyKeyboardMarkup(resize_keyboard=True)
    tin1 = KeyboardButton("⬅️Назад в меню")
    tinnaz.add(tin1)
    await message.answer(
        "<i><b>Тинькофф</b></i>\n\n<i>Напиши <b>номер карты</b> или <b>номер телефона</b>, привязанный к карте</i>\n\n<b>Если введенные вами данные коректны,бот отправит сообщение,если же нет,то и сообщения не будет!!!</b>",
        reply_markup=tinnaz,
        parse_mode="HTML",
    )
    await state.set_state(Ref_state.waiting_for_Tinkoff)


@dp.message_handler(
    Text(equals="⬅️Назад в меню", ignore_case=True), state=Ref_state.waiting_for_Tinkoff
)
async def sticker_menu_ref8(message: types.Message, state: FSMContext) -> None:
    await state.reset_state()
    return await hrgh76675(message, state)


@dp.message_handler(content_types=["text"], state=Ref_state.waiting_for_Tinkoff)
async def sber(message: types.Message, state: FSMContext):
    global kekyh
    card_pattern = r"\b\d{4}[- ]?\d{4}[- ]?\d{4}[- ]?\d{4}\b"
    phone_pattern = r"\b(?:\+7|8)?[- (]?\d{3}[- )]?\d{3}[- ]?\d{2}[- ]?\d{2}\b"

    kekyh = message.text
    if re.search(card_pattern, kekyh):
        await message.reply("Данные банковской карты обновленны!")
        await message.answer(
            f"<code><i>💳Тинькофф</i></code>\n\n<b>📃по номеру карты:</b>\n  <code>{message.text}</code>\n\n<i>Минимальный вывод: <code>350₽</code></i>\n\n<b>Введите сумму,которую хотите вывести!</b>",
            parse_mode="HTML",
        )
        await state.set_state(Ref_state.tinkoff1)
    if re.search(phone_pattern, kekyh):
        await message.reply("Данные номера телефона обновленны!")
        await message.answer(
            f"<code><i>💳Тинькофф</i></code>\n\n<b>📃по номеру телефона:</b>\n  <code>{message.text}</code>\n\n<i>Минимальный вывод: <code>350₽</code></i>\n\n<b>Введите сумму,которую хотите вывести!</b>",
            parse_mode="HTML",
        )
        await state.set_state(Ref_state.tinkoff1)
    else:
        pass


@dp.message_handler(
    Text(equals="⬅️Назад в меню", ignore_case=True), state=Ref_state.admin_panele
)
async def tex765(message: types.Message, state: FSMContext) -> None:
    await state.reset_state()
    return await hrgh76675(message, state)


@dp.message_handler(content_types=["text"], state=Ref_state.tinkoff1)
async def sber(message: types.Message, state: FSMContext):
    global recvis
    if message.text == "⬅️Назад в меню":
        await state.reset_state()
        return await hrgh76675(message, state)
    try:
        user_id = message.from_user.id
        user_balance = get_user_balance(user_id)
        amount_to_withdraw = float(message.text)
    except (UnboundLocalError, ValueError):
        await message.answer("Введите сумму,которую желаете вывести!")
        return sber

    if amount_to_withdraw >= 350.0:
        if user_balance >= amount_to_withdraw:
            new_balance = user_balance - amount_to_withdraw
            update_user_balance(user_id, new_balance)
            await message.answer(
                f"<b>Заявка на сумму {amount_to_withdraw}₽ отправленна на модерацию!</b>",
                parse_mode="HTML",
            )
            user_id1 = message.from_user.id
            request = f"<b>Новая заявка!</b>\n\n<i>Имя пользователя:</i> {message.from_user.full_name}\n\n<i>ID пользователя:</i>{message.from_user.id}\n\n<i>Username пользователя:</i> @{message.from_user.username}\n\n<i>Реквизиты:</i> {kekyh}\n<i>Банк: Тинькофф</i> \n\n<i>Сумма вывода:</i> <code>{amount_to_withdraw}₽</code>\n\n<i>💰Баланс:</i> {new_balance}₽"
            save_zayavk(user_id1, request)
            await state.reset_state()
            return await start(message)
        else:
            await message.answer(
                f"<b>На вашем балансе недостаточно средств!\n\nМинимальный вывод:350₽\n\n💰Доступно для вывода:{user_balance}₽</b>",
                parse_mode="HTML",
            )
    else:
        await message.answer(
            "<b>Минимальная сумма вывода:</b> <code>350₽</code>", parse_mode="HTML"
        )


@dp.message_handler(
    Text(equals="ВТБ", ignore_case=True), state=Ref_state.waiting_for_viplata
)
async def sticker_menu_ref1(message: types.Message, state: FSMContext) -> None:
    tinnaz = ReplyKeyboardMarkup(resize_keyboard=True)
    tin1 = KeyboardButton("⬅️Назад в меню")
    tinnaz.add(tin1)
    await message.answer(
        "<i><b>ВТБ</b></i>\n\n<i>Напиши <b>номер карты</b> или <b>номер телефона</b>, привязанный к карте</i>\n\n<b>Если введенные вами данные коректны,бот отправит сообщение,если же нет,то и сообщения не будет!!!</b>",
        reply_markup=tinnaz,
        parse_mode="HTML",
    )
    await state.set_state(Ref_state.waiting_for_VTB)


@dp.message_handler(
    Text(equals="⬅️Назад в меню", ignore_case=True), state=Ref_state.waiting_for_VTB
)
async def sticker_menu_ref8(message: types.Message, state: FSMContext) -> None:
    await state.reset_state()
    return await hrgh76675(message, state)


@dp.message_handler(content_types=["text"], state=Ref_state.waiting_for_VTB)
async def sber(message: types.Message, state: FSMContext):
    global vtb
    card_pattern = r"\b\d{4}[- ]?\d{4}[- ]?\d{4}[- ]?\d{4}\b"
    phone_pattern = r"\b(?:\+7|8)?[- (]?\d{3}[- )]?\d{3}[- ]?\d{2}[- ]?\d{2}\b"

    vtb = message.text
    if re.search(card_pattern, vtb):
        await message.reply("Данные банковской карты обновленны!")
        await message.answer(
            f"<code><i>💳ВТБ</i></code>\n\n<b>📃по номеру карты:</b>\n  <code>{message.text}</code>\n\n<i>Минимальный вывод: <code>350₽</code></i>\n\n<b>Введите сумму,которую хотите вывести!</b>",
            parse_mode="HTML",
        )
        await state.set_state(Ref_state.vtb1)
    if re.search(phone_pattern, vtb):
        await message.reply("Данные номера телефона обновленны!")
        await message.answer(
            f"<code><i>💳ВТБ</i></code>\n\n<b>📃по номеру телефона:</b>\n  <code>{message.text}</code>\n\n<i>Минимальный вывод: <code>350₽</code></i>\n\n<b>Введите сумму,которую хотите вывести!</b>",
            parse_mode="HTML",
        )
        await state.set_state(Ref_state.vtb1)
    else:
        pass


@dp.message_handler(content_types=["text"], state=Ref_state.vtb1)
async def sber(message: types.Message, state: FSMContext):
    global recvis
    if message.text == "⬅️Назад в меню":
        await state.reset_state()
        return await hrgh76675(message, state)
    try:
        user_id = message.from_user.id
        user_balance = get_user_balance(user_id)
        amount_to_withdraw = float(message.text)
    except (UnboundLocalError, ValueError):
        await message.answer("Введите сумму,которую желаете вывести!")
        return sber

    if amount_to_withdraw >= 350.0:
        if user_balance >= amount_to_withdraw:
            new_balance = user_balance - amount_to_withdraw
            update_user_balance(user_id, new_balance)
            await message.answer(
                f"<b>Заявка на сумму {amount_to_withdraw}₽ отправленна на модерацию!</b>",
                parse_mode="HTML",
            )
            user_id1 = message.from_user.id
            request = f"<b>Новая заявка!</b>\n\n<i>Имя пользователя:</i> {message.from_user.full_name}\n\n<i>ID пользователя:</i>{message.from_user.id}\n\n<i>Username пользователя:</i> @{message.from_user.username}\n\n<i>Реквизиты:</i> {vtb}\n<i>Банк: ВТБ</i> \n\n<i>Сумма вывода:</i> <code>{amount_to_withdraw}₽</code>\n\n<i>💰Баланс:</i> {new_balance}₽"
            save_zayavk(user_id1, request)
            await state.reset_state()
            return await start(message)
        else:
            await message.answer(
                f"<b>На вашем балансе недостаточно средств!\n\nМинимальный вывод:350₽\n\n💰Доступно для вывода:{user_balance}₽</b>",
                parse_mode="HTML",
            )
    else:
        await message.answer(
            "<b>Минимальная сумма вывода:</b> <code>350₽</code>", parse_mode="HTML"
        )


@dp.message_handler(
    Text(equals="⬅️Назад в меню", ignore_case=True), state=Ref_state.vtb1
)
async def sticker_menu_ref8(message: types.Message, state: FSMContext) -> None:
    await state.reset_state()
    return await hrgh76675(message, state)


@dp.message_handler(
    Text(equals="⬅️Назад в меню", ignore_case=True), state=Ref_state.waiting_for_viplata
)
async def sticker_menu_ref2(message: types.Message, state: FSMContext) -> None:
    await state.reset_state()
    return await start(message)


@dp.message_handler(
    Text(equals="ЮMoney", ignore_case=True), state=Ref_state.waiting_for_viplata
)
async def sticker_menu_ref1(message: types.Message, state: FSMContext) -> None:
    tinnaz = ReplyKeyboardMarkup(resize_keyboard=True)
    tin1 = KeyboardButton("⬅️Назад в меню")
    tinnaz.add(tin1)
    await message.answer(
        "<i><b>ЮMoney</b></i>\n\n<i>Напиши <b>номер карты</b> или <b>номер телефона</b>, привязанный к карте</i>\n\n<b>Если введенные вами данные коректны,бот отправит сообщение,если же нет,то и сообщения не будет!!!</b>",
        reply_markup=tinnaz,
        parse_mode="HTML",
    )
    await state.set_state(Ref_state.waiting_for_YMONEY)  # waiting_for_YMONEY


@dp.message_handler(
    Text(equals="⬅️Назад в меню", ignore_case=True), state=Ref_state.waiting_for_YMONEY
)
async def sticker_menu_ref8(message: types.Message, state: FSMContext) -> None:
    await state.reset_state()
    return await hrgh76675(message, state)


@dp.message_handler(content_types=["text"], state=Ref_state.waiting_for_YMONEY)
async def sber(message: types.Message, state: FSMContext):
    global ymoney
    card_pattern = r"\b\d{4}[- ]?\d{4}[- ]?\d{4}[- ]?\d{4}\b"
    phone_pattern = r"\b(?:\+7|8)?[- (]?\d{3}[- )]?\d{3}[- ]?\d{2}[- ]?\d{2}\b"

    ymoney = message.text
    if re.search(card_pattern, ymoney):
        await message.reply("Данные банковской карты обновленны!")
        await message.answer(
            f"<code><i>💳ЮMoney</i></code>\n\n<b>📃по номеру карты:</b>\n  <code>{message.text}</code>\n\n<i>Минимальный вывод: <code>350₽</code></i>\n\n<b>Введите сумму,которую хотите вывести!</b>",
            parse_mode="HTML",
        )
        await state.set_state(Ref_state.ymoney1)  # ymoney1
    if re.search(phone_pattern, ymoney):
        await message.reply("Данные номера телефона обновленны!")
        await message.answer(
            f"<code><i>💳ЮMoney</i></code>\n\n<b>📃по номеру телефона:</b>\n  <code>{message.text}</code>\n\n<i>Минимальный вывод: <code>350₽</code></i>\n\n<b>Введите сумму,которую хотите вывести!</b>",
            parse_mode="HTML",
        )
        await state.set_state(Ref_state.ymoney1)  # ymoney1
    else:
        pass


@dp.message_handler(
    Text(equals="⬅️Назад в меню", ignore_case=True), state=Ref_state.admin_panele
)
async def tex765(message: types.Message, state: FSMContext) -> None:
    await state.reset_state()
    return await start(message)


@dp.message_handler(content_types=["text"], state=Ref_state.ymoney1)
async def sber(message: types.Message, state: FSMContext):
    global recvis
    if message.text == "⬅️Назад в меню":
        return await hrgh76675(message, state)
    try:
        user_id = message.from_user.id
        user_balance = get_user_balance(user_id)
        amount_to_withdraw = float(message.text)
    except (UnboundLocalError, ValueError):
        await message.answer("Введите сумму,которую желаете вывести!")
        return sber

    if amount_to_withdraw >= 350.0:
        if user_balance >= amount_to_withdraw:
            new_balance = user_balance - amount_to_withdraw
            update_user_balance(user_id, new_balance)
            await message.answer(
                f"<b>Заявка на сумму {amount_to_withdraw}₽ отправленна на модерацию!</b>",
                parse_mode="HTML",
            )
            user_id1 = message.from_user.id
            request = f"<b>Новая заявка!</b>\n\n<i>Имя пользователя:</i> {message.from_user.full_name}\n\n<i>ID пользователя:</i>{message.from_user.id}\n\n<i>Username пользователя:</i> @{message.from_user.username}\n\n<i>Реквизиты:</i> {ymoney}\n<i>Банк: ЮMoney</i> \n\n<i>Сумма вывода:</i> <code>{amount_to_withdraw}₽</code>\n\n<i>💰Баланс:</i> {new_balance}₽"
            save_zayavk(user_id1, request)
            await state.reset_state()
            return await start(message)
        else:
            await message.answer(
                f"<b>На вашем балансе недостаточно средств!\n\nМинимальный вывод:350₽\n\n💰Доступно для вывода:{user_balance}₽</b>",
                parse_mode="HTML",
            )
    else:
        await message.answer(
            "<b>Минимальная сумма вывода:</b> <code>350₽</code>", parse_mode="HTML"
        )


@dp.message_handler(
    Text(equals="Альфа Банк", ignore_case=True), state=Ref_state.waiting_for_viplata
)
async def sticker_menu_ref1(message: types.Message, state: FSMContext) -> None:
    tinnaz = ReplyKeyboardMarkup(resize_keyboard=True)
    tin1 = KeyboardButton("⬅️Назад в меню")
    tinnaz.add(tin1)
    await message.answer(
        "<i><b>Альфа Банк</b></i>\n\n<i>Напиши <b>номер карты</b> или <b>номер телефона</b>, привязанный к карте</i>\n\n<b>Если введенные вами данные коректны,бот отправит сообщение,если же нет,то и сообщения не будет!!!</b>",
        reply_markup=tinnaz,
        parse_mode="HTML",
    )
    await state.set_state(Ref_state.waiting_for_AlfA)  # waiting_for_AlfA


@dp.message_handler(
    Text(equals="⬅️Назад в меню", ignore_case=True), state=Ref_state.waiting_for_AlfA
)
async def sticker_menu_ref8(message: types.Message, state: FSMContext) -> None:
    await state.reset_state()
    return await hrgh76675(message, state)


@dp.message_handler(content_types=["text"], state=Ref_state.waiting_for_AlfA)
async def sber(message: types.Message, state: FSMContext):
    global alfa
    card_pattern = r"\b\d{4}[- ]?\d{4}[- ]?\d{4}[- ]?\d{4}\b"
    phone_pattern = r"\b(?:\+7|8)?[- (]?\d{3}[- )]?\d{3}[- ]?\d{2}[- ]?\d{2}\b"

    alfa = message.text
    if re.search(card_pattern, alfa):
        await message.reply("Данные банковской карты обновленны!")
        await message.answer(
            f"<code><i>💳Альфа Банк</i></code>\n\n<b>📃по номеру карты:</b>\n  <code>{message.text}</code>\n\n<i>Минимальный вывод: <code>350₽</code></i>\n\n<b>Введите сумму,которую хотите вывести!</b>",
            parse_mode="HTML",
        )
        await state.set_state(Ref_state.alfa1)
    if re.search(phone_pattern, alfa):
        await message.reply("Данные номера телефона обновленны!")
        await message.answer(
            f"<code><i>💳Альфа Банк</i></code>\n\n<b>📃по номеру телефона:</b>\n  <code>{message.text}</code>\n\n<i>Минимальный вывод: <code>350₽</code></i>\n\n<b>Введите сумму,которую хотите вывести!</b>",
            parse_mode="HTML",
        )
        await state.set_state(Ref_state.alfa1)  # alfa1
    else:
        pass


@dp.message_handler(content_types=["text"], state=Ref_state.alfa1)
async def sber(message: types.Message, state: FSMContext):
    global recvis
    if message.text == "⬅️Назад в меню":
        await state.reset_state()
        return await hrgh76675(message, state)
    try:
        user_id = message.from_user.id
        user_balance = get_user_balance(user_id)
        amount_to_withdraw = float(message.text)
    except (UnboundLocalError, ValueError):
        await message.answer("Введите сумму,которую желаете вывести!")
        return sber

    if amount_to_withdraw >= 350.0:
        if user_balance >= amount_to_withdraw:
            new_balance = user_balance - amount_to_withdraw
            update_user_balance(user_id, new_balance)
            await message.answer(
                f"<b>Заявка на сумму {amount_to_withdraw}₽ отправленна на модерацию!</b>",
                parse_mode="HTML",
            )
            user_id1 = message.from_user.id
            request = f"<b>Новая заявка!</b>\n\n<i>Имя пользователя:</i> {message.from_user.full_name}\n\n<i>ID пользователя:</i>{message.from_user.id}\n\n<i>Username пользователя:</i> @{message.from_user.username}\n\n<i>Реквизиты:</i> {alfa}\n<i>Банк: Альфа Банк</i> \n\n<i>Сумма вывода:</i> <code>{amount_to_withdraw}₽</code>\n\n<i>💰Баланс:</i> {new_balance}₽"
            save_zayavk(user_id1, request)
            await state.reset_state()
            return await start(message)
        else:
            await message.answer(
                f"<b>На вашем балансе недостаточно средств!\n\nМинимальный вывод:350₽\n\n💰Доступно для вывода:{user_balance}₽</b>",
                parse_mode="HTML",
            )
    else:
        await message.answer(
            "<b>Минимальная сумма вывода:</b> <code>350₽</code>", parse_mode="HTML"
        )


@dp.message_handler(
    Text(equals="На баланс телефона", ignore_case=True),
    state=Ref_state.waiting_for_viplata,
)
async def sticker_menu_ref5(message: types.Message, state: FSMContext) -> None:
    phonebal = ReplyKeyboardMarkup(resize_keyboard=True)
    phbl1 = KeyboardButton("⬅️Назад в меню")
    phonebal.add(phbl1)
    await message.answer(
        "<i><b>На баланс телефона</b></i>\n\n<i>Напиши <b>номер телефона!!!</b></i>\n\n<b>Если введенные вами данные коректны,бот отправит сообщение,если же нет,то и сообщения не будет!!!</b>",
        reply_markup=phonebal,
        parse_mode="HTML",
    )
    await state.set_state(Ref_state.waiting_for_Phone_Balance)


@dp.message_handler(
    Text(equals="⬅️Назад в меню", ignore_case=True),
    state=Ref_state.waiting_for_Phone_Balance,
)
async def sticker_menu_ref8(message: types.Message, state: FSMContext) -> None:
    await state.reset_state()
    return await start(message)


@dp.message_handler(content_types=["text"], state=Ref_state.waiting_for_Phone_Balance)
async def sber(message: types.Message, state: FSMContext):
    global kokol
    card_pattern = r"\b\d{4}[- ]?\d{4}[- ]?\d{4}[- ]?\d{4}\b"
    phone_pattern = r"\b(?:\+7|8)?[- (]?\d{3}[- )]?\d{3}[- ]?\d{2}[- ]?\d{2}\b"
    kokol = message.text
    if re.search(phone_pattern, kokol):
        await message.reply("Данные номера телефона обновленны!")
        await message.answer(
            f"<code><i>💳На баланс телефона</i></code>\n\n<b>📃по номеру телефона:</b>\n  <code>{message.text}</code>\n\n<i>Минимальный вывод: <code>350₽</code></i>\n\n<b>Введите сумму,которую хотите вывести!</b>",
            parse_mode="HTML",
        )
        await state.set_state(Ref_state.phone)
    else:
        pass


@dp.message_handler(content_types=["text"], state=Ref_state.phone)
async def sber(message: types.Message, state: FSMContext):
    if message.text == "⬅️Назад в меню":
        await state.reset_state()
        return await start(message)
    try:
        user_id = message.from_user.id
        user_balance = get_user_balance(user_id)
        amount_to_withdraw = float(message.text)
    except (UnboundLocalError, ValueError):
        await message.answer("Введите сумму,которую желаете вывести!")
        return sber

    if amount_to_withdraw >= 350.0:
        if user_balance >= amount_to_withdraw:
            new_balance = user_balance - amount_to_withdraw
            update_user_balance(user_id, new_balance)
            await message.answer(
                f"<b>Заявка на сумму {amount_to_withdraw}₽ отправленна на модерацию!</b>",
                parse_mode="HTML",
            )
            user_id1 = message.from_user.id
            request = f"<b>Новая заявка!</b>\n\n<i>Имя пользователя:</i> {message.from_user.full_name}\n\n<i>ID пользователя:</i>{message.from_user.id}\n\n<i>Username пользователя:</i> @{message.from_user.username}\n\n<i>Реквизиты:</i> {kokol}\n<i>Банк: Сбербанк</i> \n\n<i>Сумма вывода:</i> <code>{amount_to_withdraw}₽</code>\n\n<i>💰Баланс:</i> {new_balance}₽"
            save_zayavk(user_id1, request)
            await state.reset_state()
            return await start(message)
        else:
            await message.answer(
                f"<b>На вашем балансе недостаточно средств!\n\nМинимальный вывод:350₽\n\n💰Доступно для вывода:{user_balance}₽</b>",
                parse_mode="HTML",
            )
    else:
        await message.answer(
            "<b>Минимальная сумма вывода:</b> <code>350₽</code>", parse_mode="HTML"
        )


@dp.message_handler(
    Text(equals="⬅️Назад в меню", ignore_case=True), state=Ref_state.phone
)
async def sticker_menu_ref8(message: types.Message, state: FSMContext) -> None:
    await state.reset_state()
    return await start(message)


@dp.message_handler(
    Text(equals="⬅️Назад в меню", ignore_case=True),
    state=Ref_state.waiting_for_Phone_Balance,
)
async def sticker_menu_ref6(message: types.Message, state: FSMContext) -> None:
    await state.reset_state()
    return await start(message)


@dp.message_handler(
    Text(equals="Райффайзен Банк", ignore_case=True),
    state=Ref_state.waiting_for_viplata,
)
async def sticker_menu_ref1(message: types.Message, state: FSMContext) -> None:
    tinnaz = ReplyKeyboardMarkup(resize_keyboard=True)
    tin1 = KeyboardButton("⬅️Назад в меню")
    tinnaz.add(tin1)
    await message.answer(
        "<i><b>Райффайзен Банк</b></i>\n\n<i>Напиши <b>номер карты</b> или <b>номер телефона</b>, привязанный к карте</i>\n\n<b>Если введенные вами данные коректны,бот отправит сообщение,если же нет,то и сообщения не будет!!!</b>",
        reply_markup=tinnaz,
        parse_mode="HTML",
    )
    await state.set_state(Ref_state.waiting_for_raifzn)  # waiting_for_raifzn


@dp.message_handler(
    Text(equals="⬅️Назад в меню", ignore_case=True), state=Ref_state.waiting_for_raifzn
)
async def sticker_menu_ref8(message: types.Message, state: FSMContext) -> None:
    await state.reset_state()
    return await hrgh76675(message, state)


@dp.message_handler(content_types=["text"], state=Ref_state.waiting_for_raifzn)
async def sber(message: types.Message, state: FSMContext):
    global raifzn
    card_pattern = r"\b\d{4}[- ]?\d{4}[- ]?\d{4}[- ]?\d{4}\b"
    phone_pattern = r"\b(?:\+7|8)?[- (]?\d{3}[- )]?\d{3}[- ]?\d{2}[- ]?\d{2}\b"

    raifzn = message.text
    if re.search(card_pattern, raifzn):
        await message.reply("Данные банковской карты обновленны!")
        await message.answer(
            f"<code><i>💳Райффайзен Банк</i></code>\n\n<b>📃по номеру карты:</b>\n  <code>{message.text}</code>\n\n<i>Минимальный вывод: <code>350₽</code></i>\n\n<b>Введите сумму,которую хотите вывести!</b>",
            parse_mode="HTML",
        )
        await state.set_state(Ref_state.raifzn1)  # raifzn1
    if re.search(phone_pattern, raifzn):
        await message.reply("Данные номера телефона обновленны!")
        await message.answer(
            f"<code><i>💳Райффайзен Банк</i></code>\n\n<b>📃по номеру телефона:</b>\n  <code>{message.text}</code>\n\n<i>Минимальный вывод: <code>350₽</code></i>\n\n<b>Введите сумму,которую хотите вывести!</b>",
            parse_mode="HTML",
        )
        await state.set_state(Ref_state.raifzn1)  # raifzn1
    else:
        pass


@dp.message_handler(content_types=["text"], state=Ref_state.raifzn1)
async def sber(message: types.Message, state: FSMContext):
    global recvis
    if message.text == "⬅️Назад в меню":
        await state.reset_state()
        return await hrgh76675(message, state)
    try:
        user_id = message.from_user.id
        user_balance = get_user_balance(user_id)
        amount_to_withdraw = float(message.text)
    except (UnboundLocalError, ValueError):
        await message.answer("Введите сумму,которую желаете вывести!")
        return sber

    if amount_to_withdraw >= 350.0:
        if user_balance >= amount_to_withdraw:
            new_balance = user_balance - amount_to_withdraw
            update_user_balance(user_id, new_balance)
            await message.answer(
                f"<b>Заявка на сумму {amount_to_withdraw}₽ отправленна на модерацию!</b>",
                parse_mode="HTML",
            )
            user_id1 = message.from_user.id
            request = f"<b>Новая заявка!</b>\n\n<i>Имя пользователя:</i> {message.from_user.full_name}\n\n<i>ID пользователя:</i>{message.from_user.id}\n\n<i>Username пользователя:</i> @{message.from_user.username}\n\n<i>Реквизиты:</i> {raifzn}\n<i>Банк: Райффайзен Банк</i> \n\n<i>Сумма вывода:</i> <code>{amount_to_withdraw}₽</code>\n\n<i>💰Баланс:</i> {new_balance}₽"
            save_zayavk(user_id1, request)
            await state.reset_state()
            return await start(message)
        else:
            await message.answer(
                f"<b>На вашем балансе недостаточно средств!\n\nМинимальный вывод:350₽\n\n💰Доступно для вывода:{user_balance}₽</b>",
                parse_mode="HTML",
            )
    else:
        await message.answer(
            "<b>Минимальная сумма вывода:</b> <code>350₽</code>", parse_mode="HTML"
        )


@dp.message_handler(
    Text(equals="МТС Банк", ignore_case=True),
    state=Ref_state.waiting_for_viplata,
)
async def sticker_menu_ref1(message: types.Message, state: FSMContext) -> None:
    tinnaz = ReplyKeyboardMarkup(resize_keyboard=True)
    tin1 = KeyboardButton("⬅️Назад в меню")
    tinnaz.add(tin1)
    await message.answer(
        "<i><b>МТС Банк</b></i>\n\n<i>Напиши <b>номер карты</b> или <b>номер телефона</b>, привязанный к карте</i>\n\n<b>Если введенные вами данные коректны,бот отправит сообщение,если же нет,то и сообщения не будет!!!</b>",
        reply_markup=tinnaz,
        parse_mode="HTML",
    )
    await state.set_state(Ref_state.waiting_for_mtc)  # waiting_for_mtc


@dp.message_handler(
    Text(equals="⬅️Назад в меню", ignore_case=True), state=Ref_state.waiting_for_mtc
)
async def sticker_menu_ref8(message: types.Message, state: FSMContext) -> None:
    await state.reset_state()
    return await hrgh76675(message, state)


@dp.message_handler(content_types=["text"], state=Ref_state.waiting_for_mtc)
async def sber(message: types.Message, state: FSMContext):
    global mtc
    card_pattern = r"\b\d{4}[- ]?\d{4}[- ]?\d{4}[- ]?\d{4}\b"
    phone_pattern = r"\b(?:\+7|8)?[- (]?\d{3}[- )]?\d{3}[- ]?\d{2}[- ]?\d{2}\b"

    mtc = message.text
    if re.search(card_pattern, mtc):
        await message.reply("Данные банковской карты обновленны!")
        await message.answer(
            f"<code><i>💳МТС Банк</i></code>\n\n<b>📃по номеру карты:</b>\n  <code>{message.text}</code>\n\n<i>Минимальный вывод: <code>350₽</code></i>\n\n<b>Введите сумму,которую хотите вывести!</b>",
            parse_mode="HTML",
        )
        await state.set_state(Ref_state.mtc1)  # mtc1
    if re.search(phone_pattern, mtc):
        await message.reply("Данные номера телефона обновленны!")
        await message.answer(
            f"<code><i>💳МТС Банк</i></code>\n\n<b>📃по номеру телефона:</b>\n  <code>{message.text}</code>\n\n<i>Минимальный вывод: <code>350₽</code></i>\n\n<b>Введите сумму,которую хотите вывести!</b>",
            parse_mode="HTML",
        )
        await state.set_state(Ref_state.mtc1)  # raifzn1
    else:
        pass


@dp.message_handler(content_types=["text"], state=Ref_state.mtc1)
async def sber(message: types.Message, state: FSMContext):
    global recvis
    if message.text == "⬅️Назад в меню":
        await state.reset_state()
        return await hrgh76675(message, state)
    try:
        user_id = message.from_user.id
        user_balance = get_user_balance(user_id)
        amount_to_withdraw = float(message.text)
    except (UnboundLocalError, ValueError):
        await message.answer("Введите сумму,которую желаете вывести!")
        return sber

    if amount_to_withdraw >= 350.0:
        if user_balance >= amount_to_withdraw:
            new_balance = user_balance - amount_to_withdraw
            update_user_balance(user_id, new_balance)
            await message.answer(
                f"<b>Заявка на сумму {amount_to_withdraw}₽ отправленна на модерацию!</b>",
                parse_mode="HTML",
            )
            user_id1 = message.from_user.id
            request = f"<b>Новая заявка!</b>\n\n<i>Имя пользователя:</i> {message.from_user.full_name}\n\n<i>ID пользователя:</i>{message.from_user.id}\n\n<i>Username пользователя:</i> @{message.from_user.username}\n\n<i>Реквизиты:</i> {mtc}\n<i>Банк: МТС Банк</i> \n\n<i>Сумма вывода:</i> <code>{amount_to_withdraw}₽</code>\n\n<i>💰Баланс:</i> {new_balance}₽"
            save_zayavk(user_id1, request)
            await state.reset_state()
            return await start(message)
        else:
            await message.answer(
                f"<b>На вашем балансе недостаточно средств!\n\nМинимальный вывод:350₽\n\n💰Доступно для вывода:{user_balance}₽</b>",
                parse_mode="HTML",
            )
    else:
        await message.answer(
            "<b>Минимальная сумма вывода:</b> <code>350₽</code>", parse_mode="HTML"
        )


@dp.message_handler(
    Text(equals="Банк Открытие", ignore_case=True),
    state=Ref_state.waiting_for_viplata,
)
async def sticker_menu_ref1(message: types.Message, state: FSMContext) -> None:
    tinnaz = ReplyKeyboardMarkup(resize_keyboard=True)
    tin1 = KeyboardButton("⬅️Назад в меню")
    tinnaz.add(tin1)
    await message.answer(
        "<i><b>Банк Открытие</b></i>\n\n<i>Напиши <b>номер карты</b> или <b>номер телефона</b>, привязанный к карте</i>\n\n<b>Если введенные вами данные коректны,бот отправит сообщение,если же нет,то и сообщения не будет!!!</b>",
        reply_markup=tinnaz,
        parse_mode="HTML",
    )
    await state.set_state(Ref_state.waiting_for_otk)  # waiting_for_mtc


@dp.message_handler(
    Text(equals="⬅️Назад в меню", ignore_case=True), state=Ref_state.waiting_for_otk
)
async def sticker_menu_ref8(message: types.Message, state: FSMContext) -> None:
    await state.reset_state()
    return await hrgh76675(message, state)


@dp.message_handler(content_types=["text"], state=Ref_state.waiting_for_otk)
async def sber(message: types.Message, state: FSMContext):
    global otk
    card_pattern = r"\b\d{4}[- ]?\d{4}[- ]?\d{4}[- ]?\d{4}\b"
    phone_pattern = r"\b(?:\+7|8)?[- (]?\d{3}[- )]?\d{3}[- ]?\d{2}[- ]?\d{2}\b"

    otk = message.text
    if re.search(card_pattern, otk):
        await message.reply("Данные банковской карты обновленны!")
        await message.answer(
            f"<code><i>💳Банк Открытие</i></code>\n\n<b>📃по номеру карты:</b>\n  <code>{message.text}</code>\n\n<i>Минимальный вывод: <code>350₽</code></i>\n\n<b>Введите сумму,которую хотите вывести!</b>",
            parse_mode="HTML",
        )
        await state.set_state(Ref_state.otk1)  # otk1
    if re.search(phone_pattern, otk):
        await message.reply("Данные номера телефона обновленны!")
        await message.answer(
            f"<code><i>💳Банк Открытие</i></code>\n\n<b>📃по номеру телефона:</b>\n  <code>{message.text}</code>\n\n<i>Минимальный вывод: <code>350₽</code></i>\n\n<b>Введите сумму,которую хотите вывести!</b>",
            parse_mode="HTML",
        )
        await state.set_state(Ref_state.otk1)  # raifzn1
    else:
        pass


@dp.message_handler(content_types=["text"], state=Ref_state.otk1)
async def sber(message: types.Message, state: FSMContext):
    global recvis
    if message.text == "⬅️Назад в меню":
        await state.reset_state()
        return await hrgh76675(message, state)
    try:
        user_id = message.from_user.id
        user_balance = get_user_balance(user_id)
        amount_to_withdraw = float(message.text)
    except (UnboundLocalError, ValueError):
        await message.answer("Введите сумму,которую желаете вывести!")
        return sber

    if amount_to_withdraw >= 350.0:
        if user_balance >= amount_to_withdraw:
            new_balance = user_balance - amount_to_withdraw
            update_user_balance(user_id, new_balance)
            await message.answer(
                f"<b>Заявка на сумму {amount_to_withdraw}₽ отправленна на модерацию!</b>",
                parse_mode="HTML",
            )
            user_id1 = message.from_user.id
            request = f"<b>Новая заявка!</b>\n\n<i>Имя пользователя:</i> {message.from_user.full_name}\n\n<i>ID пользователя:</i>{message.from_user.id}\n\n<i>Username пользователя:</i> @{message.from_user.username}\n\n<i>Реквизиты:</i> {otk}\n<i>Банк: Банк Открытие</i> \n\n<i>Сумма вывода:</i> <code>{amount_to_withdraw}₽</code>\n\n<i>💰Баланс:</i> {new_balance}₽"
            save_zayavk(user_id1, request)
            await state.reset_state()
            return await start(message)
        else:
            await message.answer(
                f"<b>На вашем балансе недостаточно средств!\n\nМинимальный вывод:350₽\n\n💰Доступно для вывода:{user_balance}₽</b>",
                parse_mode="HTML",
            )
    else:
        await message.answer(
            "<b>Минимальная сумма вывода:</b> <code>350₽</code>", parse_mode="HTML"
        )


@dp.message_handler(
    Text(equals="Газпром Банк", ignore_case=True),
    state=Ref_state.waiting_for_viplata,
)
async def sticker_menu_ref1(message: types.Message, state: FSMContext) -> None:
    tinnaz = ReplyKeyboardMarkup(resize_keyboard=True)
    tin1 = KeyboardButton("⬅️Назад в меню")
    tinnaz.add(tin1)
    await message.answer(
        "<i><b>Газпром Банк</b></i>\n\n<i>Напиши <b>номер карты</b> или <b>номер телефона</b>, привязанный к карте</i>\n\n<b>Если введенные вами данные коректны,бот отправит сообщение,если же нет,то и сообщения не будет!!!</b>",
        reply_markup=tinnaz,
        parse_mode="HTML",
    )
    await state.set_state(Ref_state.waiting_for_gasprom)  # waiting_for_mtc


@dp.message_handler(
    Text(equals="⬅️Назад в меню", ignore_case=True), state=Ref_state.waiting_for_gasprom
)
async def sticker_menu_ref8(message: types.Message, state: FSMContext) -> None:
    await state.reset_state()
    return await hrgh76675(message, state)


@dp.message_handler(content_types=["text"], state=Ref_state.waiting_for_gasprom)
async def sber(message: types.Message, state: FSMContext):
    global gas
    card_pattern = r"\b\d{4}[- ]?\d{4}[- ]?\d{4}[- ]?\d{4}\b"
    phone_pattern = r"\b(?:\+7|8)?[- (]?\d{3}[- )]?\d{3}[- ]?\d{2}[- ]?\d{2}\b"

    gas = message.text
    if re.search(card_pattern, gas):
        await message.reply("Данные банковской карты обновленны!")
        await message.answer(
            f"<code><i>💳Газпром Банк</i></code>\n\n<b>📃по номеру карты:</b>\n  <code>{message.text}</code>\n\n<i>Минимальный вывод: <code>350₽</code></i>\n\n<b>Введите сумму,которую хотите вывести!</b>",
            parse_mode="HTML",
        )
        await state.set_state(Ref_state.gas1)  # otk1
    if re.search(phone_pattern, gas):
        await message.reply("Данные номера телефона обновленны!")
        await message.answer(
            f"<code><i>💳Газпром Банк</i></code>\n\n<b>📃по номеру телефона:</b>\n  <code>{message.text}</code>\n\n<i>Минимальный вывод: <code>350₽</code></i>\n\n<b>Введите сумму,которую хотите вывести!</b>",
            parse_mode="HTML",
        )
        await state.set_state(Ref_state.gas1)  # raifzn1
    else:
        pass


@dp.message_handler(content_types=["text"], state=Ref_state.gas1)
async def sber(message: types.Message, state: FSMContext):
    global recvis
    if message.text == "⬅️Назад в меню":
        await state.reset_state()
        return await hrgh76675(message, state)
    try:
        user_id = message.from_user.id
        user_balance = get_user_balance(user_id)
        amount_to_withdraw = float(message.text)
    except (UnboundLocalError, ValueError):
        await message.answer("Введите сумму,которую желаете вывести!")
        return sber

    if amount_to_withdraw >= 350.0:
        if user_balance >= amount_to_withdraw:
            new_balance = user_balance - amount_to_withdraw
            update_user_balance(user_id, new_balance)
            await message.answer(
                f"<b>Заявка на сумму {amount_to_withdraw}₽ отправленна на модерацию!</b>",
                parse_mode="HTML",
            )
            user_id1 = message.from_user.id
            request = f"<b>Новая заявка!</b>\n\n<i>Имя пользователя:</i> {message.from_user.full_name}\n\n<i>ID пользователя:</i>{message.from_user.id}\n\n<i>Username пользователя:</i> @{message.from_user.username}\n\n<i>Реквизиты:</i> {gas}\n<i>Банк: Газпром Банк</i> \n\n<i>Сумма вывода:</i> <code>{amount_to_withdraw}₽</code>\n\n<i>💰Баланс:</i> {new_balance}₽"
            save_zayavk(user_id1, request)
            await state.reset_state()
            return await start(message)
        else:
            await message.answer(
                f"<b>На вашем балансе недостаточно средств!\n\nМинимальный вывод:350₽\n\n💰Доступно для вывода:{user_balance}₽</b>",
                parse_mode="HTML",
            )
    else:
        await message.answer(
            "<b>Минимальная сумма вывода:</b> <code>350₽</code>", parse_mode="HTML"
        )


@dp.message_handler(
    Text(equals="Совком Банк", ignore_case=True),
    state=Ref_state.waiting_for_viplata,
)
async def sticker_menu_ref1(message: types.Message, state: FSMContext) -> None:
    tinnaz = ReplyKeyboardMarkup(resize_keyboard=True)
    tin1 = KeyboardButton("⬅️Назад в меню")
    tinnaz.add(tin1)
    await message.answer(
        "<i><b>Совком Банк</b></i>\n\n<i>Напиши <b>номер карты</b> или <b>номер телефона</b>, привязанный к карте</i>\n\n<b>Если введенные вами данные коректны,бот отправит сообщение,если же нет,то и сообщения не будет!!!</b>",
        reply_markup=tinnaz,
        parse_mode="HTML",
    )
    await state.set_state(Ref_state.waiting_for_sovb)  # waiting_for_mtc


@dp.message_handler(
    Text(equals="⬅️Назад в меню", ignore_case=True), state=Ref_state.waiting_for_sovb
)
async def sticker_menu_ref8(message: types.Message, state: FSMContext) -> None:
    await state.reset_state()
    return await hrgh76675(message, state)


@dp.message_handler(content_types=["text"], state=Ref_state.waiting_for_sovb)
async def sber(message: types.Message, state: FSMContext):
    global sovb
    card_pattern = r"\b\d{4}[- ]?\d{4}[- ]?\d{4}[- ]?\d{4}\b"
    phone_pattern = r"\b(?:\+7|8)?[- (]?\d{3}[- )]?\d{3}[- ]?\d{2}[- ]?\d{2}\b"

    sovb = message.text
    if re.search(card_pattern, sovb):
        await message.reply("Данные банковской карты обновленны!")
        await message.answer(
            f"<code><i>💳Совком Банк</i></code>\n\n<b>📃по номеру карты:</b>\n  <code>{message.text}</code>\n\n<i>Минимальный вывод: <code>350₽</code></i>\n\n<b>Введите сумму,которую хотите вывести!</b>",
            parse_mode="HTML",
        )
        await state.set_state(Ref_state.sovb)  # otk1
    if re.search(phone_pattern, sovb):
        await message.reply("Данные номера телефона обновленны!")
        await message.answer(
            f"<code><i>💳Совком Банк</i></code>\n\n<b>📃по номеру телефона:</b>\n  <code>{message.text}</code>\n\n<i>Минимальный вывод: <code>350₽</code></i>\n\n<b>Введите сумму,которую хотите вывести!</b>",
            parse_mode="HTML",
        )
        await state.set_state(Ref_state.sovb)  # raifzn1
    else:
        pass


@dp.message_handler(content_types=["text"], state=Ref_state.sovb)
async def sber(message: types.Message, state: FSMContext):
    global recvis
    if message.text == "⬅️Назад в меню":
        await state.reset_state()
        return await hrgh76675(message, state)
    try:
        user_id = message.from_user.id
        user_balance = get_user_balance(user_id)
        amount_to_withdraw = float(message.text)
    except (UnboundLocalError, ValueError):
        await message.answer("Введите сумму,которую желаете вывести!")
        return sber

    if amount_to_withdraw >= 350.0:
        if user_balance >= amount_to_withdraw:
            new_balance = user_balance - amount_to_withdraw
            update_user_balance(user_id, new_balance)
            await message.answer(
                f"<b>Заявка на сумму {amount_to_withdraw}₽ отправленна на модерацию!</b>",
                parse_mode="HTML",
            )
            user_id1 = message.from_user.id
            request = f"<b>Новая заявка!</b>\n\n<i>Имя пользователя:</i> {message.from_user.full_name}\n\n<i>ID пользователя:</i>{message.from_user.id}\n\n<i>Username пользователя:</i> @{message.from_user.username}\n\n<i>Реквизиты:</i> {sovb}\n<i>Банк: Совком Банк</i> \n\n<i>Сумма вывода:</i> <code>{amount_to_withdraw}₽</code>\n\n<i>💰Баланс:</i> {new_balance}₽"
            save_zayavk(user_id1, request)
            await state.reset_state()
            return await start(message)
        else:
            await message.answer(
                f"<b>На вашем балансе недостаточно средств!\n\nМинимальный вывод:350₽\n\n💰Доступно для вывода:{user_balance}₽</b>",
                parse_mode="HTML",
            )
    else:
        await message.answer(
            "<b>Минимальная сумма вывода:</b> <code>350₽</code>", parse_mode="HTML"
        )


@dp.message_handler(
    Text(equals="Другой банк", ignore_case=True), state=Ref_state.waiting_for_viplata
)
async def sticker_menu_ref1(message: types.Message, state: FSMContext) -> None:
    tinnarr = ReplyKeyboardMarkup(resize_keyboard=True)
    tin44 = KeyboardButton("⬅️Назад в меню")
    tinnarr.add(tin44)
    await message.answer(
        "<i><b>Другой банк</b></i>\n\nНапиши <b>номер карты</b>!\n\n<b>Если введенные вами данные коректны,бот отправит сообщение,если же нет,то и сообщения не будет!!!</b>",
        reply_markup=tinnarr,
        parse_mode="HTML",
    )
    await state.set_state(Ref_state.another_bank)


@dp.message_handler(
    Text(equals="⬅️Назад в меню", ignore_case=True), state=Ref_state.another_bank
)
async def sticker_menu_ref6(message: types.Message, state: FSMContext) -> None:
    await state.reset_state()
    return await start(message)


@dp.message_handler(content_types=["text"], state=Ref_state.another_bank)
async def sber(message: types.Message, state: FSMContext):
    global hohikol
    hohikol = message.text
    card_pattern = r"\b\d{4}[- ]?\d{4}[- ]?\d{4}[- ]?\d{4}\b"
    if re.search(card_pattern, hohikol):
        await message.reply("Данные банковской карты обновленны!")
        await message.answer(
            f"<code><i>💳Другой банк</i></code>\n\n<b>📃по номеру карты:</b>\n  <code>{hohikol}</code>\n\n<i>Минимальный вывод: <code>350₽</code></i>\n\n<b>Введите сумму,которую хотите вывести!</b>",
            parse_mode="HTML",
        )
        await state.set_state(Ref_state.bank1)
    else:
        pass


@dp.message_handler(content_types=["text"], state=Ref_state.bank1)
async def sber(message: types.Message, state: FSMContext):
    if message.text == "⬅️Назад в меню":
        await state.reset_state()
        return await start(message)
    try:
        user_id = message.from_user.id
        user_balance = get_user_balance(user_id)
        amount_to_withdraw = float(message.text)
    except (UnboundLocalError, ValueError):
        await message.answer("Введите сумму,которую желаете вывести!")
        return sber

    if amount_to_withdraw >= 350.0:
        if user_balance >= amount_to_withdraw:
            new_balance = user_balance - amount_to_withdraw
            update_user_balance(user_id, new_balance)
            await message.answer(
                f"<b>Заявка на сумму {amount_to_withdraw}₽ отправленна на модерацию!</b>",
                parse_mode="HTML",
            )
            user_id1 = message.from_user.id
            request = f"<b>Новая заявка!</b>\n\n<i>Имя пользователя:</i> {message.from_user.full_name}\n\n<i>ID пользователя:</i>{message.from_user.id}\n\n<i>Username пользователя:</i> @{message.from_user.username}\n\n<i>Реквизиты:</i> {hohikol}\n\n<i>Сумма вывода:</i> <code>{amount_to_withdraw}₽</code>\n\n<i>💰Баланс:</i> {new_balance}₽"
            save_zayavk(user_id1, request)

            await state.reset_state()
            return await start(message)

        else:
            await message.answer(
                f"<b>На вашем балансе недостаточно средств!\n\nМинимальный вывод:350₽\n\n💰Доступно для вывода:{user_balance}₽</b>",
                parse_mode="HTML",
            )
    else:
        await message.answer(
            "<b>Минимальная сумма вывода:</b> <code>350₽</code>", parse_mode="HTML"
        )


def create_zayavk():
    conn = sqlite3.connect("database")
    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS Requests(id INTEGER PRIMARY KEY,user_id INTEGER,requisites TEXT)"
    )
    conn.commit()
    conn.close()


def save_zayavk(user_id, requisites):
    conn = sqlite3.connect("database")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO Requests (user_id,requisites)VALUES (?,?)", (user_id, requisites)
    )
    conn.commit()
    conn.close()


def get_random_application():
    conn = sqlite3.connect("database")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Requests ORDER BY RANDOM() LIMIT 1")
    random_application = cursor.fetchone()
    conn.close()
    return random_application


async def send_application_with_confirm_button(user_id, requisites):
    markup = types.InlineKeyboardMarkup()
    confirm_button = types.InlineKeyboardButton(
        text="Подтвердить", callback_data="confirm"
    )
    reject_button = types.InlineKeyboardButton(text="Отклонить", callback_data="reject")
    markup.row(confirm_button, reject_button)
    await bot.send_message(chat_id=user_id, text=requisites, reply_markup=markup)


@dp.callback_query_handler(lambda callback_query: True)
async def handle_confirmation(query: types.CallbackQuery):
    user_id = query.from_user.id
    application_id = query.message.message_id
    application_text = query.message.text

    if query.data == "confirm":
        conn = sqlite3.connect("database")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Requests WHERE id = ?", (application_id,))
        conn.commit()
        conn.close()
        await bot.delete_message(
            chat_id=query.message.chat.id, message_id=application_id
        )
        response_text = "Одна из ваших заявок на выплату быда одобрена!"
        await bot.send_message(chat_id=user_id, text=response_text)
    elif query.data == "reject":
        conn = sqlite3.connect("database")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Requests WHERE id = ?", (application_id,))
        conn.commit()
        conn.close()
        await bot.delete_message(
            chat_id=query.message.chat.id, message_id=application_id
        )
        response_text = "Одна из ваших заявок на выплату была отклонена!"
        await bot.send_message(chat_id=user_id, text=response_text)


def get_oldest_application():
    conn = sqlite3.connect("database")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Requests ORDER BY id ASC LIMIT 1")
    oldest_application = cursor.fetchone()
    conn.close()
    return oldest_application


@dp.message_handler(
    Text(equals="⬅️Назад в меню", ignore_case=True), state=Ref_state.bank1
)
async def sticker_menu_ref8(message: types.Message, state: FSMContext) -> None:
    await state.reset_state()
    return await start(message)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
