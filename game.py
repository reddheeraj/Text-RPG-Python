# -*- coding:utf-8 -*-


#Main Page   /DONE/
#Make a LORE /DONE/
#GH potions in shop /DONE/
#different attacks /DONE/
#mini quests/something to earn coins /TASKS GIVEN/ /3 DONE/ /0 LEFT/
#Monster Class - objects being different monsters /DONE/
#web /Not doing because don't know how to implement Save file/Load file in web mode
#uh locations system ig /Not Doing or maybe I shall/ /Acutally Did it/

#to do 
#potions bug (no. not changing after use) /DONE/


#changes compared to prev version: (3/7/22 to 4/7/22)
"""
1.made Weapons_in_Shop carry tuple (cost,attack)
2.made Monster Class, with objects being different species
3.made changes in entire project regarding the points 1 and 2.
4.Location system with new monsters per location added 
  > (character moves to new loc based on count value)
  > (location changes in victory() function)
  > (Location visual added as loc_image() function)
  > (We can now traverse to previously unlocked Locations via the loc_change() function)
5.linked Monsters with different locations
  > 3 monsters per location (for now)
"""


import sys
import os
import pickle
import random
import time 



Mini_Games_List = ["Impossible Tic Tac Toe", "Snake Game", "Conquer the Maze"]

Weapons_in_Shop = {"Steel Sword": (50,15), "Silver Sword":(100,30), "Blaze Sword": (200,50), "Z - Sword": (500,60), "God Killer": (700,80)} #Weapons shop category
Potions_in_Shop = {"Potion":5, "Greater Healing Potion":20} #health potions shop category

Locations = {0:"Void Cave",1:"Forest of Elves",2: "Heavenly Skies"}  #used to change locations in victory()


count = 0

new_loc_1 = False
new_loc_2 = False

class Player:  #player overlay
    def __init__(self, name):
        self.name = name
        self.MaxHealth = 100
        self.health = self.MaxHealth
        self.MaxMana = 20
        self.mana = self.MaxMana
        self.coins = 30
        self.potions = {"Potion": 3, "Greater Healing Potion": 0}
        self.base_attack = 10
        self.weapons = ["Fists", "Wooden Sword"]
        self.currentWeapon = ["Fists"]
        self.currLocation = "Void Cave"

    @property
    def attack(self):
        attack = self.base_attack
        if self.currentWeapon == "Fists":
            attack = self.base_attack
        if self.currentWeapon == "Wooden Sword":
            attack+= 5
        if self.currentWeapon == "Steel Sword":
            attack += Weapons_in_Shop["Steel Sword"][1]
        if self.currentWeapon == "Silver Sword":
            attack += Weapons_in_Shop["Silver Sword"][1]
        if self.currentWeapon == "Blaze Sword":
            attack += Weapons_in_Shop["Blaze Sword"][1]
        if self.currentWeapon == "Z - Sword":
            attack += Weapons_in_Shop["Z - Sword"][1]
        if self.currentWeapon == "God Killer":
            attack += Weapons_in_Shop["God Killer"][1]
        
        return attack




# class Ratman:
#     def __init__(self, name):
#         self.name = name
#         self.MaxHealth = 50
#         self.health = self.MaxHealth
#         self.attack = 5
#         self.Gaincoins = 10
#         #self.level = 1
# Rat = Ratman("Rat Henchman")

# class Vampire: 
#     def __init__(self, name):
#         self.name = name
#         self.MaxHealth = 70
#         self.health = self.MaxHealth
#         self.attack = 7
#         self.Gaincoins = 20
# Vamp = Vampire("Vampire Lazarus")

class Monster:
    def __init__(self,name,maxh,attack,gcoins,splatk):
        self.name = name
        self.MaxHealth = maxh
        self.health = self.MaxHealth
        self.attack = attack
        self.Gaincoins = gcoins
        self.splAttack = splatk


Rat = Monster("RatMan", 50, 5, 10, "Spear Throw")
Vamp = Monster("Vampire Lazarus", 70, 7, 20, "X - Slash")
BigBat = Monster("Big Bat", 100, 12, 25, "Super Sonic")

Archer_Elf = Monster("Archer Elf", 150, 20, 40, "Lightning Arrow")
War_Elf = Monster("Warrior Elf", 175, 30, 40, "Thunder Bagua")
Elf_Chief = Monster("Elf Chief Horith", 250, 50, 50, "Arcane Magic")

Giant_Eagle = Monster("Giant Eagle", 375, 70, 80, "Hurricane")
Wind_Dragon  = Monster("Wind Dragon", 500, 80, 85, "Air Cutter")
Sky_Monarch = Monster("Sky Monarch", 700, 100, 100, "Incinerate!!!")


