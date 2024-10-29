import random

class Cat:
    def __init__(self, name):
        self.name = name
        self.happiness = 50  # Уровень счастья от 0 до 100
        self.energy = 50     # Уровень энергии от 0 до 100

    def play(self):
        if self.energy > 10:
            self.happiness += 10
            self.energy -= 10
            print(f"{self.name} играет и радуется!")
        else:
            print(f"{self.name} слишком уставший, чтобы играть.")

    def sleep(self):
        self.energy += 20
        print(f"{self.name} спит и восстанавливает силы.")

    def status(self):
        print(f"{self.name}: счастье = {self.happiness}, энергия = {self.energy}")

# Пример использования
my_cat = Cat("Мурка")
my_cat.play()
my_cat.sleep()
my_cat.status()
