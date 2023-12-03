import sqlite3

class Database2:
  def __init__(self,db_file):
    self.connection = sqlite3.connect(db_file)
    self.cursor = self.connection.cursor()
    
    
  def card_nomer(self ,user_id, CARD_vip):
    with self.connection:
      return self.cursor.execute("UPDATE users SET CARD_vip =? WHERE user_id =?",(CARD_vip,user_id,))
  
  def phone_nomer(self, user_id, PHONE_vip):
    with self.connection:
      return self.cursor.execute("UPDATE users SET PHONE_vip =? WHERE user_id =?", (PHONE_vip, user_id,))
    
  def create_table():
    conn = sqlite3.connect('database')
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, user_id INEGER,BALANCE)")
    conn.commit()
    conn.close()