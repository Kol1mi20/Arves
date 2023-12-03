import sqlite3

class Database6:
  def __init__(self,db_file):
    self.connection = sqlite3.connect(db_file)
    self.cursor = self.connection.cursor()

  def add_user(full_name,username):
     conn = sqlite3.connect('database')
     cursor = conn.cursor()
     cursor.execute('INSERT INTO users (full_name, username) VALUES(?,?)',(full_name,username,))
     conn.commit()
     conn.close()