from character import character

from enemy import enemy

import time

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

choose = input("choose 1 or 2")
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

print("1.",c1)
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













