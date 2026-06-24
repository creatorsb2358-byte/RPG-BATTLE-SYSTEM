from character import character

from enemy import enemy

import time

import random

def restart_game():
    
    c1 = character("assassin",70,8,16,20) 
    c2 = character("warrior",85,6,12,15)
    c3 = character("mage",75,7,14,17)

    e1 = enemy("gobln_easy",50,6,10)    
    e2 = enemy("goblin_Hard",65,7,14)

    time.sleep(4)
    print("")
    print("choose your character")
    print("")

    print("1. assassin")
    print("2. warrior")
    print("3. mage")

    time.sleep(1)
    print("")

    choice = input("choose 1,2 or 3:")

    if choice == "1":
        player = c1
        print("you choose",player.name, "HP:", player.HP, "::low HP but hits hardest")
        time.sleep(1)
        print("normal attack:",player.normal_attack)
        time.sleep(1)
        print("hard attack:",player.hard_attack)
        time.sleep(1)
        print("main power:",player.main_power)
    

    elif choice == "2":
        player = c2
        print("you choose",player.name,"HP:",player.HP,"::tank,safe choice")
        time.sleep(1)
        print("normal attack:",player.normal_attack)
        time.sleep(1)
        print("hard attack:",player.hard_attack)
        time.sleep(1)
        print("main power:",player.main_power)

    elif choice == "3":
        player = c3
        print("you choose",player.name,"HP:",player.HP,"::middle ground")
        time.sleep(1)
        print("normal attack:",player.normal_attack)
        time.sleep(1)
        print("hard attack:",player.hard_attack)
        time.sleep(1)
        print("main power:",player.main_power)


    time.sleep(6)
    print("")
    print("G O B L I N   A P P E A R S")
    print("")

    while player.is_alive() > 0 and e1.is_alive() > 0:

        print("your health remaining",player.HP)
        time.sleep(1)
        print("enemy health remaining",e1.HP)

        print("")
        print("your time to choose")
        time.sleep(1)
        print("1. normal_attack")  
        print("2. hard_attack")
        print("3. main_power")
        print("4. heal")
        print("")

        select = input("choose 1,2,3 or 4:")

        print("")
    
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
                print("oops target missed")

        elif select == "4":
            player.HP += 4
            print("your total HP becomes:",player.HP)

        time.sleep(1)

        print("")
        print("your health remaining",player.HP)
        time.sleep(1)
        print("enemy health remaining",e1.HP)
    
        if player.HP <= 0  :
            print("you lose")
            continue
            
        elif e1.HP <= 0 :
            print("you won")
            continue
            

        time.sleep(1)
        print("")
        print("")
        print("G O B L I N   A T T A C K S")
        attack_choice = random.choice(["normal","hard"])
        if attack_choice == "normal":
            player.HP -= e1.normal_attack
            print("goblin hits you with damage:",e1.normal_attack)

        elif attack_choice == "hard":
            player.HP -= e1.hard_attack 
            print("goblin hits you with damage:",e1.hard_attack)

        time.sleep(1)
        print("")

        if player.HP <= 0  :
            print("Y O U   L O S E")
            print("1. retry")
            print("2. exit")
            choice = ("choose 1 or 2")
            if choice == "1":
                restart_game()
            elif choice == "2":
                exit()
            
            elif e1.HP <= 0 :
                print("Y O U   W O N")
            

        time.sleep(1)

    time.sleep(3)
    print("")      
    if player.is_alive():
        print("N E W   E N E M Y   U P C O M M I N G  !!!")

    time.sleep(1)
    print("prepare yourself again")
    player.HP += 20
    print("you get 20 HP now lets goo")

    while player.is_alive() > 0 and e2.is_alive() > 0:

        print("your health remaining",player.HP)
        time.sleep(1)
        print("enemy health remaining",e2.HP)

        print("")
        print("your time to choose")
        time.sleep(1)
        print("1. normal_attack")  
        print("2. hard_attack")
        print("3. main_power")
        print("4. heal")
        print("")

        select = input("choose 1,2,3 or 4:")

        print("")
        
        if select == "1":
            e2.take_damage(player.normal_attack)
            print("you hits goblin ",player.normal_attack,"damage")

        elif select == "2":
            chance = random.randint(1,10)
            if chance > 3:
                e2.take_damage(player.hard_attack)
                print("you hits goblin ",player.hard_attack,"damage")
            else :
                print("oops attack missed")
            
        elif select == "3":
            chance = random.randint(1,10)
            if chance > 6:
                e2.take_damage(player.main_power)
                print("you hits goblin ",player.main_power,"damage")
            else :
                print("oops target missed")

        elif select == "4":
            player.HP += 4
            print("your total HP becomes:",player.HP)

        time.sleep(1)

        print("")
        print("your health remaining",player.HP)
        time.sleep(1)
        print("enemy health remaining",e2.HP)
    
        if player.HP <= 0  :
            print("you lose")
            print("1. retry")
            print("2. exit")
            choice = ("choose 1 or 2")
            if choice == "1":
                restart_game()
            elif choice == "2":
                exit()
            continue
            
        elif e2.HP <= 0 :
            print("you won")
            continue
            

        time.sleep(1)
        print("")
        print("")
        print("G O B L I N   A T T A C K S")
        attack_choice = random.choice(["normal","hard"])
        if attack_choice == "normal":
            player.HP -= e2.normal_attack
            print("goblin hits you with damage:",e2.normal_attack)

        elif attack_choice == "hard":
            player.HP -= e2.hard_attack 
            print("goblin hits you with damage:",e2.hard_attack)

        time.sleep(1)
        print("")

        if player.HP <= 0  :
            print("Y O U   L O S E")
            print("1. retry")
            print("2. exit")
            choice = ("choose 1 or 2")
            if choice == "1":
                restart_game()
            elif choice == "2":
                exit()
            
            elif e2.HP <= 0 :
                print("Y O U   W O N")
                print("wanna play again")
            print("1. play again")
            print("2. exit")
            choice = ("choose 1 or 2")
            if choice == "1":
                restart_game()
            elif choice == "2":
                exit()


