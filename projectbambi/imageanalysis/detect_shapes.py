# USAGE
# python detect_shapes.py -i alt1.png

# import the necessary packages
import os
import argparse, imutils, cv2, numpy
from PIL import Image, ImageEnhance

from .bambiclasses import AppElement
from .shapedetector import ShapeDetector
from . import image_contrast # contrast enhancer module

# local variables
appElementObjects = []  #array to store all detected app elements in the form of objects
outputArray = []        #array to store the module output data (= list of grouped and sorted app elements for XML generation)

# open jpg, enhance brightness and contrast, save as alt1.png (Elfert)
#image_contrast

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

##textfile (Elfert)
#file = open("contours.txt", "a")
#file.truncate(0)

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

    ## multiply the contour (x, y)-coordinates by the resize ratio,
    ## then draw the contours and the name of the shape on the image
    #c = c.astype("float")
    #c *= ratio
    #c = c.astype("int")
    #cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
    #cv2.putText(image, shape, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX,
    #   0.5, (255, 255, 255), 2)

    ## show the output image
    #cv2.imshow("Image", image)
    #cv2.waitKey(0)

    ##write contours to file (Elfert)
    #file.write("\n")
    #file.write(str(shape))
    #file.write("\n")
    #file.write("X: "+str(cX)+" Y: "+str(cY))
    ##file.write("\n")
    ##file.write(str(c))
    ##file.write("\n")

    #map the shape to the shapes-code
    if ((shape == "rectangle") | (shape == "square")):
        elementShape = 1
    elif shape == "triangle":
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
        #print(newElement)
    

#file.close()

os.remove('alt1.png')   #clean up