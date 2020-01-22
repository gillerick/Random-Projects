import random

value = random.randint(1, 10)

answer = str(value)

guess = ''
while guess is not int: # Unnecessary. The try ..except checks this
    try:
        guess = int(input("Guess the correct number between 1-10: "))
        break
    except ValueError:
        print("Please enter a valid number")

calculate = value - guess

answer_1 = str(calculate)

if value == guess:
    print("HOOOORAAAAY! You got it right...GO YOU!")
elif value > guess:
    print("TRY AGAIN.....Your number is on the lower side")
elif value < guess:
    print("TRY AGAIN.....Your number is on the higher side")

print("The random value is:" + answer)
print("The difference between your guess and the random value is:" + answer_1)


''''1. In your code, you tell your user to try again. But the code stops running. You need to have some sort of loop, 
for as long as the guessed number does not match the random one.
2. Your code can be neater. For instance, after the input, take your user to the next line
3. You may want to consider implementing the same using a class and a function. Your code will look more neat and brief

Otherwise, it is a good implementation. Work on writing neater codes



'''
