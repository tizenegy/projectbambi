# USAGE
# python bambimain.py
# package projectbambi

import glob

from imageanalysis import analyze_image
from xmlgenerator import generate_xml_code

file = glob.glob('./*.png') + glob.glob('./*.jpg')   #look for *.png files, then look for *.jpg files

for entry in file:
    print('Image found: ', entry)

imageToAnalyse = file[0]

print('Analyzing image: ', imageToAnalyse)

xmlElements = analyze_image(imageToAnalyse)
generate_xml_code(xmlElements)

input("Image has been analyzed and XML code has been generated!\r\nPlease exit with 'ENTER'...")
