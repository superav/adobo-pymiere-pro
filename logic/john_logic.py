from PIL import Image, ImageFont, ImageDraw


def add_text_to_image(image=Image, specifications: list = [str, str, int, list, list]) -> Image:
    """
    Args:
        image: image to add text to
        specifications: list containing the next three values:

            * text: the text to be added on top of the image
            * font: the font type of the added text
            * size: the size of the added text
            * offset: an (x,y) tuple containing coordinates for text offset on the image
            * color: an (R,G,B) tuple containing the color values for the text

    Return:
        PIL.Image: Image with text added on top. Returns ``None`` if unsuccessful.
    """
    text = specifications[0]
    font = specifications[1]
    size = specifications[2]
    offset = tuple(specifications[3])
    color = tuple(specifications[4])

    if not isinstance(image, Image.Image):
        return None

    if not __specifications_are_valid(specifications):
        return None

    if len(offset) != 2 or len(color) != 3:
        return None

    try:
        font = ImageFont.truetype(font, size)
    except OSError:
        print("Reverting to default font and font size")

        font = ImageFont.load_default()

    draw = ImageDraw.Draw(image)
    draw.text(offset, text, color, font=font)

    return image

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

    if not (isinstance(offset, tuple) and __offset_is_valid(offset)):
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

    if not (isinstance(red, int) and isinstance(green, int) and isinstance(blue, int)):
        return False

    if not (0 <= red <= 255 and 0 <= green <= 255 and 0 <= blue <= 255):
        return False

    return True


def __offset_is_valid(offset: tuple) -> bool:
    """ Checks that offset is correct value and type

    Args:
        offset: A position tuple (x, y)

    Returns:
        bool: True if offset of correct type
    """
    if len(offset) != 2:
        return False

    x_position, y_position = offset

    if not (isinstance(x_position, int) and isinstance(y_position, int)):
        return False

    return True
