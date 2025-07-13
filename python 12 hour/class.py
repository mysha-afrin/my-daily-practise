class Monster:
    #attributes
    health = 90
    energy = 40
    def __init__(self, health, energy): #Dender method
        self.health = health
        self.energy = energy
        
    #methods
    def attack(self, damage):
        print("the monster has attacked!")
        print(f"{damage} has dealt.")
    def move(self, speed):
        print("The monster has moved!")
        print(f"It has speed of {speed}.")
monster1 = Monster(10, 20)
monster2 = Monster(health = 50, energy = 100)
print(monster1.health)
print(monster2.energy
