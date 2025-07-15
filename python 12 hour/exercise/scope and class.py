class Monster:
    def __init__(self, health, energy):
        self.health = health
        self.energy = energy
    def update_energy(self, amount):
        self.energy += amount
    def get_damage(self, amount):
        self.health -= amount


#create a hero class with 2 parametres:damage, monster
class Hero:
    def __init__(self, damage, monster):
        self.damage = damage
        self.monster = monster
#the monster class should have a method that lowers the health->get_amount(amount)
#the hero class should have an attack method


