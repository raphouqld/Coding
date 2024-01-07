import random

secretnb = 0
guess = 0
print("\n**** Welcome to this game. ****\nGuess the right number !")
def easy() :
    global secretnb
    print("Game difficulty : easy")
    secretnb = random.randint(1,10)
    
def hard() :
    global secretnb
    print("Game difficulty : hard")
    secretnb = random.randint(1,100)
    
def hardcore() :
    global secretnb
    print("Game difficulty : hardcore")
    secretnb = random.randint(1,1000)

difficulty = input("Set the game difficulty : easy, hard or hardcore ? ")
if difficulty == "easy" :
    easy()
elif difficulty == "hard" :
    hard()
elif difficulty == "hardcore" :
    hardcore()

loop = True
while loop == True :
    guess = int(input("\nWhat is your guess ? "))
    if guess > secretnb :
        print("Less !")
    elif guess < secretnb:
        print("More !")
    elif guess == secretnb :
        loop = False
        print("\nCongratulations, you won ! \nThe secret number was",secretnb)
    else :
        print("BUG")