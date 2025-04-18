import random
from character import Character
from charactertype import CharacterType

class Game:
    def __init__(self, player1: Character, player2: Character):
        self.__player1 = player1
        self.__player2 = player2

    def attack(self, attacker: Character, defender: Character):
        pass  # TODO: Implement the battle loop where players take turns attacking

    def start_battle(self):
        pass  # TODO: Implement the battle logic
