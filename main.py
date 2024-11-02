import random

class Cat:
    def __init__(self, name):
        self.name = name
        self.happiness = 50  # Уровень счастья от 0 до 100
        self.energy = 50     # Уровень энергии от 0 до 100

    def play(self):
        if self.energy > 10:
            self.happiness += random.randint(5, 15)
            self.energy -= random.randint(10, 20)
            print(f"{self.name} играет и радуется! Счастье: {self.happiness}, Энергия: {self.energy}")
        else:
            print(f"{self.name} слишком уставший, чтобы играть.")

    def sleep(self):
        self.energy += random.randint(15, 25)
        print(f"{self.name} спит и восстанавливает силы. Энергия: {self.energy}")

    def do_nothing(self):
        self.happiness -= random.randint(5, 10)
        print(f"{self.name} скучает... Счастье: {self.happiness}")

    def live_a_day(self):
        # Каждый день котик случайным образом решает, что делать
        action = random.choice(['play', 'sleep', 'do_nothing'])
        if action == 'play':
            self.play()
        elif action == 'sleep':
            self.sleep()
        else:
            self.do_nothing()

    def status(self):
        print(f"{self.name}: счастье = {self.happiness}, энергия = {self.energy}")

# Симуляция жизни котика на протяжении 10 дней
my_cat = Cat("Мурка")
for day in range(10):
    print(f"\nДень {day + 1}:")
    my_cat.live_a_day()
    my_cat.status()
