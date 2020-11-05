# Write your code her
import random


class Hangman:
    print("H A N G M A N\n")

    def __init__(self):
        self.list = ('python', 'java', 'kotlin', 'javascript')
        self.word = random.choice(self.list)
        self.censored = "-" * len(self.word)
        self.count = 8

    def guess(self):
        print(self.censored)

        letter = input("Input a letter:")
        if letter in self.censored:
            print("No improvements")
            self.reduce()
        elif letter in self.word:
            print("\n")
            for i, j in enumerate(self.word):
                if j == letter:
                    self.censored = self.censored[:(i)] + self.censored[i].replace("-", j) + self.censored[(i + 1):]
            self.reduce()
        else:
            print( "No such letter in the word\n")
            self.reduce()

    def reduce(self):
        self.count -=1

class Main:
    newhangman = Hangman()
    while newhangman.count > 0:
        newhangman.guess()
        if newhangman.censored == newhangman.word:
            break
    if newhangman.count == 0:
        print("You are hanged!")
    else:
        print("You guessed the word!\n You survived!")

if __name__ == "__main__":
    Main()




