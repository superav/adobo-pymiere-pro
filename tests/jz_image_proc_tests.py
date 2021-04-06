import unittest
import math
import operator
from functools import reduce
from PIL import ImageChops
from logic.jz_image_proc import *


# This will take the root mean square of the 2 images.
# If RMS == 0, the 2 images are equal
def compare_images(image_1, image_2):
    # Reference: https://stackoverflow.com/questions/1927660/compare-two-images-the-python-linux-way
    h1 = image_1.histogram()
    h2 = image_2.histogram()

    rms = math.sqrt(reduce(operator.add,
                           map(lambda a, b: (a - b) ** 2, h1, h2)) / len(h1))

    return rms


class TestInputValidation(unittest.TestCase):
    def test_gaussian_blur_invalid_input(self):
        pass

    def test_gaussian_blur_correct_input(self):
        pass

    def test_saturation_invalid_input(self):
        pass

    def test_saturation_correct_input(self):
        pass

    def test_watermark_text_invalid_input(self):
        pass

    def test_watermark_text_correct_input(self):
        pass


class TestImageProc(unittest.TestCase):
    def test_gaussian_blur_correct_output(self):
        input_img = Image.open("test_images/test_1.png")

        # Blur radius: 9
        expected_img = Image.open("test_images/test_1_gaussian_1.png")

        output = gaussian_blur(input_img, 9)
        output.save('test_images/output.png')

        output_img = Image.open('test_images/output.png')

        root_mean_square = compare_images(expected_img, output_img)

        self.assertEqual(0, root_mean_square)

        # Blur radius: 2
        expected_img = Image.open("test_images/test_1_gaussian_2.png")

        output = gaussian_blur(input_img, 2)
        output.save('test_images/output.png')

        output_img = Image.open('test_images/output.png')

        root_mean_square = compare_images(expected_img, output_img)

        self.assertEqual(0, root_mean_square)

    def test_saturation_correct_output(self):
        input_img = Image.open("test_images/test_1.png")

        # Saturation: 0.5
        expected_img = Image.open("test_images/test_1_saturation_1.png")

        output = change_saturation(input_img, 0.5)
        output.save('test_images/output.png')

        output_img = Image.open('test_images/output.png')

        root_mean_square = compare_images(output_img, expected_img)

        self.assertEqual(0, root_mean_square)

        # Saturation: 1.5
        expected_img = Image.open("test_images/test_1_saturation_2.png")

        output = change_saturation(input_img, 1.5)
        output.save('test_images/output.png')

        output_img = Image.open('test_images/output.png')

        root_mean_square = compare_images(output_img, expected_img)

        self.assertEqual(0, root_mean_square)

    def test_watermark_text_correct_output(self):
        input_img = Image.open("test_images/test_1.png")

        # Text: "Hello", Position: 20, 20
        expected_img = Image.open("test_images/test_1_watermark_1.png")

        output = add_watermark_text(input_img, "Hello", (20, 20))
        output.save('test_images/output.png')

        output_img = Image.open('test_images/output.png')

        root_mean_square = compare_images(expected_img, output_img)

        self.assertEqual(0, root_mean_square)

        # Text: "Hello", Position: (200, 300), font: Dela Gothic Regular, color: (161, 232, 175, 175)
        expected_img = Image.open("test_images/test_1_watermark_2.png")

        output = add_watermark_text(input_img, "Hello", (200, 300),
                                    font='test_fonts/DelaGothicOne-Regular.ttf',
                                    size=72,
                                    color=(161, 232, 175, 175))
        output.save('test_images/output.png')

        output_img = Image.open('test_images/output.png')

        root_mean_square = compare_images(expected_img, output_img)

        self.assertEqual(0, root_mean_square)

    def test_scale_image_correct_output(self):
        input_img = Image.open("test_images/test_1.png")

        # 0.1
        expected_img = Image.open("test_images/test_1_thumbnail_1.png")

        output = scale_image(input_img, 0.1)
        output.save('test_images/output.png')

        output_img = Image.open('test_images/output.png')

        root_mean_square = compare_images(expected_img, output_img)

        self.assertEqual(0, root_mean_square)

        # 0.5
        expected_img = Image.open("test_images/test_1_thumbnail_2.png")

        output = scale_image(input_img, 0.5)
        output.save('test_images/output.png')

        output_img = Image.open('test_images/output.png')

        root_mean_square = compare_images(expected_img, output_img)

        self.assertEqual(0, root_mean_square)

    def test_rotate_image_correct_output(self):
        input_img = Image.open("test_images/test_1.png")

        # 90 degrees
        expected_img = Image.open("test_images/test_1_rotate_1.png")

        output = rotate_image(input_img, 90)
        output.save('test_images/output.png')

        output_img = Image.open('test_images/output.png')

        root_mean_square = compare_images(expected_img, output_img)

        self.assertEqual(0, root_mean_square)

        # 370 degrees
        expected_img = Image.open("test_images/test_1_rotate_2.png")

        output = rotate_image(input_img, 370)
        output.save('test_images/output.png')

        output_img = Image.open('test_images/output.png')

        root_mean_square = compare_images(expected_img, output_img)

        self.assertEqual(0, root_mean_square)

    def test_import_image_correct_output(self):
        pass


class TestVideoProc(unittest.TestCase):
    def test_rotate_video_correct_output(self):
        pass
