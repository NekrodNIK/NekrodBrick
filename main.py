from PIL import Image, ImageEnhance

img = Image.open("./example_image/road.jpg")

imgSmall = img.resize((64, 64), resample=Image.BILINEAR)

result = imgSmall.resize(img.size, resample=Image.NEAREST)

result = ImageEnhance.Contrast(result).enhance(1.5)

result = result.convert("L")

result.save("./example_image/road-pixelize.jpg")
