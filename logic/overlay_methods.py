import os.path as path

from PIL import Image, ImageFont, ImageDraw
from logic.canvas_editing_methods import scale_image
from flask import abort

"""
Methods that overlay text or image(s) over the input image.

Included Methods:
    * Text over Image
    * Watermark
    * Generate Meme Text
    * Add Emoji to Image
"""


def add_text_to_image(image: Image, specifications: list) -> Image:
    """
    Args:
        image: image to add text to
        specifications: list containing the next three values:

            * text: the text to be added on top of the image
            * font: the font type of the added text
            * size: the size of the added text
            * offset: an (x,y) tuple containing coordinates for text offset on
            the image

            * color: an (R,G,B) tuple containing the color values for the text

    Return:
        PIL.Image: Image with text added on top
    """
    text = specifications[0]
    font = specifications[1]
    size = specifications[2]
    offset = tuple(specifications[3])
    color = tuple(specifications[4])

    if not isinstance(image, Image.Image):
        error = "add_text_to_image: Input image must be of type PIL.Image"
        abort(500, description=error)

    if not __specifications_are_valid(specifications):
        error = "add_text_to_image: Invalid specifications"
        abort(500, description=error)

    if len(offset) != 2 or len(color) != 3:
        error = "add_text_to_image: offset or color are wrong length"
        abort(500, description=error)

    try:
        font = ImageFont.truetype(font, size)
    except OSError:
        print("Reverting to default font and font size")

        font = ImageFont.load_default()

    draw = ImageDraw.Draw(image)
    draw.text(offset, text, color, font=font)

    return image


def add_watermark_image(input_img: Image, specifications: list) -> Image.Image:
    """ Adds a watermark image on top of the base image

    Args:
        input_img:  The image (PNG) to be changed
        specifications:

            * watermark:  The watermark image
            * position:   List [x, y] of where watermark should be placed
            * size:       Size of image (scaled downwards). Must be in range
            [0.0, 0.1]. Default is 1.0

            * opacity:    Opacity of the image. Must be in range [0.0, 0.1].
            Default is 1.0

    Returns:
        PIL.Image: Watermarked image
    """

    if not __watermark_specifications_are_valid(specifications):
        error = "add_watermark_image: Invalid specifications"
        abort(500, description=error)

    if not isinstance(input_img, Image.Image):
        error = "add_watermark_image: Input image must be of type PIL.Image"
        abort(500, description=error)

    watermark = specifications[0]
    position = specifications[1]
    size = specifications[2]
    opacity = specifications[3]

    base_img = input_img.copy()
    watermark_img = scale_image(watermark, size)
    mask = watermark_img.convert('L').point(lambda pixel: int(pixel * opacity))
    watermark_img.putalpha(mask)

    base_img.paste(watermark_img, position, watermark_img)

    return base_img


def generate_meme_text(image: Image, specifications: list) -> Image:
    """
    Args:
        image: image to add meme text to
        specifications: list containing the next two values

            * top_text: the text to be added to the top of the image
            * bottom_text: the text to be added to the bottom of the image
    Return:
        PIL.Image: Image with text added on top.
    """
    if not (isinstance(image, Image.Image)):
        error = "generate_meme_text: Input image is not of type PIL Image"
        abort(500, description=error)

    if not type(specifications) == list:
        error = "generate_meme_text: specifications is not of type list"
        abort(500, description=error)

    if len(specifications) != 2:
        error = "generate_meme_text: specifications is not of length 2"
        abort(500, description=error)

    top_text = specifications[0]
    bottom_text = specifications[1]

    if not isinstance(top_text, str):
        error = "generate_meme_text: top text is not of type string"
        abort(500, description=error)

    if not isinstance(bottom_text, str):
        error = "generate_meme_text: bottom text is not of type string"
        abort(500, description=error)

    font = "comic_sans.ttf"
    width, height = image.size
    size = int(height / 10)
    color = (0, 250, 255)
    top_offset = (int(width / 10), int(height / 20))
    bottom_offset = (int(width / 10), int((height * 8) / 10))
    image = add_text_to_image(image, [top_text, font, size, top_offset, color])
    image = add_text_to_image(image, [bottom_text, font, size, bottom_offset, color])

    return image


def add_emoji_overlay(input_image: Image, specifications: list,
                      is_test: bool = False) -> Image:
    """
    Args:
        input_image: Input image
        specifications:

            * watermark:  The filename for the emoji image
            * position:   List [x, y] of where watermark should be placed
            * size:       Size of image (scaled downwards). Must be in range
            [0.0, 0.1]. Default is 1.0

            * opacity:    Opacity of the image. Must be in range [0.0, 0.1].
            Default is 1.0

        is_test: Boolean for unit testing. Default is False

    Returns:
        PIL.Image:  Emojified image
    """

    watermark_file = specifications[0]

    if type(watermark_file) != str:
        error = "add_emoji_overlay: specifications[0] should be a string"
        abort(500, description=error)

    if watermark_file[-4:] != '.png':
        error = "add_emoji_overlay: emoji file %s should have \".png\" extension" % watermark_file
        abort(500, description=error)

    # TODO: Might have to fix this for Docker
    if is_test:
        watermark_path = path.abspath("../ui/pymiere/public/emojis/%s"
                                      % watermark_file)
    else:
        watermark_path = path.abspath("./ui/pymiere/public/emojis/%s"
                                      % watermark_file)

    try:
        watermark_image = Image.open(watermark_path)
        specifications[0] = watermark_image
        return add_watermark_image(input_image, specifications)

    except FileNotFoundError:
        error = "add_emoji_overlay: %s not found" % watermark_path
        abort(500, description=error)

# HELPER METHOD


def __specifications_are_valid(specifications: list) -> bool:
    """ Checks that specification values are valid

    Args:
        specifications: specifications being passed in

    Returns:
        bool: True if specifications are of correct type and value
    """
    if len(specifications) != 5:
        return False

    text = specifications[0]
    font = specifications[1]
    size = specifications[2]
    offset = tuple(specifications[3])
    color = tuple(specifications[4])

    if not (isinstance(text, str) and isinstance(font, str)):
        return False

    if not (isinstance(size, int)):
        return False

    if not (isinstance(offset, tuple) and __position_is_valid(offset)):
        return False

    if not (isinstance(color, tuple) and __colors_in_valid_range(color)):
        return False

    return True


def __colors_in_valid_range(color: tuple) -> bool:
    """ Checks that RGB color tuple is of correct type and value

    Args:
        color: Tuple of RGB color value, should be integers in range [0, 255]

    Returns:
        bool: True if color tuple is of correct type and value
    """
    if len(color) != 3:
        return False

    red, green, blue = color

    if not (isinstance(red, int) and isinstance(green, int)
            and isinstance(blue, int)):
        return False

    if not (0 <= red <= 255 and 0 <= green <= 255 and 0 <= blue <= 255):
        return False

    return True


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

            * opacity:    Opacity of the image. Must be in range [0.0, 0.1].
                Default is 1.0

    Returns:
        bool:   True if all specification types and values are valid
    """

    if type(specifications) != list or len(specifications) != 4:
        return False

    watermark = specifications[0]
    position = specifications[1]
    size = specifications[2]
    opacity = specifications[3]

    if not isinstance(watermark, Image.Image):
        return False
    if not ((type(size) == float or type(size) == int)
            and (type(opacity) or type(opacity) == int)):
        return False

    if not (type(position) == list or type(position) == tuple):
        return False

    if not __position_is_valid(position):
        return False

    if not (0.0 <= size <= 1.0 and 0.0 <= opacity <= 1.0):
        return False

    return True
