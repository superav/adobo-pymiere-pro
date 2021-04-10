from flask import Flask, request
from PIL.Image import Image
from logic.asset_manager import AssetManager
import logic.jz_image_proc
import logic.as_image_proc
import logic.nst


def create_app():
    flask_app = Flask(__name__)

    @flask_app.route("/logic/image_editor", methods=["GET"])
    def get_apply_effect():

        # Receive input
        ui_input = request.get_json()

        # Call pull helper method
        input_img = pull_pillow_image(ui_input)

        # Call alteration method specified by request
        var = ui_input["effect"]
        if var == "saturation":
            altered_image = logic.jz_image_proc.change_saturation(input_img, ui_input["specifications"].toJson())
        elif var == "hue":
            altered_image = logic.as_image_proc.hue_editor(input_img, ui_input["specifications"].toJson())
        elif var == "color-gradient":
            altered_image = logic.as_image_proc.apply_gradient_editor(input_img, ui_input["specifications"].toJson())
        elif var == "crop":
            altered_image = logic.jz_image_proc.crop_editor(input_img, ui_input["specifications"].toJson())
        elif var == "watermark":
            altered_image = logic.jz_image_proc.add_watermark_image(input_img, ui_input["specifications"].toJson())
        elif var == "blur":
            altered_image = logic.jz_image_proc.gaussian_blur(input_img, ui_input["specifications"].toJson())
        elif var == "opacity":
            altered_image = logic.as_image_proc.opacity_editor(input_img, ui_input["specifications"].toJson())
        elif var == "recoloration":
            altered_image = logic.as_image_proc.apply_color_editor(input_img, ui_input["specifications"].toJson())
        elif var == "rotate-image":
            altered_image = logic.jz_image_proc.rotate_image(input_img, ui_input["specifications"].toJson())
        elif var == "downscale-resolution":
            altered_image = logic.jz_image_proc.scale_image(input_img, ui_input["specifications"].toJson())
        # elif var == "reverb":
        #     altered_image = ImageEditor.reverb(input_img, ui_input["specifications"].toJson())
        # elif var == "eq":
        #     altered_image = ImageEditor.eq(input_img, ui_input["specifications"].toJson())
        # elif var == "volume":
        #     altered_image = ImageEditor.volume(input_img, ui_input["specifications"].toJson())
        elif var == "rotate-video":
            altered_image = logic.jz_image_proc.rotate_video(input_img, ui_input["specifications"].toJson())
        else:
            return None

        # Call push helper method
        url = push_pillow_image(altered_image, ui_input)

        # Return url and image information to UI
        return {"image_name": ui_input["image_name"], "url": url, "file_extension": ui_input["file_extension"]}

    def pull_pillow_image(self, ui_input: dict):
        # Receive input
        image_name = ui_input["image_name"] + "." + ui_input["file_extension"]

        # Receive Pil image from bucket
        input_img = AssetManager.import_image_from_s3(image_name, ui_input["is_working_copy"])

        return input_img

    def push_pillow_image(self, altered_image: Image, ui_input: dict):
        # Receive input
        image_name = ui_input["image_name"] + "." + ui_input["file_extension"]

        # Send new image back to S3 bucket and get url
        url = AssetManager.upload_image_to_s3(altered_image, image_name, ui_input["is_working_copy"])

        return url
