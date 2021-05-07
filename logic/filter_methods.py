from PIL import Image, ImageFilter, ImageOps
from flask import abort

"""
Methods that generally apply a filter over an entire image. These are
generally methods that apply a complex mathematical operation across the image.

Included Methods:
    * Gaussian Blur
    * Solarize
    * Mosaic Filter
    * Red-Eye Effect Removal
"""


def gaussian_blur(input_img: Image, specifications: int) -> Image.Image:
    """
    Args:
        input_img:  An image to be blurred

        specifications: The radius of the gaussian blur. Must be greater than 0

    Return:
        PIL.Image: Blurred image. Will throw a TypeError for invalid input
    """

    radius = specifications

    if not (isinstance(input_img, Image.Image)):
        error = "gaussian_blur: Input image is not of type PIL Image"
        abort(500, description=error)

    if not type(radius) == int:
        error = "gaussian_blur: radius is not of type int"
        abort(500, description=error)

    if radius < 0:
        error = "gaussian_blur: radius is less than 0"
        abort(500, description=error)

    output_img = input_img.filter(ImageFilter.GaussianBlur(radius))

    return output_img


def apply_solarize(input_img: Image, specifications: int) -> Image:
    """ Inverts the color of pixels above a given greyscale threshold

    Args:
        input_img:  The image to be changed
        specifications: int to determine the threshold of the solarization
            effect. Should be in range [0, 255]

    Returns:
        PIL.Image: Image with color mask applied changed
    """
    if not (isinstance(input_img, Image.Image)):
        error = "apply_solarize: Input image is not of type PIL Image"
        abort(500, description=error)
    if not type(specifications) == int:
        error = "apply_solarize: specifications is not of type int"
        abort(500, description=error)
    if specifications < 0 or specifications > 255:
        error = "apply_solarize: specifications is not in range [0, 255]"
        abort(500, description=error)
    if input_img.mode == 'RGBA':
        rgb_image = __convert_to_rgb(input_img.copy())
    else:
        rgb_image = input_img

    output_img = ImageOps.solarize(rgb_image, threshold=specifications)
    return output_img.convert('RGBA')


def apply_mosaic_filter(input_img: Image) -> Image:
    """ Applies a mosaic filter to an image

    Args:
        input_img:  The image to be changed

    Returns:
        PIL.Image: Image with color mask applied changed

    References:
        * https://stackoverflow.com/questions/47143332/how-to-pixelate-a-square-image-to-256-big-pixels-with-python
    """
    if not (isinstance(input_img, Image.Image)):
        error = "apply_mosaic_filter: Input image is not of type PIL Image"
        abort(500, description=error)
    output_img = input_img.resize((32, 32), resample=Image.BILINEAR)

    return output_img.resize(input_img.size, Image.NEAREST)


def apply_red_eye_filter(input_img: Image, specifications: list) -> Image:
    """ Removes red eye effect in a given area

    Args:
        input_img:  Input image
        specifications: List of integers denoting area to perform red eye
            removal.

            * Integers should be in this format: [left x value, top y value,
            right x value, bottom y value]

    Returns:
        PIL.Image: Image with red eye removed

    References:
        * https://learnopencv.com/automatic-red-eye-remover-using-opencv-cpp-python/
    """
    if not (isinstance(input_img, Image.Image)):
        error = "apply_red_eye_filter: Input image is not of type PIL Image"
        abort(500, description=error)
    if not type(specifications) == list:
        error = "apply_red_eye_filter: specifications is not of type list"
        abort(500, description=error)
    if len(specifications) != 4:
        error = "apply_red_eye_filter: specifications is not a list of length 4"
        abort(500, description=error)
    for spec in range(4):
        if not type(specifications[spec]) == int:
            error = "apply_red_eye_filter: specifications contains non-integer value"
            abort(500, description=error)

    input_img.load()

    output_img = Image.new("RGB", input_img.size, (255, 255, 255))
    output_img.paste(input_img, mask=input_img.split()[3])

    pixels = output_img.load()
    left_side_x, top_side_y, right_side_x, bottom_side_y = specifications

    for row in range(output_img.size[0]):
        for column in range(output_img.size[1]):
            red, green, blue = pixels[row, column]

            if left_side_x < row < right_side_x and \
                    top_side_y < column < bottom_side_y and \
                    150 > red > 2 * green and red > 2 * blue:
                pixels[row, column] = (int(red / 5), green, blue)

    return output_img

# HELPER METHODS


def __convert_to_rgb(image: Image):
    """Converts an RGBA image to RGB

    Args:
        image: RGBA image

    Returns:
        PIL.Image: converted RGB image
    """
    image.load()
    background = Image.new('RGB', image.size, (255, 255, 255))
    background.paste(image, mask=image.split()[3])
    return background
