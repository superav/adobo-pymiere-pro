from PIL import Image, ImageFilter, ImageEnhance, ImageDraw, ImageFont
from moviepy import Clip


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
                       size: int = 36, color: tuple = (255, 255, 255, 255)) -> Image:
    """
    Args:
        input_img:  The image (PNG) to be changed
        text:       Text of watermark
        position:   Tuple (x, y) of where watermark should be placed
        font:       Font of image. Default is Arial.
        size:       Size of text. Default is 36.
        color:      Color (RGBA value) of text. Default is solid white.

    Returns:
        output_img: Watermarked image
    """
    # https://www.tutorialspoint.com/python_pillow/python_pillow_creating_a_watermark.htm
    base_img = input_img.copy()
    text_layer = Image.new("RGBA", base_img.size, (255, 255, 255, 0))
    watermark_font = ImageFont.truetype(font, size)
    draw = ImageDraw.Draw(text_layer)

    draw.text(position, text, fill=color, font=watermark_font)

    output_img = Image.alpha_composite(base_img, text_layer)

    return output_img


def scale_image(input_img: Image, scale: float) -> Image:
    """
    Args:
        input_img:  Image to be changed
        scale:      Scale of image. Must be in range [0.0, 1.0]

    Returns:
        output_img: Scaled down image
    """
    # https://stackoverflow.com/questions/24745857/python-pillow-how-to-scale-an-image

    if not 0.0 <= scale <= 1.0:
        return None

    output_img = input_img.copy()

    max_size = max(input_img.width * scale, input_img.height * scale)
    output_img.thumbnail((max_size, max_size), Image.ANTIALIAS)

    return output_img


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


def rotate_video(input_clip: Clip, angle: float):
    """
    Args:
        input_clip: Video clip to be rotated
        angle:      Angle of rotation (in degrees)

    Returns:
        output_clip: Rotated video
    """

    return input_clip.mask.rotate(angle)


def import_image():
    pass
