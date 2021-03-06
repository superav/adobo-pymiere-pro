import math
import operator
from functools import reduce

import unittest

from logic.asset_manager import AssetManager
from logic.overlay_methods import *

ASSET_MANAGER = AssetManager('test_user_1')


# Reference:
# https://stackoverflow.com/questions/1927660/compare-two-images-the-python-linux-way
def compare_images(image_1, image_2):

    h1 = image_1.histogram()
    h2 = image_2.histogram()

    rms = math.sqrt(reduce(operator.add,
                           map(lambda a, b: (a - b) ** 2, h1, h2)) / len(h1))

    return rms


class TestOverlayInputValidation(unittest.TestCase):
    def test_watermark_image_invalid_input_type(self):
        input_img = Image.open("./test_assets/images/test_1.png")
        watermark = Image.open("./test_assets/images/test_2.png")

        with self.assertRaises(Exception):
            _ = add_watermark_image("bad", 10)

        specifications = [watermark, (10, 10), "nope", 1.0]

        with self.assertRaises(Exception):
            _ = add_watermark_image(input_img, specifications)

        specifications = [watermark, (10, "no"), "nope", 1.0]

        with self.assertRaises(Exception):
            _ = add_watermark_image(input_img, specifications)

        specifications = [watermark, (10, 3, 3), "nope", 1.0]

        with self.assertRaises(Exception):
            _ = add_watermark_image(input_img, specifications)

    def test_watermark_image_invalid_input_value(self):
        input_img = Image.open("./test_assets/images/test_1.png")
        watermark = Image.open("./test_assets/images/test_2.png")

        specifications = [watermark, (50, 50), 3.0, 1.0]

        with self.assertRaises(Exception):
            _ = add_watermark_image(input_img, specifications)

        specifications = [watermark, (50, 50), 1.0, 3.0]

        with self.assertRaises(Exception):
            _ = add_watermark_image(input_img, specifications)

        specifications = [watermark, (50, 50), 1.0, -1.0]

        with self.assertRaises(Exception):
            _ = add_watermark_image(input_img, specifications)

        specifications = [watermark, (50, 50), -0.2, 3.0]

        with self.assertRaises(Exception):
            _ = add_watermark_image(input_img, specifications)

    def test_watermark_image_correct_input(self):
        input_img = Image.open("./test_assets/images/test_1.png")
        watermark = Image.open("./test_assets/images/test_2.png")

        specifications = [watermark, [40, 40], 0.4, 1.0]
        output = add_watermark_image(input_img, specifications)

        self.assertTrue(isinstance(output, Image.Image))

    def test_add_text_to_image_invalid_input(self):
        im = 5
        specifications = ["hello", "arial.ttf", 50, [50, 50], [200, 200, 200]]

        with self.assertRaises(Exception):
            _ = add_text_to_image(im, specifications)

        im = ASSET_MANAGER.import_image_from_s3('test_2.png', False)

        specifications = [5, "arial.ttf", 50, [50, 50], [200, 200, 200]]

        with self.assertRaises(Exception):
            _ = add_text_to_image(im, specifications)

        specifications = ["hello", 5, 50, [50, 50], [200, 200, 200]]

        with self.assertRaises(Exception):
            _ = add_text_to_image(im, specifications)

        specifications = ["hello", "arial.ttf", 50, [50, 50, 50],
                          [200, 200, 200]]

        with self.assertRaises(Exception):
            _ = add_text_to_image(im, specifications)

        specifications = ["hello", "arial.ttf", 50, [50, 50], [200, 200]]

        with self.assertRaises(Exception):
            _ = add_text_to_image(im, specifications)

    def test_generate_meme_text_invalid_input(self):
        im = ASSET_MANAGER.import_image_from_s3('test_2.png', False)

        with self.assertRaises(Exception):
            _ = generate_meme_text(5, ["top text", "bottom text"])

        with self.assertRaises(Exception):
            _ = generate_meme_text(im, [1, "bottom text"])

        with self.assertRaises(Exception):
            _ = generate_meme_text(im, ["top text", 1])

        with self.assertRaises(Exception):
            _ = generate_meme_text(im, ["top text", "bottom text", "extra text"])

    def test_add_emoji_invalid_input_type(self):
        input_img = Image.open("./test_assets/images/test_1.png")
        watermark = "bugcat_owo.png"

        with self.assertRaises(Exception):
            _ = add_watermark_image("bad", 10)

        specifications = [watermark, (10, 10), "nope", 1.0]

        with self.assertRaises(Exception):
            _ = add_watermark_image(input_img, specifications)

        specifications = [watermark, (10, "no"), "nope", 1.0]

        with self.assertRaises(Exception):
            _ = add_watermark_image(input_img, specifications)

        specifications = [watermark, (10, 3, 3), "nope", 1.0]
        with self.assertRaises(Exception):
            _ = add_watermark_image(input_img, specifications)

    def test_add_emoji_invalid_input_value(self):
        input_img = Image.open("./test_assets/images/test_1.png")
        watermark = "bugcat_heart.png"

        specifications = [watermark, (50, 50), 3.0, 1.0]

        with self.assertRaises(Exception):
            _ = add_watermark_image(input_img, specifications)

        specifications = [watermark, (50, 50), 1.0, 3.0]

        with self.assertRaises(Exception):
            _ = add_watermark_image(input_img, specifications)

        specifications = [watermark, (50, 50), 1.0, -1.0]

        with self.assertRaises(Exception):
            _ = add_watermark_image(input_img, specifications)

        specifications = [watermark, (50, 50), -0.2, 3.0]

        with self.assertRaises(Exception):
            _ = add_watermark_image(input_img, specifications)

    def test_add_emoji_correct_input(self):
        input_img = Image.open("./test_assets/images/test_2.png")
        emoji_image = "bugcat_blush.png"

        specifications = [emoji_image, [40, 40], 0.4, 1.0]
        output = add_emoji_overlay(input_img, specifications, is_test=True)

        self.assertTrue(isinstance(output, Image.Image))


