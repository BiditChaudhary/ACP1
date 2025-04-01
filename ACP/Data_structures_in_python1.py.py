import random

c = random.randint(1, 100)  
guesses = [] 
i = 0

for i in range(10):
    g = int(input("Guess the number between 1 and 100: "))
    guesses.append(g) 
    
    if g < c:
        print("Too low!!")
    elif g > c:
        print("Too high!!")
    elif g == c:
        print(f"Congrats! You guessed the number in {i + 1} tries!!")
        print(f"Your guesses were {guesses}")
        break
else:
    print(f"You failed! The number was {c}.")
    print(f"Your guesses were: {guesses}")  
