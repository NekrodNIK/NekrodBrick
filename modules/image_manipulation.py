from PIL import Image, ImageEnhance, ImageOps


def gen_pixelize_image(image: Image,
                       number_pixel: int = 100,
                       color_count: int = 5,
                       contrast_value: float = 1,
                       invert_colors: bool = False,
                       monochrome: bool = False) -> Image:
    image_filtered = image.convert("P",
                                   palette=Image.ADAPTIVE,
                                   colors=color_count).convert("RGB")
    image_filtered = \
        ImageEnhance.Contrast(image_filtered).enhance(contrast_value)

    image_filtered = \
        ImageOps.invert(image_filtered) if invert_colors else image_filtered

    image_filtered = \
        image_filtered.convert("L") if monochrome else image_filtered

    image_pixilize = image_filtered.resize((number_pixel, number_pixel), resample=Image.ADAPTIVE).resize(image.size,
                                                                                                         resample=Image.NEAREST)

    return image_pixilize
