import unittest
import math
import operator
from functools import reduce
from moviepy.editor import VideoFileClip
import numpy as np

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

        with self.assertRaises(TypeError):
            _ = gaussian_blur("bad", 0)

        with self.assertRaises(TypeError):
            _ = gaussian_blur(input_img, "bad")

        with self.assertRaises(TypeError):
            _ = gaussian_blur(input_img, -10.4)

    def test_gaussian_blur_invalid_radius_value(self):
        input_img = Image.open("./test_assets/images/test_1.png")

        with self.assertRaises(ValueError):
            _ = gaussian_blur(input_img, -1)

        with self.assertRaises(ValueError):
            _ = gaussian_blur(input_img, -45)

    def test_gaussian_blur_correct_input(self):
        input_img = Image.open("./test_assets/images/test_1.png")
        output = gaussian_blur(input_img, 9)

        self.assertTrue(isinstance(output, Image.Image))

    def test_saturation_invalid_input_type(self):
        input_img = Image.open("./test_assets/images/test_1.png")

        with self.assertRaises(TypeError):
            _ = change_saturation("bad", 4.0)

        with self.assertRaises(TypeError):
            _ = change_saturation(input_img, True)

        with self.assertRaises(TypeError):
            _ = change_saturation(True, "bad")

    def test_saturation_invalid_input_value(self):
        input_img = Image.open("./test_assets/images/test_1.png")

        with self.assertRaises(ValueError):
            _ = change_saturation(input_img, -33.0)

        with self.assertRaises(ValueError):
            _ = change_saturation(input_img, -0.1)

    def test_saturation_correct_input(self):
        input_img = Image.open("./test_assets/images/test_1.png")
        output = change_saturation(input_img, 1.2)

        self.assertTrue(isinstance(output, Image.Image))

    def test_watermark_image_invalid_input_type(self):
        input_img = Image.open("./test_assets/images/test_1.png")
        watermark = Image.open("./test_assets/images/test_2.png")

        with self.assertRaises(TypeError):
            _ = add_watermark_image("bad", watermark, 10, 0.2, 0.4)

        with self.assertRaises(TypeError):
            _ = add_watermark_image(input_img, watermark, (10, 10), "nope", 1.0)

        with self.assertRaises(TypeError):
            _ = add_watermark_image(input_img, watermark, (10, "no"))

        with self.assertRaises(TypeError):
            _ = add_watermark_image(input_img, watermark, (10, 3, 3))

    def test_watermark_image_invalid_input_value(self):
        input_img = Image.open("./test_assets/images/test_1.png")
        watermark = Image.open("./test_assets/images/test_2.png")

        with self.assertRaises(ValueError):
            _ = add_watermark_image(input_img, watermark, (50, 50), size=3.0)

        with self.assertRaises(ValueError):
            _ = add_watermark_image(input_img, watermark, (50, 50), opacity=3.0)

        with self.assertRaises(ValueError):
            _ = add_watermark_image(input_img, watermark, (50, 50), opacity=-1.0)

        with self.assertRaises(ValueError):
            _ = add_watermark_image(input_img, watermark, (50, 50), size=-0.3)

    def test_watermark_image_correct_input(self):
        input_img = Image.open("./test_assets/images/test_1.png")
        watermark = Image.open("./test_assets/images/test_2.png")

        output = add_watermark_image(input_img, watermark, (40, 40), size=0.4)

        self.assertTrue(isinstance(output, Image.Image))

    def test_scale_image_invalid_input_type(self):
        input_img = Image.open("./test_assets/images/test_1.png")

        with self.assertRaises(TypeError):
            _ = scale_image("no", 0.4)

        with self.assertRaises(TypeError):
            _ = scale_image(input_img, input_img)

    def test_scale_image_invalid_input_value(self):
        input_img = Image.open("./test_assets/images/test_1.png")

        with self.assertRaises(ValueError):
            _ = scale_image(input_img, -0.3)

        with self.assertRaises(ValueError):
            _ = scale_image(input_img, 2.0)

    def test_scale_image_correct_input(self):
        input_img = Image.open("./test_assets/images/test_1.png")
        output = scale_image(input_img, 0.5)

        self.assertTrue(isinstance(output, Image.Image))

    def test_rotate_image_invalid_input_type(self):
        input_img = Image.open("./test_assets/images/test_1.png")

        with self.assertRaises(TypeError):
            _ = rotate_image("no", 44)

        with self.assertRaises(TypeError):
            _ = rotate_image(input_img, (9, 9))

    def test_rotate_image_correct_input(self):
        input_img = Image.open("./test_assets/images/test_1.png")
        output = rotate_image(input_img, 45.)

        self.assertTrue(isinstance(output, Image.Image))

    def test_rotate_video_invalid_input_type(self):
        input_clip = VideoFileClip('./test_assets/videos/video_1.mp4')

        with self.assertRaises(TypeError):
            _ = rotate_video(True, 44)

        with self.assertRaises(TypeError):
            _ = rotate_video(input_clip, (30, 30))

    def test_rotate_video_correct_input(self):
        input_clip = VideoFileClip('./test_assets/videos/video_1.mp4')
        output = rotate_video(input_clip, 45.)

        self.assertTrue(isinstance(output, Clip.Clip))


