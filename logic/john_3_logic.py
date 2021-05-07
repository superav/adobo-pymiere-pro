from logic.overlay_methods import add_text_to_image
from PIL import Image
from flask import abort


def generate_meme_text(image: Image, specifications: list) -> Image:
    """
    Args:
        image: image to add meme text to
        specifications: list containing the next two values

            * top_text: the text to be added to the top of the image
            * bottom_text: the text to be added to the bottom of the image
    Return:
        PIL.Image: Image with text added on top. Returns ``None`` if unsuccessful.
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
