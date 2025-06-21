class Car:
    def start(self):
        print("Car started")

class Tesla(Car):
    def set_battery(self, capacity):
        self.battery = capacity
    def show_battery(self):
        print("Battery:", self.battery, "kWh")

c = Tesla()
c.start()
c.set_battery(95)
c.show_battery()