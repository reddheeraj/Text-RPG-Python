# -*- coding:utf-8 -*-


#Main Page   /DONE/
#Make a LORE /DONE/
#GH potions in shop /DONE/
#different attacks /DONE/
#mini quests/something to earn coins /TASKS GIVEN/ /2 DONE/ /1 LEFT/
#Monster Class - objects being different monsters /DONE/
#web /Not doing because don't know how to implement Save file/Load file in web mode
#uh locations system ig /Not Doing or maybe I shall/ /Acutally Did it/

#to do
#potions bug (no. not changing after use)


#changes compared to prev version:
"""
1.made Weapons_in_Shop carry tuple (cost,attack)
2.made Monster Class, with objects being different species
3.made changes in entire project regarding the points 1 and 2.
4.Location system with new monsters per location added 
  > (character moves to new loc based on count value, so far cannot come back to prev loc)
  > (location changes in victory() function)
5.linked Monsters with different locations
  > 3 monsters per location (for now)
"""


import sys
import os
import pickle
import random
import time 



Mini_Games_List = ["Coin Flip", "Bhargav", "Maze-Jatin"]

Weapons_in_Shop = {"Steel Sword": (50,15), "Silver Sword":(100,30), "Blaze Sword": (200,50), "Z - Sword": (500,60), "God Killer": (700,80)} #Weapons shop category
Potions_in_Shop = {"Potion":5, "Greater Healing Potion":20} #health potions shop category

Locations = {0:"Void Cave",1:"Forest of Elves",2: "Heavenly Skies"}


count = 0

class Player:  #player overlay
    def __init__(self, name):
        self.name = name
        self.MaxHealth = 100
        self.health = self.MaxHealth
        self.MaxMana = 20
        self.mana = self.MaxMana
        self.coins = 200
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
        
        return attack




# class Ratman:
#     def __init__(self, name):
#         self.name = name
#         self.MaxHealth = 50
#         self.health = self.MaxHealth
#         self.attack = 5
#         self.GainCoins = 10
#         #self.level = 1
# Rat = Ratman("Rat Henchman")

# class Vampire: 
#     def __init__(self, name):
#         self.name = name
#         self.MaxHealth = 70
#         self.health = self.MaxHealth
#         self.attack = 7
#         self.GainCoins = 20
# Vamp = Vampire("Vampire Lazarus")

class Monster:
    def __init__(self,name,maxh,attack,gcoins,splatk):
        self.name = name
        self.MaxHealth = maxh
        self.health = self.MaxHealth
        self.attack = attack
        self.GainCoins = gcoins
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
    game1()
    #lore()

def lore():
    os.system('cls')
    lorestr1 = "A Long time ago, this World was very peaceful...\nBut One day, A Portal opened into our world, and Monsters came pouring out of it.\nA Small group of Humans suddenly started Awakening! They came together to Defeat the monsters and save Humanity."
    lorestr2 = "\n\nYou are one of the gifted Heroes who was Awakened with SuperHuman Powers and Strength! Now go kill some Monsters!"
    lorestr = lorestr1 + lorestr2
    #lorelist = lorestr.split()
    
    for l in lorestr:
        print(l, end = '')
        time.sleep(0.05)
    time.sleep(3)
    game1()

