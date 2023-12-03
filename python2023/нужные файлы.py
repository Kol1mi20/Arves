from aiogram import Bot, Dispatcher, executor, types

TOKEN = "6624846975:AAEccnyxiI4UK5S3L14MD9MAXR0R7-ZNHNc"
CHANNEL_ID = "-1002005596317"


bot = Bot(token=TOKEN)
dispatcher = Dispatcher(bot)


@dispatcher.message_handler(commands=['start'])
async def start(message: types.Message):
    user_channel_status = await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)

    if user_channel_status['status'] != 'left':
        
    else:
        button = types.InlineKeyboardMarkup(row_width=1)
        m1 = types.InlineKeyboardButton(text="Подписаться",url="https://t.me/Arves_Job")
        m2 = types.InlineKeyboardButton(text="Готово",callback_data="готово")
        button.add(m1,m2)
        await bot.send_message(message.from_user.id, "Подпишитесь на наш канал для разблокировки бота!", reply_markup=button)


@dispatcher.callback_query_handler(lambda call: True)
async def callback(call: types.CallbackQuery):
    if call.message:
        user_channel_status = await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=call.from_user.id)

        if user_channel_status["status"] != "left":
            await bot.send_message(call.from_user.id, "молодец")
        else:
            await bot.send_message(call.from_user.id, "Вы не подписались :(")


if __name__ == '__main__':
    executor.start_polling(dispatcher)
    
    
    
    
    
    
    
    global punkts
    try:
        punkts = message.text
    except (ValueError,UnboundLocalError):
        await state.set_state(ZADANIA.punkts)
        await message.reply("Это не цифра!")
        await message.answer("Укажи количество пунтов(от 1 до 25),которые должен выполнить пользователь,чтобы выполнить задание правильно!")
    if punkts > 25 and punkts < 1:
        await message.reply("От 1 до 25!Введите кол-во пунктов!")
        await state.set_state(ZADANIA.punkts)
    else:
        i = 0
        message = "Введите действия пользователя,который он должен выполнить за "
        for i in range(1,punkts):
            m1 = "\n".join(
                [f"{message}{index + 1}!"for index, in punkts]
            )
            
            
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