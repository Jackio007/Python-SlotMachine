import time
import random

credit = 100
replay = True
# List of all fruits that can be played in the game.
# fruits = ["Cherry", "Bell", "Lemon", "Orange", "Star", "Skull"]

def Play():
    global credit
    credit = credit - 20
    RandChoice()
    Pairs()
    print("You now have %s credit" %credit)

def RandChoice():
      global rand1, rand2, rand3
      rand1 = random.choice( ['Cherry', 'Bell', 'Lemon', 'Orange', 'Star', 'Lemon', 'Skull'] )
      rand2 = random.choice( ['Cherry', 'Bell', 'Lemon', 'Orange', 'Star', 'Lemon', 'Skull'] )
      rand3 = random.choice( ['Cherry', 'Bell', 'Lemon', 'Orange', 'Star', 'Lemon', 'Skull'] )
      print (rand1, rand2, rand3)

def Pairs():
    global credit
    if rand1=="Skull" and rand2=="Skull" and rand3=="Skull":
        credit = 0
        print("\nOh no you have rolled three skulls! Game over! \nYou now have %s credits!" %credit)
        
    elif rand1=="Skull" and rand2=="Skull" or rand1=="Skull" and rand3=="Skull" or rand2=="Skull" and rand3=="Skull":
        credit = credit-200
        print("\nOh no you have rolled two skulls! You lose 200 credits!\nYou now have %s credits!" %credit)
        
    elif rand1=="Bell" and rand2=="Bell" and rand3=="Bell":
        credit = credit+500
        print("\nCongratulations! You have earned 100 credits!\nYou now have %s credits!" %credit)
        
    elif rand1=="Bell" and rand2=="Bell" and rand3=="Bell":
        credit = credit+500
        print("\nCongratulations! You have earned 100 credits!\nYou now have %s credits!" %credit)
            
    elif rand1==rand2==rand3:
        credit = credit+100
        print("\nCongratulations! You have earned 100 credits!\nYou now have %s credits!" %credit)
            
    elif rand1==rand2 or rand1==rand3 or rand2==rand3:
        credit = credit+50
        print("\nCongratulations! You have earned 50 credits!")

# Code for the instructions
while replay == True:
    credit = 100
    
    print("===== Welcome to Fruit Machine =====")
    instr = input("Would you like to read the instructions(Y)? Or not?(N): ")
    instr = instr.lower() # Reverts input to lowercase
    if instr == "y":
        print("===== INSTRUCTIONS =====")
        time.sleep(2)
        print("More instructions...")
    elif instr == "n":
        print("\nLet's Play")
        time.sleep(1)
    else:
        print("\nIt looks like you typed in a wrong character!\nBut we'll assume you said no")
    
# Begins the actual application
    time.sleep(1)
    print("\nYou have %s credit" %credit)

    while credit >= 20 or credit == 0:
    
        play = input("\nTo play, hit enter:")
        if play == "":
            Play()

    rePlay = input("Would you like to play again? Y/N? : ")
    instr = instr.lower() # Reverts input to lowercase
    if rePlay == "y":
        replay = True
    else:
        replay = False



