import random as r

Hp = 0
Coins = 0
Damage = 0
LVL = 0
XP = 0

def printParameters():
    print("У тебя {0} жизней, {1} урона, {2} монет, {3} уровень и {4} опыта".format(Hp, Damage, Coins, LVL, XP))

def printHp():
    print("У тебя", Hp, "жизней.")

def printDamage():
    print("У тебя", Damage, "урона.")

def printCoins():
    print("У тебя", Coins, "монет.")

def printLVL():
    print("У тебя", LVL, "уровень.")

def printXP():
    print("У тебя", XP, "опыта.")

def Minotaur():
    global Hp
    global Coins
    global XP
    global LVL

    residentofdarknessLvl = r.randint(35, 50)
    residentofdarknessHp = residentofdarknessLvl * 1.5
    residentofdarknessDamage = residentofdarknessLvl * 2 - 1

    print("Ты набрел на Минотавра, у него {0} уровень, {1} жизней и {2} урона.".format(residentofdarknessLvl, residentofdarknessHp, residentofdarknessDamage))
    printParameters()

    while residentofdarknessHp > 0:
        Сhoice = input("Что будешь делать (атака): ").lower()

        if Сhoice == "атака":
            residentofdarknessHp -= Damage
            if residentofdarknessHp <= 0:
                print("Ты победил Минотавра. У него осталось", 0, "жизней.")
            else:
                print("Ты атаковал Минотавра и у него осталось", residentofdarknessHp, "жизней.")
        else:
            continue

        if residentofdarknessHp > 0:
            Hp -= residentofdarknessDamage
            print("Минотавр атаковал и у тебя осталось", Hp, "жизней.")

        if Hp <= 0:
            break

    else:
        loot = r.randint(0, 5) + residentofdarknessLvl
        Coins += loot
        Xp = r.randint(0, 5) + residentofdarknessLvl
        XP += Xp
        LVL += 1
        print("Тебе удалось одолеть Минотавра, за что ты получил", loot, "монет", XP, "опыта и повысил свой уровень на 1.")
        printParameters()

def residentofdarkness():
    global Hp
    global Coins
    global XP
    global LVL

    residentofdarknessLvl = r.randint(15, 25)
    residentofdarknessHp = residentofdarknessLvl * 1.5
    residentofdarknessDamage = residentofdarknessLvl * 2 - 1

    print("Ты набрел на Жителя Тьмы, у него {0} уровень, {1} жизней и {2} урона.".format(residentofdarknessLvl, residentofdarknessHp, residentofdarknessDamage))
    printParameters()

    while residentofdarknessHp > 0:
        Сhoice = input("Что будешь делать (атака): ").lower()

        if Сhoice == "атака":
            residentofdarknessHp -= Damage
            if residentofdarknessHp <= 0:
                print("Ты победил Жителя Тьмы. У него осталось", 0, "жизней.")
            else:
                print("Ты атаковал Жителя тьмы и у него осталось", residentofdarknessHp, "жизней.")
        else:
            continue

        if residentofdarknessHp > 0:
            Hp -= residentofdarknessDamage
            print("Житель Тьмы атаковал и у тебя осталось", Hp, "жизней.")

        if Hp <= 0:
            break

    else:
        loot = r.randint(0, 5) + residentofdarknessLvl
        Coins += loot
        Xp = r.randint(0, 5) + residentofdarknessLvl
        XP += Xp
        LVL += 1
        print("Тебе удалось одолеть Жителя Тьмы, за что ты получил", loot, "монет", XP, "опыта и повысил свой уровень на 1.")
        printParameters()

def guardianofdustywalls():
    global Hp
    global Coins
    global XP
    global LVL

    guardianofdustywallsLvl = r.randint(25, 35)
    guardianofdustywallsHp = guardianofdustywallsLvl * 1.5
    guardianofdustywallsDamage = guardianofdustywallsLvl * 2 - 1

    print("Ты набрел на Хранителя пыльных стен, у него {0} уровень, {1} жизней и {2} урона.".format(guardianofdustywallsLvl, guardianofdustywallsHp, guardianofdustywallsDamage))
    printParameters()

    while guardianofdustywallsHp > 0:
        Сhoice = input("Что будешь делать (атака): ").lower()

        if Сhoice == "атака":
            guardianofdustywallsHp -= Damage
            if guardianofdustywallsHp <= 0:
                print("Ты победил Хранителя пыльных стен. У него осталось", 0, "жизней.")
            else:
                print("Ты атаковал Хранителя пыльных стен и у него осталось", guardianofdustywallsHp, "жизней.")
        else:
            continue

        if guardianofdustywallsHp > 0:
            Hp -= guardianofdustywallsDamage
            print("Хранитель пыльных стен атаковал и у тебя осталось", Hp, "жизней.")

        if Hp <= 0:
            break

    else:
        loot = r.randint(0, 5) + guardianofdustywallsLvl
        Coins += loot
        Xp = r.randint(0, 5) + guardianofdustywallsLvl
        XP += Xp
        LVL += 1
        print("Тебе удалось одолеть Хранителя пыльных стен, за что ты получил", loot, "монет", XP, "опыта и повысил свой уровень на 1.")
        printParameters()

