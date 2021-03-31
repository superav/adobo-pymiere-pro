from PIL import Image, ImageFilter, ImageEnhance, ImageDraw, ImageFont


def gaussian_blur(input_img: Image, radius: int) -> Image:
    """
    Args:
        input_img:  An image to be blurred
        radius:     The radius of the gaussian blur

    Return:
        output_img: Blurred image
    """

    output_img = input_img.filter(ImageFilter.GaussianBlur(radius))

    return output_img


def change_saturation(input_img: Image, factor: float) -> Image:
    """
    Args:
        input_img:  The image to be changed
        factor:     Enhancement factor. 0.0 give a black and white image, 1.0 gives original image

    Returns:
        output_img: Image with saturation changed
    """

    converter = ImageEnhance.Color(input_img)
    output_img = converter.enhance(factor)

    return output_img


def add_watermark_text(input_img: Image, position: int, font: str = 'arial.ttf',
                       size: int = 12, color: tuple = (255, 255, 255, 255)) -> Image:
    """
    Args:
        input_img:  The image to be changed
        position:   Where the watermark is located on the image
        font:       Font of image. Default is Arial.
        size:       Size of text. Default is 12.
        color:      Color (RGBA value) of text. Default is solid white.

    Returns:
        output_img: Watermarked image
    """
    # https://www.tutorialspoint.com/python_pillow/python_pillow_creating_a_watermark.htm
    watermark_font = ImageFont.truetype(font, size)
    draw = ImageDraw.Draw(input_img)
    pass


def scale_image(input_img: Image, scale: float) -> Image:
    """
    Args:
        input_img:  Image to be changed
        scale:      Scale of image. Must be in range [0.0, 1.0]
    """
    # https://stackoverflow.com/questions/24745857/python-pillow-how-to-scale-an-image
    pass


def rotate_image(input_img: Image, angle: float) -> Image:
    # https://pythonexamples.org/python-pillow-rotate-image-90-180-270-degrees/
    pass


def rotate_video():
    pass