lis = {"Void Cave":[Rat, Vamp, BigBat],"Forest of Elves":[Archer_Elf, War_Elf, Elf_Chief], "Heavenly Skies":[Giant_Eagle, Wind_Dragon ,Sky_Monarch]}
#lis is used to choose which monster is enemy 


def main():
    ####MAIN TITLE EDIT

    os.system('cls')
    
    print("\n\n\n")
    
    print("\t\t\t███████████████████████████████████████████████████████████████████████▀█")
    print("\t\t\t█─▄▄▄▄█─▄▄─█▄─▄███─▄▄─███▄─▄███▄─▄▄─█▄─█─▄█▄─▄▄─█▄─▄███▄─▄█▄─▀█▄─▄█─▄▄▄▄█")
    print("\t\t\t█▄▄▄▄─█─██─██─██▀█─██─████─██▀██─▄█▀██▄▀▄███─▄█▀██─██▀██─███─█▄▀─██─██▄─█")
    print("\t\t\t▀▄▄▄▄▄▀▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▀▀▀▄▄▄▄▄▀▄▄▄▄▄▀▀▀▄▀▀▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▀▄▄▄▀▀▄▄▀▄▄▄▄▄▀")

    time.sleep(3)
    
    os.system('cls')
    print("----------------------------")
    print("Welcome to Solo Leveling\n".upper())
    print("1.Start\n2.Load\n3.Exit")
    print("----------------------------")

    option = input(">>>> ")
    if option == "1":
        new_game()
    elif option == "2":
        if os.path.exists("savefile") == True:
            os.system('cls')
            with open('savefile', 'rb') as file: 
                global PlayerA
                PlayerA = pickle.load(file)
            print("Loading Save state...")
            option = input(' ')
            game1()
        else: 
            print("You have no savefile.\n")
            option = input(' ')
            main()
    elif option == "3":
        sys.exit()
    else:
        main()


def new_game():   #new game
    os.system('cls')
    print("------------------")
    print("Enter your name: ")
    option = input(">>>> ")
    global PlayerA
    PlayerA = Player(option)
    #game1()
    lore()

def lore():
    os.system('cls')
    lorestr1 = "A Long time ago, this World was very peaceful...\nBut One day, A Portal opened into our world, and Monsters came pouring out of it.\nA Small group of Humans suddenly started Awakening! They came together to Defeat the monsters and save Humanity."
    lorestr2 = "\n\nYou are one of the gifted Heroes who was Awakened with SuperHuman Powers and Strength! Now go kill some Monsters!"
    lorestr = lorestr1 + lorestr2
    #lorelist = lorestr.split()
    
    for l in lorestr:
        print(l, end = '')
        time.sleep(0.05)
    print("...")    
    time.sleep(3)
    game1()

def loc_image():
    if PlayerA.currLocation == Locations[0]:
        print("/================\\")
        print("|      /\\        |")
        print("|     /  \\       |")
        print("|  /\/     \     |")
        print("| /   ---   \/\  |")
        print("|/   |   |     \\ |")
        print("\================/")
    if PlayerA.currLocation == Locations[1]:
        print("/===================\\")
        print("|        _-_        |")
        print("|     /~~   ~~\     |")
        print("|  /~~         ~~\  |")
        print("| {  ~   ~~~   ~  } |")
        print("|  \   _-   -_   /  |")
        print("|    ~ \\   // ~     |")
        print("|       |   |       |")
        print("|       |   |       |")
        print("|     //     \\      |")
        print("\===================/")
    if PlayerA.currLocation == Locations[2]:
        print("/=========================\\")
        print("|   ,--.                  |")
        print("|       )                 |")
        print("|      _'-. _             |")
        print("|     (    ) ),--.        |")
        print("|                 )-.__   |")
        print("|______________________)  |")
        print("|                         |")
        print("\=========================/")