print("DRAGON  QUEST")
time.sleep(1)
print("loading...")
time.sleep(1)
print("loading...")
time.sleep(1)
print("game ready")
print("")

input("press enter to start:")

print("")
print("1. start the game")
print("2. exit the game")
print("")

choose = input("choose 1 or 2:")
if choose == "1":
    print("game starting")
if choose == "2":
    print("thanks for playing")
    exit()


c1 = character("assassin",70,8,16,20) 
c2 = character("warrior",85,6,12,15)
c3 = character("mage",75,7,14,17)

e1 = enemy("gobln_easy",50,6,10)
e2 = enemy("goblin_Hard",65,7,14)

time.sleep(4)
print("")
print("choose your character")
print("")

print("1. assassin")
print("2. warrior")
print("3. mage")

time.sleep(1)
print("")

choice = input("choose 1,2 or 3:")

if choice == "1":
    player = c1
    print("you choose",player.name, "HP:", player.HP, "::low HP but hits hardest")
    time.sleep(1)
    print("normal attack:",player.normal_attack)
    time.sleep(1)
    print("hard attack:",player.hard_attack)
    time.sleep(1)
    print("main power:",player.main_power)
    

elif choice == "2":
    player = c2
    print("you choose",player.name,"HP:",player.HP,"::tank,safe choice")
    time.sleep(1)
    print("normal attack:",player.normal_attack)
    time.sleep(1)
    print("hard attack:",player.hard_attack)
    time.sleep(1)
    print("main power:",player.main_power)

elif choice == "3":
    player = c3
    print("you choose",player.name,"HP:",player.HP,"::middle ground")
    time.sleep(1)
    print("normal attack:",player.normal_attack)
    time.sleep(1)
    print("hard attack:",player.hard_attack)
    time.sleep(1)
    print("main power:",player.main_power)


time.sleep(6)
print("")
print("G O B L I N   A P P E A R S")
print("")

