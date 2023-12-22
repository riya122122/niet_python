import random
n = random.randrange(1,11)
user = int(input("Guess the number:"))
print("Computer's number was: ",n)
if user == n:
    print("You guessed it correctly!")
else:
    print("You guessed it wrong!")
