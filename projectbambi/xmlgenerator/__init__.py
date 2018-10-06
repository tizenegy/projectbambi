#xmlgenerator

def generate_xml_code(elements):
    global xmlElements
    xmlElements = elements
    from . import xml_generator