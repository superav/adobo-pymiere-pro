import math
import operator
from functools import reduce

import unittest

from logic.asset_manager import AssetManager
from logic.misc_methods import *

ASSET_MANAGER = AssetManager('test_user_1')


# Reference: https://stackoverflow.com/questions/1927660/compare-two-images-the-python-linux-way
def compare_images(image_1, image_2):
    h1 = image_1.histogram()
    h2 = image_2.histogram()

    rms = math.sqrt(reduce(operator.add,
                           map(lambda a, b: (a - b) ** 2, h1, h2)) / len(h1))

    return rms


class TestMiscInputValidation(unittest.TestCase):
    def test_frame_valid_value(self):
        im1 = ASSET_MANAGER.import_image_from_s3('image.png', False)
        im2 = apply_frame(im1, [266, 999, -123])

        self.assertTrue(isinstance(im2, Image.Image))

    def test_mirror_invalid_value(self):
        im1 = ASSET_MANAGER.import_image_from_s3('image.png', False)

        with self.assertRaises(Exception):
            _ = apply_mirror(im1, -4)

        with self.assertRaises(Exception):
            _ = apply_mirror(im1, 5)

    def test_draw_on_image_invalid_input_type(self):
        input_img = Image.open("./test_assets/images/test_1.png")

        specifications = [[(0, 0), (10, 10)], 12, (255, 255, 255)]

        with self.assertRaises(Exception):
            _ = draw_lines("bad", specifications)

        specifications = [[(0, 19), "hello"], 12, (20, 2, 244)]

        with self.assertRaises(Exception):
            _ = draw_lines(input_img, specifications)

        specifications = [[(10, 10), (20, 20)], (10, "no"), "nope", 1.0]

        with self.assertRaises(Exception):
            _ = draw_lines(input_img, specifications)

        specifications = [[(10, 10), (9, 2), (3, 4)], 23.4, "nope"]

        with self.assertRaises(Exception):
            _ = draw_lines(input_img, specifications)

    def test_draw_on_image_invalid_input_value(self):
        input_img = Image.open("./test_assets/images/test_1.png")

        specifications = [[(0, 0), (1, 3), (10, 10)], 23, (-10, 233, 245)]

        with self.assertRaises(Exception):
            _ = draw_lines(input_img, specifications)

        specifications = [[(0, 0), (1, 3), (10, 10)], -23, (0, 233, 245)]

        with self.assertRaises(Exception):
            _ = draw_lines(input_img, specifications)

        specifications = [[(0, 0)], 23, (-10, 233, 245)]

        with self.assertRaises(Exception):
            _ = draw_lines(input_img, specifications)

        specifications = [[(0, 0), (1, 3), (10, 10)], 23.3, (10, 233, 245)]

        with self.assertRaises(Exception):
            _ = draw_lines(input_img, specifications)

    def test_draw_on_image_correct_input(self):
        input_img = Image.open("./test_assets/images/test_1.png")

        specifications = [[[(0, 0), (1, 3), (10, 10)], 23, (10, 233, 245)]]
        output = draw_lines(input_img, specifications)

        self.assertTrue(isinstance(output, Image.Image))


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

    def test_draw_on_image_correct_output(self):
        input_img = ASSET_MANAGER.import_image_from_s3('test_2.png', False)
        expected_img = ASSET_MANAGER.import_image_from_s3('test_2_draw_1.png',
                                                          False)

        specifications = [[[(100, 1000), (900, 10), (300, 300),
                           (500, 435)], 23, (10, 233, 245)]]
        output = draw_lines(input_img, specifications)
        root_mean_square = compare_images(expected_img, output)

        self.assertEqual(0, root_mean_square)

        input_img = ASSET_MANAGER.import_image_from_s3('test_1.png', False)
        expected_img = ASSET_MANAGER.import_image_from_s3('test_1_draw_2.png',
                                                          False)

        points = []

        for idx in range(150):
            x_pos = 50 + idx * 2
            y_pos = int(x_pos ** 2 / 250) + 10

            points.append((x_pos, y_pos))

        specifications = [[points, 5, (255, 0, 0)]]

        output = draw_lines(input_img, specifications)
        root_mean_square = compare_images(expected_img, output)

        self.assertEqual(0, root_mean_square)
