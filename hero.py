class SuperHero:
    people = "people"

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def info(self):
        return f"Name: {self.name}"

    def double_health(self):
        self.health_points *= 2

    def __str__(self):
        return f"Nickname: {self.nickname}, Superpower: {self.superpower}, Health: {self.health_points}"

    def __len__(self):
        return len(self.catchphrase)


hero = SuperHero("Tony Stark", "Iron Man", "Intelligence", 100, "I am Iron Man")

hero.info()


# hero.double_health()
# print(hero)
# print(f"Length of catchphrase: {len(hero)}")


class Fire(SuperHero):
    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage, fly=False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = fly

    def __str__(self):
        return f"{super().__str__()}, Damage: {self.damage}, Can fly: {self.fly}"

    def double_health(self):
        self.health_points **= 3
        self.fly = True

    def true_phrase(self):
        print(f"{self.catchphrase}")


class Storm(Fire):
    pass


ember = Fire("Xin", "Ember Spirit", "Flame", 66, "I will not be denied!",
             100)
storm = Storm("Raijin", "Storm Spirit", "Storm", 79, "Storms are coming!",
              84,)
ember.true_phrase()
ember.double_health()
print(ember)
storm.true_phrase()
storm.double_health()
print(storm)


class Villain(Fire):
    people = "monster"

    def gen_x(self):
        pass

    def crit(self, target):
        target.damage **= 2


sf = Villain("Nevermore", "Shadow Fiend", "Dark Power", "70", "Souls for me!",
             150)
sf.crit(storm)
sf.true_phrase()
print(sf)

print(f"Damage to Storm {storm.damage}")