def game1():  #main menu for game
    os.system('cls')
    i = 1
    print("----------------------------------------")
    print("Name: %s" % PlayerA.name)
    print("Attack: %i 🗡️" % PlayerA.attack)
    print("Coins: %i 🪙" % PlayerA.coins)
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
    print(" ")
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
    else:
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
    print("-------------------------------------")
    print("%s's Health: %i/%i  %s's Health: %i/%i" % (PlayerA.name, PlayerA.health, PlayerA.MaxHealth, enemy.name, enemy.health, enemy.MaxHealth))
    print("%s's Mana: %i/%i" % (PlayerA.name, PlayerA.mana, PlayerA.MaxMana))
    print("Potions: %s" % PlayerA.potions)
    print("-------------------------------------")
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

    
    
    if option == "Potion":                       #potion = +20 health
        if PlayerA.potions[option] > 0:
            PlayerA.health += 30 
            if PlayerA.health > PlayerA.MaxHealth:
                PlayerA.health = PlayerA.MaxHealth
                PlayerA.potions["Potion"] -= 1
                print("You drank a Potion!\nPotions left: " + str(PlayerA.potions["Potion"]))
                time.sleep(2)
        else:
            print("You don't have any Potions!")
            time.sleep(2)
    elif option == "Greater Healing Potion":
            if PlayerA.potions[option] > 0:
                PlayerA.health += 80               #ghpotion increases 50 health   
                if PlayerA.health > PlayerA.MaxHealth:
                    PlayerA.health = PlayerA.MaxHealth
                    PlayerA.potions[option] -= 1
                    print("You drank a Greater Healing Potion!")
                    time.sleep(2)
            else:
                print("You don't have any Greater Healing Potions!")
                time.sleep(2)
    else:
        print("That %s does not exist!" % option)
        #os.system('cls')
        potion1()


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
    PlayerA.coins += enemy.GainCoins
    enemy.health = enemy.MaxHealth            #resets enemy health
    PlayerA.mana = PlayerA.MaxMana            #resets player mana
    print("You have defeated the enemy %s" % enemy.name)
    time.sleep(2)
    print("You have obtained %i 🪙  gold coins!" %enemy.GainCoins)
    time.sleep(2)
    print("=================================")
    global count
    count = count + 1
    if count == 2:
        PlayerA.currLocation = Locations[1]
        PlayerA.MaxHealth += 200
        print("Congratulations! You have moved to a new Location [Forest of Elves]!")
        time.sleep(3)
    if count == 4:
        PlayerA.currLocation = Locations[2]
        PlayerA.MaxHealth += 500
        print("Congratulations! You have moved to a new Location [Heavenly Skies]!")
        time.sleep(3)
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
                print ("You don't have enough 🪙 Coins!".capitalize())
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
            print("THat potion does not exist!")
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
        coinflip()  #change mini game into a more fun version
    elif option == 2:
        bhargav()  #add some insane logic minigame
    elif option == 3:
        jatin()
    elif option == 4:
        game1()
    else: 
        print("That game does not exist!")
        time.sleep(2)
        minigame()

def coinflip():   
    os.system('cls')
    print("------------------------------------------------------------------------")
    cf = "Welcome to COIN FLIP!\nBet an Amount and guess HEADS or TAILS.\nIf you guess the flip correctly, you win your bet and coins!\nIf you do not guess correctly, you lose your bet and coins.\n"
    #for c in cf:
    #    print(c, end = "")
    #    time.sleep(0.02)
    #time.sleep(2)
    print("------------------------------------------------------------------------\n")
    ####

    cfchoice = random.choice(["Heads", "Tails"])
    bet = 0
    
    print("Enter BET Amount: ")
    bet = int(input(">>>> "))

    if PlayerA.coins >= bet:
        print("Enter Guess: [HEADS(h) or TAILS(t)]")
        guess = input(">>>> ")

        if guess == "h":
            guess = "Heads"
        elif guess == "t":
            guess = "Tails"
        
        
        if guess == cfchoice:
            print("You have Guessed CORRECTLY!!!!!\nYou have Won %i 🪙" % bet)
            PlayerA.coins += bet
            time.sleep(3)
            game1()
        else:
            print("You have guessed INCORRECTLY. You lost %i 🪙" % bet)
            PlayerA.coins -= bet
            time.sleep(3)
            game1()
    else:
        print("You do not have Enough 🪙 coins!!!")
        time.sleep(4)
        minigame()
        


def bhargav():  #not finished
    os.system('cls')
    

def jatin():
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
    print("        You get traped in a maze there are monster at randon location you need to         ")          
    print("         find a way to go to the exit of the maze without encount the enemy            ")
    print("                  10 gold coins are waitng for you at the exit gate                        ")
    time.sleep(8)
    os.system('cls')
    charX = 0
    charY = 0
    mazeX = 5
    mazeY = 5
    enemy_number = 6
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
                        print("You get 10 gold coins!")
                        PlayerA.coins += 10
                        time.sleep(2)
                        game1()


        #print(ls)
        for i in board:
            print("--- --- --- --- ---")
            print(" ".join(i))
            print("--- --- --- --- ---")
        print("                   -🥇-")

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
