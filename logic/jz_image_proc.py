from PIL import Image, ImageFilter, ImageEnhance, ImageDraw, ImageFont
from moviepy import Clip


def gaussian_blur(input_img: Image, radius: int) -> Image:
    """
    Args:
        input_img:  An image to be blurred
        radius:     The radius of the gaussian blur. Must be greater than 0

    Return:
        output_img: Blurred image. Will throw a TypeError for invalid input
    """

    if not (isinstance(input_img, Image.Image) and type(radius) == int):
        raise TypeError("ERROR (gaussian_blur): Invalid parameter types")

    if radius < 0:
        raise ValueError("ERROR (gaussian_blur): Radius is less than 0")

    output_img = input_img.filter(ImageFilter.GaussianBlur(radius))

    return output_img


def change_saturation(input_img: Image, factor: float) -> Image:
    """
    Args:
        input_img:  The image to be changed
        factor:     Enhancement factor. 0.0 give a black and white image, 1.0 gives original image
                    Value must be above 0.0

    Returns:
        output_img: Image with saturation changed
        TypeError:  Thrown if parameters are invalid types
    """

    if not (isinstance(input_img, Image.Image) and type(factor) == float):
        raise TypeError("ERROR (change_saturation): Invalid parameter types")

    if factor < 0.0:
        raise ValueError("ERROR (change_saturation): scale is less than 0.0")

    converter = ImageEnhance.Color(input_img)
    output_img = converter.enhance(factor)

    return output_img


def add_watermark_image(input_img: Image, watermark: Image, position: tuple,
                        size: float = 1.0, opacity: float = 1.0) -> Image:
    """
    Args:
        input_img:  The image (PNG) to be changed
        watermark:  The image (PNG) to be watermarked
        position:   Tuple (x, y) of where watermark should be placed
        size:       Size of image (scaled downwards).
                    Must be in range [0.0, 0.1]. Default is 1.0
        opacity:    Opacity of the image.
                    Must be in range [0.0, 0.1]. Default is 1.0

    Returns:
        output_img: Watermarked image
    """

    if not (isinstance(input_img, Image.Image) and isinstance(watermark, Image.Image)
            and type(size) == float and type(opacity) == float and position_is_valid(position)):
        raise TypeError("ERROR (add_watermark_image): Invalid parameter type")

    if not (0.0 <= size <= 1.0 and 0.0 <= opacity <= 1.0):
        raise ValueError("ERROR (add_watermark_image): size and opacity must be in range [0.0, 1.0]")

    base_img = input_img.copy()
    watermark_img = scale_image(watermark, size)
    mask = watermark_img.convert('L').point(lambda x: int(x * opacity))
    watermark_img.putalpha(mask)

    base_img.paste(watermark_img, position, watermark_img)

    return base_img


def scale_image(input_img: Image, scale: float) -> Image:
    """
    Args:
        input_img:  Image to be changed
        scale:      Scale of image. Must be in range [0.0, 1.0]

    Returns:
        output_img: Scaled down image
    """

    if not (isinstance(input_img, Image.Image) and type(scale) == float):
        raise TypeError("ERROR (scale_image): Invalid parameter types")

    if not 0.0 <= scale <= 1.0:
        raise ValueError("ERROR (scale_image): scale must be in range [0.0, 1.0]")

    output_img = input_img.copy()

    max_size = max(input_img.width * scale, input_img.height * scale)
    output_img.thumbnail((max_size, max_size), Image.ANTIALIAS)

    return output_img


def rotate_image(input_img: Image, angle: int) -> Image:
    """
    Args:
        input_img:  Image to be changed
        angle:      Angle to be rotated (in degrees)

    Returns:
        output_img: Rotated image
        TypeError:  Thrown if invalid parameter types
    """

    if not (isinstance(input_img, Image.Image) and type(angle) == int):
        raise TypeError("ERROR (rotate_image): Invalid parameter types")

    return input_img.rotate(angle, Image.NEAREST, expand=1)


# HELPER METHOD

def position_is_valid(position: tuple) -> bool:
    """
    Args:
        position:   Position

    Returns:
        is_valid:   If position is a tuple of correct type and size
    """
    if len(position) != 2:
        return False

    x, y = position

    return type(x) == int and type(y) == int
