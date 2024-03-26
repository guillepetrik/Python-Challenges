# Class Shopping Cart Challenge

class Item:
    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add(self, item: Item):
        self.items.append(item)

    def total(self) -> int:
        return sum(item.price for item in self.items)

    def __len__(self):
        return len(self.items)

# Class areas of rectangle and circle
import math
class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width
    
    def area(self) -> int:
        return self.length * self.width
    pass

class Circle:
    def __init__(self, radius: int):
        self.radius = radius
    
    def area(self) -> float:
        return math.pi * self.radius**2
    pass

# String Representation of Objects

class Car:
    def __init__(self, maximum_speed, unit):
        self.maximum_speed = maximum_speed
        self.unit = unit
    
    def __str__(self):
        return f"Car with the maximum speed of {self.maximum_speed} {self.unit}"


class Boat:
    def __init__(self, speed):
        self.speed = speed
    
    def __str__(self):
        return f"Boat with the maximum speed of {self.speed} knots"

# String Transformation

def transformSentence(sentence):
    words = sentence.split()
    res = ""
    for i in words:
        res += i[0]
        for j in range(1, len(i)):
            if i[j-1].lower() < i[j].lower():
                res+=i[j].upper()
            elif i[j-1].lower() > i[j].lower():
                res += i[j].lower()
            else:
                res += i[j]
        res += " "

    return res[:-1:]