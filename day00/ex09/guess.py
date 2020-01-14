import random
print("This is an interactive guessing game!")
print("You have to enter a number between 1 and", end='')
print("99 to find out the secret number.")
print("Type 'exit' to end the game.")
print("Good luck!\n\n")
var = ''
var = input("What's your guess between 1 and 99?\n")
number = random.randint(1, 99)
i = 1
while var != 'exit':
    if int(var) > number:
        print("Too high!")
    elif int(var) < number:
        print("Too low!")
    else:
        if number == 42:
            print("That's it. That's all there is.")
        else:
            if i == 1:
                print("Congratulations, you've got it on your first try!")
            else:
                print("Congratulations, you've got it!")
                print(f"You won in {i} attempts!")
        quit()
    i = i + 1
    var = input()
print("Goodbye!")
