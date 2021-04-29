import math
import operator
from functools import reduce

import unittest

from logic.asset_manager import AssetManager
from logic.color_methods import *

ASSET_MANAGER = AssetManager('test_user_1')


def compare_images(image_1, image_2):
    # Reference: https://stackoverflow.com/questions/1927660/compare-two-images-the-python-linux-way

    h1 = image_1.histogram()
    h2 = image_2.histogram()

    rms = math.sqrt(reduce(operator.add,
                           map(lambda a, b: (a - b) ** 2, h1, h2)) / len(h1))

    return rms


class TestColorInputValidation(unittest.TestCase):
    def test_saturation_invalid_input_type(self):
        input_img = Image.open("./test_assets/images/test_1.png")

        output = change_saturation("bad", 4.0)
        self.assertEqual(None, output)

        output = change_saturation(input_img, True)
        self.assertEqual(None, output)

        output = change_saturation(True, "bad")
        self.assertEqual(None, output)

    def test_saturation_invalid_input_value(self):
        input_img = Image.open("./test_assets/images/test_1.png")

        output = change_saturation(input_img, -33.0)
        self.assertEqual(None, output)

        output = change_saturation(input_img, -0.1)
        self.assertEqual(None, output)

    def test_saturation_correct_input(self):
        input_img = Image.open("./test_assets/images/test_1.png")
        output = change_saturation(input_img, 1.2)

        self.assertTrue(isinstance(output, Image.Image))

    def test_hue_invalid_value(self):
        im1 = ASSET_MANAGER.import_image_from_s3('image.png', False)
        im2 = hue_editor(im1, 580)
        im3 = hue_editor(im1, -1)

        self.assertEqual(im2, None)
        self.assertEqual(im3, None)

    def test_opacity_invalid_inputs(self):
        im1 = ASSET_MANAGER.import_image_from_s3('image.png', False)
        im2 = opacity_editor(im1, 400)
        im3 = opacity_editor(im1, -400)

        self.assertEqual(im2, None)
        self.assertEqual(im3, None)

    def test_recoloration_invalid_value(self):
        im1 = ASSET_MANAGER.import_image_from_s3('image.png', False)
        im2 = apply_color_editor(im1, [256, 0, 0, 128])
        im3 = apply_color_editor(im1, [256, 0, 300, 128])
        im4 = apply_color_editor(im1, [256, -1, 0, 128])
        im5 = apply_color_editor(im1, [256, 0, 0, 277])
        im6 = apply_color_editor(im1, [256, 0, 0, -128])

        self.assertEqual(im2, None)
        self.assertEqual(im3, None)
        self.assertEqual(im4, None)
        self.assertEqual(im5, None)
        self.assertEqual(im6, None)

    def test_gradient_invalid_value(self):
        im1 = ASSET_MANAGER.import_image_from_s3('image.png', False)
        im2 = apply_gradient_editor(im1, [70, [255, 0, 0], [0, -10, 255]])
        im3 = apply_gradient_editor(im1, [70, [0, 290, 0], [0, 0, 255]])
        im4 = apply_gradient_editor(im1, [70, [255, 0, 0], [0, -7, 255]])
        im5 = apply_gradient_editor(im1, [70, [255, 0, 0], [-9, 0, 255]])
        im6 = apply_gradient_editor(im1, [70, [14, 190, 300], [0, 0, 255]])
        im7 = apply_gradient_editor(im1, [700, [255, 0, 0], [0, 0, 255]])
        im8 = apply_gradient_editor(im1, [-7, [255, 0, 0], [0, 0, 255]])

        self.assertEqual(im2, None)
        self.assertEqual(im3, None)
        self.assertEqual(im4, None)
        self.assertEqual(im5, None)
        self.assertEqual(im6, None)
        self.assertEqual(im7, None)
        self.assertEqual(im8, None)


class TestColorImageProc(unittest.TestCase):
    def test_saturation_correct_output(self):
        # Saturation: 0.5
        input_img = ASSET_MANAGER.import_image_from_s3('test_2.png', False)
        expected_img = ASSET_MANAGER.import_image_from_s3('test_2_saturation_1.png', False)

        output = change_saturation(input_img, 0.5)
        root_mean_square = compare_images(output, expected_img)

        self.assertEqual(0, root_mean_square)

        # Saturation: 1.5
        input_img = ASSET_MANAGER.import_image_from_s3('test_3.png', False)
        expected_img = ASSET_MANAGER.import_image_from_s3('test_3_saturation_1.png', False)

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
        fin = ASSET_MANAGER.import_image_from_s3('opacity_expected_50.png', False)
        im2 = opacity_editor(im1, 50)

        self.assertTrue(compare_images(fin, im2) == 0)

    def test_recoloration_correct_output(self):
        im1 = ASSET_MANAGER.import_image_from_s3('image.png', False)
        fin = ASSET_MANAGER.import_image_from_s3('gradient_expected_255_0_0_128.png', False)
        im2 = apply_color_editor(im1, [255, 0, 0, 128])

        self.assertTrue(compare_images(fin, im2) == 0)

    def test_gradient_correct_output(self):
        im1 = ASSET_MANAGER.import_image_from_s3('image.png', False)
        fin = ASSET_MANAGER.import_image_from_s3('filter_expected_70_255_0_0_0_0_255.png', False)
        im2 = apply_gradient_editor(im1, [70, [255, 0, 0], [0, 0, 255]])

        self.assertTrue(compare_images(fin, im2) == 0)
