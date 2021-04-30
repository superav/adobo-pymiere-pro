from PIL import Image, ImageEnhance, ImageDraw
import colorsys
import numpy as np

"""
Methods that change the color of the image.

Included Methods:
    * Change Saturation
    * Change Hue
    * Change Opacity
    * Recoloration Filter
    * Apply Color Gradient
"""


def change_saturation(input_img: Image, specifications: float) -> Image:
    """
    Args:
        input_img:  The image to be changed
        specifications:

            * factor:  Enhancement factor. 0.0 gives a black and white image,
            1.0 gives original image. Value must be above 0.0

    Returns:
        PIL.Image: Image with saturation changed
    """
    factor = specifications

    if not (isinstance(input_img, Image.Image)
            and (type(factor) == float or type(factor) == int)):
        return None

    if factor < 0:
        return None

    converter = ImageEnhance.Color(input_img)
    output_img = converter.enhance(factor)

    return output_img


def hue_editor(input_img: Image, specifications: int) -> Image:
    """
    Args:
        input_img:  The image to be changed
        specifications:     The hue factor that will be set

    Returns:
        PIL.Image: Image with hue changed

    References:
        * https://stackoverflow.com/questions/7274221/changing-image-hue-with-python-pil
    """
    factor = specifications

    if factor > 360 or factor < 0:
        return None

    img = input_img.convert('RGBA')
    arr = np.array(np.asarray(img).astype('float'))

    rgb_to_hsv = np.vectorize(colorsys.rgb_to_hsv)
    hsv_to_rgb = np.vectorize(colorsys.hsv_to_rgb)

    red, green, blue, alpha = np.rollaxis(arr, axis=-1)
    hue, saturation, value = rgb_to_hsv(red, green, blue)
    hue = (hue + factor / 360.) % 1
    red, green, blue = hsv_to_rgb(hue, saturation, value)
    arr = np.dstack((red, green, blue, alpha))

    output_img = Image.fromarray(arr.astype('uint8'), 'RGBA')

    return output_img


def opacity_editor(input_img: Image, specifications: int) -> Image:
    """
    Args:
        input_img:  The image to be changed
        specifications: The value determining how opaque the image will
                 be - 0 being invisible, 100 being opaque

    Returns:
        PIL.Image: Image with opacity changed
    """

    value = specifications

    if type(value) != int:
        return None

    if value > 100 or value < 0:
        return None

    input_img.putalpha(int(value * 2.55))

    return input_img


def apply_color_editor(input_img: Image,
                       specifications: list = [255, 255, 255, 255]) -> Image.Image:
    """ Applies a color filter over an image

       Args:
            input_img:  The image to be changed
            specifications: A list of four ints, being the rgba fo
                        the color mask

       Returns:
           PIL.Image: Image with color mask applied changed
    """

    red, green, blue, alpha = specifications
    if __color_val_in_range(red, green, blue):
        return None

    color = Image.new('RGB', input_img.size, (red, green, blue))
    mask = Image.new('RGBA', input_img.size, (0, 0, 0, alpha))
    output_image = Image.composite(input_img, color, mask).convert('RGB')
    return output_image


def apply_gradient_editor(input_img: Image, specifications: list) -> Image:
    """ Applies a color gradient over an image.

    Args:
        input_img:  The image to be changed
        specifications: list containing the next 3 values:

             * alpha: the alpha value of the mask to be applied
             * color_initial: A list of three ints, being the rgb for the first
             half of the color mask

             * color_secondary: A list of three ints, being the rgb for the
             second half of the color mask

    Returns:
        PIL.Image: Image with color mask applied changed

    References:
        * https://python-catalin.blogspot.com/2013/10/how-to-make-color-gradient-and-images.html
    """
    alpha = specifications[0]
    color_initial = specifications[1]
    color_secondary = specifications[2]

    red, green, blue = color_initial
    red_secondary, green_secondary, blue_secondary = color_secondary

    if __color_val_in_range(red, green, blue):
        return None
    if __color_val_in_range(red_secondary, green_secondary, blue_secondary):
        return None
    if alpha < 0 or alpha > 255:
        return None

    color = Image.new("RGB", input_img.size, "#FFFFFF")
    draw = ImageDraw.Draw(color)
    draw_red = (red_secondary - red) / input_img.width
    draw_green = (green_secondary - green) / input_img.width
    draw_blue = (blue_secondary - blue) / input_img.width

    for i in range(input_img.width):
        red, green, blue = red + draw_red, green + draw_green, blue + draw_blue
        draw.line((i, 0, i, input_img.height),
                  fill=(int(red), int(green), int(blue)))

    mask = Image.new('RGBA', input_img.size, (0, 0, 0, alpha))
    output_image = Image.composite(input_img, color, mask).convert('RGB')

    return output_image

# HELPER METHODS


def __color_val_in_range(red: int, green: int, blue: int) -> bool:
    """ Checks that all color values are in the range [0, 255]
    Args:
        red:    Red color value
        green:  Green color value
        blue:   Blue color value

    Returns:
        bool:   True if all color values are in range
    """
    if 255 >= red >= 0 and 255 >= green >= 0 and 255 >= blue >= 0:
        return False
    else:
        return True
