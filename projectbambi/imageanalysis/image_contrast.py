from PIL import Image, ImageEnhance

#from __init__ import image

img2 = Image.open(str(image))
enhancer = ImageEnhance.Contrast(img2)
img2 = enhancer.enhance(4)
enhancer = ImageEnhance.Brightness(img2)
img2 = enhancer.enhance(4)
enhancer = ImageEnhance.Contrast(img2)
img2 = enhancer.enhance(5)
enhancer = ImageEnhance.Brightness(img2)
img2 = enhancer.enhance(5)
#img2.rotate(270).save("alt1.jpg")
enhancer.enhance(5).save("alt1.png")

# img = Image.open('2.jpg')
# enhancer = ImageEnhance.Brightness(img)
# enhancer.enhance(0.0).save("ImageEnhance_Brightness_000.jpg")
# enhancer.enhance(0.25).save("ImageEnhance_Brightness_025.jpg")
# enhancer.enhance(0.5).save("ImageEnhance_Brightness_050.jpg")
# enhancer.enhance(0.75).save("ImageEnhance_Brightness_075.jpg")
# enhancer.enhance(1.0).save("ImageEnhance_Brightness_100.jpg")
