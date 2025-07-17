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

class fish:
    def __init__(self, speed, scale):
        self.speed = speed
        self.scale = scale
    def swim(self):
        print(f"The fish is swimming at {self.speed}")

class Shark(Monster, fish):
    def __init__(self, bite_strength, health, energy):
        self.bite_strength = bite_strength
        super().__init__(health, energy)

shark = Shark(bite_strength = 50, health=120, energy=80)
print(shark.health)