while player.is_alive() > 0 and e1.is_alive() > 0:

    print("your health remaining",player.HP)
    time.sleep(1)
    print("enemy health remaining",e1.HP)

    print("")
    print("your time to choose")
    time.sleep(1)
    print("1. normal_attack")  
    print("2. hard_attack")
    print("3. main_power")
    print("4. heal")
    print("")

    select = input("choose 1,2,3 or 4:")

    print("")
    
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
            print("oops target missed")

    elif select == "4":
        player.HP += 4
        print("your total HP becomes:",player.HP)

    time.sleep(1)

    print("")
    print("your health remaining",player.HP)
    time.sleep(1)
    print("enemy health remaining",e1.HP)
 
    if player.HP <= 0  :
        print("you lose")
        print("1. retry")
        print("2. exit")
        choice = ("choose 1 or 2")
        if choice == "1":
            restart_game()
        elif choice == "2":
            exit()
        continue
        
    elif e1.HP <= 0 :
        print("you won")
        continue
        

    time.sleep(1)
    print("")
    print("")
    print("G O B L I N   A T T A C K S")
    attack_choice = random.choice(["normal","hard"])
    if attack_choice == "normal":
        player.HP -= e1.normal_attack
        print("goblin hits you with damage:",e1.normal_attack)

    elif attack_choice == "hard":
        player.HP -= e1.hard_attack 
        print("goblin hits you with damage:",e1.hard_attack)

    time.sleep(1)
    print("")

    if player.HP <= 0  :
        print("Y O U   L O S E")
        print("1. retry")
        print("2. exit")
        choice = ("choose 1 or 2")
        if choice == "1":
            restart_game()
        elif choice == "2":
            exit()
  
        
    elif e1.HP <= 0 :
        print("Y O U   W O N")
        

    time.sleep(1)

time.sleep(3)
print("")      
if player.is_alive():
    print("N E W   E N E M Y   U P C O M M I N G  !!!")

time.sleep(1)
print("prepare yourself again")
player.HP += 20
print("you get 20 HP now lets goo")

while player.is_alive() > 0 and e2.is_alive() > 0:

    print("your health remaining",player.HP)
    time.sleep(1)
    print("enemy health remaining",e2.HP)

    print("")
    print("your time to choose")
    time.sleep(1)
    print("1. normal_attack")  
    print("2. hard_attack")
    print("3. main_power")
    print("4. heal")
    print("")

    select = input("choose 1,2,3 or 4:")

    print("")
    
    if select == "1":
        e2.take_damage(player.normal_attack)
        print("you hits goblin ",player.normal_attack,"damage")

    elif select == "2":
        chance = random.randint(1,10)
        if chance > 3:
            e2.take_damage(player.hard_attack)
            print("you hits goblin ",player.hard_attack,"damage")
        else :
            print("oops attack missed")
        
    elif select == "3":
        chance = random.randint(1,10)
        if chance > 6:
            e2.take_damage(player.main_power)
            print("you hits goblin ",player.main_power,"damage")
        else :
            print("oops target missed")

    elif select == "4":
        player.HP += 4
        print("your total HP becomes:",player.HP)

    time.sleep(1)

    print("")
    print("your health remaining",player.HP)
    time.sleep(1)
    print("enemy health remaining",e2.HP)
 
    if player.HP <= 0  :
        print("you lose")
        print("1. retry")
        print("2. exit")
        choice = ("choose 1 or 2")
        if choice == "1":
            restart_game()
        elif choice == "2":
            exit()
        continue
        
    elif e2.HP <= 0 :
        print("you won")
        continue
        

    time.sleep(1)
    print("")
    print("")
    print("G O B L I N   A T T A C K S")
    attack_choice = random.choice(["normal","hard"])
    if attack_choice == "normal":
        player.HP -= e2.normal_attack
        print("goblin hits you with damage:",e2.normal_attack)

    elif attack_choice == "hard":
        player.HP -= e2.hard_attack 
        print("goblin hits you with damage:",e2.hard_attack)

    time.sleep(1)
    print("")

    if player.HP <= 0  :
        print("Y O U   L O S E")
        print("1. retry")
        print("2. exit")
        choice = ("choose 1 or 2")
        if choice == "1":
            restart_game()
        elif choice == "2":
            exit()
        
    elif e2.HP <= 0 :
        print("Y O U   W O N")
        print("wanna play again")
        print("1. play again")
        print("2. exit")
        choice = ("choose 1 or 2")
        if choice == "1":
            restart_game()
        elif choice == "2":
            exit()
        
        

    time.sleep(1)



    


    



    

       












