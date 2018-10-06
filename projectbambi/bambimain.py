# USAGE
# python bambimain.py
# package projectbambi

from imageanalysis import analyze_image
from xmlgenerator import generate_xml_code

xmlElements = analyze_image('ipad3.jpg')
generate_xml_code(xmlElements)