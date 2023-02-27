# Ccылка на 8 task:
# https://docs.google.com/document/d/18kSJw3s1mWnL3Z1HE4avoGahlc96vcMFtSlQyVLZa3c/edit
# Я делала по 17 картинке
# Для подбора координат используйте этот сайт:
# https://www.desmos.com/calculator?lang=ru

""" Из (from) файлов наших классов импортируем (import) сами классы.
    Т.е. наш класс Point находится в файле Point.py. Аналогично с остальными классами. """

from Point import Point
from Parabola import Parabola
from Line import Line
from Color import Color

""" Создаём функцию, где мы вводим две координаты нашей точки - x, y. Но т.к. мы в нашу другую функцию должны передать 
    точку, а не координаты отдельные, то её нужно отсюда вернуть. В return вызываем конструктор нашего класса Point и 
    передаём ему параметры - координаты. """


def input_point():
    x = float(input("Enter x: "))
    y = float(input("Enter y: "))

    """ Если введённые координаты попадают в предел, мы возвращаем точку. Иначе мы возвращаем None. """

    if -10 <= x <= 10 and -10 <= y <= 10:
        return Point(x, y)
    else:
        return None

""" Создаём функцию, которая будет определять цвет координатной плоскости в переданной точке. """

def init_color(p):
    """ Для начала необходимо определить, какие функции (математические) у нас на рисунке в условии.
        Это наши экземпляры классов. Уже не просто абстрактные структуры,
        а конкретные объекты. """

    parabola1 = Parabola(0.25, -2.5, 6.25)
    parabola2 = Parabola(8/67, 0, 2, True)
    line1 = Line(6, 27)
    line2 = Line(1/4, -15/4)

    if parabola1.is_point_inside_of_parabola(p) and not parabola2.is_point_inside_of_parabola(p):
        return Color.GREEN.name
    elif parabola1.is_point_inside_of_parabola(p) and parabola2.is_point_inside_of_parabola(p):
        return Color.GREY.name
    elif line1.is_point_at_the_right_side_of_the_line(p) and line2.is_point_at_the_right_side_of_the_line(p):
        return Color.GREEN.name
    elif not line1.is_point_at_the_right_side_of_the_line(p) and not parabola2.is_point_inside_of_parabola(
            p) and not parabola1.is_point_inside_of_parabola(p):
        return Color.ORANGE.name
    elif line2.is_point_at_the_right_side_of_the_line(p) and parabola2.is_point_inside_of_parabola(p):
        return Color.GREY.name
    elif parabola2.is_point_inside_of_parabola(p) and not parabola1.is_point_inside_of_parabola(
            p) and not line2.is_point_at_the_right_side_of_the_line(p):
        return Color.WHITE.name

# line2 - горизонтальная; parabola2 - горизонтальная

if __name__ == '__main__':
    _point = input_point() # создаём точку

    """ Если мы ввели неверные координаты, то из функции input_point() у нас вернётся None. Если вернётся None, то мы 
        просто выводим в консоль, что у нас пустая точка и прекращаем работу программы. """

    if _point is not None:
        print(init_color(_point)) # печатаем результат нашей функции, которой мы передали нашу точку.
    else:
        print("Point is None.") # выводится, если в нашем случае point оказалась None.

    """ Вы можете сделать сразу несколько переменных-точек и потом передать их в функцию и распечатать в консоли. 
        Это будет даже удобнее, чем 10 раз запускать программу и по 10 раз выводить разные результаты. 
        Например будет печататься так: Point(6, -9) -> GREEN. 
        В питоне можно вроде в консоль выводить цветной текст. Можете сами изучить этот момент и сделать красивый вывод 
        результата. """