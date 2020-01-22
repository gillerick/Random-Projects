import random


class Random:
    def __init__(self):
        self.guess = int(input("Guess any number between 0 and 10\n"))
        self.num = random.randrange(10) # Or randint(0, 10)

    def go(self):
        try:
            if self.guess == self.num:
                print(f"You guessed right. The correct number is {self.num}.")
            elif self.guess > 10:
                self.guess = int(input("The number entered is outside the range. Please try again!\n"))
                Random.go(self)
            elif self.guess > self.num:
                self.guess = int(input(f"Ooops! Please try again. The number was too high.\n"))
                Random.go(self)
            elif self.guess < self.num:
                self.guess = int(input(f"Ooops! Please try again. The number was too low.\n"))
                Random.go(self)
        except ValueError:
            self.guess = int(input("Please enter an integer value.\n"))


if __name__ == '__main__':
    rand = Random()
    rand.go()