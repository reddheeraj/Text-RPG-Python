import sys
import os
import pickle
import random
import time

Weapons_in_Shop = {"Steel Sword": 40, "Silver Sword":80} #shop

class Player:  #player overlay
    def __init__(self, name):
        self.name = name
        self.MaxHealth = 100
        self.health = self.MaxHealth
        self.coins = 20
        self.potions = 3
        self.base_attack = 10
        self.weapons = ["Wooden Sword"]
        self.currentWeapon = ["Wooden Sword"]

    @property
    def attack(self):
        attack = self.base_attack
        if self.currentWeapon == "Wooden Sword":
            attack+= 5
        if self.currentWeapon == "Steel Sword":
            attack += 15
        if self.currentWeapon == "Silver Sword":
            attack += 30
        
        return attack

class Goblin:
    def __init__(self, name):
        self.name = name
        self.MaxHealth = 50
        self.health = self.MaxHealth
        self.attack = 5
        self.GainCoins = 10
        #self.level = 1
Goblin1 = Goblin("Goblin 1")

class Wolf: 
    def __init__(self, name):
        self.name = name
        self.MaxHealth = 70
        self.health = self.MaxHealth
        self.attack = 7
        self.GainCoins = 20
Wolf1 = Wolf("Wolf 1")

def main():
    os.system('cls')
    print("Welcome to Solo Leveling\n")
    print("1.Start\n2.Load\n3.Exit")

    option = input(">>>> ")
    if option == "1":
        start()
    elif option == "2":
        if os.path.exists("savefile") == True:
            os.system('cls')
            with open('savefile', 'rb') as file: 
                global PlayerA
                PlayerA = pickle.load(file)
            print("Loading Save state...")
            option = input(' ')
            start1()
        else: 
            print("You have no savefile.\n")
            option = input(' ')
            main()
    elif option == "3":
        sys.exit()
    else:
        main()


def start():   #new game
    os.system('cls')
    print("Enter your name: ")
    option = input(">>>> ")
    global PlayerA
    PlayerA = Player(option)
    start1()

def start1():  #main menu for game
    os.system('cls')
    print("Name: %s" % PlayerA.name)
    print("Attack: %i" % PlayerA.attack)
    print("Coins: %i" % PlayerA.coins)
    print("Health: %i/%i" % (PlayerA.health, PlayerA.MaxHealth))
    print("Potions: %i" % PlayerA.potions)
    print("Weapons: %s\n" % PlayerA.weapons)
    print("Current Weapon: %s\n" % PlayerA.currentWeapon)

    print("1.Fight\n2.Shop\n3.Inventory\n4.Save\n5.Exit\n")
    option = input(">>>> ")
    if option == "1":
        prepare_to_fight()
    elif option == "2":
        shop()
    elif option == "3":
        inventory()
    elif option == "4":
        os.system('cls')
        with open('savefile', 'wb') as file:
            pickle.dump(PlayerA, file)
            print("Save State Loaded")
            option = input(' ')
            start1()            
    elif option == "5":
        sys.exit()
    else:
        start1()

def prepare_to_fight():
    global enemy
    enemychoice = random.randint(1,2)
    if enemychoice == 1:
        enemy = Goblin1
    else:
        enemy = Wolf1
    fight()

def fight():
    os.system('cls')
    print("    %s        vs        %s" % (PlayerA.name, enemy.name))
    print("%s's Health: %i/%i  %s's Health: %i/%i" % (PlayerA.name, PlayerA.health, PlayerA.MaxHealth, enemy.name, enemy.health, enemy.MaxHealth))
    print("Potions: %i" % PlayerA.potions)
    print("1.Attack\n2.Drink Potion\n3.Run\n")
    option = input(">>>>")
    if option == "1":
        attack()                                          
    if option == "2":
        potion()
    if option == "3":
        run()
        
    else:
        fight()

