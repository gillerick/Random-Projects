import random


class Random:
    def __init__(self, count=0):
        self.count = count

    def go(self):
        num = random.randrange(12)
        print("Guess any number between 0 and 12. You have only 4 attempts")
        guess = int(input("Guess any number between 0 and 12\n"))

        if guess == num:
            print(f"You guessed right. The correct number is {num}")
        else:
            print(f"Ooops! Please try again. The correct number was {num}")
            self.count += 1


if __name__ == '__main__':
    # Create a class instance called rand
    rand = Random()
    rand.go()
