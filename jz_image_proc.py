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


def add_watermark_text(input_img: Image, text: str, position: tuple, font: str = 'arial.ttf',
                       size: int = 12, color: tuple = (255, 255, 255, 255)) -> Image:
    """
    Args:
        input_img:  The image to be changed
        text:       Text of watermark
        position:   Tuple (x, y) of where watermark should be placed
        font:       Font of image. Default is Arial.
        size:       Size of text. Default is 12.
        color:      Color (RGBA value) of text. Default is solid white.

    Returns:
        output_img: Watermarked image
    """
    # https://www.tutorialspoint.com/python_pillow/python_pillow_creating_a_watermark.htm
    watermark_font = ImageFont.truetype(font, size)
    draw = ImageDraw.Draw(input_img)

    draw.text(position, text, fill=color, font=watermark_font)

    return input_img


def scale_image(input_img: Image, scale: float) -> Image:
    """
    Args:
        input_img:  Image to be changed
        scale:      Scale of image. Must be in range [0.0, 1.0]

    Returns:
        output_img: Scaled down image
    """
    # https://stackoverflow.com/questions/24745857/python-pillow-how-to-scale-an-image

    max_size = max(input_img.width * scale, input_img.height * scale)
    input_img.thumbnail((max_size, max_size), Image.ANTIALIAS)

    return input_img


def rotate_image(input_img: Image, angle: float) -> Image:
    """
    Args:
        input_img:  Image to be changed
        angle:      Angle to be rotated (in degrees)

    Returns:
        output_img: Rotated image
    """
    # https://pythonexamples.org/python-pillow-rotate-image-90-180-270-degrees/

    return input_img.rotate(angle)


def rotate_video():
    pass
