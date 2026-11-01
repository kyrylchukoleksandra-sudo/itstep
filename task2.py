# ==============================================================================
# 🎮 СИМУЛЯТОР ЖИТТЯ (ТАМАГОЧІ) НА PYTHON + ООП
# ==============================================================================
# 1. Клас — це креслення/шаблон (як 3D-модель у Minecraft чи Sims),
#    а Об'єкт — це конкретний персонаж, створений за цим кресленням.
# 2. Атрибути — це "шкали та характеристики" (здоров'я, гроші, ситість).
# 3. Методи — це "кнопки дій" (їсти, працювати, відпочивати).
# 4. Взаємодія — об'єкт Людина керує іншими об'єктами (Авто, Дім, Робота).
# ==============================================================================

import random


# ==============================================================================
# 📌 [ООП: КЛАС] Клас Human
# Це головний шаблон для створення персонажа.
# ==============================================================================
class Human:
    # 📌 [ООП: КОНСТРУКТОР __init__]
    # Автоматично викликається при створенні об'єкта. Задає початкові характеристики.
    # self — це "Я" об'єкта (вказує на конкретного персонажа, якого ми створюємо).
    def __init__(self, name="Human", job=None, home=None, car=None):
        # 📌 [ООП: АТРИБУТИ] Змінні об'єкта ("шкали персонажа")
        self.name = name  # Ім'я персонажа
        self.money = 100  # Баланс гаманця
        self.gladness = 50  # Рівень щастя
        self.satiety = 50  # Рівень ситості

        # 📌 [ООП: КОМПОЗИЦІЯ / АГРЕГАЦІЯ]
        # Об'єкт може містити всередині себе інші об'єкти!
        # Початково у людини немає роботи, дому чи авто (вони None).
        self.job = job
        self.car = car
        self.home = home

    # 📌 [ООП: МЕТОД] get_home
    # Заселяє персонажа в будинок (створює екземпляр класу House).
    def get_home(self):
        self.home = House()

    # 📌 [ООП: МЕТОД] get_car
    # Купує авто (створює екземпляр класу Auto, передаючи туди список марок).
    def get_car(self):
        self.car = Auto(brands_of_car)

    # 📌 [ООП: МЕТОД ВЗАЄМОДІЇ] get_job
    # Персонаж намагається доїхати на співбесіду.
    def get_job(self):
        # 🎮 Логіка: викликаємо метод drive() об'єкта car (перевіряємо, чи їде авто)
        if self.car.drive():
            pass
        else:
            self.to_repair()  # Якщо зламалася — ремонтуємо
            return
        # Створюємо об'єкт Робота
        self.job = Job(job_list)

    # 📌 [ООП: МЕТОД] eat
    # Поповнює ситість, використовуючи ресурси з об'єкта Home.
    def eat(self):
        # 🎮 Логіка: перевіряємо атрибут food у об'єкта self.home
        if self.home.food <= 0:
            self.shopping("food")  # Якщо їжі немає — їдемо в магазин
        else:
            if self.satiety >= 100:
                self.satiety = 100
                return
            self.satiety += 5  # Збільшуємо ситість людини
            self.home.food -= 5  # Зменшуємо запаси їжі в будинку

    # 📌 [ООП: МЕТОД] work
    # Виконує роботу для заробляння грошей.
    def work(self):
        # Перевірка: чи може машина довезти до роботи
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                self.shopping("fuel")
                return
            else:
                self.to_repair()
                return

        # 📌 [ООП: ЗВ'ЯЗОК ОБ'ЄКТІВ]
        # Звертаємося до атрибутів об'єкта job (salary та gladness_less)
        self.money += self.job.salary
        self.gladness -= self.job.gladness_less
        self.satiety -= 4

    # 📌 [ООП: МЕТОД] shopping
    # Витрачає гроші персонажа для поповнення пального, їжі або щастя.
    def shopping(self, manage):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                manage = "fuel"
            else:
                self.to_repair()
                return

        if manage == "fuel":
            print("I bought fuel")
            self.money -= 100
            self.car.fuel += 100
        elif manage == "food":
            print("Bought food")
            self.money -= 50
            self.home.food += 50
        elif manage == "delicacies":
            print("Hooray! Delicious!")
            self.gladness += 10
            self.satiety += 2
            self.money -= 15

    # 📌 [ООП: МЕТОД] chill
    # Відпочинок: підвищує щастя, але створює безлад у будинку (self.home.mess).
    def chill(self):
        self.gladness += 10
        self.home.mess += 5

    # 📌 [ООП: МЕТОД] clean_home
    # Зменшує щастя, але скидає безлад у будинку до 0.
    def clean_home(self):
        self.gladness -= 5
        self.home.mess = 0

    # 📌 [ООП: МЕТОД] to_repair
    # Відновлює міцність об'єкта car за гроші.
    def to_repair(self):
        self.car.strength += 100
        self.money -= 50

    # 🎮 [ІГРОВА ЛОГІКА] Вивід дашборду стану персонажа, будинку та авто в консоль
    def days_indexes(self, day):
        day = f" Today the {day} of {self.name} 's life "
        print(f"{day:=^50}", "\n")
        human_indexes = self.name + "'s indexes"
        print(f"{human_indexes:^50}", "\n")
        print(f"Money – {self.money}")
        print(f"Satiety – {self.satiety}")
        print(f"Gladness – {self.gladness}")

        home_indexes = "Home indexes"
        print(f"{home_indexes:^50}", "\n")
        print(f"Food – {self.home.food}")
        print(f"Mess – {self.home.mess}")

        car_indexes = f"{self.car.brand} car indexes"
        print(f"{car_indexes:^50}", "\n")
        print(f"Fuel – {self.car.fuel}")
        print(f"Strength – {self.car.strength}")

    # 🎮 [ІГРОВА ЛОГІКА] Перевірка критичних умов (Game Over)
    def is_alive(self):
        if self.gladness < 0:
            print("Depression...")
            return False
        if self.satiety < 0:
            print("Dead...")
            return False
        if self.money < -500:
            print("Bankrupt...")
            return False
        return True

    # 🎮 [ГОЛОВНИЙ ІГРОВИЙ МЕТОД] live
    # Керує поведінкою персонажа протягом одного дня.
    def live(self, day):
        if self.is_alive() == False:
            return False

        # Автоматичне заповнення відсутніх атрибутів у перший день
        if self.home is None:
            print("Settled in the house")
            self.get_home()
        if self.car is None:
            self.get_car()
            print(f"I bought a car {self.car.brand}")
        if self.job is None:
            self.get_job()
            print(f"I don't have a job, going to get a job {self.job.job} with salary {self.job.salary}")

        self.days_indexes(day)

        # 🎮 Прийняття рішень: пріоритет виживання або випадкова дія (кубик)
        dice = random.randint(1, 4)
        if self.satiety < 20:
            print("I'll go eat")
            self.eat()
        elif self.gladness < 20:
            if self.home.mess > 15:
                print("I want to chill, but there is so much mess...\n So I will clean the house")
                self.clean_home()
            else:
                print("Let`s chill!")
                self.chill()
        elif self.money < 0:
            print("Start working")
            self.work()
        elif self.car.strength < 15:
            print("I need to repair my car")
            self.to_repair()
        elif dice == 1:
            print("Let`s chill!")
            self.chill()
        elif dice == 2:
            print("Start working")
            self.work()
        elif dice == 3:
            print("Cleaning time!")
            self.clean_home()
        elif dice == 4:
            print("Time for treats!")
            self.shopping(manage="delicacies")


