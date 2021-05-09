from PIL import Image, ImageFilter, ImageOps
import cv2
import numpy as np
from flask import abort

"""
Methods that generally apply a filter over an entire image. These are
generally methods that apply a complex mathematical operation across the image.

Included Methods:
    * Gaussian Blur
    * Solarize
    * Mosaic Filter
    * Red-Eye Effect Removal
    * Add Vignette to Image
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


def apply_vignette(input_img: Image) -> Image:
    """
        Args:
            input_img:  The image to be changed

        Returns:
            PIL.Image: Image with vignette applied
    """
    # https://www.geeksforgeeks.org/create-a-vignette-filter-using-python-opencv/
    if not isinstance(input_img, Image.Image):
        abort(500, description="apply_contrast: invalid input types")

    # helper to convert to cv
    input_img = __convert_to_rgb(input_img)
    input_cv = __pil_to_cv(input_img)

    # Extracting the height and width of an image
    rows, cols = input_cv.shape[:2]

    # generating vignette mask using Gaussian resultant_kernels
    x_resultant_kernel = cv2.getGaussianKernel(cols, int(cols/2.4))
    y_resultant_kernel = cv2.getGaussianKernel(rows, int(rows/2.4))

    # generating resultant_kernel matrix
    resultant_kernel = y_resultant_kernel * x_resultant_kernel.T

    # creating mask and normalising by using np.linalg function
    mask = 255 * resultant_kernel / np.linalg.norm(resultant_kernel)
    output = np.copy(input_cv)

    # applying the mask to each channel in the input image
    for i in range(3):
        output[:, :, i] = output[:, :, i] * mask

    # helper to convert to pil
    output_img = __cv_to_pil(output)

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


def __cv_to_pil(input_img):
    """
        Args:
            input_img:  CV2 image to be converted to PIL

        Returns:
            output_img: new PIL image
    """
    # https://stackoverflow.com/questions/43232813/convert-opencv-image-format-to-pil-image-format
    cv_image = cv2.cvtColor(input_img, cv2.COLOR_BGR2RGB)
    output_img = Image.fromarray(cv_image)

    return output_img


def __pil_to_cv(input_img):
    """
        Args:
            input_img:  Pillow image to be converted to CV2

        Returns:
            output_img: new CV2 image
    """
    # https://stackoverflow.com/questions/14134892/convert-image-from-pil-to-opencv-format
    open_cv_image = np.array(input_img)
    output_img = open_cv_image[:, :, ::-1].copy()

    return output_img
