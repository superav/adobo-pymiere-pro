import unittest
import math
import operator
from functools import reduce

from logic.jz_image_proc import *
from logic.asset_manager import AssetManager


# This will take the root mean square of the 2 images.
# If RMS == 0, the 2 images are equal
def compare_images(image_1, image_2):
    # Reference: https://stackoverflow.com/questions/1927660/compare-two-images-the-python-linux-way
    h1 = image_1.histogram()
    h2 = image_2.histogram()

    rms = math.sqrt(reduce(operator.add,
                           map(lambda a, b: (a - b) ** 2, h1, h2)) / len(h1))

    return rms


ASSET_MANAGER = AssetManager('test_user_1')


class TestInputValidation(unittest.TestCase):
    def test_gaussian_blur_invalid_input_types(self):
        input_img = Image.open('./test_assets/images/test_1.png')

        output = gaussian_blur("bad", 0)
        self.assertEqual(None, output)

        output = gaussian_blur(input_img, "bad")
        self.assertEqual(None, output)

        output = gaussian_blur(input_img, -10.4)
        self.assertEqual(None, output)

    def test_gaussian_blur_invalid_radius_value(self):
        input_img = Image.open("./test_assets/images/test_1.png")

        output = gaussian_blur(input_img, -1)
        self.assertEqual(None, output)

        output = gaussian_blur(input_img, -45)
        self.assertEqual(None, output)

    def test_gaussian_blur_correct_input(self):
        input_img = Image.open("./test_assets/images/test_1.png")
        output = gaussian_blur(input_img, 9)

        self.assertTrue(isinstance(output, Image.Image))

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

    def test_watermark_image_invalid_input_type(self):
        input_img = Image.open("./test_assets/images/test_1.png")
        watermark = Image.open("./test_assets/images/test_2.png")

        output = add_watermark_image("bad", 10)

        self.assertEqual(None, output)

        specifications = [watermark, (10, 10), "nope", 1.0]
        output = add_watermark_image(input_img, specifications)
        self.assertEqual(None, output)

        specifications = [watermark, (10, "no"), "nope", 1.0]
        output = add_watermark_image(input_img, specifications)
        self.assertEqual(None, output)

        specifications = [watermark, (10, 3, 3), "nope", 1.0]
        output = add_watermark_image(input_img, specifications)
        self.assertEqual(None, output)

    def test_watermark_image_invalid_input_value(self):
        input_img = Image.open("./test_assets/images/test_1.png")
        watermark = Image.open("./test_assets/images/test_2.png")

        specifications = [watermark, (50, 50), 3.0, 1.0]
        output = add_watermark_image(input_img, specifications)
        self.assertEqual(None, output)

        specifications = [watermark, (50, 50), 1.0, 3.0]
        output = add_watermark_image(input_img, specifications)
        self.assertEqual(None, output)

        specifications = [watermark, (50, 50), 1.0, -1.0]
        output = add_watermark_image(input_img, specifications)
        self.assertEqual(None, output)

        specifications = [watermark, (50, 50), -0.2, 3.0]
        output = add_watermark_image(input_img, specifications)
        self.assertEqual(None, output)

    def test_watermark_image_correct_input(self):
        input_img = Image.open("./test_assets/images/test_1.png")
        watermark = Image.open("./test_assets/images/test_2.png")

        specifications = [watermark, (40, 40), 0.4, 1.0]
        output = add_watermark_image(input_img, specifications)

        self.assertTrue(isinstance(output, Image.Image))

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


class TestImageProc(unittest.TestCase):
    def test_gaussian_blur_correct_output(self):
        # Blur radius: 9
        input_img = ASSET_MANAGER.import_image_from_s3('test_1.png', False)
        expected_img = ASSET_MANAGER.import_image_from_s3('test_1_gaussian_1.png', False)

        output = gaussian_blur(input_img, 9)
        root_mean_square = compare_images(expected_img, output)

        self.assertEqual(0, root_mean_square)

        # Blur radius: 2
        input_img = ASSET_MANAGER.import_image_from_s3('test_2.png', False)
        expected_img = ASSET_MANAGER.import_image_from_s3('test_2_gaussian_1.png', False)

        output = gaussian_blur(input_img, 2)
        root_mean_square = compare_images(expected_img, output)

        self.assertEqual(0, root_mean_square)

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

    def test_watermark_text_correct_output(self):
        # Position: (40, 40), Size: 0.5, Opacity: 1.0
        input_img = ASSET_MANAGER.import_image_from_s3('test_3.png', False)
        watermark = ASSET_MANAGER.import_image_from_s3('test_1.png', False)
        expected_img = ASSET_MANAGER.import_image_from_s3('test_3_watermark_1.png', False)

        specifications = [watermark, (40, 40), 0.5, 1.0]
        output = add_watermark_image(input_img, specifications)
        root_mean_square = compare_images(expected_img, output)

        self.assertEqual(0, root_mean_square)

        # Position: (40, 60), Size: 1.0, Opacity: 0.1
        input_img = ASSET_MANAGER.import_image_from_s3('test_2.png', False)
        watermark = ASSET_MANAGER.import_image_from_s3('test_1.png', False)
        expected_img = ASSET_MANAGER.import_image_from_s3('test_2_watermark_1.png', False)

        specifications = [watermark, (40, 60), 1.0, 0.1]
        output = add_watermark_image(input_img, specifications)
        root_mean_square = compare_images(expected_img, output)

        self.assertEqual(0, root_mean_square)

    def test_scale_image_correct_output(self):
        # 0.1
        input_img = ASSET_MANAGER.import_image_from_s3('test_2.png', False)
        expected_img = ASSET_MANAGER.import_image_from_s3('test_2_scale_1.png', False)

        output = scale_image(input_img, 0.1)
        root_mean_square = compare_images(expected_img, output)

        self.assertEqual(0, root_mean_square)

        # 0.5
        input_img = ASSET_MANAGER.import_image_from_s3('test_1.png', False)
        expected_img = ASSET_MANAGER.import_image_from_s3('test_1_scale_1.png', False)

        output = scale_image(input_img, 0.5)
        root_mean_square = compare_images(expected_img, output)

        self.assertEqual(0, root_mean_square)

    def test_rotate_image_correct_output(self):
        # 90 degrees
        input_img = ASSET_MANAGER.import_image_from_s3('test_3.png', False)
        expected_img = ASSET_MANAGER.import_image_from_s3('test_3_rotate_1.png', False)

        output = rotate_image(input_img, 90)
        root_mean_square = compare_images(expected_img, output)

        self.assertEqual(0, root_mean_square)

        # 370 degrees
        input_img = ASSET_MANAGER.import_image_from_s3('test_3.png', False)
        expected_img = ASSET_MANAGER.import_image_from_s3('test_3_rotate_2.png', False)

        output = rotate_image(input_img, 370)
        root_mean_square = compare_images(expected_img, output)

        self.assertEqual(0, root_mean_square)
