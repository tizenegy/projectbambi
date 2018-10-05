# USAGE
# python detect_shapes.py -i alt1.png

# import the necessary packages
from pyimagesearch.shapedetector import ShapeDetector
import argparse, imutils, cv2, numpy
from PIL import Image, ImageEnhance
# import contrast enhancer module
import image_contrast

appElementObjects = []  #array to store all detected app elements in the for of objects
numOfElementGroups = 1  #number of groups of app elements (elements that lie horizontally on the same line, shall be grouped together)

class AppElement(object):
    def __init__(self, shape, hight, length, centerX, centerY):
        self.shape = shape
        self.hight = hight
        self.length = length
        self.centerX = centerX
        self.centerY = centerY
        self.group = numOfElementGroups

    def __str__(self):
        return "Shape = {0} H = {1} L = {2} Mc = ({3} | {4}) Group = {5}".format(self.shape, self.hight, self.length, self.centerX, self.centerY, self.group)


# open jpg, enhance brightness and contrast, save as alt1.png (Elfert)
image_contrast

# construct the argument parse and parse the arguments
#ap = argparse.ArgumentParser()
#ap.add_argument("-i", "--image", required=True,
#   help="path to the input image")
#args = vars(ap.parse_args())

# load the image and resize it to a smaller factor so that
# the shapes can be approximated better
#image = cv2.imread(args["image"])
image = Image.open('alt1.png')

# invert (Elfert)
image = numpy.invert(image)

resized = imutils.resize(image, width=300)
ratio = image.shape[0] / float(resized.shape[0])

# convert the resized image to grayscale, blur it slightly,
# and threshold it
gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]

# find contours in the thresholded image and initialize the
# shape detector
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if imutils.is_cv2() else cnts[1]
sd = ShapeDetector()

# loop over the contours
for c in cnts:
    # compute the center of the contour, then detect the name of the
    # shape using only the contour
    M = cv2.moments(c)
    try:
        cX = int((M["m10"] / M["m00"]) * ratio)
        cY = int((M["m01"] / M["m00"]) * ratio)
        shape = sd.detect(c)
    except ZeroDivisionError:
        shape = "unknown"

    #map the shape to the shapes-code
    if shape == "rectangle":
        elementShape = 1
    elif ((shape == "triangle") | (shape == "square")):
        elementShape = 2
    elif shape == "circle":
        elementShape = 3
    else:
        elementShape = 0
    

    xArray = []
    yArray = []
    for point in c:
        xArray.append(point[0][0])
        yArray.append(point[0][1])
    
    maxX = sorted(xArray, reverse=True)[0]
    minX = sorted(xArray, reverse=True)[len(xArray)-1]
    length = maxX - minX

    maxY = sorted(yArray, reverse=True)[0]
    minY = sorted(yArray, reverse=True)[len(yArray)-1]
    hight = maxY - minY

    #store the element data in an array of app element objects
    #(but only if the detected shape is valid)
    if elementShape != 0:
        newElement = AppElement(elementShape, hight, length, cX, cY)
        appElementObjects.append(newElement)
        print(newElement)
    
    #print(c)

#Sort elements vertically: (which element is higher/lower on the screen?)
appElementObjects = sorted(appElementObjects, key=lambda appElement: appElement.centerY)

#print("First element:")
#print(appElementObjects[0])
#print("Last element:")
#print(appElementObjects[len(appElementObjects)-1])

#Group the elements that lie on the same horizontal line:
#Note about the algorithm:
#If y-value of center point of the (i+1)-th element lies within the range (hight) of the i-th element, the i-th element and the (i+1)-th element should be grouped together
index = 0
while index < (len(appElementObjects)-1):
    if (appElementObjects[index+1].centerY <= (appElementObjects[index].centerY + appElementObjects[index].hight)) & (appElementObjects[index+1].centerY >= (appElementObjects[index].centerY - appElementObjects[index].hight)):
        appElementObjects[index+1].group = appElementObjects[index].group
    else:
        numOfElementGroups += 1
        appElementObjects[index+1].group = numOfElementGroups
    index += 1
            
#Sort the elements within one group horizontally: (which element is more on the left/right on the screen?)
appElementObjects = sorted(sorted(appElementObjects, key = lambda appElement: appElement.centerX), key = lambda appElement: appElement.group)

print("\r\n\r\n")
for element in appElementObjects:
    print(element)