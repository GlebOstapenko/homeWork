from all_func import get_any_type


def creation_vehicle(func):
    def creation():
        create_information = {}
        create_information.setdefault("mark", get_any_type("Укажите марку: ", "str_only_words"))
        create_information.setdefault("model", get_any_type("Укажите модель: ", "str_only_words"))
        create_information.setdefault("max_speed", get_any_type("Укажите максимальную скорость: ", "int"))
        create_information.setdefault("fuel_consumption",get_any_type("Укажите расход топлива: ", "float"))
        create_information.setdefault("maximum_load", get_any_type("Укажите максимальную грузоподёмность: ", "int"))
        create_information.setdefault("volume_fuel_tank", get_any_type("Укажите обьём бака: ", "int"))
        create_information.setdefault("number_passenger", get_any_type("Укажите кол-во пасажиров: ", "int"))
        for arg in (res := func()):
            create_information.setdefault(arg, res[arg])
        return create_information

    return creation


@creation_vehicle
def creation_car():
    car_information = {}
    car_information.setdefault("engine_capacity", get_any_type("Укажите обьём двигателя: ", "float"))
    car_information.setdefault("number_wheels", get_any_type("Укажите количество колёс: ", "int"))
    return car_information


@creation_vehicle
def creation_plane():
    plane_information = {}
    plane_information.setdefault("number_engines", get_any_type("Укажите количество двигателей: ", "int"))
    plane_information.setdefault("maximum_flight_altitude", get_any_type("Укажите максимальную высоту: ", "int"))
    plane_information.setdefault("minimum_flight_altitude", get_any_type("Укажите минимальную высоту: ", "int"))


@creation_vehicle
def creation_ship():
    ship_information = {}
    ship_information.setdefault("number_of_screws", get_any_type("Укажите количество винтов: ", "int"))
    ship_information.setdefault("ship_type", get_any_type("Укажите тип судна: ", "str_only_words"))