# ==============================================================================
# 📌 [ООП: ОКРЕМИЙ КЛАС] Клас Auto
# Описує автомобіль. Має власні атрибути пального, міцності та витрати.
# ==============================================================================
class Auto:
    def __init__(self, brand_list):
        # 🎮 Вибираємо випадкову марку зі словника та зчитуємо її параметри
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]["fuel"]
        self.strength = brand_list[self.brand]["strength"]
        self.consumption = brand_list[self.brand]["consumption"]

    def drive(self):
        # 🎮 Перевірка можливість поїздки (наявність пального та справність)
        if self.strength > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.strength -= 1
            return True
        else:
            print("The car cannot move")
            return False


# ==============================================================================
# 📌 [ООП: ПРОСТИЙ КЛАС] Клас House
# Зберігає стан житла (кількість їжі та рівень безладу).
# ==============================================================================
class House:
    def __init__(self):
        self.mess = 0
        self.food = 0


# ==============================================================================
# 📌 [СТРУКТУРИ ДАНИХ] Словники з вихідними даними для об'єктів
# ==============================================================================
job_list = {
    "Java developer": {"salary": 50, "gladness_less": 10},
    "Python developer": {"salary": 40, "gladness_less": 3},
    "C++ developer": {"salary": 45, "gladness_less": 25},
    "Rust developer": {"salary": 70, "gladness_less": 1},
}

brands_of_car = {
    "BMW": {"fuel": 100, "strength": 100, "consumption": 6},
    "Lada": {"fuel": 50, "strength": 40, "consumption": 10},
    "Volvo": {"fuel": 70, "strength": 150, "consumption": 8},
    "Ferrari": {"fuel": 80, "strength": 120, "consumption": 14},
}


# ==============================================================================
# 📌 [ООП: ОКРЕМИЙ КЛАС] Клас Job
# Описує роботу, її зарплату та рівень втоми (витрати щастя).
# ==============================================================================
class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]["salary"]
        self.gladness_less = job_list[self.job]["gladness_less"]


# ==============================================================================
# 📌 [ООП: СТВОРЕННЯ ОБ'ЄКТА / ЕКЗЕМПЛЯРА]
# Тут випікається конкретний персонаж "nick" за формою-класом "Human".
# ==============================================================================
nick = Human(name="Nick")

# 🎮 [ГОЛОВНИЙ ЦИКЛ ГРИ (GAME LOOP)]
# Симуляція 7 днів життя створеного об'єкта nick.
for day in range(1, 8):
    if nick.live(day) == False:
        break