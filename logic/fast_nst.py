# -*- coding: utf-8 -*-
import functools
import os

import matplotlib.pylab as plt
import numpy as np
import tensorflow as tf
import tensorflow_hub as hub


# content_image_url =
# 'https://upload.wikimedia.org/wikipedia/commons/d/d7/Green_Sea_Turtle_grazing_seagrass.jpg'
# style_image_url =
# 'https://upload.wikimedia.org/wikipedia/commons/0/0a/The_Great_Wave_off_Kanagawa.jpg'

def crop_center(image):
    """ Returns a cropped square image.
    Args:
        image: Image tensor containing an RGB image
    Returns:
        image: Cropped Image Tensor of size 256,256
    """
    shape = image.shape
    new_shape = min(shape[1], shape[2])
    offset_y = max(shape[1] - shape[2], 0) // 2
    offset_x = max(shape[2] - shape[1], 0) // 2
    image = tf.image.crop_to_bounding_box(image, offset_y, offset_x,
                                          new_shape, new_shape)
    return image


def load_image(image_url, image_size=(256, 256), preserve_aspect_ratio=True):
    """ Loads and preprocesses images.
    Args:
        image_url: String containing the URL from which to load image
        image_size: integer tuple containing the dimensions of the image to load
        preserve_aspect_ratio: Boolean if u want to preserve the aspect ratio
        or modify it
    Returns:
        img: Image Tensor containing the loaded and preprocessed image
    """
    # Cache image file locally.
    image_path = tf.keras.utils.get_file(os.path.basename(image_url)[-128:],
                                         image_url)
    # Load and convert to float32 numpy array, add batch dimension,
    # and normalize to range [0, 1].
    img = plt.imread(image_path).astype(np.float32)[np.newaxis, ...]
    if img.max() > 1.0:
        img = img / 255.
    if len(img.shape) == 3:
        img = tf.stack([img, img, img], axis=-1)
    img = crop_center(img)
    img = tf.image.resize(img, image_size, preserve_aspect_ratio=True)
    return img


def run_nst(content_image_url, style_image_url, output_image_size=384):
    """ Runs Fast Arbitrary NST on a content image based on a provided style
    image

    Args:
        content_image_url: String containing the URL of the content image
        style_image_url: String containing the URL of the style image
        output_image_size: Integer describing the integers of the output image
            size

    Returns:
        stylized_image_url: String containing the url of the stylized image
    """
    content_img_size = (output_image_size, output_image_size)
    style_img_size = (256, 256)
    content_image = load_image(content_image_url, content_img_size)
    style_image = load_image(style_image_url, style_img_size)
    style_image = tf.nn.avg_pool(style_image, ksize=[3, 3], strides=[1, 1],
                                 padding='SAME')

    hub_handle = 'https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2'
    hub_module = hub.load(hub_handle)

    outputs = hub_module(tf.constant(content_image), tf.constant(style_image))
    stylized_image = outputs[0]
    arr_ = np.squeeze(stylized_image)  # you can give axis attribute if you wanna squeeze in specific dimension
    plt.imshow(arr_)
    plt.axis('off')
    stylized_image_url = "stylizedImage.png"
    plt.savefig(stylized_image_url, bbox_inches='tight', pad_inches=0)
    plt.show()
    return stylized_image_url
