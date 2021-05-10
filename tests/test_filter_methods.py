import math
import operator
from functools import reduce
from http.client import HTTPException

import unittest

from logic.asset_manager import AssetManager
from logic.filter_methods import *

ASSET_MANAGER = AssetManager('test_user_1')


# Reference: https://stackoverflow.com/questions/1927660/compare-two-images-the-python-linux-way
def compare_images(image_1, image_2):

    h1 = image_1.histogram()
    h2 = image_2.histogram()

    rms = math.sqrt(reduce(operator.add,
                           map(lambda a, b: (a - b) ** 2, h1, h2)) / len(h1))

    return rms


class TestFilterInputValidation(unittest.TestCase):
    def test_gaussian_blur_invalid_input_types(self):
        input_img = Image.open('./test_assets/images/test_1.png')

        with self.assertRaises(Exception):
            _ = gaussian_blur("bad", 0)

        with self.assertRaises(Exception):
            _ = gaussian_blur(input_img, "bad")

        with self.assertRaises(Exception):
            _ = gaussian_blur(input_img, -10.4)

    def test_gaussian_blur_invalid_radius_value(self):
        input_img = Image.open("./test_assets/images/test_1.png")

        with self.assertRaises(Exception):
            _ = gaussian_blur(input_img, -1)

        with self.assertRaises(Exception):
            _ = gaussian_blur(input_img, -45)

    def test_gaussian_blur_correct_input(self):
        input_img = Image.open("./test_assets/images/test_1.png")
        output = gaussian_blur(input_img, 9)

        self.assertTrue(isinstance(output, Image.Image))

    def test_solarize_invalid_value(self):
        im1 = ASSET_MANAGER.import_image_from_s3('image.png', False)

        with self.assertRaises(Exception):
            _ = apply_solarize("bad", 23)

        with self.assertRaises(Exception):
            _ = apply_solarize(im1, "hi")

        with self.assertRaises(Exception):
            _ = apply_solarize(im1, -4)

    def test_solarize_valid_value(self):
        im1 = ASSET_MANAGER.import_image_from_s3('image.png', False)
        im2 = apply_solarize(im1, 23)
        im3 = apply_solarize(im1, 45)

        self.assertTrue(isinstance(im2, Image.Image))
        self.assertTrue(isinstance(im3, Image.Image))

    def test_red_eye_invalid_value(self):
        im1 = ASSET_MANAGER.import_image_from_s3('redeye.png', False)

        with self.assertRaises(Exception):
            _ = apply_red_eye_filter("bad", [-23, 1000, 150, 150])

        with self.assertRaises(Exception):
            _ = apply_red_eye_filter(im1, "hi")

        with self.assertRaises(Exception):
            _ = apply_red_eye_filter(im1, ["hi", 1000, 150, 150])

        with self.assertRaises(Exception):
            _ = apply_red_eye_filter(im1, [-23, "hi", 150, 150])

        with self.assertRaises(Exception):
            _ = apply_red_eye_filter(im1, [-23, 1000, "hi", 150])

        with self.assertRaises(Exception):
            _ = apply_red_eye_filter(im1, [-23, 1000, 150, "hi"])

    def test_red_eye_valid_value(self):
        im1 = ASSET_MANAGER.import_image_from_s3('redeye.png', False)
        im2 = apply_red_eye_filter(im1, [-23, 1000, 150, 150])

        self.assertTrue(isinstance(im2, Image.Image))

    # def test_vignette_invalid_value(self):
    #     with self.assertRaises(Exception):
    #         _ = apply_vignette("test")


class TestFilterImageProc(unittest.TestCase):
    def test_gaussian_blur_correct_output(self):
        # Blur radius: 9
        input_img = ASSET_MANAGER.import_image_from_s3('test_1.png', False)
        expected_img =\
            ASSET_MANAGER.import_image_from_s3('test_1_gaussian_1.png', False)

        output = gaussian_blur(input_img, 9)
        root_mean_square = compare_images(expected_img, output)

        self.assertEqual(0, root_mean_square)

        # Blur radius: 2
        input_img = ASSET_MANAGER.import_image_from_s3('test_2.png', False)
        expected_img =\
            ASSET_MANAGER.import_image_from_s3('test_2_gaussian_1.png', False)

        output = gaussian_blur(input_img, 2)
        root_mean_square = compare_images(expected_img, output)

        self.assertEqual(0, root_mean_square)

    def test_solarize_correct_output(self):
        im1 = ASSET_MANAGER.import_image_from_s3('image.png', False)
        fin =\
            ASSET_MANAGER.import_image_from_s3('solarize_expected_128.png', False)
        im2 = apply_solarize(im1, 128)

        self.assertEqual(compare_images(fin, im2), 0)

    def test_mosaic_correct_output(self):
        im1 = ASSET_MANAGER.import_image_from_s3('image.png', False)
        fin = ASSET_MANAGER.import_image_from_s3('mosaic_expected.png', False)
        im2 = apply_mosaic_filter(im1)

        self.assertEqual(compare_images(fin, im2), 0)

    def test_red_eye_correct_output(self):
        im1 = ASSET_MANAGER.import_image_from_s3('redeye.png', False)
        fin =\
            ASSET_MANAGER.import_image_from_s3('red_eye_expected_35_110_150_150.png', False)
        im2 = apply_red_eye_filter(im1, [35, 110, 150, 150])

        self.assertEqual(compare_images(fin, im2), 0)

    # def test_vignette_correct_output(self):
    #     im1 = ASSET_MANAGER.import_image_from_s3('image.png', False)
    #     fin = ASSET_MANAGER.import_image_from_s3('vignette_expected.png', False)
    #
    #     im2 = apply_vignette(im1)
    #
    #     self.assertTrue(compare_images(fin, im2) < 1)
