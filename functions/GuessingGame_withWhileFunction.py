import random
#to use random number generator import random library first
secret_number = random.randint(0,9)
guess_count = 0
guess_limit = 5
while guess_count <= guess_limit:
    guess = int(input("Guess: "))
    guess_count += 1
    if guess == secret_number:
        print("You won!")
        break
else:
    print("Better luck next time")
print("_"*15)