def game1():  #main menu for game
    os.system('cls')
    i = 1
    print("----------------------------------------")
    print("Name: %s" % PlayerA.name)
    print("Attack: %i 🗡️" % PlayerA.attack)
    print("coins: %i 🪙" % PlayerA.coins)
    print("Mana: %i 🔥 "% PlayerA.mana)
    print("Health: %i/%i ❤️" % (PlayerA.health, PlayerA.MaxHealth))
    print("Mana: %i/%i 💙" % (PlayerA.mana, PlayerA.MaxMana))

    for key,value in PlayerA.potions.items():
        print("\t" + str(i)+ ") " + key + ": 🧪 " + str(value))
        i += 1
    #print("Potions: %i ➕\nGreater Healing Potions: %i 🧪" % (PlayerA.potions[], PlayerA.potions[2]))

    #print("Potions: %i ➕" % PlayerA.potions) 
    print("Weapons: %s\n" % PlayerA.weapons)
    print("Current Weapon: %s" % PlayerA.currentWeapon)
    
    print("Location: " + PlayerA.currLocation)
    print("----------------------------------------")
    
    loc_image()

    print("----------------------------------------")
    print(" ")
    if new_loc_1 == True or new_loc_2 == True:
        print("1.Fight\n2.Shop\n3.Inventory\n4.Mini-Games\n5.Save\n6.Exit\n7.Move Locations\n")
    else:
        print("1.Fight\n2.Shop\n3.Inventory\n4.Mini-Games\n5.Save\n6.Exit\n")
    print("----------------------------------------")
    option = input(">>>> ")
    if option == "1":
        prepare_to_fight()
    elif option == "2":
        shop()
    elif option == "3":
        inventory()
    elif option == "4":
        minigame() 
    elif option == "5":
        os.system('cls')
        with open('savefile', 'wb') as file:
            pickle.dump(PlayerA, file)
            print("Save State Loaded")
            option = input(' ')
            game1()            
    elif option == "6":
        sys.exit()
    elif option == "7":
        loc_change()
    else:
        game1()

def loc_change():
    
    if new_loc_2 == True:
        print("Available locations are: ")
        time.sleep(1)
        print("0. Void Cave\n1. Forest of Elves\n2. Heavenly Skies")
        print("===============================")
        time.sleep(1)
        ch = int(input("Enter choice no.\n>>>> "))
        if PlayerA.currLocation == Locations[ch]:
            print("You are in [" + Locations[ch] + "] already!")
            time.sleep(2)
            game1()

        elif PlayerA.currLocation != Locations[ch]:
            print("You have moved to [" + Locations[ch] + "]")
            PlayerA.currLocation = Locations[ch]
            time.sleep(2)
            game1()

    elif new_loc_1 == True:
        print("Available locations are: ")
        time.sleep(1)
        print("0. Void Cave\n1. Forest of Elves")
        print("===============================")
        time.sleep(1)
        ch = int(input("Enter choice [0 or 1]\n>>>> "))
        if PlayerA.currLocation == Locations[ch]:
            print("You are in [" + Locations[ch] + "] already!")
            time.sleep(2)
            game1()

        elif PlayerA.currLocation != Locations[ch]:
            print("You have moved to [" + Locations[ch] + "]")
            PlayerA.currLocation = Locations[ch]
            time.sleep(2)
            game1()
    else:
        print("You have not unlocked any Locations yet!\nPlay the game and defeat more enemies!")
        time.sleep(2)
        game1()
            

def prepare_to_fight():
    global enemy
    
    no = [0,1,2]
    ch = random.choice(no)
    enemy = lis[PlayerA.currLocation][ch]
    
    # no = [1,2,3]
    # enemychoice = random.choice(no)
    # if enemychoice == 1:
    #     enemy = Rat
    # elif enemychoice == 2:
    #     enemy = Vamp
    # else:
    #     enemy = BigBat
    fight()

def fight():

    if PlayerA.mana < 0:
        PlayerA.mana = 0

    os.system('cls')

    

    print("    %s        vs        %s" % (PlayerA.name, enemy.name))
    print("---------------------------------------------------------")
    print("%s's Health: %i/%i  %s's Health: %i/%i" % (PlayerA.name, PlayerA.health, PlayerA.MaxHealth, enemy.name, enemy.health, enemy.MaxHealth))
    print("%s's Mana: %i/%i" % (PlayerA.name, PlayerA.mana, PlayerA.MaxMana))
    print("Potions: %s" % PlayerA.potions)
    print("---------------------------------------------------------")
    print("1.Attack\n2.Drink Potion\n3.Run\n")
    option = input(">>>> ")
    if option == "1":
        pre_attack()                                         
    if option == "2":
        potion()
    if option == "3":
        run()
        
    else:
        fight()
        
def pre_attack():
    print("-----------------------------------")
    print("1.Basic Attack\n2.Special Attack")
    print("-----------------------------------")
    attack_input = int(input(">>>> "))
    if attack_input == 1:
        attack()
    elif attack_input == 2:
        special_attack()
    else: 
        print("That move doesn't exist!!!")
        time.sleep(2)
        
        fight()    

    
