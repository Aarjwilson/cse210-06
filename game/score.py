from action import Action
"""
Score : Keeps track of the players score.

Attributes: 
self._score
self._value

"""
class Score(Action):
    def __init__(self):
        self._score = 0
        self._value = 10

    def add_points(self):
        self._score += self._value

    def lose_points(self):
        self._score -= self._value

        if self._score < 0:
            self._score = 0
    
    def get_score(self):
        return self._score

    def reset(self):
        self._score = 0
