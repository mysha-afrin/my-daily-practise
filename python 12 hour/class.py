class Monster:
    #attributes
    health = 90
    energy = 40
    #methods
    def attack(something, damage):
        print("the monster has attacked!")
monster = Monster()
monster.attack(40)
print(monster.health)
print(monster.energy)
