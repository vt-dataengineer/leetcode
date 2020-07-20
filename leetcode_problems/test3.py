class Car:

    def __init__(self, speed=0):
        self.speed = speed

    def accelerate(self):
            return 7

    def brake(self):
            return 10


if __name__ == '__main__':

    my_car = Car()
    action = input("Enter name: ").upper()
    if action == "RONALDO":
            print("Number: "+format(my_car.accelerate()))
    elif action == "MESSI":
            print("Number: "+format(my_car.brake()))
