from charactertype import CharacterType

# Accessing the CharacterType Enum
my_character_type = CharacterType.WARRIOR

print(my_character_type)        # Output: CharacterType.WARRIOR
print(my_character_type.name)   # Output: "WARRIOR"
print(my_character_type.value)  # Output: "warrior"

from game import Game
from character import Character
from charactertype import CharacterType

# Create characters
alice = Character(name="Alice", character_type=CharacterType.WARRIOR, health=100, attack_power=15)
bob = Character(name="Bob", character_type=CharacterType.MAGE, health=70, attack_power=20)

# Start the game
game = Game(alice, bob)
game.start_battle()
