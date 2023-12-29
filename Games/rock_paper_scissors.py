import random

computerscore = 0
userscore = 0
winorlose = 0

def lose() :
    global computerscore
    print("You lose this round !")
    winorlose = 0
    computerscore = computerscore + 1

def win() :
    global userscore
    print("You win this round !")
    winorlose = 1
    userscore = userscore + 1

def samechoice() :
    print("You both played the same thing. Retry !")
    winorlose = 2

    #function for each round
def round() :
    if userchoice == "r" :
        if computerchoice == 1 :
            samechoice()
            return False
        elif computerchoice == 2 :
            lose()
        elif computerchoice == 3 :
            win()

    elif userchoice == "p" :
        if computerchoice == 1 :
            win()
        elif computerchoice == 2 :
            samechoice()
            return False
        elif computerchoice == 3 :
            lose()

    elif userchoice == "s" :
        if computerchoice == 1 :
            lose()
        elif computerchoice == 2 :
            win()
        elif computerchoice == 3 :
            samechoice()
            return False
    return True
            
    # function for telling the computer choice
def tellcomputerchoice() :
    if computerchoice == 1 :
        print("The computer chose rock.")
    elif computerchoice == 2 :
        print("The computer chose paper.")
    elif computerchoice == 3 :
        print("The computer chose scissors.")
print("#####  Welcome to this rock,paper,scissors game !  #####")
i = 1
while i <= 3 :
    print("Round :",i)
    userchoice = input("Rock, paper or scissors ? (r,p,s)")
    computerchoice = random.randint(1,3)
    tellcomputerchoice()
    if round() == True :
        i = i+1

if computerscore > userscore :
    print("You LOSE !")
    print("Your score was :",userscore)
    print("Your opponent score was :",computerscore)
elif userscore > computerscore :
    print("You WIN !")
    print("Your score was :",userscore)
    print("Your opponent score was :",computerscore)
elif userscore == computerscore :
    print("It's a DRAW !")
    print("Your score was :",userscore)
    print("Your opponent score was :",computerscore)
else :
    print("BUG")