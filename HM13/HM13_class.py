from math import dist


class Point:

    def __init__(self, x=0, y=0, *args, **kwargs):
        self.__point_x = self.check_point_type(x)
        self.__point_y = self.check_point_type(y)

    @classmethod
    def check_point_type(cls, x):
        try:
            return int(x)
        except:
            raise TypeError("Кординаты могут быть только числовым значением")

    @property
    def point_x(self):
        return self.__point_x

    @point_x.setter
    def point_x(self, x):
        self.__point_x = self.check_point_type(x)

    @property
    def point_y(self):
        return self.__point_y

    @point_y.setter
    def point_y(self, y):
        self.__point_y = self.check_point_type(y)


class Line:
    def __init__(self, a_point=Point(0, 0), b_point=Point(0, 0), *args, **kwargs):
        if not isinstance(a_point, Point) or not isinstance(b_point, Point):
            raise TypeError("Данные указаны не верно, необходимо указать елементы класса Point")
        self.__a_point = a_point
        self.__b_point = b_point
        self.__length = self.get_length(self.__a_point, self.__b_point)

    @classmethod
    def get_length(cls, a_point, b_point):
        length = dist([a_point.point_x, a_point.point_y], [b_point.point_x, b_point.point_y])
        return length

    @property
    def length(self):
        return self.__length


class Triangle:
    def __init__(self, a_point=Point(0, 0), b_point=Point(0, 0), c_point=Point(0, 0), *args, **kwargs):
        if not isinstance(a_point, Point) or not isinstance(b_point, Point) or not isinstance(c_point, Point):
            raise TypeError("Данные указаны не верно, необходимо указать елементы класса Point")
        self.__a_point = a_point
        self.__b_point = b_point
        self.__c_point = c_point
        self.__ab_line = Line(self.__a_point, self.__b_point).length
        self.__bc_line = Line(self.__b_point, self.__c_point).length
        self.__ca_line = Line(self.__c_point, self.__a_point).length
        self.__area = self.get_area(self.__ab_line, self.__bc_line, self.__ca_line)

    @classmethod
    def get_area(self, ab_line, bc_line, ca_line):
        act1 = (ab_line + bc_line + ca_line) / 2
        act2 = act1 * (act1 - ab_line) * (act1 - bc_line) * (act1 - ca_line)
        area = act2 ** 0.5
        return area

    @property
    def area(self):
        return self.__area
