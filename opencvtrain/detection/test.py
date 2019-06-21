from PIL import Image

img_PIL = Image.open('11111.png')

image = img_PIL.resize((28, 28), Image.ANTIALIAS)

image.show()

image.save("q3.png")