import random


class Random:
    def __init__(self):
        self.guess = int(input("Guess any number between 0 and 10\n"))
        self.num = random.randrange(10) # Or randint(0, 10)

    def go(self):
        if self.guess == self.num:
            print(f"You guessed right. The correct number is {self.num}")
        elif self.guess > self.num:
            print(f"Ooops! Please try again. The number was too high")
        elif self.guess < self.num:
            print(f"Ooops! Please try again. The number was too low")


if __name__ == '__main__':
    # Create a class instance called rand
    rand = Random()
    rand.go()