import sqlite3

class DataBase1:
  def __init__(self,db_file):
    self.connection = sqlite3.connect(db_file)
    self.cursor = self.connection.cursor()
  
  
  def set_active(self, user_id, active):
        with self.connection:
            return self.cursor.execute("UPDATE users SET active =? WHERE user_id =?", (active, user_id,))
  
  
  def get_users(self):
        with self.connection:
            return self.cursor.execute("SELECT user_id,active FROM users").fetchall()