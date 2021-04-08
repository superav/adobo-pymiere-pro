from logic.asset_manager import AssetManager
import unittest
import math
import operator
import requests
from io import BytesIO
from functools import reduce
from PIL import Image


# This will take the root mean square of the 2 images.
# If RMS == 0, the 2 images are equal
def compare_images(image_1, image_2):
    # Reference: https://stackoverflow.com/questions/1927660/compare-two-images-the-python-linux-way
    h1 = image_1.histogram()
    h2 = image_2.histogram()

    rms = math.sqrt(reduce(operator.add,
                           map(lambda a, b: (a - b) ** 2, h1, h2)) / len(h1))

    return rms


class TestInitializeAssetManager(unittest.TestCase):
    def test_invalid_username(self):
        with self.assertRaises(Exception):
            _ = AssetManager('bad username')

        with self.assertRaises(Exception):
            _ = AssetManager('badername ')

        with self.assertRaises(Exception):
            _ = AssetManager(' badusername')

    def test_valid_username(self):
        manager_one = AssetManager("good_username")
        manager_two = AssetManager("good002")
        manager_three = AssetManager("__xXX_raven_XXx__")

        self.assertEqual("good_username", manager_one.username)
        self.assertEqual("good002", manager_two.username)
        self.assertEqual("good002", manager_two.username)
        self.assertEqual("__xXX_raven_XXx__", manager_three.username)


class TestImportImages(unittest.TestCase):
    asset_manager = AssetManager('test_user_1')

    def test_import_existing_image(self):
        expected_image = Image.open('./test_assets/test_images/working_copy.png')

        image = self.asset_manager.import_image_from_s3('test_1.png', False)

        image.save('./test_assets/output.png')

        output = Image.open('./test_assets/output.png')
        root_mean_square = compare_images(expected_image, output)

        self.assertEqual(0, root_mean_square)

    def test_import_nonexistent_image(self):
        location_one = 'nope.png'
        location_two = 'test_1.png'
        location_three = 'working_copy.png'

        image_one = self.asset_manager.import_image_from_s3(location_one, False)
        image_two = self.asset_manager.import_image_from_s3(location_two)
        image_three = self.asset_manager.import_image_from_s3(location_three, False)

        self.assertEqual(None, image_one)
        self.assertEqual(None, image_two)
        self.assertEqual(None, image_three)

    def test_import_invalid_image_extension(self):
        location_one = 'test_user_1/image_projects/assets/bad'
        location_two = 'test_user_1/image_projects/assets/bad.txt'
        location_three = 'test_user_1/image_projects/assets/bad.'

        image_one = self.asset_manager.import_image_from_s3(location_one)
        image_two = self.asset_manager.import_image_from_s3(location_two)
        image_three = self.asset_manager.import_image_from_s3(location_three)

        self.assertEqual(None, image_one)
        self.assertEqual(None, image_two)
        self.assertEqual(None, image_three)


class TestUploadImages(unittest.TestCase):
    asset_manager = AssetManager('test_user_1')

    def test_upload_invalid_image_extension(self):
        image = Image.open('./test_assets/test_images/test_2.png')

        location_one = 'test_user_1/image_projects/assets/bad'
        location_two = 'test_user_1/image_projects/assets/bad.txt'
        location_three = 'test_user_1/image_projects/assets/bad.'

        image_one = self.asset_manager.upload_image_to_s3(image, location_one)
        image_two = self.asset_manager.upload_image_to_s3(image, location_two, False)
        image_three = self.asset_manager.upload_image_to_s3(image, location_three)

        self.assertEqual("Missing \".png\" extension!", image_one)
        self.assertEqual("Missing \".png\" extension!", image_two)
        self.assertEqual("Missing \".png\" extension!", image_three)

    def test_upload_valid_image_asset(self):
        image_one = Image.open('./test_assets/test_images/test_2.png')
        image_two = Image.open('./test_assets/test_images/test_3.png')

        expected_url_one = "https://adobo-pymiere.s3.amazonaws.com/test_user_1/image_projects/assets/test_2.png"
        expected_url_two = "https://adobo-pymiere.s3.amazonaws.com/test_user_1/image_projects/assets/test_3.png"

        url_one = self.asset_manager.upload_image_to_s3(image_one, "test_2.png", False)
        url_two = self.asset_manager.upload_image_to_s3(image_two, "test_3.png", False)

        r = requests.get(url_one)
        output = Image.open(BytesIO(r.content))

        root_mean_square = compare_images(output, image_one)

        self.assertEqual(0, root_mean_square)
        self.assertEqual(expected_url_one, url_one)

        r = requests.get(url_two)
        output = Image.open(BytesIO(r.content))

        root_mean_square = compare_images(output, image_two)

        self.assertEqual(0, root_mean_square)
        self.assertEqual(expected_url_two, url_two)

    def test_upload_valid_working_copy(self):
        image = Image.open('./test_assets/test_images/test_1.png')

        expected_url = "https://adobo-pymiere.s3.amazonaws.com/test_user_1/image_projects/working_copy.png"

        url = self.asset_manager.upload_image_to_s3(image)

        r = requests.get(url)
        output = Image.open(BytesIO(r.content))

        root_mean_square = compare_images(output, image)

        self.assertEqual(0, root_mean_square)
        self.assertEqual(expected_url, url)
