import sqlite3 as s

def insert(table, **kwargs):
    conection = s.connect("game_rpg.db")
    cursor = conection.cursor()
    columns = ', '.join(["'" + k + "'" for k in kwargs.keys()])
    values = ', '.join(["'" + str(v) + "'" for v in kwargs.values()])
    cursor.execute(f'''
    insert into {table} ({columns}) values 
    ({values})
    ''')
    conection.commit()
    conection.close()
insert("RAS", id=2, ras="Колдун", hp=1, DMG=300)
def cal_name(columns,table):
    conection = s.connect("game_rpg.db")
    cursor = conection.cursor()
    cursor.execute(f'''
    SELECT {columns}
    From {table}
    ''')
    resalt = cursor.fetchall()
    conection.commit()
    conection.close()
    res = [i[0] for i in resalt]
    return res
print(cal_name("*","RAS"))
