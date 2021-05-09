import json
import sys
import math
import operator
from functools import reduce
from PIL import Image

from logic.asset_manager import AssetManager

ASSET_MANAGER = AssetManager('test_user_1')


# Reference: https://stackoverflow.com/questions/1927660/compare-two-images-the-python-linux-way
def compare_hue_feature_test_images():
    ret = json.loads(sys.argv[1])

    file_name = ret["image_name"] + "." + ret["file_extension"]

    image_1 = ASSET_MANAGER.import_image_from_s3(file_name, False)
    image_2 = ASSET_MANAGER.import_image_from_s3('hue_expected_180.png', False)

    h1 = image_1.histogram()
    h2 = image_2.histogram()

    rms = math.sqrt(reduce(operator.add,
                           map(lambda a, b: (a - b) ** 2, h1, h2)) / len(h1))

    img = Image.open('./tests/test_assets/images/image.png')
    ASSET_MANAGER.upload_image_to_s3(img, "image.png", False)

    if rms != 0.0:
        sys.exit([1])

    return rms


def compare_red_eye_feature_test_images():
    # Reference: https://stackoverflow.com/questions/
    #               1927660/compare-two-images-the-python-linux-way
    ret = json.loads(sys.argv[2])

    file_name = ret["image_name"] + "." + ret["file_extension"]

    image_1 = ASSET_MANAGER.import_image_from_s3(file_name, False)
    image_2 = ASSET_MANAGER.import_image_from_s3(
        'red_eye_expected_35_110_150_150.png', False)

    h1 = image_1.histogram()
    h2 = image_2.histogram()

    rms = math.sqrt(reduce(operator.add,
                           map(lambda a, b: (a - b) ** 2, h1, h2)) / len(h1))

    img = Image.open('./tests/test_assets/images/redeye.png')
    ASSET_MANAGER.upload_image_to_s3(img, "redeye.png", False)

    if rms != 0.0:
        sys.exit([1])

    return rms


def compare_vignette_feature_test_images():
    # Reference: https://stackoverflow.com/questions/
    #               1927660/compare-two-images-the-python-linux-way
    ret = json.loads(sys.argv[3])

    file_name = ret["image_name"] + "." + ret["file_extension"]

    image_1 = ASSET_MANAGER.import_image_from_s3(file_name, False)
    image_2 = ASSET_MANAGER.import_image_from_s3(
        'red_eye_expected_35_110_150_150.png', False)

    h1 = image_1.histogram()
    h2 = image_2.histogram()

    rms = math.sqrt(reduce(operator.add,
                           map(lambda a, b: (a - b) ** 2, h1, h2)) / len(h1))

    img = Image.open('./tests/test_assets/images/redeye.png')
    ASSET_MANAGER.upload_image_to_s3(img, "redeye.png", False)

    if rms != 0.0:
        sys.exit([1])

    return rms


def compare_nst_feature_test_images():
    # Reference: https://stackoverflow.com/questions/
    #               1927660/compare-two-images-the-python-linux-way
    ret = json.loads(sys.argv[4])
    file_name = ret["image_name"] + "." + ret["file_extension"]

    image_1 = ASSET_MANAGER.import_image_from_s3(file_name, False)

    if not (isinstance(image_1, Image.Image)):
        sys.exit([1])

    return 0


if __name__ == "__main__":
    compare_hue_feature_test_images()
    compare_red_eye_feature_test_images()
    compare_vignette_feature_test_images()
    compare_nst_feature_test_images()
