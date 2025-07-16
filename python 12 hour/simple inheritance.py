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
class Shark(Monster):
    def __init__(self, speed):
        self.speed = speed
    def bite(self):
        print("The shark has bitten.")
    def move(self):
        print("The shark has moved.")
        print(f"The speed of the shark is {self.speed}.")
shark = Shark(speed = 120)
shark.move()