def special_attack():
    # player SAttack
    SPA = random.randint(15, 25)  #special player attack damage
    
    if PlayerA.mana >= 10:
        PlayerA.mana -= 10
        enemy.health -= SPA
        print("You have used Fire Strike!")
        print("You have dealt %i damage" % SPA)
        time.sleep(2)

        if enemy.health <= 0:
            victory()
            
    else: 
        print("You don't have enough mana!")
        time.sleep(1)
        fight()
    

    # enemy SAttack   #so enemy can either attack or dodge the spcial attack
    SEA = 0
    #Enemy_SA = ""
    if PlayerA.currLocation == "Void Cave":
        SEA = random.randint(7,15)
       # Enemy_name = enemy.name
       # Enemy_SA = "Spear Throw"
    if PlayerA.currLocation == "Forest of Elves":
        SEA = random.randint(10,20)
       # Enemy_name = enemy.name
       # Enemy_SA = "X - Slash"
    if PlayerA.currLocation == "Heavenly Skies":
        SEA = random.randint(10,25)


    if SEA > 13:
        PlayerA.health -= SEA
        print("%s has used %s" % (enemy.name, enemy.splAttack))
        print("%s has dealt %i damage to you" % (enemy.name, SEA))
        time.sleep(2)

        if PlayerA.health <= 0:
            defeat()
        else:
            fight()

    else:
        EDamage = random.randint(int(enemy.attack/3), enemy.attack)     #if p/3, then enemy miss the atteck  
        if EDamage == int(enemy.attack/3):
            print("%s's Attack Missed!" % enemy.name)
            time.sleep(2)
        else: 
            PlayerA.health -= EDamage
            print("%s has dealt %i damage to you" % (enemy.name, EDamage))
            time.sleep(2)

        if PlayerA.health <= 0:
            defeat()

        else:                                       #check it later
            fight()

    #else:                
        #enemy.health += SPA
    #    print("Enemy dodged your attack!")
    #    time.sleep(2)


def attack():
    
    PDamage = random.randint(int(PlayerA.attack/3), PlayerA.attack) #if p/3, player miss the chance
    EDamage = random.randint(int(enemy.attack/3), enemy.attack)     #if p/3, then enemy miss  the atteck  
    
    if PDamage == int(PlayerA.attack/3):
        print("Your Attack Missed!")
        time.sleep(1)
    else: 
        enemy.health -= PDamage
        print("You have dealt %i damage" % PDamage)
        time.sleep(1)
    
    if enemy.health <= 0:
        victory()
    
    if EDamage == int(enemy.attack/3):
        print("%s's Attack Missed!" % enemy.name)
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
    potion1()
    fight()
    
def potion1():    #INCREASES HEALTH 
    i = 1
    print("------------------------------------")
    print("Which potion do you want?")
    print("[Type the name of the potion you want to drink.]")
    for key,value in PlayerA.potions.items():
        print(str(i) + ") " + key + ": " + str(value))
        i += 1
    print("------------------------------------")
    option = input(">>>> ")

    
    
    if option == "Potion":                       #potion = +30 health
        if PlayerA.potions[option] > 0:
            PlayerA.health += 30 
            PlayerA.potions["Potion"] -= 1
            if PlayerA.health > PlayerA.MaxHealth:
                PlayerA.health = PlayerA.MaxHealth
            print("You drank a Potion!\nPotions left: " + str(PlayerA.potions["Potion"]))
            time.sleep(2)
        else:
            print("You don't have any Potions!")
            time.sleep(2)
    elif option == "Greater Healing Potion":
            if PlayerA.potions[option] > 0:
                PlayerA.health += 80               #ghpotion increases 80 health   
                PlayerA.potions[option] -= 1
                if PlayerA.health > PlayerA.MaxHealth:
                    PlayerA.health = PlayerA.MaxHealth
                print("You drank a Greater Healing Potion!")
                time.sleep(2)
            else:
                print("You don't have any Greater Healing Potions!")
                time.sleep(2)
    else:
        print("That %s does not exist!" % option)
        time.sleep(2)
        #os.system('cls')



def run():                 # decrease coins if want to run, else fight
    if PlayerA.coins > 5:
          PlayerA.coins -=5
          print("You ran away \n")
          time.sleep(2)
          game1()
    else:
        print("You Don't have enough 🪙 to run away!")
        time.sleep(2)
        fight()

def victory():
    #os.system('cls')
    PlayerA.coins += enemy.Gaincoins
    enemy.health = enemy.MaxHealth            #resets enemy health
    print("You have defeated the enemy %s" % enemy.name)
    time.sleep(2)
    print("You have obtained %i 🪙  gold coins!" %enemy.Gaincoins)
    print("=================================")
    time.sleep(2)
    global count
    global new_loc_1
    global new_loc_2
    count = count + 1
    if count == 5:
        PlayerA.currLocation = Locations[1]
        PlayerA.MaxHealth += 150
        PlayerA.MaxMana += 20
        PlayerA.health = PlayerA.MaxHealth        #reset player health after location upgrade
        print("Congratulations! You have moved to a new Location [Forest of Elves]!")
        new_loc_1 = True
        time.sleep(3)
    if count == 15:
        PlayerA.currLocation = Locations[2]
        PlayerA.MaxHealth += 400
        PlayerA.MaxMana += 50
        PlayerA.health = PlayerA.MaxHealth        #reset player health after location upgrade
        print("Congratulations! You have moved to a new Location [Heavenly Skies]!")
        new_loc_2 = True
        time.sleep(3)
    PlayerA.mana = PlayerA.MaxMana            #resets player mana
    game1()



