from logic.asset_manager import AssetManager
from logic.draw_on_image import *

from PIL import Image

import unittest
import math
import operator
from functools import reduce


ASSET_MANAGER = AssetManager('test_user_1')


# This will take the root mean square of the 2 images.
# If RMS == 0, the 2 images are equal
def compare_images(image_1, image_2):
    # Reference: https://stackoverflow.com/questions/1927660/compare-two-images-the-python-linux-way
    h1 = image_1.histogram()
    h2 = image_2.histogram()

    rms = math.sqrt(reduce(operator.add,
                           map(lambda a, b: (a - b) ** 2, h1, h2)) / len(h1))

    return rms


class TestDrawOnImageInputValidation(unittest.TestCase):
    def test_draw_on_image_invalid_input_type(self):
        input_img = Image.open("./test_assets/images/test_1.png")

        specifications = [[(0, 0), (10, 10)], 12, (255, 255, 255)]
        output = draw_line("bad", specifications)

        self.assertEqual(None, output)

        specifications = [[(0, 19), "hello"], 12, (20, 2, 244)]
        output = draw_line(input_img, specifications)
        self.assertEqual(None, output)

        specifications = [[(10, 10), (20, 20)], (10, "no"), "nope", 1.0]
        output = draw_line(input_img, specifications)
        self.assertEqual(None, output)

        specifications = [[(10, 10), (9, 2), (3, 4)], 23.4, "nope"]
        output = draw_line(input_img, specifications)
        self.assertEqual(None, output)

    def test_draw_on_image_invalid_input_value(self):
        input_img = Image.open("./test_assets/images/test_1.png")

        specifications = [[(0, 0), (1, 3), (10, 10)], 23, (-10, 233, 245)]
        output = draw_line(input_img, specifications)
        self.assertEqual(None, output)

        specifications = [[(0, 0), (1, 3), (10, 10)], -23, (0, 233, 245)]
        output = draw_line(input_img, specifications)
        self.assertEqual(None, output)

        specifications = [[(0, 0)], 23, (-10, 233, 245)]
        output = draw_line(input_img, specifications)
        self.assertEqual(None, output)

        specifications = [[(0, 0), (1, 3), (10, 10)], 23.3, (10, 233, 245)]
        output = draw_line(input_img, specifications)
        self.assertEqual(None, output)

    def test_draw_on_image_correct_input(self):
        input_img = Image.open("./test_assets/images/test_1.png")

        specifications = [[(0, 0), (1, 3), (10, 10)], 23, (10, 233, 245)]
        output = draw_line(input_img, specifications)

        self.assertTrue(isinstance(output, Image.Image))


class TestDrawOnImageCorrectOutputs(unittest.TestCase):
    def test_watermark_text_correct_output(self):
        # Position: (40, 40), Size: 0.5, Opacity: 1.0
        input_img = ASSET_MANAGER.import_image_from_s3('test_2.png', False)
        expected_img = ASSET_MANAGER.import_image_from_s3('test_2_draw_1.png', False)

        specifications = [[[100, 1000], [900, 10], [300, 300], [500, 435]], 23, [10, 233, 245]]
        output = draw_line(input_img, specifications)
        root_mean_square = compare_images(expected_img, output)

        self.assertEqual(0, root_mean_square)

        # Position: (40, 60), Size: 1.0, Opacity: 0.1
        input_img = ASSET_MANAGER.import_image_from_s3('test_1.png', False)
        expected_img = ASSET_MANAGER.import_image_from_s3('test_1_draw_2.png', False)

        points = []

        for i in range(150):
            x = 50 + i * 2
            y = int(x ** 2 / 250) + 10

            points.append([x, y])

        specifications = [points, 5, [255, 0, 0]]

        output = draw_line(input_img, specifications)
        root_mean_square = compare_images(expected_img, output)

        self.assertEqual(0, root_mean_square)
