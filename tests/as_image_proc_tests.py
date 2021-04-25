import math

from PIL import Image
import unittest
import operator
from functools import reduce
from logic import as_image_proc
from logic.asset_manager import AssetManager

ASSET_MANAGER = AssetManager('test_user_1')


def compare_images(image_1, image_2):
    # Reference: https://stackoverflow.com/questions/
    #               1927660/compare-two-images-the-python-linux-way
    h1 = image_1.histogram()
    h2 = image_2.histogram()

    rms = math.sqrt(reduce(operator.add,
                           map(lambda a, b: (a - b) ** 2, h1, h2)) / len(h1))

    return rms


class EditImageTestCase(unittest.TestCase):
    def test_hue_editing_image(self):
        im1 = ASSET_MANAGER.import_image_from_s3('image.png', False)
        fin = ASSET_MANAGER.import_image_from_s3('hue_expected_180.png', False)
        im2 = as_image_proc.hue_editor(im1, 180)
        self.assertTrue(compare_images(fin, im2) == 0)

    def test_hue_invalid_value(self):
        im1 = ASSET_MANAGER.import_image_from_s3('image.png', False)
        im2 = as_image_proc.hue_editor(im1, 580)
        im3 = as_image_proc.hue_editor(im1, -1)
        self.assertTrue(im2 is None, True)
        self.assertTrue(im3 is None, True)

    def test_crop_editing_image(self):
        im1 = ASSET_MANAGER.import_image_from_s3('image.png', False)
        fin = ASSET_MANAGER.import_image_from_s3(
            'crop_expected_20_30_700_700.png', False)
        im2 = as_image_proc.crop_editor(im1, [20, 30, 700, 700])
        self.assertTrue(compare_images(fin, im2) == 0)

    def test_crop_invalid_value(self):
        im1 = ASSET_MANAGER.import_image_from_s3('image.png', False)
        im2 = as_image_proc.crop_editor(im1, [20, 30, 1500, 1000])
        im3 = as_image_proc.crop_editor(im1, [20, 30, 1000, 1500])
        im4 = as_image_proc.crop_editor(im1, [20, 30, 10, 1000])
        im5 = as_image_proc.crop_editor(im1, [20, 30, 1000, 10])
        im6 = as_image_proc.crop_editor(im1, [-20, 30, 700, 700])
        im7 = as_image_proc.crop_editor(im1, [20, -30, 700, 700])

        self.assertTrue(im2 is None, True)
        self.assertTrue(im3 is None, True)
        self.assertTrue(im4 is None, True)
        self.assertTrue(im5 is None, True)
        self.assertTrue(im6 is None, True)
        self.assertTrue(im7 is None, True)

    def test_opacity_editing_image(self):
        im1 = ASSET_MANAGER.import_image_from_s3('image.png', False)
        fin = ASSET_MANAGER.import_image_from_s3(
            'opacity_expected_50.png', False)
        im2 = as_image_proc.opacity_editor(im1, 50)
        self.assertTrue(compare_images(fin, im2) == 0)

    def test_opacity_invalid_inputs(self):
        im1 = ASSET_MANAGER.import_image_from_s3('image.png', False)
        im2 = as_image_proc.opacity_editor(im1, 400)
        im3 = as_image_proc.opacity_editor(im1, -400)

        self.assertTrue(im2 is None, True)
        self.assertTrue(im3 is None, True)

    def test_gradient_color_image(self):
        im1 = ASSET_MANAGER.import_image_from_s3('image.png', False)
        fin = ASSET_MANAGER.import_image_from_s3(
            'gradient_expected_255_0_0_128.png', False)
        im2 = as_image_proc.apply_color_editor(im1, [255, 0, 0, 128])
        self.assertTrue(compare_images(fin, im2) == 0)

    def test_gradient_invalid_value(self):
        im1 = ASSET_MANAGER.import_image_from_s3('image.png', False)
        im2 = as_image_proc.apply_color_editor(im1, [256, 0, 0, 128])
        im3 = as_image_proc.apply_color_editor(im1, [256, 0, 300, 128])
        im4 = as_image_proc.apply_color_editor(im1, [256, -1, 0, 128])
        im5 = as_image_proc.apply_color_editor(im1, [256, 0, 0, 277])
        im6 = as_image_proc.apply_color_editor(im1, [256, 0, 0, -128])

        self.assertTrue(im2 is None, True)
        self.assertTrue(im3 is None, True)
        self.assertTrue(im4 is None, True)
        self.assertTrue(im5 is None, True)
        self.assertTrue(im6 is None, True)

    def test_filter_editing_image(self):
        im1 = ASSET_MANAGER.import_image_from_s3('image.png', False)
        fin = ASSET_MANAGER.import_image_from_s3(
            'filter_expected_70_255_0_0_0_0_255.png', False)
        im2 = as_image_proc.apply_gradient_editor(im1, [70, [255, 0, 0],
                                                        [0, 0, 255]])
        self.assertTrue(compare_images(fin, im2) == 0)

    def test_filter_invalid_value(self):
        im1 = ASSET_MANAGER.import_image_from_s3('image.png', False)
        im2 = as_image_proc.apply_gradient_editor(im1, [70, [255, 0, 0],
                                                        [0, -10, 255]])
        im3 = as_image_proc.apply_gradient_editor(im1, [70, [0, 290, 0],
                                                        [0, 0, 255]])
        im4 = as_image_proc.apply_gradient_editor(im1, [70, [255, 0, 0],
                                                        [0, -7, 255]])
        im5 = as_image_proc.apply_gradient_editor(im1, [70, [255, 0, 0],
                                                        [-9, 0, 255]])
        im6 = as_image_proc.apply_gradient_editor(im1, [70, [14, 190, 300],
                                                        [0, 0, 255]])
        im7 = as_image_proc.apply_gradient_editor(im1, [700, [255, 0, 0],
                                                        [0, 0, 255]])
        im8 = as_image_proc.apply_gradient_editor(im1, [-7, [255, 0, 0],
                                                        [0, 0, 255]])
        self.assertTrue(im2 is None, True)
        self.assertTrue(im3 is None, True)
        self.assertTrue(im4 is None, True)
        self.assertTrue(im5 is None, True)
        self.assertTrue(im6 is None, True)
        self.assertTrue(im7 is None, True)
        self.assertTrue(im8 is None, True)

    def test_mirror_color_image(self):
        im1 = ASSET_MANAGER.import_image_from_s3('image.png', False)
        im2 = as_image_proc.apply_mirror(im1, 0)
        fin2 = ASSET_MANAGER.import_image_from_s3('mirror_expected.png', False)
        im3 = as_image_proc.apply_mirror(im1, 1)
        fin3 = ASSET_MANAGER.import_image_from_s3('flip_expected.png', False)
        self.assertTrue(compare_images(fin2, im2) == 0)
        self.assertTrue(compare_images(fin3, im3) == 0)

    def test_mirror_invalid_value(self):
        im1 = ASSET_MANAGER.import_image_from_s3('image.png', False)
        im2 = as_image_proc.apply_mirror(im1, -4)
        im3 = as_image_proc.apply_mirror(im1, 5)

        self.assertTrue(im2 is None, True)
        self.assertTrue(im3 is None, True)

    def test_frame_color_image(self):
        im1 = ASSET_MANAGER.import_image_from_s3('image.png', False)
        fin = ASSET_MANAGER.import_image_from_s3(
            'frame_expected_120_75_225.png', False)
        im2 = as_image_proc.apply_frame(im1, [255, 0, 0])
        self.assertTrue(compare_images(fin, im2) == 0)

    def test_frame_invalid_value(self):
        im1 = ASSET_MANAGER.import_image_from_s3('image.png', False)
        im2 = as_image_proc.apply_frame(im1, [266, 999, -123])
        self.assertTrue(im2 is not None, True)

    def test_solarize_color_image(self):
        im1 = ASSET_MANAGER.import_image_from_s3('image.png', False)
        fin = ASSET_MANAGER.import_image_from_s3(
            'solarize_expected_128.png', False)
        im2 = as_image_proc.apply_solarize(im1, 128)
        self.assertTrue(compare_images(fin, im2) == 0)

    def test_solarize_invalid_value(self):
        im1 = ASSET_MANAGER.import_image_from_s3('image.png', False)
        im2 = as_image_proc.apply_solarize(im1, 9999)
        im3 = as_image_proc.apply_solarize(im1, -1234)
        self.assertTrue(im2 is not None, True)
        self.assertTrue(im3 is not None, True)

    def test_mosaic_color_image(self):
        im1 = ASSET_MANAGER.import_image_from_s3('image.png', False)
        fin = ASSET_MANAGER.import_image_from_s3('mosaic_expected.png', False)
        im2 = as_image_proc.apply_mosaic_filter(im1)
        self.assertTrue(compare_images(fin, im2) == 0)

    def test_red_eye_color_image(self):
        im1 = ASSET_MANAGER.import_image_from_s3('redeye.png', False)
        fin = ASSET_MANAGER.import_image_from_s3(
            'red_eye_expected_35_110_150_150.png', False)
        im2 = as_image_proc.apply_red_eye_filter(im1, [35, 110, 150, 150])
        self.assertTrue(compare_images(fin, im2) == 0)

    def test_red_eye_invalid_value(self):
        im1 = ASSET_MANAGER.import_image_from_s3('redeye.png', False)
        im2 = as_image_proc.apply_red_eye_filter(im1, [-23, 1000, 150, 150])
        self.assertTrue(im2 is not None, True)
