""" Класс параболы."""


class Parabola:
    def __init__(self, a, b, c, is_horizontal=False):
        self.a = a
        self.b = b
        self.c = c
        self.is_horizontal = is_horizontal

    """ Проверяем положение точки относительно данной параболы. """

    def is_point_inside_of_parabola(self, point):
        if self.is_horizontal:
            res = point.x >= self.a * (point.y ** 2) + self.b * point.y + self.c    # Формула для горизонтальной параболы
        else:
            res = point.y >= self.a * (point.x ** 2) + self.b * point.x + self.c    # Формула для обычной параболы
        return res
