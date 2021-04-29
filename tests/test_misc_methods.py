import math
import operator
from functools import reduce

import unittest

from logic.asset_manager import AssetManager
from logic.misc_methods import *

ASSET_MANAGER = AssetManager('test_user_1')


def compare_images(image_1, image_2):
    # Reference: https://stackoverflow.com/questions/1927660/compare-two-images-the-python-linux-way

    h1 = image_1.histogram()
    h2 = image_2.histogram()

    rms = math.sqrt(reduce(operator.add,
                           map(lambda a, b: (a - b) ** 2, h1, h2)) / len(h1))

    return rms


class TestMiscInputValidation(unittest.TestCase):
    def test_frame_valid_value(self):
        im1 = ASSET_MANAGER.import_image_from_s3('image.png', False)
        im2 = apply_frame(im1, [266, 999, -123])

        self.assertNotEqual(im2, None)

    def test_mirror_invalid_value(self):
        im1 = ASSET_MANAGER.import_image_from_s3('image.png', False)
        im2 = apply_mirror(im1, -4)
        im3 = apply_mirror(im1, 5)

        self.assertEqual(im2, None)
        self.assertEqual(im3, None)


class TestMiscImageProc(unittest.TestCase):
    def test_mirror_image_correct_output(self):
        im1 = ASSET_MANAGER.import_image_from_s3('image.png', False)

        im2 = apply_mirror(im1, 0)
        fin2 = ASSET_MANAGER.import_image_from_s3('mirror_expected.png', False)

        im3 = apply_mirror(im1, 1)
        fin3 = ASSET_MANAGER.import_image_from_s3('flip_expected.png', False)

        self.assertTrue(compare_images(fin2, im2) == 0)
        self.assertTrue(compare_images(fin3, im3) == 0)

    def test_frame_image_correct_output(self):
        im1 = ASSET_MANAGER.import_image_from_s3('image.png', False)
        fin = ASSET_MANAGER.import_image_from_s3(
            'frame_expected_120_75_225.png', False)

        im2 = apply_frame(im1, [255, 0, 0])

        self.assertTrue(compare_images(fin, im2) == 0)
