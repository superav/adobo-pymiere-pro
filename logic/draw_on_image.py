from PIL import Image, ImageDraw


def draw_line(image: Image, specifications: list) -> Image:
    """ Can draw single or multi segment lines.

    Args:
        image:  Input image
        specifications: A list of specs (in order)
            * points: A list of points to draw the line. Is a list of tuples ``[(x1, y1), (x2, y2)...]``.
            Must be at least 2 tuples.

            * stroke_size:    Size of line
            * color:  Line color, formatted as (R, G, B)

    Returns:
        PIL.Image: Image with line drawn on
    """

    if not __specifications_are_valid(specifications):
        return None

    if not isinstance(image, Image.Image):
        return None

    points = specifications[0]
    stroke_size = specifications[1]
    color = specifications[2]

    output = image.copy()
    draw = ImageDraw.Draw(output)

    is_multi_segment_line = len(points) > 2

    draw.line(points, color, stroke_size, is_multi_segment_line)

    return output


def __all_points_are_valid(points: list) -> bool:
    """
    Args:
        points: List of tuples, should be in the format [(x, y), (x, y)...]

    Returns:
        is_valid:   Returns true if points are correctly formatted.
    """

    if len(points) < 2:
        return False

    for point in points:
        if len(point) != 2:
            return False

        x_pos, y_pos = point

        if type(x_pos) != int or type(y_pos) != int:
            return False

    return True


def __specifications_are_valid(specifications: list) -> bool:
    """
    Args:
        specifications:
            points: A list of points to draw the line. Is a list of tuples [(x1, y1), (x2, y2)...]
                    Must be at least 2 tuples
            stroke_size:    Size of line
            color:  Line color, formatted as (R, G, B)

    Returns:
    """

    if len(specifications) != 3:
        return False

    points = specifications[0]
    stroke_size = specifications[1]
    color = specifications[2]

    if type(points) != list or type(stroke_size) != int or type(color) != tuple:
        return False

    if stroke_size < 0:
        return False

    if len(color) != 3:
        return False

    red, green, blue = color

    if not (0 <= red <= 255 and 0 <= green <= 255 and 0 <= blue <= 255):
        return False

    return __all_points_are_valid(points)

