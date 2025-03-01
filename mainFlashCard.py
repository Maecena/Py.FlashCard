import random

##def main():
##    while True:
##        addQuestion()

easy = -5
hard = 5

#holds the flash cards, key is a number and class Card is the card
questionList = []  

class Card:
    def __init__(self, answer, question):
        self.level = "regular"
        self.challenge = 0
        self.answer = answer
        self.question = question
        
    #adds or subtracts from the challenge level
    def correct(self):
        choice = None
        while choice != "y" or choice != "n":
            choice = input("Did you get it right? y/n")
        if choice == "y":
            self.challenge -= 1
            levelCheck(self)
        elif choice == "n":
            self.challenge += 1
            levelCheck(self)

    #checks to see what the level should be
    def levelCheck(self):
        if self.challege <= easy:
            self.level = "easy"
        elif self.challenge >= hard:
            self.level = "hard"
        else:
            self.level = "regular"

#adds flash card
def addQuestion():
    question = input("What's the question?")
    answer = input("And the answer is?")
    questionList.append(Card(answer, question))


##FUTURE

#make lists based
