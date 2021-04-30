from PIL import Image

"""
Methods that change the size, scale, or rotation of the image.

Included Methods:
    * Scale Image
    * Rotate Image
    * Crop Image
"""


def scale_image(input_img: Image, specifications: float) -> Image:
    """
    Args:
        input_img:  Image to be changed
        specifications: Scale of image. Must be in range [0.0, 1.0]

    Returns:
        PIL.Image: Scaled down image
    """

    scale = specifications

    if not isinstance(input_img, Image.Image):
        return None

    if not ((type(scale) == float or type(scale) == int)
            and 0.0 < scale <= 1.0):
        return None

    output_img = input_img.copy()

    max_size = max(input_img.width * scale, input_img.height * scale)
    output_img.thumbnail((max_size, max_size), Image.ANTIALIAS)

    return output_img


def rotate_image(input_img: Image, specifications: int) -> Image.Image:
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


def crop_editor(input_img: Image,
                specifications: list = [int, int, int, int]) -> Image.Image:
    """
    Args:
        input_img:  The image to be changed
        specifications:list of 4 floats, being the left, top, right, bottom,
                    of where the image is to be cropped by pixel count, that
                    have to be within the image size

    Returns:
        PIL.Image: Image that has been cropped
    """

    left, top, right, bottom = specifications
    width, height = input_img.size

    if not __crop_in_given_dimensions(width, height, top, left, right, bottom):
        return None

    output_img = input_img.crop((left, top, right, bottom))

    return output_img

# HELPER METHODS


def __crop_in_given_dimensions(width: int, height: int, top: int, left: int,
                               right: int, bottom: int) -> bool:
    """
    Args:
        width: width to be checked
        height: height to be checked
        top: top y coordinate
        left: left x coordinate
        right: right x coordinate
        bottom: bottom y coordinate

    Returns:
        bool: bool that says if the crop will fit in the dimensions
    """
    if width >= right > left >= 0 and height >= bottom > top >= 0:
        return True
    else:
        return False
