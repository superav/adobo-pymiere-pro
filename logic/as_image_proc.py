from PIL import Image, ImageDraw, ImageOps
import numpy as np
import colorsys


def hue_editor(input_img: Image, specifications: int) -> Image:
    """
       Args:
           input_img:  The image to be changed
           specifications:     The hue factor that will be set -

       Returns:
           output_img: Image with hue changed
    """
    # https://stackoverflow.com/questions/7274221/changing-image-hue-with-python-pil

    if specifications > 360 or specifications < 0:
        return None

    img = input_img.convert('RGBA')
    arr = np.array(np.asarray(img).astype('float'))

    rgb_to_hsv = np.vectorize(colorsys.rgb_to_hsv)
    hsv_to_rgb = np.vectorize(colorsys.hsv_to_rgb)

    red, green, blue, alpha = np.rollaxis(arr, axis=-1)
    hue, saturation, value = rgb_to_hsv(red, green, blue)
    hue = (hue + specifications / 360.) % 1
    red, green, blue = hsv_to_rgb(hue, saturation, value)
    arr = np.dstack((red, green, blue, alpha))

    output_img = Image.fromarray(arr.astype('uint8'), 'RGBA')
    return output_img


def crop_editor(input_img: Image,
                specifications: list = [int, int, int, int]) -> Image:
    """
       Args:
           input_img:  The image to be changed
           specifications:list of 4 floats, being the left, top, right, bottom,
                       of where the image is to be cropped by pixel count, that
                       have to be within the image size

       Returns:
           output_img: Image that has been cropped
    """

    left, top, right, bottom = specifications
    width, height = input_img.size
    if left >= width or right >= width or top >= height or bottom >= height \
            or right <= left or bottom <= top or left < 0 or top < 0:
        return None
    output_img = input_img.crop((left, top, right, bottom))
    return output_img


def opacity_editor(input_img: Image, specifications: int) -> Image:
    """
       Args:
               input_img:  The image to be changed
               specifications: The value determining how opaque the image will
                        be - 0 being invisible, 100 being opaque

       Returns:
           output_img: Image with opacity changed
    """

    if specifications > 100 or specifications < 0:
        return None

    input_img.putalpha(int(specifications * 2.55))
    return input_img


def apply_color_editor(input_img: Image,
                       specifications: list = [255, 255, 255, 255]) -> Image:
    """
       Args:
            input_img:  The image to be changed
            specifications: A list of four ints, being the rgba for the color
                        mask

       Returns:
           output_img: Image with color mask applied changed
    """

    red, green, blue, alpha = specifications
    if red < 0 or green < 0 or blue < 0 or alpha < 0 or \
            red > 255 or green > 255 or blue > 255 or alpha > 255:
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

                           alpha: the alpha value of the mask to be applied
                           color_initial: A list of three ints, being the rgb
                                            for the first half of the color
                                            mask
                           color_secondary: A list of three ints, being the
                                            rgb for the second half of the
                                            color mask

       Returns:
           output_img: Image with color mask applied changed
    """
    # https://python-catalin.blogspot.com/2013/10/how-to-make-color-gradient-and-images.html
    alpha = specifications[0]
    color_initial = specifications[1]
    color_secondary = specifications[2]

    red, green, blue = color_initial
    red_secondary, green_secondary, blue_secondary = color_secondary

    if red < 0 or green < 0 or blue < 0 or \
            red > 255 or green > 255 or blue > 255:
        return None
    if red_secondary < 0 or green_secondary < 0 or blue_secondary < 0 or \
            red_secondary > 255 or \
            green_secondary > 255 or blue_secondary > 255:
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


def apply_mirror(input_img: Image, specifications: int) -> Image:
    """
        Args:
            input_img:  The image to be changed
            specifications: int determining if its a horizontal or vertical
                            mirror, 0 -> flip across the y axis
                                    1 -> flip across the x axis

        Returns:
            output_img: Image with color mask applied changed
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
            output_img: Image with color mask applied changed
    """
    # https://stackoverflow.com/questions/11142851/adding-borders-to-an-image-using-python
    old_size = input_img.size
    red, green, blue = specifications
    new_size = (int(input_img.height * 1.1), int(input_img.width * 1.1))
    new_im = Image.new("RGB", new_size)
    new_im.paste((red, green, blue), [0, 0, new_im.size[0], new_im.size[1]])
    new_im.paste(input_img, ((new_size[0] - old_size[0]) // 2,
                             (new_size[1] - old_size[1]) // 2))
    return new_im


def apply_solarize(input_img: Image, specifications: int) -> Image:
    """
        Args:
            input_img:  The image to be changed
            specifications: int to determine the threshold of the
                            solarization effect

        Returns:
            output_img: Image with color mask applied changed
    """
    return ImageOps.solarize(input_img, threshold=specifications)


def apply_mosaic_filter(input_img: Image) -> Image:
    """
        Args:
            input_img:  The image to be changed

        Returns:
            output_img: Image with color mask applied changed
    """
    # https://stackoverflow.com/questions/47143332/how-to-pixelate-a-square-image-to-256-big-pixels-with-python
    # Resize smoothly down to smaller pixel dimensions
    img_small = input_img.resize((32, 32),
                                 resample=Image.BILINEAR)

    # Scale back up using NEAREST to original size
    return img_small.resize(input_img.size, Image.NEAREST)


def apply_red_eye_filter(input_img: Image,
                         specifications: list = [int, int, int, int]) -> Image:
    """
        Args:
            input_img:  The image to be changed
            specifications: list of 4 ints to determine what area has
                            the red eyes in it -> left x value
                                                  top y value
                                                  right x value
                                                  bottom y value

        Returns:
            output_img: Image with color mask applied changed
    """
    # https://learnopencv.com/automatic-red-eye-remover-using-opencv-cpp-python/
    pixels = input_img.load()

    left_side_x, top_side_y, right_side_x, bottom_side_y = specifications

    for row in range(input_img.size[0]):  # for every pixel:
        for column in range(input_img.size[1]):
            red, green, blue = pixels[row, column]
            # determine if the pixel is in the box and mostly red
            if left_side_x < row < right_side_x and \
                    top_side_y < column < bottom_side_y and \
                    150 > red > 2 * green and red > 2 * blue:
                # change to black if red
                pixels[row, column] = (int(red / 5), green, blue)

    return input_img
