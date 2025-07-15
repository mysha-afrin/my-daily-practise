def update_health(ammount):
    monster.health += ammount
class Monster:
    def __init__(self, health, energy):
        self.health = health
        self.energy = energy
    def update_energy(self, ammount):
        self.energy += ammount
    def set_energy(self, energy):
        new_energy = energy
        return new_energy
monster = Monster(health = 100, energy = 50)
print(monster.energy)
