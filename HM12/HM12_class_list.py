from abc import ABC, abstractmethod


class Vehicle(ABC):
    mark = ""
    model = ""
    max_speed = 0
    fuel_consumption = ""
    maximum_load = ""
    volume_fuel_tank = ""
    number_passenger = 0

    @abstractmethod
    def __init__(self, create_information):
        self.mark = create_information["mark"]
        self.model = create_information["model"]
        self.max_speed = create_information["max_speed"]
        self.fuel_consumption = create_information["fuel_consumption"]
        self.maximum_load_capacity = create_information["maximum_load"]
        self.volume_tank = create_information["volume_fuel_tank"]
        self.number_passenger = create_information["number_passenger"]

    @abstractmethod
    def start_sound(self):
        pass


class Car(Vehicle):
    engine_capacity = 0
    number_wheels = 0
    count_car = 0

    def __init__(self, create_information):
        super(Car, self).__init__(create_information)
        self.engine_capacity = create_information["engine_capacity"]
        self.number_wheels = create_information["number_wheels"]
        Car.count_car += 1

    def __call__(self, *args, **kwargs):
        print(self.mark)
        print(self.model)

    def start_sound(self):
        print("Врум")


class Plane(Vehicle):
    number_engines = 0
    maximum_flight_altitude = ""
    minimum_flight_altitude = ""

    def __init__(self, create_information):
        super(Plane, self).__init__(create_information)
        self.number_engines = create_information["number_engines"]
        self.maximum_flight_altitude = create_information["maximum_flight_altitude"]
        self.minimum_flight_altitude = create_information["minimum_flight_altitude"]

    def start_sound(self):
        print("Виуууу")


class Ship(Vehicle):
    number_of_screws = 0
    ship_type = ""

    def __init__(self, create_information):
        super(Ship, self).__init__(create_information)
        self.number_of_screws = create_information["number_of_screws"]
        self.ship_type = create_information["ship_type"]

    def start_sound(self):
        print("ТуууТуууу")
