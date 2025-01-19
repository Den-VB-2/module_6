class Figure:
    sides_count = 0
    name_D = 0
    color_2 = None
    filled = False

    def __init__(self, name, __color, *__sides):
        self.name = name
        self.__color = __color
        self.__sides = __sides

    def set_color(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b
        self.color_2 = (self.r, self.g, self.b)
        self._Figure__is_valid_color(self.color_2)

    def get_color(self):
        if self.filled == False and i == 0:
            print("")
            return (f"Прошлые данные объекта {self.name} и новые данные вне цветового охвата.\n"
                    f"НЕ ПОКРАШЕНО!")
        elif self.filled == True and i == 0:
            print("")
            return (f"Объект {self.name} ранее был покрашен в цвет: R={self.__color[0]}, "
                    f"G={self.__color[1]}, B={self.__color[2]}\n"
                    f"Новые данные вне цветового охвата, объект не перекрашен!")
        elif self.filled == False and i == 1:
            print("")
            self.__color = self.color_2
            self.color_2 = None
            self.filled = True
            return (f"Ранее объект {self.name} не был покрашен,\n"
                    f"сейчас его покрасили в цвет: R={self.__color[0]}, "
                    f"G={self.__color[1]}, B={self.__color[2]}")
        else:
            temp_1 = self.__color
            temp_2 = self.color_2
            self.__color = self.color_2
            self.color_2 = None
            print("")
            return (f"Объект {self.name} ранее был покрашен в цвет: R={temp_1[0]}, "
             f"G={temp_1[1]}, B={temp_1[2]}.\n"
             f"Объект перекрашен в цвет: R={temp_2[0]}, "
             f"G={temp_2[1]}, B={temp_2[2]}.")

    def __is_valid_color(self, __color):
        global i
        i = 0
        if self.__color[0] >= 0 and self.__color[0] <= 255 and isinstance(self.__color[0], int) \
            and self.__color[1] >= 0 and self.__color[1] <= 255 and isinstance(self.__color[1], int) \
            and self.__color[2] >= 0 and self.__color[2] <= 255 and isinstance(self.__color[2], int):
            self.filled = True
        if self.color_2[0] >= 0 and self.color_2[0] <= 255 and isinstance(self.color_2[0], int) \
            and self.color_2[1] >= 0 and self.color_2[1] <= 255 and isinstance(self.color_2[1], int) \
            and self.color_2[2] >= 0 and self.color_2[2] <= 255 and isinstance(self.color_2[2], int):
            i = 1

    def set_sides(self, *new_sides):
        global l, J
        self.temp_1 = []
        self.temp_2 = []
        l = 2
        self.new_sides = new_sides
        print("")
        self._Figure__is_valid_sides(self.__sides)
        self.__sides = self.temp_3
        if j == 0:
            l = 0
        elif j == 1:
            l = 1
        self.temp_1 = self.temp_3
        self._Figure__is_valid_sides(self.new_sides)
        if j == 1:
            self.temp_2 = self.temp_3
            self.__sides = self.temp_3

    def __is_valid_sides(self, temp_3):
        self.temp_3 = list(temp_3)
        global l, j
        j = 1
        if len(self.temp_3) == 1:
            if isinstance(self.temp_3[0], int) == False or self.temp_3[0] <= 0:
                j = 0
            else:
                self.temp_3 = [self.temp_3[0]] * self.sides_count
        elif len(self.temp_3) > 1 and len(self.temp_3) != self.sides_count:
                j = 0
        else:
            for k in range(len(self.temp_3)):
                if isinstance(self.temp_3[k], int) == False or self.temp_3[k] <= 0:
                    j = 0
                break
        if l == 2:
            if len(self.temp_3) == 1 and j == 1:
                self.temp_3 = [self.temp_3[0]] * self.sides_count
            elif len(self.temp_3) == self.sides_count and j == 1:
                if self.name_D == 3 and len(set(self.temp_3)) != 1:
                    self.temp_3 = [1] * self.sides_count
                    j = 0
            else:
                self.temp_3 = [1] * self.sides_count
        elif j == 1:
            return True
        else:
            return False

    def get_sides(self):
        if l == 0 and self._Figure__is_valid_sides(self.temp_3) == True:
            return (f"Прошлые данные объекта {self.name} не верны и были присвоены единичные размеры, мм: {self.temp_1}\n"
                  f"Новые данные верны, у объекта изменились размеры, мм: {self.temp_2}")
        elif l == 1 and self._Figure__is_valid_sides(self.temp_3) == True:
            return (f"Прошлые размеры объекта {self.name} были, мм: {self.temp_1}\n"
                  f"на текущий момент они изменились, мм: {self.temp_2}")
        elif l == 0 and self._Figure__is_valid_sides(self.temp_3) == False:
            return (f"Прошлые данные объекта {self.name} не верны и были присвоены единичные размеры, мм: {self.temp_1}\n"
                  f"Новые данные не верны, размеры не изменились")
        elif l == 1 and self._Figure__is_valid_sides(self.temp_3) == False:
            return (f"Прошлые размеры объекта {self.name} были, мм: {self.temp_1}\n"
                  f"Новые данные не верны, размеры не изменились")

    def __len__(self):
        print("")
        if self.sides_count == 1:
            print (f"Длина окружности {self.name}, мм: ", end="")
        else:
            print (f"Сумма всех сторон объекта {self.name}, мм: ", end="")
        return sum(self.__sides)


class Circle(Figure):
    filled = False
    sides_count = 1
    name_D = 2

    def get_square(self):
        if self._Figure__is_valid_sides(self.temp_3) == True:
            r = round(self.temp_2[0] / (2 * 3.14), 2)
        else:
            r = round(self.temp_1[0] / (2 * 3.14), 2)
        print("")
        print(f"Радиус объекта {self.name}, мм: {r}")
        return(f"Площадь объекта {self.name}, кв.мм: {round((3.14 * (r ** 2)), 2)}")


class Triangle(Figure):
    filled = False
    sides_count = 3
    name_D = 2

    def get_square(self):
        if self._Figure__is_valid_sides(self.temp_3) == True:
            s = (sum(self.temp_2)) / 2
            a = self.temp_2[0]
            b = self.temp_2[1]
            c = self.temp_2[2]
        else:
            s = (sum(self.temp_1)) / 2
            a = self.temp_1[0]
            b = self.temp_1[1]
            c = self.temp_1[2]
        print("")
        return(f"Площадь объекта {self.name}, кв.мм:  \
{round((s * (s - a) * (s - b) * (s - c)) ** 0.5, 2)}")


class Cube(Figure):
    filled = False
    sides_count = 12
    name_D = 3

    def get_volume(self):
        if self._Figure__is_valid_sides(self.temp_3) == True:
            v = self.temp_2[0]**3
        else:
            v = self.temp_1[0]**3
        print("")
        return (f"Oбъём объекта {self.name}, куб.мм: {round(v, 2)}")


# Код для проверки (по заданию):
print("")
print("")
print("ПРОВЕРКА КОДА ПО ЗАДАНИЮ")

# Исходные данные:
circle1 = Circle("circle1", (200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube("cube1",(222, 35, 130), 6)

circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())


print("")
print("")
print("РАСШИРЕННАЯ ПРОВЕРКА ВСЕХ ФУНКЦИЙ")

# Исходные данные:
circle1 = Circle("Круг-1",(200, 200, 100), 10)
circle2 = Circle("Круг-2",(50, 60, 70), 10, 5)
triangle1 = Triangle("Tреугольник-1", (-100, 35, 35), 10, 5, 3)
triangle2 = Triangle("Tреугольник-2",(30, 40, 55), 4, 7)
cube1 = Cube("Куб-1", (222, 35, 130), 6)
cube2 = Cube("Куб-2", (-100, 100, 100), 5, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)
print(circle1.get_color())
circle1.set_color(155, 166, 277)
print(circle1.get_color())
triangle1.set_color(300, 300, 300)
print(triangle1.get_color())
cube1.set_color(300, 70, 15)
print(cube1.get_color())
cube2.set_color(100, 70, 15)
print(cube1.get_color())

# Проверка на изменение сторон:
circle1.set_sides(15)
print(circle1.get_sides())
circle1.set_sides(15, -2)
print(circle1.get_sides())
circle2.set_sides(3)
print(circle2.get_sides())
triangle1.set_sides(15)
print(triangle1.get_sides())
triangle1.set_sides(7, 8, 6)
print(triangle1.get_sides())
triangle2.set_sides(5, 4)
print(triangle2.get_sides())
cube1.set_sides(5, 3, 12, 4, 5)
print(cube1.get_sides())
cube1.set_sides(5)
print(cube1.get_sides())
cube2.set_sides(-4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4)
print(cube2.get_sides())

# Проверка расчета суммы сторон:
print(len(circle1))
print(len(triangle1))
print(len(cube1))

# Проверка расчетов индивидуальных параметров:
print(circle1.get_square())
print(circle2.get_square())
print(triangle1.get_square())
print(triangle2.get_square())
print(cube1.get_volume())
print(cube2.get_volume())