def defeat():
    #os.system('cls')
    PlayerA.coins -= 10
    print("YOU HAVE BEEN DEFEATED")
    time.sleep(2)
    PlayerA.health = PlayerA.MaxHealth     #resets player health
    PlayerA.mana = PlayerA.MaxMana         #resets player mana
    game1()
    

    
def inventory():
    os.system('cls')
    i = 1
    print("-----------------------------")
    print("Weapons: ")
    for weap in PlayerA.weapons:
        print(str(i) + ') ' + weap)
        i += 1
    print("-----------------------------")
    i = 1
    print("Potions: ")
    for key,value in PlayerA.potions.items():
        print(str(i) + ") " + key + ": " + str(value))
        i += 1
    #print("Potions: %i" % PlayerA.potions)
    #print("Greater Healing Potions: %i" % PlayerA.potions)
    print("-----------------------------")

    time.sleep(2)
    print('What do you want to do?\n')
    print("1.Choose Weapon\n2.Close Inventory\n")
    print("-----------------------------")
    option = input(">>>> ")
    if option == "1":
        equip()
    elif option == "2":
        game1()


def equip():
    os.system('cls')
    i = 1
    print("-----------------------------")
    print("Choose Weapon to equip: ")
    for weap in PlayerA.weapons:
        print(str(i) + ") " + weap)
        i += 1
    print("Type 'Back' to go back\nType Weapon Name to choose: ")
    print("-----------------------------")
    option = input(">>>> ")

    if option in PlayerA.currentWeapon:
        print("Already equipped %s" % option)
        time.sleep(2)
        equip()
    
    elif option == 'Back':
        game1()

    elif option in PlayerA.weapons:
        PlayerA.currentWeapon = option
        print("You have equipped %s" % PlayerA.currentWeapon)
        time.sleep(2)
        game1()
    else:
        print("That item %s does not exist in your inventory" % option)
        time.sleep(2)
        equip()


def shop():
    os.system('cls')

    print("-----------------------------")
    print("\nWelcome to shop!\nWhat would you like to buy?\n")
    print("1.Weapons\n2.Potions\n3.Back\n")
    print("-----------------------------")

    option = input(">>>> ")

    if option == "1":
        i = 1
        for key,value in Weapons_in_Shop.items():
            print(str(i) + ') ' + key + ': ' + str(Weapons_in_Shop[key][0]) + " 🪙\n  > Damage: " + str(Weapons_in_Shop[key][1]))
            i += 1
        print("Which weapon do you want to buy?\n[press 1 to get back to main menu]")
        time.sleep(2)
        option = input(">>>> ")
        
        if option == "1":
            game1()

        if option in Weapons_in_Shop:
            print("------------------------------")
            print("That will cost %i 🪙" % Weapons_in_Shop[option][0])
            time.sleep(2)
            if PlayerA.coins >= Weapons_in_Shop[option][0]:
                PlayerA.coins -= Weapons_in_Shop[option][0]
                PlayerA.weapons.append(option)
                print("------------------------------")
                print("You have bought %s!" % option)    
                time.sleep(2)
                shop()
            else:
                print("------------------------------")
                print ("You don't have enough 🪙 coins!".capitalize())
                time.sleep(2)
                shop()
        else:
            print("That weapon does not exist!")
            time.sleep(2)
            shop()



    elif option == "2":
        i = 1
        for key,value in Potions_in_Shop.items():
            print(str(i) + ') ' + key + ': ' + str(value) + " 🪙")
            i += 1

        print("which one you want?")
        print("--------------------------------------")

        option = input(">>>> ")   
        if option == "Potion":
            print("How many potions do you want to buy?\n")
            print("--------------------------------------")
            time.sleep(2)
            count = int(input(">>>> "))
            cost = Potions_in_Shop[option]*count
            if PlayerA.coins >= cost:
                PlayerA.coins -= cost
                PlayerA.potions[option] += count
                print("You have bought %i Potions!" % count)
                time.sleep(2)
                shop()
            else:
                print("You don't have enough 🪙!")
                time.sleep(2)
                shop()
        elif option == "Greater Healing Potion":
            print("How many Greater Healing Potions you want to buy? ")
            print("--------------------------------------")    
            count = int(input(">>>> "))
            cost = int(int(Potions_in_Shop[option])*int(count))
            if PlayerA.coins >= cost:
                PlayerA.coins -= cost
                PlayerA.potions[option] += int(count)
                print("You have bought %i GHP!" % count)
                time.sleep(2)
                shop()
            else:
                print("You don't have enough 🪙!")
                time.sleep(2)
                shop()
        else:
            print("That potion does not exist!")
            time.sleep(2)
            shop()
    
    elif option == "3":
        game1()
    else:
        print("That option does not exist. Try Again.")
        time.sleep(2)
        shop()

