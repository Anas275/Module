import random
Cnumber = random.randrange(1,9)
userInput = int(input("Enter your number: "))
if userInput > Cnumber:
    print("Cumputer Number", Cnumber)
    print("Your guess number is too high")
elif Cnumber > userInput:
    print("Computer Number", Cnumber)
    print("Your number is too low")
else:
    print("Computer Number", Cnumber)
    print("Your guess number is equal")
