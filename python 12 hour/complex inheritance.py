class Monster:
    health = 100
    energy = 50
    def __init__(self, health, energy):
        self.health = health
        self.energy = energy
    def attack(self, health, energy, **kwargs):
        print(kwargs)
        self.health = health
        self.energy = energy
        super(). __init__(speed = 25, has_scale = False)
    

class fish:
    def __init__(self, speed, scale):
        self.speed = speed
        self.scale = scale
    def swim(self):
        print(f"The fish is swimming at {self.speed}")

class Shark(Monster, fish):
    def __init__(self, bite_strength, health, energy, speed, has_scales):
        self.bite_strength = bite_strength
        Monster.__init__(self, health, energy)
        fish.__init__(self, speed, has_scales)
shark = Shark(bite_strength = 50, health = 200, energy = 100, speed = 30, has_scales = True)
