import math
import operator
from functools import reduce

import unittest

from logic.asset_manager import AssetManager
from logic.as_sprint_3 import *

ASSET_MANAGER = AssetManager('test_user_1')


# Reference: https://stackoverflow.com/questions/1927660/compare-two-images-the-python-linux-way
def compare_images(image_1, image_2):

    h1 = image_1.histogram()
    h2 = image_2.histogram()

    rms = math.sqrt(reduce(operator.add,
                           map(lambda a, b: (a - b) ** 2, h1, h2)) / len(h1))

    return rms


class TestColorInputValidation(unittest.TestCase):
    def test_contrast_invalid_value(self):
        im1 = ASSET_MANAGER.import_image_from_s3('tree.png', False)

        with self.assertRaises(Exception):
            _ = apply_contrast(im1, 5.80)

        with self.assertRaises(Exception):
            _ = apply_contrast("test", -1)

    def test_autocontrast_invalid_value(self):
        with self.assertRaises(Exception):
            _ = apply_autocontrast(580)

    def test_vignette_invalid_value(self):
        with self.assertRaises(Exception):
            _ = apply_vignette("test")

    def test_brightness_invalid_value(self):
        im1 = ASSET_MANAGER.import_image_from_s3('tree.png', False)

        with self.assertRaises(Exception):
            _ = apply_brightness(None, -1)

        with self.assertRaises(Exception):
            _ = apply_brightness(im1, "test")


class TestColorImageProc(unittest.TestCase):
    def test_autocontrast_correct_output(self):
        im1 = ASSET_MANAGER.import_image_from_s3('tree.png', False)
        fin = ASSET_MANAGER.import_image_from_s3('autocontrast_expected.png', False)

        im2 = apply_autocontrast(im1)

        self.assertEqual(compare_images(fin, im2), 0)

    def test_contrast_correct_output(self):
        im1 = ASSET_MANAGER.import_image_from_s3('tree.png', False)
        fin = ASSET_MANAGER.import_image_from_s3('contrast_expected_50.png', False)

        im2 = apply_contrast(im1, 50)

        self.assertEqual(compare_images(fin, im2), 0)

    def test_brightness_correct_output(self):
        im1 = ASSET_MANAGER.import_image_from_s3('tree.png', False)
        fin = ASSET_MANAGER.import_image_from_s3('brightness_expected_5.png', False)

        im2 = apply_brightness(im1, 0.5)

        self.assertEqual(compare_images(fin, im2), 0)

    def test_vignette_correct_output(self):
        im1 = ASSET_MANAGER.import_image_from_s3('image.png', False)
        fin = ASSET_MANAGER.import_image_from_s3('vignette_expected.png', False)

        im2 = apply_vignette(im1)

        self.assertEqual(compare_images(fin, im2), 0)
