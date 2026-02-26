class Car:
    color="black"
    @staticmethod
    def start():
        print("car started")
    
    @staticmethod
    def stop():
        print("car stop")

class Toyotacar(Car):
    def __init__(self, name):
        self.name=name

car1= Toyotacar("fortuner")
car2=Toyotacar("prius")
  
print(car1.color) 

