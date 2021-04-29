from flask import Flask, request
from PIL.Image import Image
from flask_cors import CORS

from logic.filter_methods import *
from logic.overlay_methods import *
from logic.canvas_editing_methods import *
from logic.color_methods import *
from logic.misc_methods import *
from logic.asset_manager import AssetManager

ass_man = AssetManager("test_user_1")


def create_app():
    flask_app = Flask(__name__)

    CORS(flask_app)
    
    @flask_app.route("/logic/image_editor", methods=["POST"])
    def get_apply_effect():
        # Receive input
        ui_input = request.get_json()
        # Call pull helper method
        input_img = pull_pillow_image(ui_input)
        # Call alteration method specified by request
        var = ui_input["effect"]
        if var == "saturation":
            altered_image = change_saturation(
                input_img, ui_input["specifications"])
        elif var == "hue":
            altered_image = hue_editor(
                input_img, ui_input["specifications"])
        elif var == "color-gradient":
            altered_image = apply_gradient_editor(
                input_img, ui_input["specifications"])
        elif var == "crop":
            altered_image = crop_editor(
                input_img, ui_input["specifications"])
        elif var == "watermark":
            altered_image = add_watermark_image(
                input_img, ui_input["specifications"])
        elif var == "blur":
            altered_image = gaussian_blur(
                input_img, ui_input["specifications"])
        elif var == "opacity":
            altered_image = opacity_editor(
                input_img, ui_input["specifications"])
        elif var == "recoloration":
            altered_image = apply_color_editor(
                input_img, ui_input["specifications"])
        elif var == "rotate":
            altered_image = rotate_image(
                input_img, ui_input["specifications"])
        elif var == "downscale-resolution":
            altered_image = scale_image(
                input_img, ui_input["specifications"])
        elif var == "add-text":
            altered_image = add_text_to_image(
                input_img, ui_input["specifications"])
        elif var == "draw-line":
            altered_image = draw_line(
                input_img, ui_input["specifications"])
        elif var == "mirror":
            altered_image = apply_mirror(
                input_img, ui_input["specifications"])
        elif var == "red-eye-remover":
            altered_image = apply_red_eye_filter(
                input_img, ui_input["specifications"])
        elif var == "solarize":
            print(ui_input)
            altered_image = apply_solarize(
                input_img, ui_input["specifications"])
        elif var == "mosaic":
            altered_image = apply_mosaic_filter(input_img)
        elif var == "frame":
            altered_image = apply_frame(
                input_img, ui_input["specifications"])
        else:
            return None

        # Call push helper method
        url = push_pillow_image(altered_image, ui_input)

        # Return url and image information to UI
        return {"image_name": ui_input["image_name"], "url": url,
                "file_extension": ui_input["file_extension"]}

    @flask_app.route("/logic/image_list", methods=["GET"])
    def get_list_bucket():
        # Receive input
        ui_input = request.get_json()

        return {"list": ass_man.list_bucket(ui_input["list_everything"])}

    # @flask_app.route("/logic/image_editor", methods=["GET"])
    # def get_import_image():
    #     # Receive input
    #     ui_input = request.get_json()

    #     # Call pull helper method
    #     input_img = pull_pillow_image(ui_input)

    #     return input_img

    # @flask_app.route("/logic/image_editor", methods=["POST"])
    # def post_upload_image():
    #     # Receive input
    #     ui_input = request.get_json()

    #     # Call pull helper method, can we send pilImage?
    #     # we may not need this method
    #     input_img = push_pillow_image(ui_input["altered_image"], ui_input)

    #     return input_img

    def pull_pillow_image(ui_input: dict):
        # Receive input
        image_name = ui_input["image_name"] + "." + ui_input["file_extension"]

        # Receive Pil image from bucket
        input_img = ass_man.import_image_from_s3(image_name,
                                                 ui_input["is_working_copy"])

        return input_img

    def push_pillow_image(altered_image: Image, ui_input: dict):
        # Receive input
        image_name = ui_input["image_name"] + "." + ui_input["file_extension"]

        # Send new image back to S3 bucket and get url
        url = ass_man.upload_image_to_s3(
            altered_image, image_name, ui_input["is_working_copy"])

        return url

    return flask_app
