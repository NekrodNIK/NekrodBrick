from PIL import Image

img = Image.open("./example_image/road.jpg")

imgSmall = img.resize((64, 64), resample=Image.BILINEAR)

result = imgSmall.resize(img.size, resample=Image.NEAREST)

result.save("./example_image/road-pixelize.jpg")
