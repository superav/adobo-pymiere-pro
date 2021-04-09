import unittest
from PIL import Image, ImageFont, ImageDraw
from moviepy.editor import *
from john_logic import *


class MyTestCase(unittest.TestCase):
    def test_add_text_to_image_invalid_input(self):
        im = 5
        self.assertEqual(None, add_text_to_image(im, "hello", "arial.ttf", 50, (50, 50), (200, 200, 200)))
        im = Image.open("hopper.jpg")
        self.assertEqual(None, add_text_to_image(im, 5, "arial.ttf", 50, (50, 50), (200, 200, 200)))
        self.assertEqual(None, add_text_to_image(im, "hello", 5, 50, (50, 50), (200, 200, 200)))
        self.assertEqual(None, add_text_to_image(im, "hello", "arial.ttf", 50, [50, 50], (200, 200, 200)))
        self.assertEqual(None, add_text_to_image(im, "hello", "arial.ttf", 50, (50, 50), [200, 200, 200]))
        self.assertEqual(None, add_text_to_image(im, "hello", "arial.ttf", 50, (50, 50, 50), (200, 200, 200)))
        self.assertEqual(None, add_text_to_image(im, "hello", "arial.ttf", 50, (50, 50), (200, 200)))

    def test_add_text_to_image_valid_input(self):
        im = Image.open("hopper.jpg")
        self.assertNotEqual(None, add_text_to_image(im, "hello", "arial.ttf", 50, (50, 50), (200, 200, 200)))

    def test_store_image_in_filesystem_invalid_input(self):
        im = 5
        self.assertEqual(None, store_image_in_filesystem(im, "hellohop.jpg"))
        im = Image.open("hopper.jpg")
        self.assertEqual(None, store_image_in_filesystem(im, 5))

    def test_store_image_in_filesystem_valid_input(self):
        im = Image.open("hopper.jpg")
        self.assertNotEqual(None, store_image_in_filesystem(im, "hellohop.jpg"))

    def test_change_volume_invalid_input(self):
        cl = 5
        self.assertEqual(None, change_volume(cl, 0.0))
        cl = VideoFileClip("munobrars.mp4")
        self.assertEqual(None, change_volume(cl, 1))

    def test_change_volume_valid_input(self):
        cl = VideoFileClip("munobrars.mp4")
        self.assertNotEqual(None, change_volume(cl, 0.0))

    def test_audio_normalize_effect_invalid_input(self):
        cl = 5
        self.assertEqual(None, audio_normalize_effect(cl))

    def test_audio_normalize_effect_valid_input(self):
        cl = VideoFileClip("munobrars.mp4")
        self.assertNotEqual(None, audio_normalize_effect(cl))

    def test_audio_fade_effect_invalid_input(self):
        cl = 5
        self.assertEqual(None, audio_fade_effect(cl, 5, 5))
        cl = VideoFileClip("munobrars.mp4")
        self.assertEqual(None, audio_fade_effect(cl, 5.0, 5))
        self.assertEqual(None, audio_fade_effect(cl, 5, 5.0))

    def test_audio_fade_effect_valid_input(self):
        cl = VideoFileClip("munobrars.mp4")
        self.assertNotEqual(None, audio_fade_effect(cl, 5, 5))


if __name__ == '__main__':
    unittest.main()
