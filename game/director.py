from random import randint
from game.math_quiz import MathQuiz
from game.score import Score

"""
Director: This is the main controller of the game. It updates and displays all game mechenics.
"""

class Director:
    def __init__(self):
        self._is_playing = True
        self._round = 0
        self._guess = 0
        self._anwer = 0
        self._correct = True

        self._quiz = MathQuiz()
        self._score = Score()

    def start_game(self): #Start the game loop

        print(f"\nWELCOME TO 'WHO WANTS TO BE A MATHAMATICION!'")
        print(f"\n1. You will be presented with a simple random math problem.")
        print(f"2. The problem will be either Addition, Subtraction, Multiplication, or Division.")
        print(f"3. If you guess correctly, you earn 10 points.")
        print(f"4. If you guess incorrectly, you lose 10 points")
        print(f"5. There will be rounds of 10 questions, in which case you will be prompted to play again, or end the game.")

        while self._is_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()
            self.play_again()

    def get_inputs(self): #Get the users input in regards to the question provided
        self._round += 1
        _topic = randint(1,4)
        if _topic == 1:
            self._quiz.addition()
        elif _topic == 2:
            self._quiz.subtraction()
        elif _topic == 3:
            self._quiz.multiplication()
        elif _topic == 4:
            self._quiz.division()

        print(f"\nQuestion {self._round}: {self._quiz.display_question()}")
        try:
            self._guess = int(input("Your guess (rounded to the nearest whole number): "))
        except:
            print("Incorrect type of answer, please try again.")

    def do_updates(self): #Updated the score based off the players answer
        self._answer = self._quiz.get_answer()

        if self._guess == self._answer:
            self._correct = True
            self._score.add_points()
        else:
            self._correct = False
            self._score.lose_points()

    def do_outputs(self): #Print out the results of the answer given
        if self._correct:
            print(f"\nCORRECT! The answer was {self._answer}! Your score is {self._score.get_score()}.")
        else:
            print(f"\nINCORRECT! The answer was {self._answer} and you guess {self._guess}. Your score is {self._score.get_score()}.")
            print(f"Try again next time.\n")

    def play_again(self): #When time, prompt the user to play again, or end the game.
        if self._round == 10:
            keep_playing = input("\nWould you like to play again to try to earn more points (Y/N)? ")
            if keep_playing.lower() == "y":
                self._is_playing = True
                self._quiz.reset()
                self._score.reset()
            else:
                self._is_playing = False
                print(f"\nThank you for playing! You ended with {self._score.get_score()} points.")
        else:
            pass