import random

secretnb = 0
guess = 0
tries = 1

print("\n**** Welcome to this game. ****\nGuess the right number !")
def easy() :
    global secretnb
    print("Game difficulty : easy\nThe secret number is between 1 and 10")
    secretnb = random.randint(1,10)
    
def hard() :
    global secretnb
    print("Game difficulty : hard\nThe secret number is between 1 and 100")
    secretnb = random.randint(1,100)
    
def hardcore() :
    global secretnb
    print("Game difficulty : hardcore\nThe secret number is between 1 and 1000")
    secretnb = random.randint(1,1000)

difficultycheck = True
while difficultycheck == True :
    difficulty = input("\nSet the game difficulty : easy, hard or hardcore ? ")
    if difficulty == "easy" :
        easy()
        difficultycheck = False
    elif difficulty == "hard" :
        hard()
        difficultycheck = False
    elif difficulty == "hardcore" :
        hardcore()
        difficultycheck = False
    else :
        print("Please enter “easy”, “hard” or “hardcore” only")

loop = True
while loop :
    guess = int(input("\nWhat is your guess ? "))
    if guess > secretnb :
        print("Less !")
    elif guess < secretnb:
        print("More !")
    elif guess == secretnb :
        loop = False
        print("\nCongratulations, you won ! \n   The secret number was",secretnb,"\n      Your number of tries :",tries)
    else :
        print("BUG")
    tries = tries + 1