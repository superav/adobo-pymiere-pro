from PIL import Image, ImageFilter, ImageEnhance


def gaussian_blur(input_img: Image, specifications: list) -> Image:
    """
    Args:
        input_img:  An image to be blurred

        specifications: The radius of the gaussian blur. Must be greater than 0

    Return:
        PIL.Image: Blurred image. Will throw a TypeError for invalid input
    """

    radius = specifications[0]

    if not (isinstance(input_img, Image.Image) and type(radius) == int):
        return None

    if radius < 0:
        return None

    output_img = input_img.filter(ImageFilter.GaussianBlur(radius))

    return output_img


def change_saturation(input_img: Image, specifications: list) -> Image:
    """
    Args:
        input_img:  The image to be changed
        specifications:
            * factor:  Enhancement factor.
                * 0.0 give a black and white image, 1.0 gives original image. Value must be above 0.0

    Returns:
        PIL.Image: Image with saturation changed
    """
    factor = specifications[0]

    if not (isinstance(input_img, Image.Image) and type(factor) == float):
        return None

    if factor < 0:
        return None

    print("paramters validated")
    converter = ImageEnhance.Color(input_img)
    output_img = converter.enhance(factor)
    print("output image found")
    return output_img


def add_watermark_image(input_img: Image, specifications: list) -> Image:
    """ Adds a watermark image on top of the base image

    Args:
        input_img:  The image (PNG) to be changed
        specifications:

            * watermark:  The image (PNG) to be watermarked
            * position:   Tuple (x, y) of where watermark should be placed
            * size:       Size of image (scaled downwards). Must be in range [0.0, 0.1]. Default is 1.0
            * opacity:    Opacity of the image. Must be in range [0.0, 0.1]. Default is 1.0

    Returns:
        PIL.Image: Watermarked image
    """

    if not __watermark_specifications_are_valid(specifications):
        return None

    if not isinstance(input_img, Image.Image):
        return None

    watermark = specifications[0]
    position = specifications[1]
    size = specifications[2]
    opacity = specifications[3]

    base_img = input_img.copy()
    watermark_img = scale_image(watermark, size)
    mask = watermark_img.convert('L').point(lambda x: int(x * opacity))
    watermark_img.putalpha(mask)

    base_img.paste(watermark_img, position, watermark_img)

    return base_img


def scale_image(input_img: Image, specifications: list) -> Image:
    """
    Args:
        input_img:  Image to be changed
        specifications: Scale of image. Must be in range [0.0, 1.0]

    Returns:
        PIL.Image: Scaled down image
    """

    scale = specifications[0]

    if not isinstance(input_img, Image.Image):
        return None

    if not (type(scale) == float and 0.0 <= scale <= 1.0):
        return None

    output_img = input_img.copy()

    max_size = max(input_img.width * scale, input_img.height * scale)
    output_img.thumbnail((max_size, max_size), Image.ANTIALIAS)

    return output_img


def rotate_image(input_img: Image, specifications: int) -> Image:
    """
    Args:
        input_img:  Image to be changed
        specifications: Angle to be rotated (in degrees)

    Returns:
        PIL.Image: Rotated image
    """

    angle = specifications

    if not (isinstance(input_img, Image.Image) and type(angle) == int):
        return None

    return input_img.rotate(angle, Image.NEAREST, expand=1)


# HELPER METHODS

def __position_is_valid(position: tuple) -> bool:
    """
    Args:
        position:   Position

    Returns:
        bool:   If position is a tuple of correct type and size
    """
    if len(position) != 2:
        return False

    x, y = position

    return type(x) == int and type(y) == int


def __watermark_specifications_are_valid(specifications: list):
    """
    Args:
        specifications:
            * watermark:  The image (PNG) to be watermarked
            * position:   Tuple (x, y) of where watermark should be placed
            * size:       Size of image (scaled downwards).
                Must be in range [0.0, 0.1]. Default is 1.0

            * opacity:    Opacity of the image. Must be in range [0.0, 0.1]. Default is 1.0

    Returns:
        bool:   True if all specification types and values are valid
    """

    if type(specifications) != list or len(specifications) != 4:
        return False

    watermark = specifications[0]
    position = specifications[1]
    size = specifications[2]
    opacity = specifications[3]

    if not (isinstance(watermark, Image.Image)
            and type(size) == float and type(opacity)):
        return False

    if type(position) != tuple:
        return False

    if not __position_is_valid(position):
        return False

    if not (0.0 <= size <= 1.0 and 0.0 <= opacity <= 1.0):
        return False

    return True