class TestOverlayImageProc(unittest.TestCase):
    def test_watermark_text_correct_output(self):
        # Position: (40, 40), Size: 0.5, Opacity: 1.0
        input_img = ASSET_MANAGER.import_image_from_s3('test_3.png', False)
        watermark = ASSET_MANAGER.import_image_from_s3('test_1.png', False)
        expected_img =\
            ASSET_MANAGER.import_image_from_s3('test_3_watermark_1.png', False)

        specifications = [watermark, (40, 40), 0.5, 1.0]
        output = add_watermark_image(input_img, specifications)
        root_mean_square = compare_images(expected_img, output)

        self.assertEqual(0, root_mean_square)

        # Position: (40, 60), Size: 1.0, Opacity: 0.1
        input_img = ASSET_MANAGER.import_image_from_s3('test_2.png', False)
        watermark = ASSET_MANAGER.import_image_from_s3('test_1.png', False)
        expected_img =\
            ASSET_MANAGER.import_image_from_s3('test_2_watermark_1.png', False)

        specifications = [watermark, (40, 60), 1.0, 0.1]
        output = add_watermark_image(input_img, specifications)
        root_mean_square = compare_images(expected_img, output)

        self.assertEqual(0, root_mean_square)

    def test_add_text_to_image_correct_output(self):
        im = ASSET_MANAGER.import_image_from_s3('test_2.png', False)
        specifications = ["hello", "arial.ttf", 50, [50, 50], [200, 200, 200]]

        self.assertNotEqual(None, add_text_to_image(im, specifications))

        fin = ASSET_MANAGER.import_image_from_s3('test_2_hello.png', False)
        rms = compare_images(im, fin)

        self.assertEqual(0, rms)

    def test_generate_meme_text_correct_output(self):
        im = ASSET_MANAGER.import_image_from_s3('test_2.png', False)
        output = generate_meme_text(im, ["top text", "bottom text"])

        self.assertTrue(isinstance(output, Image.Image))

        fin = ASSET_MANAGER.import_image_from_s3('test_2_memed.png', False)
        rms = compare_images(output, fin)

        self.assertEqual(0, rms)

    def test_add_emoji_correct_output(self):
        # Watermark: "bugcat_cry.png"
        # Position: (40, 40), Size: 0.5, Opacity: 1.0
        input_img = ASSET_MANAGER.import_image_from_s3('test_3.png', False)
        expected_img = ASSET_MANAGER.import_image_from_s3('test_3_emoji_1.png',
                                                          False)
        emoji = "bugcat_cry.png"

        specifications = [emoji, [400, 400], 0.5, 1.0]
        output = add_emoji_overlay(input_img, specifications, is_test=True)
        root_mean_square = compare_images(expected_img, output)

        self.assertEqual(0, root_mean_square)

        # Emoji: "bugcat_derp.png" Position: (40, 60), Size: 0.5, Opacity: 1.0
        input_img = ASSET_MANAGER.import_image_from_s3('test_1.png', False)
        expected_img = ASSET_MANAGER.import_image_from_s3('test_1_emoji_2.png',
                                                          False)
        emoji = "bugcat_derp.png"

        specifications = [emoji, (40, 60), 0.5, 1.0]
        output = add_emoji_overlay(input_img, specifications, is_test=True)
        root_mean_square = compare_images(expected_img, output)

        self.assertEqual(0, root_mean_square)
