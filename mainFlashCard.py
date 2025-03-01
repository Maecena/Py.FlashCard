import random

##def main():
##    while True:
##        addQuestion()

easy = 12
medium = 7

#holds the flash cards, key is a number and class Card is the card
questionDict = {}

class Card:
    def __init__(self, answer, question):
        self.level = "hard"
        self.challenge = 0
        self.answer = answer
        self.question = question
        
    #adds or subtracts from the challenge level
    def correct(self):
        choice = input("Did you get it right? y/n")
        while choice != "y" or "n":
            if choice == "y":
                self.challenge += 1
                levelCheck(self)
            elif choice == "n":
                self.challenge -= 1
                levelCheck(self)

    #checks to see what the level should be
    def levelCheck(self):
        if self.challege < medium:
            self.level = "hard"
        elif self.challenge < easy:
            self.level = "medium"
        else:
            self.level = "easy"


##def difficulty():
##    x = randint(1, 10)
##    if x <= 6:
##        return "hard"
##    elif x <= 9:
##        return "medium"
##    else:
##        return "easy"

#adds flash card
def addQuestion():
    z = 0
    question = input("What's the question?")
    answer = input("And the answer is?")
    questionDict[z] = Card(answer, question)
    z += 1

##def showDict():
##    for k, v in questionDict.items():
##        print (k, v)
