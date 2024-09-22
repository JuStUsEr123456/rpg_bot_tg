import random as r
import time as t
class Hero:
    ras = ["Самурай","Воин","Колдун"]
    def __init__(self, name, hp, dg, skill):
        
        self.name = name 
        self.hp = hp
        self.dg = dg
        self.skill = skill

    def __str__(self):
        return f"{self.name}\nздоровье: {self.hp}\nурон: {self.dg}"

    @staticmethod
    def create_hero(name: object, hero: object) -> object:
        if hero == "Самурай":
            hp = 75
            dg = 0
            skill = None
            print(f"Теперь у тебя {hp} хп и {dg } урон ")
        elif hero == "Воин":
            hp = 105
            dg = 50
            skill = None
            print(f"Теперь у тебя {hp} хп и {dg} урон")
        elif hero == "Колдун":
            hp = 60
            dg = 150
            skill = None
            print(f"Теперь у тебя {hp} хп и {dg} урон")
        elif hero == "Пират":
            hp = 100
            dg = 100
            skill = None
            print(f"Теперь у тебя {hp} хп и {dg} урон")
        elif hero == "Бродяга":
            hp = 95
            dg = 65
            skill = None
            print(f"Теперь у тебя {hp} хп и {dg} урок")
        elif hero == "Берсерк":
            hp = 205
            dg = 175
            skill = None
            print(f"Теперь у тебя {hp} хп и {dg} урок")
        else :
            print("Такой расы нет")
            hp = 0
            dg = 0
            skill = None
        return Hero(name,hp,dg,skill)
    def ataka(self,enemy):
        enemy.hp = enemy.hp-self.dg
        if  enemy.hp <= 0:
            print("Легенда пала  ")
            '''itm = r.randint(0,3)
            self.skill = r.choice(pw)
            print(f"Вы накурились и обрели способности {self.skill}")
            if itm == 1:
                a = self.food()
                print("ВЫ нашли сундук с сокровищами в было "+ a)
                print(self.hp, "хп")
            elif itm == 2:
                b = self.wapon()
                print("ВЫ нашли сундук с сокровищами в было "+ b[0], b[1])
                print(self.dg , "урон")
            elif itm == 3:
                f = self.sheld()
                print("ВЫ нашли сундук с сокровищами в было "+ f[0], f[1])
                print(self.hp, "хп")
            else:
                print("Вас обдилили удачей ")'''
            return False
        else:
#print( f"У врага осталось столько хп {bad_boy.hp}")
            return True
    '''def ability():

        if hero.skill == "Сибирь":

            print("Враг в ступаре от вашего мето жительствав ")
            bad_boy.dg = 0

        elif hero.skill == "Похмеле":
            print("Врагу плоха от вашего внешнего вида ")
            bad_boy.hp -= 10

        else:
            print("вы что то зделали я сам хз ")
            hero.hp += 10
    def att(self, victim):
            if self.skill != None:
                self.ability()
                print(victim.name ,"Получил", victim.hp,"хп")'''
    def food(self):
        disies = {5: "негор в пене ", 10: "сухарик в кормане крутки ", 15: "Бабушкины перожки ",20: "маторное масло "}
        k = r.choice(list(disies.keys()))
        self.hp += k
        return   disies[k]
    def wapon(self):
        wapon = {"сковорода": 25, "стул" : 15, "палка" : 30,"арматура" : 25}
        w  = r.choice(list(wapon.keys()))
        rar = ["редкий", "эпический", "легендарный", "мифический ", "друг вернуший сотку"]
        rar_chos = r.choice(rar)
        if rar_chos == "редкий":
            self.dg += 5 + wapon[w]
        elif rar_chos == "эпический":
            self.dg += 10 + wapon[w]
        elif rar_chos == "легендарный":
            self.dg += 15 + wapon[w]
        elif rar_chos == "мифический":
            self.dg += 20 + wapon[w]
        elif rar_chos == "друг вернуший сотку":
            self.dg += 25 + wapon[w]
        return w , rar_chos
    def sheld(self):
        shelds = {"Шлем": 5, "Шит": 15, "barbarnomi": 20 }
        armor = r.choice(list(shelds.keys()))
        rar_shelds = ["редкий", "эпический", "легендарный", "мифический", "друг вернуший сотку"]
        rar_chos1 = r.choice(rar_shelds)
        if rar_chos1 == "редкий":
            self.hp += 5 + shelds[armor]
        elif rar_chos1 == "эпический":
            self.hp += 10 + shelds[armor]
        elif rar_chos1 == "легендарный":
            self.hp += 15 + shelds[armor]
        elif rar_chos1 == "мифический":
            self.hp += 20 + shelds[armor]
        elif rar_chos1 == "друг вернуший сотку":
            self.hp += 25 + shelds[armor]
        return armor , rar_chos1
class BAD_BOY:      
    def __init__(self, name, hp, dg ):
        self.name = name 
        self.hp = hp
        self.dg = dg
    def __str__(self):
        return f"{self.name}\nздоровье: {self.hp}\nурон: {self.dg}"
    def create_enemy():
        name = r.randint(0, 4)
        hp_enemy = r.randint(50, 80)
        dg_enemy = r.randint(60, 100)
        if name == 1:
            name = "ВЫ потратили все своё время на тик ток "+"На вас напал TimeLord"
        elif name == 2:
            name = "пока вы переходили пешеходный перехо на вас напала фура"
        elif name == 3:
            name = "Пока вы лежали на диване вас позвала мама на вас напала диван "
        elif name == 4:
            name = "Ваш сон потривожел будилник"
        return BAD_BOY(name, hp_enemy, dg_enemy)
    def ataka(self,enemy):
        enemy.hp = enemy.hp-self.dg
        if  enemy.hp <= 0:
            print("Вы погибли ахахахаххахахахахахахахахахахахахахахахахахаххахахаха!!!!!!!!!")
            return False
            quit()
        else:
            print( f"У вас осталось столько хп {enemy.hp}")
            print( f"У вас осталось столько урон {enemy.dg}")
            return True
def fs():
    vs = input("Здатся или Уреть да?")
    if vs == "да":
        rezalt = hero_frs.ataka(bad_boy)
        if rezalt:
            bad_boy.ataka(hero_frs)
            fs()
    elif vs == "нет":
        coin = r.choice([0,1])
        if coin:
            print("Игра в Дашу питишественуцу не удолась вас побили ")
            t.sleep(1)
            bad_boy.ataka(hero_frs)

            fs()
        else :
            print("ВЫ сбежали пока что")
            t.sleep(2)
    else :
        print("У вас нет таких прав ")
        fs()
pw = ["Сибирь", "Похмеле", "Шаманство"]
def main():
    name = input("Ведите имя ")
    t.sleep(2)
    hero = input("Выберете тип персонажа: Самурай, Воин, Колдун, Метчиник, Бродяга, Берсерк"+"   "  )
    t.sleep(2)
    hero_frs = Hero.create_hero(name, hero)
    while True:
        road = r.randint(0,1)
        if road:
            print("Вы павернили на лево и вас паймали ")
            t.sleep(2)
            bad_boy = BAD_BOY.create_enemy()
            print(f"У туби {hero_frs.hp} хп")
            print(f"У туби {hero_frs.dg} урон")
            print(f"У врага {bad_boy.hp} хп")
            print(f"У врага {bad_boy.dg} урон")
            fs()
        else:
            print("ТЫ был одорён удачей ")
    print(f"Твоё {hero_frs.hp} хп")

