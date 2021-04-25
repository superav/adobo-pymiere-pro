from PIL import Image, ImageDraw, ImageOps
import numpy as np
import colorsys


def hue_editor(input_img: Image, specifications: int) -> Image.Image:
    """
       Args:
           input_img:  The image to be changed
           specifications:     The hue factor that will be set -

       Returns:
           PIL.Image: Image with hue changed
    """
    # https://stackoverflow.com/questions/7274221/
    #                           changing-image-hue-with-python-pil

    factor = specifications

    if factor > 360 or factor < 0:
        return None

    img = input_img.convert('RGBA')
    arr = np.array(np.asarray(img).astype('float'))

    rgb_to_hsv = np.vectorize(colorsys.rgb_to_hsv)
    hsv_to_rgb = np.vectorize(colorsys.hsv_to_rgb)

    red, green, blue, alpha = np.rollaxis(arr, axis=-1)
    hue, saturation, value = rgb_to_hsv(red, green, blue)
    hue = (hue + factor / 360.) % 1
    red, green, blue = hsv_to_rgb(hue, saturation, value)
    arr = np.dstack((red, green, blue, alpha))

    output_img = Image.fromarray(arr.astype('uint8'), 'RGBA')
    return output_img


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
    # Determines if the crop dimensions will fit in the given image
    if not __crop_in_given_dimensions(width, height, top, left, right, bottom):
        return None
    output_img = input_img.crop((left, top, right, bottom))
    return output_img


def opacity_editor(input_img: Image, specifications: int) -> Image.Image:
    """
       Args:
               input_img:  The image to be changed
               specifications: The value determining how opaque the image will
                        be - 0 being invisible, 100 being opaque

       Returns:
           PIL.Image: Image with opacity changed
    """

    value = specifications

    if type(value) != int:
        return None

    if value > 100 or value < 0:
        return None

    input_img.putalpha(int(value * 2.55))
    return input_img


def apply_color_editor(input_img: Image,
                       specifications: list = [255, 255, 255, 255]) -> Image.Image:
    """
       Args:
            input_img:  The image to be changed
            specifications: A list of four ints, being the rgba for the color mask

       Returns:
           PIL.Image: Image with color mask applied changed
    """

    red, green, blue, alpha = specifications
    if __color_val_in_range(red, green, blue):
        return None

    color = Image.new('RGB', input_img.size, (red, green, blue))
    mask = Image.new('RGBA', input_img.size, (0, 0, 0, alpha))
    output_image = Image.composite(input_img, color, mask).convert('RGB')
    return output_image


def apply_gradient_editor(input_img: Image, specifications: list) -> Image:
    """
       Args:
           input_img:  The image to be changed
           specifications: list containing the next 3 values ->

                           * alpha: the alpha value of the mask to be applied
                           * color_initial: A list of three ints, being the rgb for the first half of the color mask
                           * color_secondary: A list of three ints, being the rgb for the second half of the color mask

       Returns:
           PIL.Image: Image with color mask applied changed
    """
    # https://python-catalin.blogspot.com/2013/10/
    #                       how-to-make-color-gradient-and-images.html
    alpha = specifications[0]
    color_initial = specifications[1]
    color_secondary = specifications[2]

    red, green, blue = color_initial
    red_secondary, green_secondary, blue_secondary = color_secondary

    if __color_val_in_range(red, green, blue):
        return None
    if __color_val_in_range(red_secondary, green_secondary, blue_secondary):
        return None
    if alpha < 0 or alpha > 255:
        return None

    color = Image.new("RGB", input_img.size, "#FFFFFF")
    draw = ImageDraw.Draw(color)
    draw_red = (red_secondary - red) / input_img.width
    draw_green = (green_secondary - green) / input_img.width
    draw_blue = (blue_secondary - blue) / input_img.width
    for i in range(input_img.width):
        red, green, blue = red + draw_red, green + draw_green, blue + draw_blue
        draw.line((i, 0, i, input_img.height),
                  fill=(int(red), int(green), int(blue)))

    mask = Image.new('RGBA', input_img.size, (0, 0, 0, alpha))
    output_image = Image.composite(input_img, color, mask).convert('RGB')
    return output_image


