#create a scorption class that inherits from monster
#health and energy from parent class
class Monster:
    health = 100
    energy = 50
    def attack(self, amount):
        print("The monster has attacked.")
        print(f"{amount} was dealth.")
        self.health -= 20
    def move(self, speed):
        print("The monster is moved .")
        print(f"{speed} was the speed.")
class Parent(Monster):
    def __init__(self, speed, health, energy):
        Monster.__init__(self, health, energy)
        self.speed = speed
    def poison_damage(amount):
        print(f"{amount} was dealth.")
    def move(self):
        print("The parent has moved.")
        print(f"The speed of the parent is {self.speed}.")
class Scorpion(Monster):
    def __init__(self, speed, health, energy):
        Monster.__init__(self, health, energy)
        self.speed = speed
    def sting(self):
        print("The scorpion has stung.")
    def move(self):
        print("The scorpion has moved.")
        print(f"The speed of the scorpion is {self.speed}.")
