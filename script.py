# from PIL import Image, ImageEnhance

"""img = Image.open("./example_image/cat.jpg")

img = img.convert("P", palette=Image.ADAPTIVE, colors=5).convert('L')

imgSmall = img.resize((64, 64), resample=Image.ADAPTIVE)

img = imgSmall.resize(img.size, resample=Image.NEAREST)

img = ImageEnhance.Contrast(img).enhance(3)

img.save("./example_image/output.png")"""

"""
img = Image.open("./example_image/cat.jpg")

            img = img.convert("P", palette=Image.ADAPTIVE,
                            colors=5).convert('RGBA')

            img = ImageEnhance.Contrast(img).enhance(3)

            img = (img.resize([64, 64], resample=Image.ADAPTIVE)).resize(
                    img.size,
                    Image.NEAREST
                )

            self.set_image(
                img
            )
"""
