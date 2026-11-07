class Engine:
    def start(self):
        print("Engine is starting")


class ElectricVehicle:
    def charge(self):
        print("Charging the electric vehicle")


class HybridCar(Engine, ElectricVehicle):
    def drive(self):
        print("Hybrid car is driving")


car = HybridCar()
car.start()
car.charge()
car.drive()