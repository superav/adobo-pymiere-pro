import math
import operator
from functools import reduce

import unittest

from logic.asset_manager import AssetManager
from logic.canvas_editing_methods import *

ASSET_MANAGER = AssetManager('test_user_1')


# Reference: https://stackoverflow.com/questions/1927660/compare-two-images-the-python-linux-way
def compare_images(image_1, image_2):

    h1 = image_1.histogram()
    h2 = image_2.histogram()

    rms = math.sqrt(reduce(operator.add,
                           map(lambda a, b: (a - b) ** 2, h1, h2)) / len(h1))

    return rms


class TestCanvasEditingInputValidation(unittest.TestCase):
    def test_crop_invalid_value(self):
        im1 = ASSET_MANAGER.import_image_from_s3('image.png', False)
        im2 = crop_editor(im1, [20, 30, 1500, 1000])
        im3 = crop_editor(im1, [20, 30, 1000, 1500])
        im4 = crop_editor(im1, [20, 30, 10, 1000])
        im5 = crop_editor(im1, [20, 30, 1000, 10])
        im6 = crop_editor(im1, [-20, 30, 700, 700])
        im7 = crop_editor(im1, [20, -30, 700, 700])

        self.assertEqual(im2, None)
        self.assertEqual(im3, None)
        self.assertEqual(im4, None)
        self.assertEqual(im5, None)
        self.assertEqual(im6, None)
        self.assertEqual(im7, None)

    def test_scale_image_invalid_input_type(self):
        input_img = Image.open("./test_assets/images/test_1.png")

        output = scale_image("no", 0.4)
        self.assertEqual(None, output)

        output = scale_image(input_img, input_img)
        self.assertEqual(None, output)

    def test_scale_image_invalid_input_value(self):
        input_img = Image.open("./test_assets/images/test_1.png")

        output = scale_image(input_img, -0.3)
        self.assertEqual(None, output)

        output = scale_image(input_img, 2.0)
        self.assertEqual(None, output)

    def test_scale_image_correct_input(self):
        input_img = Image.open("./test_assets/images/test_1.png")
        output = scale_image(input_img, 0.5)

        self.assertTrue(isinstance(output, Image.Image))

    def test_rotate_image_invalid_input_type(self):
        input_img = Image.open("./test_assets/images/test_1.png")

        output = rotate_image("no", 44)
        self.assertEqual(None, output)

        output = rotate_image(input_img, (9, 9))
        self.assertEqual(None, output)

    def test_rotate_image_correct_input(self):
        input_img = Image.open("./test_assets/images/test_1.png")
        output = rotate_image(input_img, 45)

        self.assertTrue(isinstance(output, Image.Image))


class TestCanvasEditingImageProc(unittest.TestCase):
    def test_crop_image_correct_output(self):
        im1 = ASSET_MANAGER.import_image_from_s3('image.png', False)
        fin = ASSET_MANAGER.import_image_from_s3(
            'crop_expected_20_30_700_700.png', False)

        im2 = crop_editor(im1, [20, 30, 700, 700])
        self.assertTrue(compare_images(fin, im2) == 0)

    def test_rotate_image_correct_output(self):
        # 90 degrees
        input_img = ASSET_MANAGER.import_image_from_s3('test_3.png', False)
        expected_img = ASSET_MANAGER.import_image_from_s3('test_3_rotate_1.png',
                                                          False)

        output = rotate_image(input_img, 90)
        root_mean_square = compare_images(expected_img, output)

        self.assertEqual(0, root_mean_square)

        # 370 degrees
        input_img = ASSET_MANAGER.import_image_from_s3('test_3.png', False)
        expected_img = ASSET_MANAGER.import_image_from_s3('test_3_rotate_2.png',
                                                          False)

        output = rotate_image(input_img, 370)
        root_mean_square = compare_images(expected_img, output)

        self.assertEqual(0, root_mean_square)

    def test_scale_image_correct_output(self):
        # 0.1
        input_img = ASSET_MANAGER.import_image_from_s3('test_2.png', False)
        expected_img = ASSET_MANAGER.import_image_from_s3('test_2_scale_1.png',
                                                          False)

        output = scale_image(input_img, 0.1)
        root_mean_square = compare_images(expected_img, output)

        self.assertEqual(0, root_mean_square)

        # 0.5
        input_img = ASSET_MANAGER.import_image_from_s3('test_1.png', False)
        expected_img = ASSET_MANAGER.import_image_from_s3('test_1_scale_1.png',
                                                          False)

        output = scale_image(input_img, 0.5)
        root_mean_square = compare_images(expected_img, output)

        self.assertEqual(0, root_mean_square)
