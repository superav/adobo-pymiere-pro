from PIL import Image, ImageOps, ImageDraw
from flask import abort

"""
Methods that don't exactly fit any other category.

Included Methods:
    * Mirror Image
    * Add Frame to Image
"""


def apply_mirror(input_img: Image, specifications: int) -> Image:
    """ Reflects the image over a given axis

    Args:
        input_img:  The image to be changed
        specifications: int determining if its a horizontal or vertical mirror:

            * 0 -> flip across the y axis
            * 1 -> flip across the x axis

    Returns:
        PIL.Image: Image with color mask applied changed
    """
    if specifications == 0:
        return ImageOps.mirror(input_img)

    if specifications == 1:
        return ImageOps.flip(input_img)

    error = "apply_mirror: specifications %s is not 1 or 0"
    abort(500, description=error)


def apply_frame(input_img: Image,
                specifications: list = [255, 255, 255]) -> Image:
    """
    Args:
        input_img:  The image to be changed
        specifications: list containing 3 ints, being the red, green,
                        and blue values for the border's color

    Returns:
        PIL.Image: Image with color mask applied changed

    References:
        * https://stackoverflow.com/questions/11142851/adding-borders-to-an-image-using-python
    """

    old_size = input_img.size
    red, green, blue = specifications
    new_size = (int(input_img.width * 1.1), int(input_img.height * 1.1))
    output_img = Image.new("RGB", new_size)

    output_img.paste((red, green, blue), [0, 0, output_img.size[0],
                                          output_img.size[1]])
    output_img.paste(input_img, ((new_size[0] - old_size[0]) // 2,
                                 (new_size[1] - old_size[1]) // 2))

    return output_img


def draw_lines(image: Image, specifications: list) -> Image:
    """ Can draw single or multi segment lines.

    Args:
        image:  Input image
        specifications: A list of strokes. Strokes must be formatted as such:
            * points: A list of points to draw the line. Is a list of tuples
            ``[(x1, y1), (x2, y2)...]``. Must be at least 2 tuples.

            * stroke_size:    Size of line
            * color:  Line color, formatted as (R, G, B)

    Returns:
        PIL.Image: Image with line drawn on
    """

    if not __all_strokes_are_valid(specifications):
        error = "draw_lines: Invalid specifications"
        abort(500, description=error)

    if not isinstance(image, Image.Image):
        error = "draw_lines: Input image must be of type PIL.Image"
        abort(500, description=error)

    output = image.copy()

    for stroke in specifications:
        points = [tuple(point) for point in stroke[0]]
        stroke_size = stroke[1]
        color = tuple(stroke[2])

        draw = ImageDraw.Draw(output)

        is_multi_segment_line = len(points) > 2

        draw.line(points, color, stroke_size, is_multi_segment_line)

    return output

# HELPER METHODS


def __all_points_are_valid(points: list) -> bool:
    """
    Args:
        points: List of tuples, should be in the format [(x, y), (x, y)...]

    Returns:
        bool:   Returns true if points are correctly formatted.
    """

    if len(points) < 2:
        return False

    for point in points:
        if len(point) != 2:
            return False

        if not (type(point) == list or type(point) == tuple):
            return False

        x_pos, y_pos = point

        if type(x_pos) != int or type(y_pos) != int:
            return False

    return True


def __strokes_are_valid(stroke: list) -> bool:
    """
    Args:
        stroke:
            points: A list of points to draw the line. Is a list of tuples [(x1, y1), (x2, y2)...]
                    Must be at least 2 tuples
            stroke_size:    Size of line
            color:  Line color, formatted as [R, G, B]

    Returns:
        bool: True if the stroke is properly formatted with correct types and values
    """

    if len(stroke) != 3:
        return False

    points = stroke[0]
    stroke_size = stroke[1]
    color = stroke[2]

    if not (type(points) == list and type(stroke_size) == int):
        return False

    if not (type(color) == list or type(color) == tuple):
        return False

    if stroke_size < 0:
        return False

    if len(color) != 3:
        return False

    red, green, blue = tuple(color)

    if not (0 <= red <= 255 and 0 <= green <= 255 and 0 <= blue <= 255):
        return False

    return __all_points_are_valid(points)


def __all_strokes_are_valid(specifications: list):
    """
    Args:
        specifications: A list of strokes

    Returns:
        bool: True if all strokes are properly formatted
    """

    if type(specifications) != list:
        return False

    for stroke in specifications:
        if not __strokes_are_valid(stroke):
            return False

    return True
