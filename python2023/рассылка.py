import asyncio
import logging
from aiogram import Bot, Dispatcher, types, executor
from db1 import DataBase1
import config as cfg

 
logging.basicConfig(level=logging.INFO)


bot = Bot(token=cfg.TOKEN) 
dp = Dispatcher(bot) 
db1 = DataBase1('database') 

   
 
@dp.message_handler(commands=["sendall"])  
async def broadcaster(message: types.Message):
    if message.chat.type == "private":
       if message.from_user.id == int(cfg.ADMIN_ID):
         text = message.text
         users = db1.get_users()
         for row in users:
               try:
                 await asyncio.sleep(.05) 
                 await bot.send_message(row[0], text)
                 if int(row[1]) != 1:
                     db1.set_active(row[0], 1)
               except:
                     db1.set_active(row[0], 0)
         await bot.send_message(message.from_user.id,"Успешно!") 
        
    
         
    

 
if __name__ == "__main__":
  executor.start_polling(dp, skip_updates=True)


 