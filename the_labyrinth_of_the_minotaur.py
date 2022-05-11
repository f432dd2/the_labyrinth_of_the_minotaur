import random as r

Hp = 0
Coins = 0
Damage = 0

def printParameters():
    print("У тебя {0} жизней, {1} урона и {2} монет.".format(Hp, Damage, Coins))

def printHp():
    print("У тебя", Hp, "жизней.")

def printCoins():
    print("У тебя", Coins, "монет.")

def printDamage():
    print("У тебя", Damage, "урона.")

def Taverna():
    global Hp
    global Damage
    global Coins

    def buy(Price):
        global Coins
        if Coins >= Price:
            Coins -= Price
            printCoins()
            return True
        print("У тебя маловато монет!")
        return False

    weaponLvl = r.randint(1, 3)
    weaponDmg = r.randint(1, 5) * weaponLvl
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
                Damage = weaponDmg
                printDamage()
        else:
            print("Ты мне зубы не заговаривай. Либо покупай, либо проваливай!")

def meetMonster():
    global Hp
    global Coins

    monsterLvl = r.randint(1, 5)
    monsterHp = monsterLvl
    monsterDmg = monsterLvl * 2 - 1
    monsters = ["Grock", "Clop", "Cholop", "Madrock", "Lilbitch"]

    monster = r.choice(monsters)

    print("Ты набрел на монстра - {0}, у него {1} уровень, {2} жизней и {3} урона.".format(monster, monsterLvl, monsterHp, monsterDmg))
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
            Hp -= monsterDmg
            print("Монстр атаковал и у тебя осталось", Hp, "жизней.")

        if Hp <= 0:
            break
    else:
        loot = r.randint(0, 2) + monsterLvl
        Coins += loot
        print("Тебе удалось одолеть монстра, за что ты получил", loot, "монет.")
        printCoins()

def initGame(initHp, initCoins, initDamage):
    global Hp
    global Coins
    global Damage

    Hp = initHp
    Coins = initCoins
    Damage = initDamage

    print("Ворота закрываются за тобой и теперь ты вынужден гнить в этих лабиринтах до конца своих дней.")
    printParameters()

def gameLoop():
    situation = r.randint(0, 3)

    if situation == 0:
        Taverna()
    elif situation == 1:
        meetMonster()
    else:
        input("Бродим во тьме...")

initGame(5, 5, 5)

while True:
    gameLoop()

    if Hp <= 0:
        if input("Твои кости станут частью этих стен. Хочешь начать сначала?: ").lower() == "да":
            initGame(5, 5, 5)
        else:
            break
