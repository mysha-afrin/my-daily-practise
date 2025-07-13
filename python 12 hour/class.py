class Monster:
    #attributes
    health = 90
    energy = 40
    #methods
    def attack(self, damage):
        print("the monster has attacked!")
        print(f"{damage} has dealt.")
    def move(self, speed):
        print("The monster has moved!")
        print(f"It has speed of {speed}.")
monster = Monster()
monster.attack(40)
monster.speed = 40
print(monster.health)
print(monster.energy)
