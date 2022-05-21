from HM12_class_list import Car, Plane, Ship
from HM12_func import creation_ship, creation_plane, creation_car

my_car = Car(creation_car())
my_car()
print(Car.count_car)
my_car2 = Car(creation_car())
print(Car.count_car)