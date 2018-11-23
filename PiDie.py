import random
from random import randint
import time


class PiDie:
    def __init__(self, players, turn):
        self.players = players
        self.turn = turn
        
    def roll(self, player):
        print("You rolled a " + str(randint(1, 6)) + ", " + player)

    def play(self):
        for player in self.players:
            self.roll(player)
            time.sleep(3)
            print("")



def is_factor(a,b):
    if b % a == 0:
        return True
    else:
        return False

players = ["Stephan", "Alois"]

PiDie1 = PiDie(players, 0)

while True:
    PiDie1.play()
    
