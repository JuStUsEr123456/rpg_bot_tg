import sqlite3 as s

conection = s.connect("game_rpg.db")

cursor = conection.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
chat_id INTEGER PRIMERY KEY,
user_id INTEGER PRIMERY KEY,
user_name TEXT)
   ''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS RAS(
id INTEGER PRIMERY KEY,
ras TEXT,
hp REAL,
DMG REAL)
   ''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Hero(
id_hero INTEGER PRIMERY KEY,
hero_name TEXT,
hp REAL,
DMG REAL,
lvl INTEGER,
exp INTEGER)
   ''')



cursor.execute('''
insert into RAS values 
(0, "Самурай", 75, 65),
(1, "Воин", 105, 50),
(2, "Берсерк", 205, 175),
(3, "Пират", 100, 100)
''')

cursor.execute('''
DELETE FROM RAS
''')


print(cursor.fetchall())

conection.commit()
conection.close()