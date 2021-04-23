import unittest
from logic.asset_manager import AssetManager
from logic.john_logic import *
import math
import operator
from functools import reduce
from PIL import Image

ASSET_MANAGER = AssetManager('test_user_1')


def compare_images(image_1, image_2):
    # Reference: https://stackoverflow.com/questions/1927660/compare-two-images-the-python-linux-way
    h1 = image_1.histogram()
    h2 = image_2.histogram()

    rms = math.sqrt(reduce(operator.add,
                           map(lambda a, b: (a - b) ** 2, h1, h2)) / len(h1))

    return rms


class YinjunSprintOneTests(unittest.TestCase):

    def test_add_text_to_image_invalid_input(self):
        im = 5
        self.assertEqual(None, add_text_to_image(im, ["hello", "arial.ttf", 50, [50, 50], [200, 200, 200]]))
        im = ASSET_MANAGER.import_image_from_s3('test_2.png', False)
        self.assertEqual(None, add_text_to_image(im, [5, "arial.ttf", 50, [50, 50], [200, 200, 200]]))
        self.assertEqual(None, add_text_to_image(im, ["hello", 5, 50, [50, 50], [200, 200, 200]]))
        self.assertEqual(None, add_text_to_image(im, ["hello", "arial.ttf", 50, [50, 50, 50], [200, 200, 200]]))
        self.assertEqual(None, add_text_to_image(im, ["hello", "arial.ttf", 50, [50, 50], [200, 200]]))

    def test_add_text_to_image_valid_input(self):
        im = ASSET_MANAGER.import_image_from_s3('test_2.png', False)
        self.assertNotEqual(None, add_text_to_image(im, ["hello", "arial.ttf", 50, [50, 50], [200, 200, 200]]))
        fin = ASSET_MANAGER.import_image_from_s3('test_2_hello.png', False)
        rms = compare_images(im, fin)
        self.assertEqual(0, rms)

    def test_store_image_in_filesystem_invalid_input(self):
        im = 5
        self.assertEqual(None, store_image_in_filesystem(im, "hellohop.jpg"))
        im = ASSET_MANAGER.import_image_from_s3('test_2.png', False)
        self.assertEqual(None, store_image_in_filesystem(im, 5))

    def test_store_image_in_filesystem_valid_input(self):
        im = ASSET_MANAGER.import_image_from_s3('test_2.png', False)
        self.assertNotEqual(None, store_image_in_filesystem(im, "test_2_stored.png"))
        fin = Image.open('test_2_stored.png')
        rms = compare_images(im, fin)
        self.assertEqual(0, rms)


if __name__ == '__main__':
    unittest.main()
