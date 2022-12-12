from random import randint
from game.action import Action

"""
MathQuiz: provides the quiz questions and answers

attributes: 
self._question
self._answer

"""
class MathQuiz(Action):
    def __init__(self):
        self._question = ""
        self._answer = ""
        self._number1 = 0
        self._number2 = 0
        
    def addition(self): #Provide an Addition problem
        self._number1 = randint(1,100)
        self._number2 = randint(1,100)
        self._question = str(self._number1) + " + " + str(self._number2)
        self._answer = self._number1 + self._number2

    def subtraction(self): #Provide a Subtraction problem
        self._number1 = randint(1,100)
        self._number2 = randint(1,100)
        self._question = str(self._number1) + " - " + str(self._number2)
        self._answer = self._number1 - self._number2

    def multiplication(self): #Provide a Multiplication Problem
        self._number1 = randint(1,50)
        self._number2 = randint(1,12)
        self._question = str(self._number1) + " x " + str(self._number2)
        self._answer = self._number1 * self._number2

    def division(self): #Provide a division problem
        self._number1 = randint(1,50)
        self._number2 = randint(1,12)
        self._question = str(self._number1) + " / " + str(self._number2)
        self._answer = round((self._number1 / self._number2), 0)

    def display_question(self): #Display the question that was created
        return self._question

    def get_answer(self): #Return the answer to beused by another function
        return self._answer

    def reset(self): #Clear out the questions and answers so a new one can be generated.
        self._question = ""
        self._answer = ""
        self._number1 = 0
        self._number2 = 0
