import math
import operator
from functools import reduce

import unittest

from logic.asset_manager import AssetManager
from logic.color_methods import *

ASSET_MANAGER = AssetManager('test_user_1')


# Reference: https://stackoverflow.com/questions/1927660/compare-two-images-the-python-linux-way
def compare_images(image_1, image_2):

    h1 = image_1.histogram()
    h2 = image_2.histogram()

    rms = math.sqrt(reduce(operator.add,
                           map(lambda a, b: (a - b) ** 2, h1, h2)) / len(h1))

    return rms


class TestColorInputValidation(unittest.TestCase):
    def test_saturation_invalid_input_type(self):
        input_img = Image.open("./test_assets/images/test_1.png")

        with self.assertRaises(Exception):
            _ = change_saturation("bad", 4.0)

        with self.assertRaises(Exception):
            _ = change_saturation(input_img, True)

        with self.assertRaises(Exception):
            _ = change_saturation(True, "bad")

        input_img.close()

    def test_saturation_invalid_input_value(self):
        input_img = Image.open("./test_assets/images/test_1.png")

        with self.assertRaises(Exception):
            _ = change_saturation(input_img, -33.0)

        with self.assertRaises(Exception):
            _ = change_saturation(input_img, -0.1)

        input_img.close()

    def test_saturation_correct_input(self):
        input_img = Image.open("./test_assets/images/test_1.png")
        output = change_saturation(input_img, 1.2)

        self.assertTrue(isinstance(output, Image.Image))

        input_img.close()

    def test_hue_invalid_value(self):
        im1 = ASSET_MANAGER.import_image_from_s3('image.png', False)

        with self.assertRaises(Exception):
            _ = hue_editor(im1, 580)
        with self.assertRaises(Exception):
            _ = hue_editor(im1, -1)

    def test_opacity_invalid_inputs(self):
        im1 = ASSET_MANAGER.import_image_from_s3('image.png', False)

        with self.assertRaises(Exception):
            _ = opacity_editor(im1, 400)

        with self.assertRaises(Exception):
            _ = opacity_editor(im1, -400)

    def test_recoloration_invalid_value(self):
        im1 = ASSET_MANAGER.import_image_from_s3('image.png', False)

        with self.assertRaises(Exception):
            _ = apply_color_editor(im1, [256, 0, 0, 128])

        with self.assertRaises(Exception):
            _ = apply_color_editor(im1, [256, 0, 300, 128])

        with self.assertRaises(Exception):
            _ = apply_color_editor(im1, [256, -1, 0, 128])

        with self.assertRaises(Exception):
            _ = apply_color_editor(im1, [256, 0, 0, 277])

        with self.assertRaises(Exception):
            _ = apply_color_editor(im1, [256, 0, 0, -128])

    def test_gradient_invalid_value(self):
        im1 = ASSET_MANAGER.import_image_from_s3('image.png', False)

        with self.assertRaises(Exception):
            _ = apply_gradient_editor(im1, [70, [255, 0, 0], [0, -10, 255]])

        with self.assertRaises(Exception):
            _ = apply_gradient_editor(im1, [70, [0, 290, 0], [0, 0, 255]])

        with self.assertRaises(Exception):
            _ = apply_gradient_editor(im1, [70, [255, 0, 0], [0, -7, 255]])

        with self.assertRaises(Exception):
            _ = apply_gradient_editor(im1, [70, [255, 0, 0], [-9, 0, 255]])

        with self.assertRaises(Exception):
            _ = apply_gradient_editor(im1, [70, [14, 190, 300], [0, 0, 255]])

        with self.assertRaises(Exception):
            _ = apply_gradient_editor(im1, [700, [255, 0, 0], [0, 0, 255]])

        with self.assertRaises(Exception):
            _ = apply_gradient_editor(im1, [-7, [255, 0, 0], [0, 0, 255]])

    def test_contrast_invalid_value(self):
        im1 = ASSET_MANAGER.import_image_from_s3('tree.png', False)

        with self.assertRaises(Exception):
            _ = apply_contrast(im1, 5.80)

        with self.assertRaises(Exception):
            _ = apply_contrast("test", -1)

    def test_autocontrast_invalid_value(self):
        with self.assertRaises(Exception):
            _ = apply_autocontrast(580)

    def test_brightness_invalid_value(self):
        im1 = ASSET_MANAGER.import_image_from_s3('tree.png', False)

        with self.assertRaises(Exception):
            _ = apply_brightness(None, -1)

        with self.assertRaises(Exception):
            _ = apply_brightness(im1, "test")


class TestColorImageProc(unittest.TestCase):
    def test_saturation_correct_output(self):
        # Saturation: 0.5
        input_img = ASSET_MANAGER.import_image_from_s3('test_2.png', False)
        expected_img =\
            ASSET_MANAGER.import_image_from_s3('test_2_saturation_1.png', False)

        output = change_saturation(input_img, 0.5)
        root_mean_square = compare_images(output, expected_img)

        self.assertEqual(0, root_mean_square)

        # Saturation: 1.5
        input_img = ASSET_MANAGER.import_image_from_s3('test_3.png', False)
        expected_img =\
            ASSET_MANAGER.import_image_from_s3('test_3_saturation_1.png', False)

        output = change_saturation(input_img, 1.5)
        root_mean_square = compare_images(output, expected_img)

        self.assertEqual(0, root_mean_square)

    def test_hue_correct_output(self):
        im1 = ASSET_MANAGER.import_image_from_s3('image.png', False)
        fin = ASSET_MANAGER.import_image_from_s3('hue_expected_180.png', False)
        im2 = hue_editor(im1, 180)

        self.assertEqual(compare_images(fin, im2), 0)

    def test_opacity_correct_output(self):
        im1 = ASSET_MANAGER.import_image_from_s3('image.png', False)
        fin =\
            ASSET_MANAGER.import_image_from_s3('opacity_expected_50.png', False)
        im2 = opacity_editor(im1, 50)

        self.assertEqual(compare_images(fin, im2), 0)

    def test_recoloration_correct_output(self):
        im1 = ASSET_MANAGER.import_image_from_s3('image.png', False)
        fin = ASSET_MANAGER.import_image_from_s3(
            'gradient_expected_255_0_0_128.png', False)
        im2 = apply_color_editor(im1, [255, 0, 0, 128])

        self.assertTrue(compare_images(fin, im2), 0)

    def test_gradient_correct_output(self):
        im1 = ASSET_MANAGER.import_image_from_s3('image.png', False)
        fin = ASSET_MANAGER.import_image_from_s3(
                'filter_expected_70_255_0_0_0_0_255.png', False)
        im2 = apply_gradient_editor(im1, [70, [255, 0, 0], [0, 0, 255]])

        self.assertEqual(compare_images(fin, im2), 0)

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
