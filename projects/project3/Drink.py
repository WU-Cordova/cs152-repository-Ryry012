from dataclasses import dataclass


@dataclass
class Drink:
    name: str
    price: float
    size: str
    customization: str = ''

