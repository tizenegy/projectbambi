# USAGE
# python detect_shapes.py -i alt1.png

# import the necessary packages
from bambiclasses import AppElement
from shapedetection.detect_shapes import appElementObjects

xmlElements = []        #array to store the module output data (= list of grouped and sorted app elements for XML generation)
numOfElementGroups = 1  #number of groups of app elements (elements that lie horizontally on the same line, shall be grouped together)

#Sort elements vertically: (which element is higher/lower on the screen?)
appElementObjects = sorted(appElementObjects, key=lambda appElement: appElement.centerY)

#Group the elements that lie on the same horizontal line:
#Note about the algorithm:
#If y-value of center point of the (i+1)-th element lies within the range (hight) of the i-th element, the i-th element and the (i+1)-th element should be grouped together
index = 0
while index < (len(appElementObjects)-1):
    if (appElementObjects[index+1].centerY <= (appElementObjects[index].centerY + 0.5*appElementObjects[index].hight)) & (appElementObjects[index+1].centerY >= (appElementObjects[index].centerY - 0.5*appElementObjects[index].hight)):
        appElementObjects[index+1].group = appElementObjects[index].group
    else:
        numOfElementGroups += 1
        appElementObjects[index+1].group = numOfElementGroups
    index += 1
            
#Sort the elements within one group horizontally: (which element is more on the left/right on the screen?)
appElementObjects = sorted(sorted(appElementObjects, key = lambda appElement: appElement.centerX), key = lambda appElement: appElement.group)

#Generate output array
#Note: xmlElements = [(elementType, group)]
#      with:
#      elementType =    0   for   new group
#                       1   for   rectangle
#                       2   for   triangle
#                       3   for   circle
xmlElements.append([0, 1])
index = 0
while index <= (len(appElementObjects)-1):
    xmlElements.append([appElementObjects[index].shape, appElementObjects[index].group])
    if index == (len(appElementObjects)-1):
        break
    if appElementObjects[index].group != appElementObjects[index+1].group:
        xmlElements.append([0, appElementObjects[index+1].group])
    index += 1

#print(xmlElements)