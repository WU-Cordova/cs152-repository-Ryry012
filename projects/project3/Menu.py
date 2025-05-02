from datastructures.array import Array
from projects.project3.Drink import Drink
class Menu:

    def __init__(self):
        self._menu = []
        self._menu.append(Drink(name= 'Hot Cocoa', price= 4.00, size= 'Medium'))
        self._menu.append(Drink(name= 'Americano', price= 4.25, size= 'Medium'))
        self._menu.append(Drink(name= 'Latte', price= 5.00, size= 'Medium'))
        self._menu.append(Drink(name= 'Lemonade', price= 4.00, size= 'Medium'))
        self._menu.append(Drink(name= 'Iced Coffee', price= 3.50, size= 'Medium'))

    def print_menu(self):
        print("\nAvailable Drinks:")
        for index, item in enumerate(self._menu, start=1):
            print(f"{index}. {item}")

    def get_drink(self, num: int) -> Drink:
        return self._menu[num]

    def return_items(self) -> str:
        return self._menu
    
    def __str__(self):
        print(self._menu)