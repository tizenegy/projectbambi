

class AppElement(object):
    def __init__(self, shape, hight, length, centerX, centerY):
        self.shape = shape
        self.hight = hight
        self.length = length
        self.centerX = centerX
        self.centerY = centerY
        self.group = 1

    def __str__(self):
        return "Shape = {0} H = {1} L = {2} Mc = ({3} | {4}) Group = {5}".format(self.shape, self.hight, self.length, self.centerX, self.centerY, self.group)