def minigame():
    os.system('cls')
    i = 1
    print("---------------------------------------------------")
    print("which game do you want to play?\nEnter 4 to exit")
    for x in Mini_Games_List:
        print(str(i) + ") " + x)
        i += 1
    print("---------------------------------------------------")
    option = int(input(">>>> "))
    if option == 1:
        TicTacToe()  #minigame with min max logic
    elif option == 2:
        snakegame()  #snake game
    elif option == 3:
        mazegame()  # maze game with monsters
    elif option == 4:
        game1()
    else: 
        print("That game does not exist!")
        time.sleep(2)
        minigame()

def TicTacToe():   
    os.system('cls')
    def intro():
        print("                It is impossible to win in this still you can try you best XD ")
        print("                       Enter board number in you turn to play your move           ")
        print("                     +_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+")
        time.sleep(5)
        os.system('cls')

    board = {1: ' ', 2: ' ', 3: ' ',
            4: ' ', 5: ' ', 6: ' ',
            7: ' ', 8: ' ', 9: ' '}
    pp = 'O'
    computer = 'X'
    #we implement minimax algo....
    #reference from https://levelup.gitconnected.com/mastering-tic-tac-toe-with-minimax-algorithm-3394d65fa88f
    #Mastering Tic-Tac-Toe with Minimax Algorithm in Python
    intro()
    def printBoard(board):
        os.system('cls')
        print(board[1] + " |" + board[2] + " |" + board[3])
        print("-+-+-+-+-")
        print(board[4] + " |" + board[5] + " |" + board[6])
        print("-+-+-+-+-")
        print(board[7] + " |" + board[8] + " |" + board[9])
        print("\n")
       

    def spaceIsFree(position):
        if board[position] == ' ':
            return True 
        return False 

    def insertLetter(letter, position):
        if spaceIsFree(position):
            board[position] = letter 
            printBoard(board)
            if checkDraw():
                print("Draw!")
                time.sleep(2)
                game1()
                
            if checkWin():
                if letter == 'X':
                    print("Bot wins!")
                    time.sleep(2)
                    game1()
                    
                else:
                    print("player wins!")
                    PlayerA.coins += 500
                    time.sleep(2)
                    game1()
            return 
        else:
            print("Invalid position")
            position = int(input("Please enter a new position: "))
            insertLetter(letter, position)
            return    

    def checkWin():
        if (board[1] == board[2] and board[1] == board[3] and board[1] != ' '):
            return True
        elif (board[4] == board[5] and board[4] == board[6] and board[4] != ' '):
            return True
        elif (board[7] == board[8] and board[7] == board[9] and board[7] != ' '):
            return True
        elif (board[1] == board[4] and board[1] == board[7] and board[1] != ' '):
            return True
        elif (board[2] == board[5] and board[2] == board[8] and board[2] != ' '):
            return True
        elif (board[3] == board[6] and board[3] == board[9] and board[3] != ' '):
            return True
        elif (board[1] == board[5] and board[1] == board[9] and board[1] != ' '):
            return True
        elif (board[7] == board[5] and board[7] == board[3] and board[7] != ' '):
            return True
        else:
            return False

    def checkWhichMarkWon(mark):
        if (board[1] == board[2] and board[1] == board[3] and board[1] == mark):
            return True
        elif (board[4] == board[5] and board[4] == board[6] and board[4] == mark):
            return True
        elif (board[7] == board[8] and board[7] == board[9] and board[7] == mark):
            return True
        elif (board[1] == board[4] and board[1] == board[7] and board[1] == mark):
            return True
        elif (board[2] == board[5] and board[2] == board[8] and board[2] == mark):
            return True
        elif (board[3] == board[6] and board[3] == board[9] and board[3] == mark):
            return True
        elif (board[1] == board[5] and board[1] == board[9] and board[1] == mark):
            return True
        elif (board[7] == board[5] and board[7] == board[3] and board[7] == mark):
            return True
        else:
            return False

    def checkDraw():
        for key in board.keys():
            if board[key] == ' ':
                return False 
        return True 

    def ppMove():
        position = int(input("Enter a position for 'O': "))
        insertLetter(pp, position)
        return 

    def compMove():
        bestScore = -800
        bestMove = 0
        for key in board.keys():
            if board[key] == ' ':
                board[key] = computer
                score = minimax(board, False)
                board[key] = ' '
                if score > bestScore:
                    bestScore = score 
                    bestMove = key
        insertLetter(computer, bestMove)
        return 
    def minimax(board, isMaximizing):
        if checkWhichMarkWon(computer):
            return 1 
        elif checkWhichMarkWon(pp):
            return -1 
        elif checkDraw():
            return 0
            
        if isMaximizing:
            bestScore = -800 
            for key in board.keys():
                if board[key] == ' ':
                    board[key] = computer 
                    score = minimax(board, False)
                    board[key] = ' '
                    if score > bestScore:
                        bestScore = score
            return bestScore 
        else:
            bestScore = 800 
            for key in board.keys():
                if board[key] == ' ':
                    board[key] = pp 
                    score = minimax(board, True)
                    board[key] = ' '
                    if score < bestScore:
                        bestScore = score 
            return bestScore

    def firstmover():
            printBoard(board)
            first = int(input("\n| 1 for first move\n| 2 for going second\n>>> "))
            if first == 1:
                while not checkWin():
                    ppMove()
                    time.sleep(1)
                    compMove()
            if first == 2:
                while not checkWin():
                    compMove()
                    time.sleep(1)
                    ppMove()
    firstmover()

        


