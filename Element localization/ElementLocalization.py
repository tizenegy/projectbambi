

from aenum import Enum

class ShapeEnum(Enum):
    UNDEFINED = 0
    RECTANGLE = 1
    TRIANGLE = 2
    CIRCLE = 3

class AppElement:
    global ShapeEnum

    shape = UNDEFINED
    hight = 0
    length = 0
    centerPoint = [0, 0]
    group = 0
    verticalSequenceNumber = 0
    horizontalSequenceNumber = 0

def create_new_element():










from abc import ABCMeta, abstractmethod


class AppElement(object):
    def __init__(self, wheels=4, seats=4, color="Black"):
        global ShapeEnum

        self.shape = UNDEFINED
        self.hight = 0
        self.length = 0
        self.centerPoint = [0, 0]
        self.group = 0
        self.verticalSequenceNumber = 0
        self.horizontalSequenceNumber = 0

    def __str__(self):
        return "This is a {0} element within group {1} wheels and {2} seats.".format(
            self.color, self.wheels, self.seats
        )


class Builder:
    __metaclass__ = ABCMeta

    @abstractmethod
    def set_wheels(self, value):
        pass

    @abstractmethod
    def set_seats(self, value):
        pass

    @abstractmethod
    def set_color(self, value):
        pass

    @abstractmethod
    def get_result(self):
        pass


class CarBuilder(Builder):
    def __init__(self):
        self.car = Car()

    def set_wheels(self, value):
        self.car.wheels = value
        return self

    def set_seats(self, value):
        self.car.seats = value
        return self

    def set_color(self, value):
        self.car.color = value
        return self

    def get_result(self):
        return self.car


class CarBuilderDirector(object):
    @staticmethod
    def construct():
        return CarBuilder()
                .set_wheels(8)
                .set_seats(4)
                .set_color("Red")
                .get_result()

car = CarBuilderDirector.construct()
