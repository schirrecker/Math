import random
from random import randint

class User:
    def __init__(self, name, points):
        self.name = name
        self.points = points

    def EasyQuiz(self, intro):
        print(intro)
        num1 = randint(12, 50)
        num2 = randint(12, 50)
        quiz = int(input("What is " + str(num1) + " * " + str(num2) + "? "))
        answer = num1 * num2

        if answer == quiz:
            print("Correct!")
            self.points += 1
            print("You now have " + str(self.points) + " points!")
        else:
            print("Incorrect!")
            print("The answer was " + str(answer))
            print("Maybe next time.")

    def MediumQuiz(self, intro):
        print(intro)
        num1 = randint(35, 35)
        num2 = randint(12, 50)
        num3 = randint(30, 50)
        quiz = int(input("What is (" + str(num1) + " * " + str(num2) + ") + " + str(num3) + "?"))
        answer = (num1 * num2) + num3

        if answer == quiz:
            print("Correct!")
            self.points += 3
            print("You now have " + str(self.points) + " points!")
        else:
            print("Incorrect!")
            print("The answer was " + str(answer))
            print("Maybe next time.")
            
    def HardQuiz(self, intro):
        print(intro)
        num1 = randint(30, 80)
        num2 = randint(30, 80)
        num3 = randint(30, 80)
        quiz = int(input("What is " + str(num1) + " * " + str(num2) + " * " + str(num3) + "?"))
        answer = num1 * num2 * num3

        if answer == quiz:
            print("Correct!")
            self.points += 5
            print("You now have " + str(self.points) + " points!")
            
        else:
            print("Incorrect!")
            print("The answer was " + str(answer)) 
            print("Maybe next time.")

    def get_points(self, printThem):
        if printThem:
            print(str(self.points))
        return self.points

name = input("What is your name? ")

PersonalFile = open(name+".txt", "w")

Alois = User(name, 0)

while True:
    Alois.HardQuiz("May the quiz begin!")

    
