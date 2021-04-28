import math
import operator
from functools import reduce

import unittest

from logic.asset_manager import AssetManager
from logic.filter_methods import *

ASSET_MANAGER = AssetManager('test_user_1')


def compare_images(image_1, image_2):
    # Reference: https://stackoverflow.com/questions/1927660/compare-two-images-the-python-linux-way

    h1 = image_1.histogram()
    h2 = image_2.histogram()

    rms = math.sqrt(reduce(operator.add,
                           map(lambda a, b: (a - b) ** 2, h1, h2)) / len(h1))

    return rms


class TestFilterInputValidation(unittest.TestCase):
    def test_gaussian_blur_invalid_input_types(self):
        input_img = Image.open('./test_assets/images/test_1.png')

        output = gaussian_blur("bad", 0)
        self.assertEqual(None, output)

        output = gaussian_blur(input_img, "bad")
        self.assertEqual(None, output)

        output = gaussian_blur(input_img, -10.4)
        self.assertEqual(None, output)

    def test_gaussian_blur_invalid_radius_value(self):
        input_img = Image.open("./test_assets/images/test_1.png")

        output = gaussian_blur(input_img, -1)
        self.assertEqual(None, output)

        output = gaussian_blur(input_img, -45)
        self.assertEqual(None, output)

    def test_gaussian_blur_correct_input(self):
        input_img = Image.open("./test_assets/images/test_1.png")
        output = gaussian_blur(input_img, 9)

        self.assertTrue(isinstance(output, Image.Image))

    def test_solarize_valid_value(self):
        im1 = ASSET_MANAGER.import_image_from_s3('image.png', False)
        im2 = apply_solarize(im1, 9999)
        im3 = apply_solarize(im1, -1234)

        self.assertNotEqual(im2, None)
        self.assertNotEqual(im3, None)

    def test_red_eye_valid_value(self):
        im1 = ASSET_MANAGER.import_image_from_s3('redeye.png', False)
        im2 = apply_red_eye_filter(im1, [-23, 1000, 150, 150])

        self.assertNotEqual(im2, None)


class TestFilterImageProc(unittest.TestCase):
    def test_gaussian_blur_correct_output(self):
        # Blur radius: 9
        input_img = ASSET_MANAGER.import_image_from_s3('test_1.png', False)
        expected_img = ASSET_MANAGER.import_image_from_s3('test_1_gaussian_1.png', False)

        output = gaussian_blur(input_img, 9)
        root_mean_square = compare_images(expected_img, output)

        self.assertEqual(0, root_mean_square)

        # Blur radius: 2
        input_img = ASSET_MANAGER.import_image_from_s3('test_2.png', False)
        expected_img = ASSET_MANAGER.import_image_from_s3('test_2_gaussian_1.png', False)

        output = gaussian_blur(input_img, 2)
        root_mean_square = compare_images(expected_img, output)

        self.assertEqual(0, root_mean_square)

    def test_solarize_correct_output(self):
        im1 = ASSET_MANAGER.import_image_from_s3('image.png', False)
        fin = ASSET_MANAGER.import_image_from_s3('solarize_expected_128.png', False)
        im2 = apply_solarize(im1, 128)

        self.assertTrue(compare_images(fin, im2) == 0)

    def test_mosaic_correct_output(self):
        im1 = ASSET_MANAGER.import_image_from_s3('image.png', False)
        fin = ASSET_MANAGER.import_image_from_s3('mosaic_expected.png', False)
        im2 = apply_mosaic_filter(im1)

        self.assertTrue(compare_images(fin, im2) == 0)

    def test_red_eye_correct_output(self):
        im1 = ASSET_MANAGER.import_image_from_s3('redeye.png', False)
        fin = ASSET_MANAGER.import_image_from_s3('red_eye_expected_35_110_150_150.png', False)
        im2 = apply_red_eye_filter(im1, [35, 110, 150, 150])

        self.assertTrue(compare_images(fin, im2) == 0)
