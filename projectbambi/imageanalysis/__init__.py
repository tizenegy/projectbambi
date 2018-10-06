#imageanalysis

def analyze_image(img):
    global image
    image = img
    from .element_localization import xmlElements
    return xmlElements