from character import character

from enemy import enemy

import time

import random

print("Dragon Quest")
time.sleep(1)
print("loading...")
time.sleep(1)
print("loading...")
time.sleep(1)
print("game ready")

input("press enter to start:")

print("1. start the game")
print("2. exit the game")

choose = input("choose 1 or 2:")
if choose == "1":
    print("game starting")
if choose == "2":
    print("thanks for playing")
    exit()


c1 = character("assassin",80,8,16,20) 
c2 = character("warrior",100,6,12,15)
c3 = character("mage",85,7,14,17)

e1 = enemy("gobln",40,4,10)
e2 = enemy("goblin_Hard",50,6,12)

time.sleep(4)

print("choose your character")

print("1. assassin")
print("2. warrior")
print("3. mage")

time.sleep(1)

choice = input("choose 1,2 or 3:")

if choice == "1":
    player = c1
    print("you choose",player.name, "HP:", player.HP, "low HP but hits hardest")
    print("normal attack:",player.normal_attack)

elif choice == "2":
    player = c2
    print("you choose",player.name,"HP:",player.HP,"tank,safe choice")
    print("normal attack:",player.normal_attack)

elif choice == "3":
    player = c3
    print("you choose",player.name,"HP:",player.HP,"middle ground")
    print("normal attack:",player.normal_attack)

time.sleep(3)
print("Goblin appears")

while player.is_alive() > 0 and e1.is_alive() > 0:
    
    if player.HP < 0 and e1.HP < 0 :
        break
    
    print("your time to select")
    time.sleep(1)
    print("1. normal_attack")
    print("2. hard_attack")
    print("3. main_power")
    print("4. heal")
    time.sleep(1)
    select = input("choose 1,2,3 or 4:")
    
    if select == "1":
        e1.take_damage(player.normal_attack)
        print("you hits goblin ",player.normal_attack,"damage")

    elif select == "2":
        chance = random.randint(1,10)
        if chance > 3:
            e1.take_damage(player.hard_attack)
            print("you hits goblin ",player.hard_attack,"damage")
        else :
            print("oops attack missed")
        
    elif select == "3":
        chance = random.randint(1,10)
        if chance > 6:
            e1.take_damage(player.main_power)
            print("you hits goblin ",player.main_power,"damage")
        else :
            print("oops target missec")

    elif select == "4":
        player.HP += 8
        print("your total HP becomes:",player.HP)

    
    print("goblin attacks")
    attack_choice = random.choice(["normal","hard"])
    if attack_choice == "normal":
        player.HP -= e1.normal_attack
        print("goblin hits you with damage:",e1.normal_attack)

    elif attack_choice == "hard":
        player.HP -= e1.hard_attack 
        print("goblin hits you with damage:",e1.hard_attack)

    else :
        print("user died")

    time.sleep(3)


    

       












