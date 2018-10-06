# USAGE
# python bambimain.py
# package projectbambi

from imageanalysis import analyze_image

image = 'ipad3.jpg'
testElements = analyze_image(image)
print(testElements)