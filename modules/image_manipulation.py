from PIL import Image, ImageEnhance, ImageOps


def gen_pixelize_image(image: Image,
                       number_pixel: int = 100,
                       color_count: int = 5,
                       contrast_value: float = 1,
                       invert_colors: bool = False,
                       monochrome: bool = False) -> Image:

    image_man = image.resize((number_pixel, number_pixel), resample=Image.ADAPTIVE).resize(
        image.size,
        resample=Image.NEAREST)

    image_man = \
        ImageEnhance.Contrast(image_man).enhance(contrast_value)

    image_man = \
        ImageOps.invert(image_man) if invert_colors else image_man

    image_man = \
        image_man.convert("L") if monochrome else image_man

    image_man = image_man.convert("P",
                                   palette=Image.ADAPTIVE,
                                   colors=color_count).convert("RGB")

    return image_man
