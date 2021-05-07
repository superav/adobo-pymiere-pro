import cv2
import numpy as np
from PIL import Image, ImageOps, ImageEnhance
from flask import abort


def apply_contrast(input_img: Image, specifications: int) -> Image:
    """
        Args:
            input_img:  The image to be changed
            specifications: int to determine the percent of the lightest and
                            darkest pixels from the pixel histogram and remaps
                            them

        Returns:
            output_img: Image with contrast changed
    """
    cutoff = int(abs((specifications/2)))

    if not isinstance(input_img, Image.Image):
        abort(500, description="apply_contrast: invalid input image")
    if type(specifications) != int:
        abort(500, description="apply_contrast: invalid int input")

    if cutoff >= 50:
        cutoff = 49
    if cutoff < 0:
        cutoff = 0
    input_img = input_img.convert("RGB")
    output_img = ImageOps.autocontrast(input_img, cutoff, None)
    return output_img


def apply_autocontrast(input_img: Image) -> Image:
    """
        Args:
            input_img:  The image to be changed

        Returns:
            output_img: Image with contrast changed
    """
    if not isinstance(input_img, Image.Image):
        abort(500, description="apply_contrast: invalid input types")

    input_img = input_img.convert("RGB")
    output_img = ImageOps.autocontrast(input_img, None)
    return output_img


def apply_brightness(input_img: Image, specifications: int) -> Image:
    """
        Args:
            input_img:  The image to be changed
            specifications: int from 0 to 1, to determine how dark or
                            light to make the image

        Returns:
            output_img: Image with brightness changed
    """
    if not isinstance(input_img, Image.Image):
        abort(500, description="apply_contrast: invalid input image")
    if type(specifications) != int and type(specifications) != float:
        abort(500, description="apply_contrast: invalid int/float input")

    value = specifications * 2
    enhancer = ImageEnhance.Brightness(input_img)
    output_img = enhancer.enhance(value)
    return output_img


def apply_vignette(input_img: Image) -> Image:
    """
        Args:
            input_img:  The image to be changed

        Returns:
            output_img: Image with vignette applied
    """
    # https://www.geeksforgeeks.org/create-a-vignette-filter-using-python-opencv/
    if not isinstance(input_img, Image.Image):
        abort(500, description="apply_contrast: invalid input types")

    # helper to convert to cv
    input_img = input_img.convert("RGB")
    input_cv = pil_to_cv(input_img)

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
    output_img = cv_to_pil(output)

    return output_img


def pil_to_cv(input_img):
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


def cv_to_pil(input_img):
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
