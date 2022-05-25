from HM13.HM13_class import Triangle, Point, Line

p1 = Point(1, 5)
p2 = Point(10, 15)
p3 = Point(15, 15)
l1 = Line(p1, p2)
print(l1.length)
l2 = Line(p2, p3)
print(l2.length)
l3 = Line(p3, p1)
print(l3.length)
tr1 = Triangle(p1, p2, p3)
print(tr1.area)