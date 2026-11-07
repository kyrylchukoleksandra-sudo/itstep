class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def attack(self):
        pass


class Hero(Character):
    def __init__(self, name, health, weapon):
        super().__init__(name, health)
        self.weapon = weapon

    def attack(self):
        print(f"{self.name} attacks with {self.weapon}!")


class Enemy(Character):
    def __init__(self, name, health, damage):
        super().__init__(name, health)
        self.damage = damage

    def attack(self):
        print(f"{self.name} deals {self.damage} damage!")


hero = Hero("Heroic Hero", 100, "Sword")
hero.attack()

enemy = Enemy("Evil Enemy", 50, 10)
enemy.attack()