def snakegame():  
    os.system('cls')

    import pygame
    import time
    import random

    snake_speed = 15
    score = 0
    x = 0

    window_x = 720
    window_y = 480

    
    black = pygame.Color(0, 0, 0)
    white = pygame.Color(255, 255, 255)
    red = pygame.Color(255, 0, 0)
    snake_color = pygame.Color(247, 138, 119)
    #blue = pygame.Color(0, 0, 255)

    pygame.init()

    pygame.display.set_caption('Snake Game')
    game_window = pygame.display.set_mode((window_x, window_y))
    fps = pygame.time.Clock()

    snake_position = [100, 50]
    snake_body = [[100, 50],
                [90, 50],
                [80, 50],
                [70, 50]]

    fruit_position = [random.randrange(1, (window_x//10)) * 10, random.randrange(1, (window_y//10)) * 10]
    fruit_spawn = True

    
    direction = 'RIGHT'
    change_to = direction

    def show_score(choice, color, font, size):

        score_font = pygame.font.SysFont(font, size)
        score_surface = score_font.render('Score : ' + str(score), True, color)
        score_rect = score_surface.get_rect()
        game_window.blit(score_surface, score_rect)

    def game_over():

        my_font = pygame.font.SysFont('freesansbold', 50)
        game_over_surface = my_font.render(
            'Your Score is : ' + str(score), True, red)

        game_over_rect = game_over_surface.get_rect()
        game_over_rect.midtop = (window_x/2, window_y/4)
        game_window.blit(game_over_surface, game_over_rect)

        pygame.display.flip()
        time.sleep(2)
        pygame.quit()
        
        print("\nPlayer earned " + str(x) + '🪙')
        PlayerA.coins += x

        time.sleep(5)
        minigame()


    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    change_to = 'UP'
                if event.key == pygame.K_DOWN:
                    change_to = 'DOWN'
                if event.key == pygame.K_LEFT:
                    change_to = 'LEFT'
                if event.key == pygame.K_RIGHT:
                    change_to = 'RIGHT'


        if change_to == 'UP' and direction != 'DOWN':
            direction = 'UP'
        if change_to == 'DOWN' and direction != 'UP':
            direction = 'DOWN'
        if change_to == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        if change_to == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'


        if direction == 'UP':
            snake_position[1] -= 10
        if direction == 'DOWN':
            snake_position[1] += 10
        if direction == 'LEFT':
            snake_position[0] -= 10
        if direction == 'RIGHT':
            snake_position[0] += 10


        snake_body.insert(0, list(snake_position))
        if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
            score += 10
            x += 2
            fruit_spawn = False
        else:
            snake_body.pop()
            
        if not fruit_spawn:
            fruit_position = [random.randrange(1, (window_x//10)) * 10,
                            random.randrange(1, (window_y//10)) * 10]
            
        fruit_spawn = True
        game_window.fill(black)
        
        for pos in snake_body:
            pygame.draw.rect(game_window, snake_color,
                            pygame.Rect(pos[0], pos[1], 10, 10))
        pygame.draw.rect(game_window, white, pygame.Rect(
            fruit_position[0], fruit_position[1], 10, 10))


        if snake_position[0] < 0 or snake_position[0] > window_x-10:
            game_over()
        if snake_position[1] < 0 or snake_position[1] > window_y-10:
            game_over()

        for block in snake_body[1:]:
            if snake_position[0] == block[0] and snake_position[1] == block[1]:
                game_over()

        show_score(1, white, 'times new roman', 20)

        pygame.display.update()
        fps.tick(snake_speed)


    

def mazegame():
    from random import randint
    os.system('cls')

    print("      .----------------.  .----------------.  .----------------.  .----------------.     ")
    print("     | .--------------. || .--------------. || .--------------. || .--------------. |         ")
    print("     | | ____    ____ | || |      __      | || |   ________   | || |  _________   | |")
    print("     | ||_   \  /   _|| || |     /  \     | || |  |  __   _|  | || | |_   ___  |  | |")
    print("     | |  |   \/   |  | || |    / /\ \    | || |  |_/  / /    | || |   | |_  \_|  | |")
    print("     | |  | |\  /| |  | || |   / ____ \   | || |     .'.' _   | || |   |  _|  _   | |")
    print("     | | _| |_\/_| |_ | || | _/ /    \ \_ | || |   _/ /__/ |  | || |  _| |___/ |  | |")
    print("     | ||_____||_____|| || ||____|  |____|| || |  |________|  | || | |_________|  | |")
    print("     | |              | || |              | || |              | || |              | |")
    print("     | '--------------' || '--------------' || '--------------' || '--------------' |")
    print("     ' ----------------'  '----------------'  '----------------'  '----------------' ")

    time.sleep(2)
    os.system('cls')
    print("        You get trapped in a maze there are monsters at randon locations! you need to         ")          
    print("           find a way to go to the exit of the maze without encountering the enemy.            ")
    print("                      100 gold coins are waitng for you at the exit.                        ")
    time.sleep(8)
    os.system('cls')
    charX = 0
    charY = 0
    mazeX = 5
    mazeY = 5
    enemy_number = 6
    X = int(input("Enter the size of the row( M X M) should be greater then 5):>> "))
    if X < 5:
        X = 5
    mazeX = X
    mazeY = X
    enemy_number = int(0.25 * (mazeX * mazeY))
    board = [["| |" for a in range(mazeX)] for b in range(mazeY)]
    currentposition = "|&|" 
    board[charX][charY] = currentposition
    ls = []
    for m in range(enemy_number):
        enemyX = randint(1,5)
        enemyY = randint(1,5)
        ele = (enemyX,enemyY)
        ls.append(ele)

    while True:
        def check():
            for i in range(4):

                    if ls[i][0] == charX and ls[i][1] == charY:

                        print("YOU WERE ATTACKED BY THE MONSTER!\nGAME OVER")
                        board[charX][charY] = "|X|"
                        time.sleep(2)
                        game1()
                    if charX == mazeX-1 and charY == mazeY-1:

                        print("You WON the game")
                        print("You get 100 gold coins!")
                        PlayerA.coins += 100
                        time.sleep(2)
                        game1()


        #print(ls)
        for i in board:
            print("----"*mazeX)
            print(" ".join(i))
            print("----"*mazeX)
        print("    "*mazeX + "-🥇-")

        print("Instructions :")
        print("Up: W  ||  Down: S  || Left: A  || Right: D")

        option = input("Enter you option:>>> ")

        if option == "W":
            os.system('cls')
            board[charX][charY] = "| |"
            charX -= 1
            if mazeX > charX:
                board[charX][charY] = "|&|"
            else:
                print("You hit the wall")
                charX = 0
                charY = 0
                board[charX][charY] = "|&|"
            check()

        elif option == "S":
            os.system('cls')
            board[charX][charY] = "| |"
            charX += 1
            if mazeX > charX:
                board[charX][charY] = "|&|"
            else:
                print("You hit the wall")
                time.sleep(1)
                charX = 0
                charY = 0
                board[charX][charY] = "|&|"
            check()
        elif option == "A":
            os.system('cls')
            board[charX][charY] = "| |"
            charY -= 1
            if mazeY > charY:
                board[charX][charY] = "|&|"
            else:
                print("You hit the wall")
                charX = 0
                charY = 0
                board[charX][charY] = "|&|"
            check()
        elif option == "D":
            os.system('cls')
            board[charX][charY] = "| |"
            charY += 1
            if mazeY > charY:
                board[charX][charY] = "|&|"
            else:
                print("You hit the wall")
                charX = 0
                charY = 0
                board[charX][charY] = "|&|"
            check()



main()