def attack():
    
    PDamage = random.randint(int(PlayerA.attack/3), PlayerA.attack) #if p/3, player miss the chance
    EDamage = random.randint(int(enemy.attack/3), enemy.attack)     #if p/3, then enemy miss  the atteck  
    
    if PDamage == PlayerA.attack/3:
        print("Attack Missed!")
        time.sleep(2)
    else: 
        enemy.health -= PDamage
        print("You have dealt %i damage" % PDamage)
        time.sleep(2)
    
    if enemy.health <= 0:
        victory()
    
    if EDamage == enemy.attack/3:
        print("Attack Missed!")
        time.sleep(2)
    else: 
        PlayerA.health -= EDamage
        print("%s has dealt %i damage to you" % (enemy.name, EDamage))
        time.sleep(2)
    
    if PlayerA.health <= 0:
        defeat()

    else:                                       #check it later
        fight()
   
    
def potion():
    if PlayerA.potions > 0:
        PlayerA.health += 30               #potion increases 30 health   
        if PlayerA.health > PlayerA.MaxHealth:
            PlayerA.health = PlayerA.MaxHealth
        PlayerA.potions -= 1
        print("You drank a potion!")
        time.sleep(2)
    else:
        print("You don't have potions!")
        time.sleep(2)
    fight()

def run():                 # decrease coins if want to run, else fight
    os.system('cls')
    if PlayerA.coins > 5:
          PlayerA.coins -=5
          print("You ran away \n")
          time.sleep(2)
          start1()
    else:
        print("You Don't have enough coins to run away!")
        time.sleep(2)
        fight()

def victory():
    #os.system('cls')
    PlayerA.coins += enemy.GainCoins
    enemy.health = enemy.MaxHealth
    print("You have defeated the enemy %s" % enemy.name)
    time.sleep(2)
    print("You have obtained %i gold coins!" %enemy.GainCoins)
    time.sleep(2)
    start1()



def defeat():
    #os.system('cls')
    PlayerA.coins -= 10
    print("YOU HAVE BEEN DEFEATED")
    time.sleep(2)
    PlayerA.health = PlayerA.MaxHealth
    start1()
    

    
def inventory():
    os.system('cls')
    print("Weapons: ")
    for weap in PlayerA.weapons:
        print(weap)
    print("\n")
    print("Potions: %i" % PlayerA.potions)
    time.sleep(2)
    print('What do you want to do?')
    time.sleep(2)
    print("1. Choose Weapon\n2.Close Inventory\n")
    time.sleep(2)
    option = input(">>>>")
    if option == "1":
        equip()
    elif option == "2":
        start1()


def equip():
    os.system('cls')
    print("Choose Weapon to equip: ")
    for weap in PlayerA.weapons:
        print(weap)
    print("Type 'Back' to go back")
    option = input(">>>> ")

    if option == PlayerA.currentWeapon:
        print("Already equipped")
        time.sleep(2)
        equip()
    
    elif option == 'Back':
        start1()

    elif option in PlayerA.weapons:
        PlayerA.currentWeapon = option
        print("You have equipped %s" % PlayerA.currentWeapon)
        time.sleep(2)
        start1()
    else:
        print("That item %s does not exist in your inventory" % option)
        time.sleep(2)
        equip()


def shop():
    os.system('cls')
    print("Welcome to shop!\nWhat would you like to buy?\n")
    print("1.Weapons\n2.Potions\n3.Back\n")

    option = input(">>>> ")

    if option == "1":
        for weap in Weapons_in_Shop:
            print(weap)
        print("Which weapon do you want to buy?")
        time.sleep(2)
        option = input(">>>> ")
        
        if option in Weapons_in_Shop:
            print("That will cost %i", Weapons_in_Shop[option])
            time.sleep(2)
            if PlayerA.coins >= Weapons_in_Shop[option]:
                PlayerA.coins -= Weapons_in_Shop[option]
                PlayerA.weapons.append(option)
                print("You have bought %s" % option)    
                time.sleep(2)
                shop()



    if option == "2":
        print("How many potions do you want to buy?\n")
        time.sleep(2)
        option = int(input(">>>> "))
        cost = 5*option
        if cost >= PlayerA.coins:
            PlayerA.coins -= cost
            PlayerA.potions += option
        else:
            print("You don't have enough coins!")
            time.sleep(2)
        
        shop()
    
    if option == "3":
        start1()

main()