class TestImageProc(unittest.TestCase):
    def test_gaussian_blur_correct_output(self):
        # Blur radius: 9
        input_img = ASSET_MANAGER.import_image_from_s3('test_1.png', False)
        expected_img = ASSET_MANAGER.import_image_from_s3('test_1_gaussian_1.png', False)

        output = gaussian_blur(input_img, 9)
        output.save('./test_assets/output.png')

        output_img = Image.open('test_assets/output.png')

        root_mean_square = compare_images(expected_img, output_img)

        self.assertEqual(0, root_mean_square)

        # Blur radius: 2
        input_img = ASSET_MANAGER.import_image_from_s3('test_2.png', False)
        expected_img = ASSET_MANAGER.import_image_from_s3('test_2_gaussian_1.png', False)

        output = gaussian_blur(input_img, 2)
        output.save('test_assets/output.png')

        output_img = Image.open('test_assets/output.png')

        root_mean_square = compare_images(expected_img, output_img)

        self.assertEqual(0, root_mean_square)

    def test_saturation_correct_output(self):
        # Saturation: 0.5
        input_img = ASSET_MANAGER.import_image_from_s3('test_2.png', False)
        expected_img = ASSET_MANAGER.import_image_from_s3('test_2_saturation_1.png', False)

        output = change_saturation(input_img, 0.5)
        output.save('test_assets/output.png')

        output_img = Image.open('test_assets/output.png')

        root_mean_square = compare_images(output_img, expected_img)

        self.assertEqual(0, root_mean_square)

        # Saturation: 1.5
        input_img = ASSET_MANAGER.import_image_from_s3('test_3.png', False)
        expected_img = ASSET_MANAGER.import_image_from_s3('test_3_saturation_1.png', False)

        output = change_saturation(input_img, 1.5)
        output.save('test_assets/output.png')

        output_img = Image.open('test_assets/output.png')

        root_mean_square = compare_images(output_img, expected_img)

        self.assertEqual(0, root_mean_square)

    def test_watermark_text_correct_output(self):
        # Position: (40, 40), Size: 0.5, Opacity: 1.0
        input_img = ASSET_MANAGER.import_image_from_s3('test_3.png', False)
        watermark = ASSET_MANAGER.import_image_from_s3('test_1.png', False)
        expected_img = ASSET_MANAGER.import_image_from_s3('test_3_watermark_1.png', False)

        output = add_watermark_image(input_img, watermark, (40, 40), size=0.5)
        output.save('test_assets/output.png')

        output_img = Image.open('test_assets/output.png')

        root_mean_square = compare_images(expected_img, output_img)

        self.assertEqual(0, root_mean_square)

        # Text: "Hello", Position: (200, 300), font: Dela Gothic Regular, color: (161, 232, 175, 175)
        input_img = ASSET_MANAGER.import_image_from_s3('test_2.png', False)
        watermark = ASSET_MANAGER.import_image_from_s3('test_1.png', False)
        expected_img = ASSET_MANAGER.import_image_from_s3('test_2_watermark_1.png', False)

        output = add_watermark_image(input_img, watermark, (40, 60), opacity=0.1)
        output.save('test_assets/output.png')

        output_img = Image.open('test_assets/output.png')

        root_mean_square = compare_images(expected_img, output_img)

        self.assertEqual(0, root_mean_square)

    def test_scale_image_correct_output(self):
        # 0.1
        input_img = ASSET_MANAGER.import_image_from_s3('test_2.png', False)
        expected_img = ASSET_MANAGER.import_image_from_s3('test_2_scale_1.png', False)

        output = scale_image(input_img, 0.1)
        output.save('test_assets/output.png')

        output_img = Image.open('test_assets/output.png')

        root_mean_square = compare_images(expected_img, output_img)

        self.assertEqual(0, root_mean_square)

        # 0.5
        input_img = ASSET_MANAGER.import_image_from_s3('test_1.png', False)
        expected_img = ASSET_MANAGER.import_image_from_s3('test_1_scale_1.png', False)

        output = scale_image(input_img, 0.5)
        output.save('test_assets/output.png')

        output_img = Image.open('test_assets/output.png')

        root_mean_square = compare_images(expected_img, output_img)

        self.assertEqual(0, root_mean_square)

    def test_rotate_image_correct_output(self):
        # 90 degrees
        input_img = ASSET_MANAGER.import_image_from_s3('test_3.png', False)
        expected_img = ASSET_MANAGER.import_image_from_s3('test_3_rotate_1.png', False)

        output = rotate_image(input_img, 90)
        output.save('test_assets/output.png')

        output_img = Image.open('test_assets/output.png')

        root_mean_square = compare_images(expected_img, output_img)

        self.assertEqual(0, root_mean_square)

        # 370 degrees
        input_img = ASSET_MANAGER.import_image_from_s3('test_3.png', False)
        expected_img = ASSET_MANAGER.import_image_from_s3('test_3_rotate_2.png', False)

        output = rotate_image(input_img, 370)
        output.save('test_assets/output.png')

        output_img = Image.open('test_assets/output.png')

        root_mean_square = compare_images(expected_img, output_img)

        self.assertEqual(0, root_mean_square)


class TestVideoProc(unittest.TestCase):
    def test_rotate_video_correct_output(self):
        clip = VideoFileClip("./test_assets/videos/video_1.mp4")

        # 45
        expected_clip = VideoFileClip("./test_assets/videos/video_1_rotate_1.mp4")
        output_clip = rotate_video(clip, 45)

        output_clip.write_videofile("./test_assets/output.mp4")

        output = VideoFileClip("./test_assets/output.mp4")

        expected_frames = list(expected_clip.iter_frames())
        output_frames = list(output.iter_frames())

        for expected_frame, output_frame in zip(expected_frames, output_frames):
            self.assertTrue(np.array_equal(expected_frame, output_frame))

        # -80
        expected_clip = VideoFileClip("./test_assets/videos/video_1_rotate_2.mp4")
        output_clip = rotate_video(clip, -80)

        output_clip.write_videofile("./test_assets/output.mp4")

        output = VideoFileClip("./test_assets/output.mp4")

        expected_frames = list(expected_clip.iter_frames())
        output_frames = list(output.iter_frames())

        for expected_frame, output_frame in zip(expected_frames, output_frames):
            self.assertTrue(np.array_equal(expected_frame, output_frame))
