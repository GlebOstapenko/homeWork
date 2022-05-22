from abc import ABC, abstractmethod
import inspect


class Vehicle(ABC):
    __slots__ = (
        "mark", "model", "max_speed", "fuel_consumption", "maximum_load", "volume_fuel_tank", "number_passenger")

    def __init__(self, mark, model, **kwargs):
        self.mark = mark
        self.model = model

        for param, value in kwargs.items():

            try:
                command_exec = f"self.{param} = {value}"
                exec(command_exec)
            except NameError:
                print(f"{param} - може бути лише числовим значенням, [{value}] не підходить")
            except AttributeError:
                print(f"Параметр {param} не в списку допустимих параметрів")

    def __call__(self):
        for i in inspect.getmembers(self):
            if not i[0].startswith('_'):
                if not inspect.ismethod(i[1]):
                    print(f"{i[0]} -> {i[1]}")

    @abstractmethod
    def start_sound(self):
        pass


class Car(Vehicle):
    __slots__ = "number_wheels", "engine_capacity"

    def start_sound(self):
        print("Врум")


class Plane(Vehicle):
    __slots__ = "number_engines", "maximum_flight_altitude", "minimum_flight_altitude"

    def start_sound(self):
        print("Виуууу")


class Ship(Vehicle):
    __slots__ = "number_of_screws", "ship_type"

    def start_sound(self):
        print("ТуууТуууу")