def scroll():
    global Hp
    global Damage
    global Coins
    global LVL
    global XP

    def buy(XPPrice):
        global XP
        if XP >= XPPrice:
            XP -= XPPrice
            printXP()
            return True
        print("У тебя маловато опыта!")
        return False

    XPPrice = 10

    print("Ты нашел подозрительно светящийся свиток.")
    printParameters()

    while input("Подобрать свиток?: ").lower() == "подобрать":
        print("1) Повысить уровень -", XPPrice, "опыта;")

        Choice = input("Что хочешь прочесть?: ")
        if Choice == "1":
            if buy(XPPrice):
                LVL += 1
                Hp += r.randint(2, 5)
                Damage += r.randint(2, 5)
                printParameters()
        else:
            print("Не получается прочитать свиток!")

def Taverna():
    global Hp
    global Damage
    global Coins
    global LVL
    global XP

    def buy(Price):
        global Coins
        if Coins >= Price:
            Coins -= Price
            printCoins()
            return True
        print("У тебя маловато монет!")
        return False

    weaponLvl = r.randint(1, 3)
    weaponDamage = r.randint(1, 5) * weaponLvl
    weapons = ["Сломанный меч", "Ржавый топор", "Самодельный лук", "Булава", "Заточка", "Палка", "Кость Тролля", "Булыжник", "Копье", "Сюрикэн", "Кинжал", "Секира"]
    weaponRarities = ["Обычный", "Редкий", "Эпический", "Легендарный"]
    weaponRarity = weaponRarities[weaponLvl - 1]
    weaponPrice = r.randint(3, 10) * weaponLvl
    weapon = r.choice(weapons)

    OneHpPrice = 2
    ThreeHpPrice = 5
    OneDamagePrice = 3
    ThreeDamagePrice = 7

    print("Вдалеке ты видишь свет из окон таверны.")
    printParameters()

    while input("Вы подошли к таверне (зайти / уйти): ").lower() == "зайти":
        print("1) Одна единица здоровья -", OneHpPrice, "монет;")
        print("2) Три единицы здоровья -", ThreeHpPrice, "монет;")
        print("3) Одна единица урона -", OneDamagePrice, "монет;")
        print("4) Три единицы урона -", ThreeDamagePrice, "монет;")
        print("5) {0} {1} - {2} монет".format(weaponRarity, weapon, weaponPrice))

        Choice = input("Что хочешь приобрести: ")
        if Choice == "1":
            if buy(OneHpPrice):
                Hp += 1
                printHp()
        elif Choice == "2":
            if buy(ThreeHpPrice):
                Hp += 3
                printHp()
        elif Choice == "3":
            if buy(OneDamagePrice):
                Damage += 1
                printDamage()
        elif Choice == "4":
            if buy(ThreeDamagePrice):
                Damage += 1
                printDamage()
        elif Choice == "5":
            if buy(weaponPrice):
                Damage = weaponDamage
                printDamage()
        else:
            print("Ты мне зубы не заговаривай. Либо покупай, либо проваливай!")

def meetMonster():
    global Hp
    global Coins
    global XP
    global LVL

    monsterLvl = r.randint(1, 6)
    monsterHp = monsterLvl
    monsterDamage = monsterLvl * 2 - 1
    monsters = ["Grock", "Clop", "Cholop", "Madrock", "Lilbitch"]

    monster = r.choice(monsters)

    print("Ты набрел на монстра - {0}, у него {1} уровень, {2} жизней и {3} урона.".format(monster, monsterLvl, monsterHp, monsterDamage))
    printParameters()

    while monsterHp > 0:
        Сhoice = input("Что будешь делать (атака / бег): ").lower()

        if Сhoice == "атака":
            monsterHp -= Damage
            if monsterHp <= 0:
                print("Ты атаковал монстра и у него осталось", 0, "жизней.")
            else:
                print("Ты атаковал монстра и у него осталось", monsterHp, "жизней.")
        elif Сhoice == "бег":
            chance = r.randint(1, 2)
            if chance == 1:
                print("Тебе удалось потеряться среди стен лабиринта!")
                break
            else:
                print("Монстр оказался чересчур быстрым и догнал тебя...")
        else:
            continue

        if monsterHp > 0:
            Hp -= monsterDamage
            print("Монстр атаковал и у тебя осталось", Hp, "жизней.")

        if Hp <= 0:
            break

    else:
        loot = r.randint(0, 2) + monsterLvl
        Coins += loot
        Xp = r.randint(0, 2) + monsterLvl
        XP += Xp
        print("Тебе удалось одолеть монстра, за что ты получил", loot, "монет и", XP, "опыта.")
        printCoins()
        printXP()

def initGame(initHp, initCoins, initDamage, initLVL, initXP):
    global Hp
    global Coins
    global Damage
    global LVL
    global XP

    Hp = initHp
    Coins = initCoins
    Damage = initDamage
    LVL = initLVL
    XP = initXP

    print("Ворота закрываются за тобой и теперь ты вынужден гнить в этих лабиринтах до конца своих дней.")
    printParameters()

def gameLoop():
    situation = r.randint(0, 6)

    if situation == 0:
        Taverna()
    elif situation == 1:
        meetMonster()
    elif situation == 3:
        scroll()
    elif LVL == 10:
        residentofdarkness()
    elif LVL == 20:
        guardianofdustywalls()
    elif LVL == 30:
        Minotaur()
    else:
        input("Бродим во тьме...")

initGame(5, 5, 5, 1, 0)

while True:
    gameLoop()

    if Hp <= 0:
        if input("Твои кости станут частью этих стен. Хочешь начать сначала?: ").lower() == "да":
            initGame(5, 5, 5, 1, 0)
        else:
            break
