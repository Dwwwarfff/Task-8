""" Класс линии. """


class Line:
    def __init__(self, k, b):
        self.k = k
        self.b = b

    """ Проверка положения точки относительно этой линии. """

    def is_point_at_the_right_side_of_the_line(self, point):
        return point.y >= self.k * point.x + self.b
