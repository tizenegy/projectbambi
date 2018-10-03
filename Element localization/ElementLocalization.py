
'''
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
'''

from abc import ABCMeta, abstractmethod


class AppElement(object):
    def __init__(self, shape, centerX, centerY):
        self.shape = shape
        self.hight = 0
        self.length = 0
        self.centerX = centerX
        self.centerY = centerY
        self.group = 0
        self.verticalSequenceNumber = 0
        self.horizontalSequenceNumber = 0

    def __str__(self):
        return "This is a {0} element placed in {1}. place within group {2}.".format(
            self.shape, self.horizontalSequenceNumber, self.group
        )

'''
class Builder:
    __metaclass__ = ABCMeta

    @abstractmethod
    def set_shape(self, value):
        pass

    @abstractmethod
    def set_centerX(self, value):
        pass

    @abstractmethod
    def set_centerY(self, value):
        pass

    @abstractmethod
    def get_result(self):
        pass


class ElementBuilder(Builder):
    def __init__(self):
        self.element = AppElement()

    def set_shape(self, value):
        self.element.shape = value
        return self

    def set_centerX(self, value):
        self.element.centerX = value
        return self

    def set_centerY(self, value):
        self.element.centerY = value
        return self

    def get_result(self):
        return self.element


class ElementBuilderDirector(object):
    @staticmethod
    def construct(shape, centerX, centerY):
        return ElementBuilder()
                    .set_shape(shape)
                    .set_centerX(centerX)
                    .set_centerY(centerY)
                    .get_result()
'''


elementArray = [[1, 131, 265], 
                [1, 172, 197], 
                [1, 68, 198], 
                [2, 117, 149], 
                [0, 117, 149], 
                [2, 47, 97], 
                [1, 73, 88], 
                [3, 58, 92], 
                [0, 58, 92], 
                [0, 39, 90], 
                [1, 114, 95], 
                [1, 32, 86], 
                [3, 87, 84], 
                [1, 154, 57], 
                [3, 65, 55], 
                [0, 65, 55], 
                [2, 104, 53], 
                [3, 39, 48], 
                [1, 144, 104], 
                [1, 102, 35]]
'''
elementArray = [['rectangle', 131, 265], 
                ['rectangle', 172, 197], 
                ['rectangle', 68, 198], 
                ['triangle', 117, 149], 
                ['unknown', 117, 149], 
                ['triangle', 47, 97], 
                ['rectangle', 73, 88], 
                ['circle', 58, 92], 
                ['unknown', 58, 92], 
                ['pentagon', 39, 90], 
                ['rectangle', 114, 95], 
                ['rectangle', 32, 86], 
                ['circle', 87, 84], 
                ['rectangle', 154, 57], 
                ['circle', 65, 55], 
                ['unknown', 65, 55], 
                ['triangle', 104, 53], 
                ['circle', 39, 48], 
                ['rectangle', 144, 104], 
                ['rectangle', 102, 35]]
'''

appElementObjects = []

for element in elementArray:
    shape = element[0]
    if shape != 0:
        cX = element[1]
        cY = element[2]
        #appElements.append(ElementBuilderDirector.construct(shape, cX, cY))
        newElement = AppElement(shape, cX, cY)
        appElementObjects.append(newElement)
        print(newElement)

print("Done! First element:")
print(appElementObjects[0].centerX)

#Sort elements: which element is higher/lower on the screen?
sorted(appElementObjects, key=lambda appElement: appElement.centerY)
index = 0
for element in appElementObjects:
    element.verticalSequenceNumber = index
    index += 1