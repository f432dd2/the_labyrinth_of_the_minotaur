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

# Рейдеры #

def raiders():
    global Hp
    global Coins
    global XP
    global LVL
    print("На пути тебе встретилась группа рейдеров. Против толпы не попрешь... Они требуют все твое золото, либо душу.")
    Choice = input("Отдать золото (отдать / бег): ").lower()
    if Choice == "отдать":
        print("Скромная плата за жизнь.")
        Coins = 0
    elif Choice == "отдать" and Coins == 0:
        print("Обманывать не хорошо...")
        Hp = 0
    elif Choice == "бег" or " ":
        chance = r.randint(-5, 1)
        if chance >= -3:
            Hp -= 1
            print("Тебе удалось потеряться среди стен лабиринта! Но камень вдогонку пришелся прямо в затылок.")
        else:
            Coins = 0
            Hp -= 1
            print("Похоже они знают эти стены лучше тебя.")
            if Hp <= 0:
                print("Против толпы не попрешь... Ты так и не успел найти товарищей.")
    printParameters()

# Босс #

def Minotaur():
    global Hp
    global Coins
    global XP
    global LVL

    MinotaurLvl = r.randint(30, 40)
    MinotaurHp = MinotaurLvl * 1.5
    MinotaurDamage = MinotaurLvl * 2 - 1

    print("Ты набрел на Минотавра, у него {0} уровень, {1} жизней и {2} урона.".format(MinotaurLvl, MinotaurHp, MinotaurDamage))
    printParameters()

    while MinotaurHp > 0:
        Сhoice = input("Что будешь делать (атака): ").lower()

        if Сhoice == "атака":
            MinotaurHp -= Damage
            if MinotaurHp <= 0:
                print("Ты победил Минотавра. У него осталось", 0, "жизней.")
            else:
                print("Ты атаковал Минотавра и у него осталось", MinotaurHp, "жизней.")
        else:
            continue

        if MinotaurHp > 0:
            Hp -= MinotaurDamage
            if Hp > 0:
                print("Минотавр атаковал и у тебя осталось", Hp, "жизней.")
            else:
                print("Минотавр атаковал и у тебя осталось", 0, "жизней.")

        if Hp <= 0:
            break

    else:
        loot = r.randint(0, 5) + MinotaurLvl
        Coins += loot
        Xp = r.randint(0, 5) + MinotaurLvl
        XP += Xp
        LVL += 1
        print("Тебе удалось одолеть Минотавра, за что ты получил", loot, "монет", XP, "опыта и повысил свой уровень на 1.")
        printParameters()

# Босс #

def residentofdarkness():
    global Hp
    global Coins
    global XP
    global LVL

    residentofdarknessLvl = r.randint(10, 20)
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
            if Hp > 0:
                print("Житель Тьмы атаковал и у тебя осталось", Hp, "жизней.")
            else:
                print("Житель Тьмы атаковал и у тебя осталось", 0, "жизней.")

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

# Босс #

def guardianofdustywalls():
    global Hp
    global Coins
    global XP
    global LVL

    guardianofdustywallsLvl = r.randint(20, 30)
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
            if Hp > 0:
                print("Хранитель пыльных стен атаковал и у тебя осталось", Hp, "жизней.")
            else:
                print("Хранитель пыльных стен атаковал и у тебя осталось", 0, "жизней.")

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

# Таверна #

def Tavern():
    global Hp
    global Damage
    global Coins
    global LVL
    global XP

    def buy(Price):
        global Coins
        if Coins >= Price:
            Coins -= Price
            return True
        print("У тебя маловато монет!")
        return False

    potions = ["Зелье здоровья", "Зелье силы"]
    potionPrice = LVL * 1.5
    PotionRarity = r.randint(1, 2)

    if PotionRarity == 1:
        potions = "Зелье здоровья"
    else:
        potions = "Зелье силы"

    weaponLvl = LVL + r.randint(1, 30)

    if weaponLvl > LVL:
        weaponLvl = LVL + r.randint(1, 3)


    weapons = ["Сломанный меч", "Ржавый топор", "Самодельный лук", "Булава", "Заточка", "Палка", "Кость Тролля", "Булыжник", "Копье", "Сюрикэн", "Кинжал", "Секира"]
    weaponRarities = ["Обычный", "Редкий", "Эпический", "Легендарный"]
    weaponRarity = r.randint(1, 4)
    weaponPrice = LVL * weaponLvl - LVL
    weapon = r.choice(weaponRarities) + " " + r.choice(weapons)

    if weaponRarity == 1:
        weaponRarities == "Обычный"
        weaponDamage = weaponLvl
    elif weaponRarity == 2:
        weaponRarities == "Редкий"
        weaponDamage = 2 * weaponLvl
    elif weaponRarity == 3:
        weaponRarities == "Эпический"
        weaponDamage = 3 * weaponLvl + LVL
    else:
        weaponRarities == "Легендарный"
        weaponDamage = 4 * weaponLvl + LVL

    while input("Вы подошли к таверне (зайти / уйти): ").lower() == "зайти":
        print("1)", weapon, "за", weaponPrice, "монет c уроном -", weaponDamage, ";")
        print("2)", potions, "за", potionPrice, "монет;")
        printParameters()

        Choice = input("Что хочешь приобрести?:")
        
        if Choice == "1":
            if buy(weaponPrice):
                Damage = weaponDamage
        if Choice == "2":
            if buy(potionPrice) and potions == "Зелье здоровья":
                Hp += 2 + (LVL/2)
            else:
                Damage += 2 + (LVL/2)
        printParameters()

# Монстры #

def Monsters():
    global Hp
    global Coins
    global XP
    global LVL

    monsterLvl = LVL + r.randint(1, 5)
    monsterHp = monsterLvl
    monsterDamage = monsterLvl * 2
    monsters = ["Орк", "Муха", "Дряхлый скелет", "Приведение", "Кентавр"]

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
            chance = r.randint(-5, 1)
            if chance >= -3:
                print("Тебе удалось потеряться среди стен лабиринта!")
                break
            else:
                print("Монстр оказался чересчур быстрым и догнал тебя...")
        else:
            continue

        if monsterHp > 0:
            Hp -= monsterDamage
            
        if Hp > 0:
            print("Монстр атаковал и у тебя осталось", Hp, "жизней.")
        else:
            print("Монстр атаковал и у тебя осталось", 0, "жизней.")

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

# Начало игры #

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

# Игровые ситуации #

def gameLoop():
    global Hp
    global Coins
    global Damage
    global LVL
    global XP

    situation = r.randint(0, 5)

    if situation == 0:
        Tavern()
    elif situation == 1:
        Monsters()
    elif situation == 3.5:
        raiders()
    elif LVL == 10:
        residentofdarkness()
    elif LVL == 30:
        guardianofdustywalls()
    elif LVL == 50:
        Minotaur()
    elif XP >= 10:
        XP -= 10
        LVL += 1
        Hp += 1
        Damage += 1
    else:
        input("Бродим во тьме...")

# Здоровье Урон Золото Уровень Опыт #

initGame(5, 5, 5, 1, 0)

while True:
    gameLoop()

    if Hp <= 0:
        if input("Твои кости станут частью этих стен. Хочешь начать сначала? (да): ").lower() == "да":
            initGame(5, 5, 5, 1, 0)
        else:
            break
