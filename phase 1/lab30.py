#1

answer = input("Name please: " )
while True:
    answer2 = input("How much money do you have? ")
    try:
        number = int(answer2)
    except  ValueError :
        print("Please try again.")
    else:
        break
answer3= number/2
print(answer + ", give me " + "$"+str(answer3))

#2

import random
number_guess = 0

print("Think of a number between 1 and 10 and I’ll try to guess it." )

min = 0

max = 10


guess = random.randint(min,max)
while True:
    number_guess += 1
    print("is your number " + str(guess) + "?")
    print("Please press:" ,end= "\n") 
    print("'y' for yes", end ="\n")
    print("'n' for no")
    inputt = input()
    if inputt == "y":
        break
    else:
        print("No? Then please press:", end= "\n")
        print("'h' if " + str(guess) + " is higher than your number", end= "\n")
        print("'l' if "+ str(guess) + " is lower than your number")
        input2 = input()
        if input2 == "h":
            guess = random.randint(guess, max)
        else:
            guess = random.randint(min, guess)
print("Hurray! Only " +str(number_guess) + " guesses."))
       
