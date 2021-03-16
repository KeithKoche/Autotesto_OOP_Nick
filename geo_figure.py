class GeometricFigure:

  def __init__(self, name, area, angles, perimeter):
    self.name = name
    self.area = area
    self.angles = angles
    self.perimeter = perimeter
    print(f"Инициализирован '{self.name}'")

  @classmethod
  def this_geo(cls):
      print(f"Фигура относится к  {cls}")
      return cls


  @property
  def p_area(self):
      return self.area

  @p_area.setter
  def p_area(self, value):
      if not isinstance(value, (int, float)):
          raise ValueError('Значение не является числом')
      print(f"Площадь фигуры '{self.name}' = {self.area + value}")


  @property
  def r_q_angles(self):
      return self.angles

  @r_q_angles.setter
  def r_q_angles(self, value):
      if not isinstance(value, (int, float)):
          raise ValueError('Значение не является числом')
      if self.angles + value == 4:
          print(f"Количество углов фигуры = {self.angles + value}")
      else:
          raise ValueError('Фигура не является четырехугольником')

  @property
  def p_perimeter(self):
      return self.perimeter

  @p_perimeter.setter
  def p_perimeter(self, value):
      print(f"Периметр фигуры {self.name} = {self.perimeter + value}")


  def add_area(self, alt_area):
      if isinstance(alt_area, (int, float)):
          print(f"По методу адд-арея площадь фигуры {self.name} = {self.area + alt_area}")
      else:
          raise TypeError("Передана не геометрическая фигура")

  @staticmethod
  def terminator():
      print('----------------')

class Triangle(GeometricFigure):

    def __init__(self, name, area, angles, perimeter):
        super().__init__(name, area, angles, perimeter)

    @property
    def p_triangles(self):
        return self.angles

    @p_triangles.setter
    def p_triangles(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError('Передано не цифровое значение')
        self.angles = value
        if self.angles == 3:
            print(f"Количество углов фигуры = {self.angles}")
        else:
            raise ValueError('Фигура не является треугольником')



t = Triangle("Треугольник", 0, 0, 0)
t.this_geo()
t.p_area = 5
t.p_triangles = 3
t.p_perimeter = 9
t.add_area(alt_area=11)
t.terminator()


class Rectangle(GeometricFigure):
    def __init__(self, name, area, angles, perimeter):
        super().__init__(name, area, angles, perimeter)

r = Rectangle("Прямоугольник", 0, 0, 0)
r.this_geo()
r.p_area = 2
r.r_q_angles = 4
r.p_perimeter = 7
r.add_area(alt_area=5)
r.terminator()


class Quadrate(GeometricFigure):
    def __init__(self, name, area, angles, perimeter):
        super().__init__(name, area, angles, perimeter)

    def q_sides(self):
        print(f"Длина стороны фигуры {self.name} = {self.area ** 0.5}")
        return self.area ** 0.5

q = Quadrate("Квадрат", 0, 0, 0)
q.this_geo()
q.p_area = 3
q.r_q_angles = 4
q.p_perimeter = 8
q.q_sides()
q.add_area(alt_area=6)
r.terminator()


class Circle(GeometricFigure):
    def __init__(self, name, area, angles, perimeter):
        super().__init__(name, area, angles, perimeter)

    @property
    def circle_true(self):
        return self.angles

    @circle_true.setter
    def circle_true(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError('Передано не цифровое значение')
        self.angles = value
        if self.angles == 0:
            print(f"Эта фигура - {self.name} т.к. количество углов = {self.angles}")
        else:
            raise ValueError('Фигура не является кругом ')


c = Circle("Круг", 0, 0, 0)
c.this_geo()
c.p_area = 4
c.p_perimeter = 3
c.circle_true = 0
c.add_area(alt_area=7)
c.terminator()



