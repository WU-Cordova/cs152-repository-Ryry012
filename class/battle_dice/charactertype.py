from enum import Enum

class CharacterType(Enum):
    WARRIOR = "warrior"
    MAGE = "Mage"
    ROGUE = "Rogue"

from charactertype import CharacterType

# Accessing the CharacterType Enum
my_character_type = CharacterType.WARRIOR

print(my_character_type)        # Output: CharacterType.WARRIOR
print(my_character_type.name)   # Output: "WARRIOR"
print(my_character_type.value)  # Output: "warrior"
