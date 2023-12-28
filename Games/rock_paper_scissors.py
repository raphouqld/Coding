import random

userchoice = input("Rock, paper or scissors ? (r,p,s)")
computerchoice = random.randint(1,3)

# Tell the computer choice
if computerchoice == 1 :
    print("The computer chose rock.")
elif computerchoice == 2 :
    print("The computer chose paper.")
elif computerchoice == 3 :
    print("The computer chose scissors.")


if userchoice == "r" :
    if computerchoice == 1 :
        print("You both played rock. Retry !")
    elif computerchoice == 2 :
        print("You lose !")
    elif computerchoice == 3 :
        print("You win !")

if userchoice == "p" :
    if computerchoice == 1 :
        print("You win !")
    elif computerchoice == 2 :
        print("You both played paper. Retry !")
    elif computerchoice == 3 :
        print("You lose !")

if userchoice == "s" :
    if computerchoice == 1 :
        print("You lose !")
    elif computerchoice == 2 :
        print("You win !")
    elif computerchoice == 3 :
        print("You both played scissors. Retry !")

else :
    print("You can only enter r, p or s. Retry !")