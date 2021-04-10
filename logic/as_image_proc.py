from PIL import Image, ImageDraw
import numpy as np
import colorsys


def hue_editor(input_img: Image, hue: int) -> Image:
    """
       Args:
           input_img:  The image to be changed
           hue:     The hue factor that will be set -

       Returns:
           output_img: Image with hue changed
    """
    #https://stackoverflow.com/questions/7274221/changing-image-hue-with-python-pil

    if hue > 360 or hue < 0:
        return None

    img = input_img.convert('RGBA')
    arr = np.array(np.asarray(img).astype('float'))

    rgb_to_hsv = np.vectorize(colorsys.rgb_to_hsv)
    hsv_to_rgb = np.vectorize(colorsys.hsv_to_rgb)

    r, g, b, a = np.rollaxis(arr, axis=-1)
    h, s, v = rgb_to_hsv(r, g, b)
    h = (h + hue / 360.) % 1
    r, g, b = hsv_to_rgb(h, s, v)
    arr = np.dstack((r, g, b, a))

    output_img = Image.fromarray(arr.astype('uint8'), 'RGBA')
    return output_img


def crop_editor(input_img: Image,
                bounds: list = [int, int, int, int]) -> Image:
    """
       Args:
           input_img:  The image to be changed
           bounds:     list of 4 floats, being the left, top, right, bottom,
                       of where the image is to be cropped by pixel count, that
                       have to be within the image size

       Returns:
           output_img: Image that has been cropped
    """

    left, top, right, bottom = bounds
    w, h = input_img.size
    if left >= w or right >= w or top >= h or bottom >= h \
            or right <= left or bottom <= top or left < 0 or top < 0:
        return None
    output_img = input_img.crop((left, top, right, bottom))
    return output_img


def opacity_editor(input_img: Image, alpha: int) -> Image:
    """
       Args:
               input_img:  The image to be changed
               alpha:      The value determining how opaque the image will be -
                           0 being invisible, 100 being opaque

       Returns:
           output_img: Image with opacity changed
    """

    if alpha > 100 or alpha < 0:
        return None

    input_img.putalpha(int(alpha * 2.55))
    return input_img


def apply_color_editor(input_img: Image,
                       color_mask: list = [255, 255, 255, 255]) -> Image:
    """
       Args:
            input_img:  The image to be changed
            color_mask: A list of four ints, being the rgba for the color
                        mask

       Returns:
           output_img: Image with color mask applied changed
    """

    r, g, b, a = color_mask
    if r < 0 or g < 0 or b < 0 or a < 0 or \
            r > 255 or g > 255 or b > 255 or a > 255:
        return None

    color = Image.new('RGB', input_img.size, (r, g, b))
    mask = Image.new('RGBA', input_img.size, (0, 0, 0, a))
    output_image = Image.composite(input_img, color, mask).convert('RGB')
    return output_image


def apply_gradient_editor(input_img: Image, alpha: int,
                          color_initial: list = [255, 255, 255],
                          color_secondary: list = [255, 255, 255]) -> Image:
    """
       Args:
           input_img:  The image to be changed
           alpha: the alpha value of the mask to be applied
           color_initial: A list of three ints, being the rgb for the first
                          half of the color mask
           color_secondary: A list of three ints, being the rgb for the
                            second half of the color mask

       Returns:
           output_img: Image with color mask applied changed
    """
    #https://python-catalin.blogspot.com/2013/10/how-to-make-color-gradient-and-images.html

    r, g, b = color_initial
    r2, g2, b2 = color_secondary

    if r < 0 or g < 0 or b < 0 or r > 255 or g > 255 or b > 255:
        return None
    if r2 < 0 or g2 < 0 or b2 < 0 or r2 > 255 or g2 > 255 or b2 > 255:
        return None
    if alpha < 0 or alpha > 255:
        return None

    color = Image.new("RGB", input_img.size, "#FFFFFF")
    draw = ImageDraw.Draw(color)
    dr = (r2 - r) / input_img.width
    dg = (g2 - g) / input_img.width
    db = (b2 - b) / input_img.width
    for i in range(input_img.width):
        r, g, b = r + dr, g + dg, b + db
        draw.line((i, 0, i, input_img.height), fill=(int(r), int(g), int(b)))

    mask = Image.new('RGBA', input_img.size, (0, 0, 0, alpha))
    output_image = Image.composite(input_img, color, mask).convert('RGB')
    return output_image
