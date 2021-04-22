from PIL import Image, ImageFont, ImageDraw
from moviepy.editor import *


def add_text_to_image(image=Image, specifications: list = [str, str, int, list, list]) -> Image:
    """
    Args:
        image: image to add text to
        specifications: list of additional parameters needed to call this function (text, font, size, offset, color)

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


def change_volume(clip=VideoFileClip, factor=float) -> VideoFileClip:
    """
    Args:
        clip: Video clip to change volume of
        factor: factor to scale current volume by

    Return:
        output_clip: Video clip with changed volume. Returns None if unsuccessful.
    """
    valid_parameters = isinstance(clip, VideoFileClip)
    valid_parameters = valid_parameters and isinstance(factor, float)
    if not valid_parameters:
        return None
    clip = clip.volumex(factor)
    return clip


def audio_normalize_effect(clip=VideoFileClip) -> VideoFileClip:
    """
    Args:
        clip: Video clip to normalize audio of

    Return:
        output_clip: Video clip with audio normalized. Returns None if unsuccessful.
    """
    valid_parameters = isinstance(clip, VideoFileClip)
    if not valid_parameters:
        return None
    clip = clip.fx(afx.audio_normalize)
    return clip


def audio_fade_effect(clip=VideoFileClip, specifications: list = [int, int]) -> VideoFileClip:
    """
    Args:
        clip: Video clip fade audio of
        specifications: list of parameters to fade audio (fade in time, fade out time)

    Return:
        output_clip: Video clip with faded audio. Returns None if unsuccessful.
    """
    fade_in = specifications[0]
    fade_out = specifications[1]

    valid_parameters = isinstance(clip, VideoFileClip)
    valid_parameters = valid_parameters and isinstance(fade_in, int)
    valid_parameters = valid_parameters and isinstance(fade_out, int)
    if not valid_parameters:
        return None
    clip = clip.fx(afx.audio_fadein, fade_in)
    clip = clip.fx(afx.audio_fadeout, fade_out)
    return clip