def apply_mirror(input_img: Image, specifications: int) -> Image.Image:
    """
        Args:
            input_img:  The image to be changed
            specifications: int determining if its a horizontal or vertical
                            mirror:
                            * 0 -> flip across the y axis
                            * 1 -> flip across the x axis

        Returns:
            PIL.Image: Image with color mask applied changed
    """
    if specifications == 0:
        return ImageOps.mirror(input_img)
    elif specifications == 1:
        return ImageOps.flip(input_img)
    else:
        return None


def apply_frame(input_img: Image,
                specifications: list = [255, 255, 255]) -> Image:
    """
        Args:
            input_img:  The image to be changed
            specifications: list containing 3 ints, being the red, green,
                            and blue values for the border's color

        Returns:
            PIL.Image: Image with color mask applied changed
    """
    # https://stackoverflow.com/questions/
    #                   11142851/adding-borders-to-an-image-using-python
    old_size = input_img.size
    red, green, blue = specifications
    # make new_size bigger, change background and then paste back image
    new_size = (int(input_img.height * 1.1), int(input_img.width * 1.1))
    output_img = Image.new("RGB", new_size)
    output_img.paste((red, green, blue), [0, 0, output_img.size[0],
                                          output_img.size[1]])
    output_img.paste(input_img, ((new_size[0] - old_size[0]) // 2,
                                 (new_size[1] - old_size[1]) // 2))
    return output_img


def apply_solarize(input_img: Image, specifications: int) -> Image:
    """
        Args:
            input_img:  The image to be changed
            specifications: int to determine the threshold of the solarization effect

        Returns:
            PIL.Image: Image with color mask applied changed
    """
    # Have to make rgba image rgb
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
    """
    # https://stackoverflow.com/questions/47143332/
    #           how-to-pixelate-a-square-image-to-256-big-pixels-with-python

    # Resize smoothly down to smaller pixel dimensions
    output_img = input_img.resize((32, 32), resample=Image.BILINEAR)

    # Scale back up using NEAREST to original size
    return output_img.resize(input_img.size, Image.NEAREST)


def apply_red_eye_filter(input_img: Image,
                         specifications: list = [int, int, int, int]) -> Image:
    """ Removes red eye effect in a given area

    Args:
        input_img:  Input image
        specifications: List of integers denoting area to perform red eye removal.
            * Integers should be in this format: [left x value, top y value, right x value, bottom y value]

    Returns:
        PIL.Image: Image with red eye removed
    """
    # https://learnopencv.com/
    #           automatic-red-eye-remover-using-opencv-cpp-python/
    input_img.load()

    # Have to make rgba image rgb
    output_img = Image.new("RGB", input_img.size, (255, 255, 255))
    output_img.paste(input_img, mask=input_img.split()[3])

    pixels = output_img.load()
    left_side_x, top_side_y, right_side_x, bottom_side_y = specifications

    for row in range(output_img.size[0]):  # for every pixel:
        for column in range(output_img.size[1]):
            red, green, blue = pixels[row, column]
            # determine if the pixel is in the box and mostly red
            if left_side_x < row < right_side_x and \
                    top_side_y < column < bottom_side_y and \
                    150 > red > 2 * green and red > 2 * blue:
                # change to black if red
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


def __color_val_in_range(red: int, green: int, blue: int) -> bool:
    """ Checks that all color values are in the range [0, 255]
    Args:
        red:    Red color value
        green:  Green color value
        blue:   Blue color value

    Returns:
        bool:   True if all color values are in range
    """
    if 255 >= red >= 0 and 255 >= green >= 0 and 255 >= blue >= 0:
        return False
    else:
        return True


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
    if width > right > left >= 0 and height > bottom > top >= 0:
        return True
    else:
        return False
