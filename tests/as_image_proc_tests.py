from PIL import Image
import unittest
import imageEdit


class EditImageTestCase(unittest.TestCase):
    def test_hue_editing_image(self):
        im1 = Image.open(r"image.png")
        im2 = imageEdit.hue_editor(im1, 180)
        #im2.show()
        self.assertTrue(im2 is not None, True)

    def test_hue_invalid_value(self):
        im1 = Image.open(r"image.png")
        im2 = imageEdit.hue_editor(im1, 580)
        im3 = imageEdit.hue_editor(im1, -1)
        self.assertTrue(im2 is None, True)
        self.assertTrue(im3 is None, True)

    def test_crop_editing_image(self):
        im1 = Image.open(r"image.png")
        im2 = imageEdit.crop_editor(im1, (20, 30, 700, 700))
        #im2.show()
        self.assertTrue(im2 is not None, True)

    def test_crop_invalid_value(self):
        im1 = Image.open(r"image.png")
        im2 = imageEdit.crop_editor(im1, (20, 30, 1500, 1000))
        im3 = imageEdit.crop_editor(im1, (20, 30, 1000, 1500))
        im4 = imageEdit.crop_editor(im1, (20, 30, 10, 1000))
        im5 = imageEdit.crop_editor(im1, (20, 30, 1000, 10))
        im6 = imageEdit.crop_editor(im1, (-20, 30, 700, 700))
        im7 = imageEdit.crop_editor(im1, (20, -30, 700, 700))

        self.assertTrue(im2 is None, True)
        self.assertTrue(im3 is None, True)
        self.assertTrue(im4 is None, True)
        self.assertTrue(im5 is None, True)
        self.assertTrue(im6 is None, True)
        self.assertTrue(im7 is None, True)

    def test_opacity_editing_image(self):
        im1 = Image.open(r"image.png")
        im2 = imageEdit.opacity_editor(im1, 50)
        #im2.show()
        self.assertTrue(im2 is not None, True)

    def test_opacity_invalid_inputs(self):
        im1 = Image.open(r"image.png")
        im2 = imageEdit.opacity_editor(im1, 400)
        im3 = imageEdit.opacity_editor(im1, -400)

        self.assertTrue(im2 is None, True)
        self.assertTrue(im3 is None, True)

    def test_gradient_color_image(self):
        im1 = Image.open(r"image.png")
        im2 = imageEdit.apply_color_editor(im1, (255, 0, 0, 128))
        #im2.show()
        self.assertTrue(im2 is not None, True)

    def test_gradient_color_image(self):
        im1 = Image.open(r"image.png")
        im2 = imageEdit.apply_color_editor(im1, (256, 0, 0, 128))
        im3 = imageEdit.apply_color_editor(im1, (256, 0, 300, 128))
        im4 = imageEdit.apply_color_editor(im1, (256, -1, 0, 128))
        im5 = imageEdit.apply_color_editor(im1, (256, 0, 0, 277))
        im6 = imageEdit.apply_color_editor(im1, (256, 0, 0, -128))

        self.assertTrue(im2 is None, True)
        self.assertTrue(im3 is None, True)
        self.assertTrue(im4 is None, True)
        self.assertTrue(im5 is None, True)
        self.assertTrue(im6 is None, True)

    def test_filter_editing_image(self):
        im1 = Image.open(r"image.png")
        im2 = imageEdit.apply_gradient_editor(im1, 70, (255, 0, 0),
                                              (0, 0, 255))
        #im2.show()
        self.assertTrue(im2 is not None, True)

    def test_filter_editing_image(self):
        im1 = Image.open(r"image.png")
        im2 = imageEdit.apply_gradient_editor(im1, 70, (255, 0, 0),
                                              (0, -10, 255))
        im3 = imageEdit.apply_gradient_editor(im1, 70, (0, 290, 0),
                                              (0, 0, 255))
        im4 = imageEdit.apply_gradient_editor(im1, 70, (255, 0, 0),
                                              (0, -7, 255))
        im5 = imageEdit.apply_gradient_editor(im1, 70, (255, 0, 0),
                                              (-9, 0, 255))
        im6 = imageEdit.apply_gradient_editor(im1, 70, (14, 190, 300),
                                              (0, 0, 255))
        im7 = imageEdit.apply_gradient_editor(im1, 700, (255, 0, 0),
                                              (0, 0, 255))
        im8 = imageEdit.apply_gradient_editor(im1, -7, (255, 0, 0),
                                              (0, 0, 255))
        self.assertTrue(im2 is None, True)
        self.assertTrue(im3 is None, True)
        self.assertTrue(im4 is None, True)
        self.assertTrue(im5 is None, True)
        self.assertTrue(im6 is None, True)
        self.assertTrue(im7 is None, True)
        self.assertTrue(im8 is None, True)
