from PIL import Image, ImageFont, ImageDraw


def add_text_to_image(image=Image, specifications: list = [str, str, int, list, list]) -> Image:
    """
    Args:
        image: image to add text to
        specifications: list containing the next three values ->

            text: the text to be added on top of the image
            font: the font type of the added text
            size: the size of the added text 
            offset: an (x,y) tuple containing coordinates for text offset on the image
            color: an (R,G,B) tuple containing the color values for the text

    Return:
        output_img: Image with text added on top. Returns None if unsuccessful.
    """
    text = specifications[0]
    font = specifications[1]
    size = specifications[2]
    offset = tuple(specifications[3])
    color = tuple(specifications[4])

    valid_parameters = isinstance(image, Image.Image)
    valid_parameters = valid_parameters and len(specifications) == 5
    valid_parameters = valid_parameters and isinstance(text, str)
    valid_parameters = valid_parameters and isinstance(font, str)
    valid_parameters = valid_parameters and isinstance(size, int)
    valid_parameters = valid_parameters and isinstance(offset, tuple)
    valid_parameters = valid_parameters and isinstance(color, tuple)
    if not valid_parameters:
        return None
    if len(offset) != 2 or len(color) != 3:
        return None
    font = ImageFont.truetype(font, size)
    draw = ImageDraw.Draw(image)
    draw.text(offset, text, color, font=font)
    return image


def store_image_in_filesystem(image=Image, filename=str) -> Image:
    """
    Args:
        image: Image to be stored in local filesystem
        filename: Name to give to new stored file

    Return:
        output_img: Image that was saved to local filesystem. Returns None if unsuccessful.
    """
    valid_parameters = isinstance(image, Image.Image)
    valid_parameters = valid_parameters and isinstance(filename, str)
    if not valid_parameters:
        return None
    image.save(filename)
    return image
