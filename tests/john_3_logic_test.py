import unittest
from logic.asset_manager import AssetManager
from logic.john_3_logic import *
import math
import operator
from functools import reduce

ASSET_MANAGER = AssetManager('test_user_1')


def compare_images(image_1, image_2):
    # Reference: https://stackoverflow.com/questions/1927660/compare-two-images-the-python-linux-way
    h1 = image_1.histogram()
    h2 = image_2.histogram()

    rms = math.sqrt(reduce(operator.add,
                           map(lambda a, b: (a - b) ** 2, h1, h2)) / len(h1))

    return rms


class JohnSprintThreeTests(unittest.TestCase):
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

    def test_generate_meme_text_valid_input(self):
        im = ASSET_MANAGER.import_image_from_s3('test_2.png', False)
        self.assertTrue(isinstance(generate_meme_text(im, ["top text", "bottom text"]), Image.Image))
        fin = ASSET_MANAGER.import_image_from_s3('test_2_memed.png', False)
        rms = compare_images(im, fin)
        self.assertEqual(0, rms)


if __name__ == '__main__':
    unittest.main()
