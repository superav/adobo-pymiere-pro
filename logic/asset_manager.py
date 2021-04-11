import boto3
from PIL import Image
from io import BytesIO

BUCKET_NAME = 'adobo-pymiere'


class AssetManager:
    """
    This is a class that will manage uploading and downloading assets from the S3 bucket.

    The file structure of the S3 bucket is as follows:
        .
        └── _username/
        │   ├── _video_projects/
        │   │   ├── _assets/
        │   │   │   ├── example_audio.mp3
        │   │   │   └── example_video.mp4
        │   │   └── working_copy.mp4
        │   └── _image_projects/
        │       ├── _assets/
        │       │   └── example_image.png
        │       └── working_copy.png
        └── _other_username/
            └── [same internal file structure as _username]

    All images loaded into the S3 bucket will be in PNG format (so that we can also use the
    alpha channel when doing image processing)
    """

    def __init__(self, username: str):
        """
        Args:
            username:   username of user (no spaces allowed in username)
        """

        if ' ' in username:
            raise Exception("AssetManager: username must not have spaces in it!")

        self.s3_client = boto3.client('s3',
                                      aws_access_key_id='AKIAYA22OMIBDDNHCQWM',
                                      aws_secret_access_key='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'
                                      )
        self.username = username

    def list_bucket(self, list_everything: bool = True) -> list:
        """
        Lists all the contents of the S3 bucket

        Returns:
            bucket_list:    List of all objects in the bucket
        """

        bucket_list = []

        for key in self.s3_client.list_objects(Bucket=BUCKET_NAME)['Contents']:
            if list_everything or self.username in key['Key']:
                bucket_list.append(key['Key'])

        return bucket_list

    def import_image_from_s3(self,
                             image_name: str = "working_copy.png", is_working_copy: bool = True) -> Image:
        """
        Args:
            image_name: Name of image in S3 bucket to be read into a buffer. Must have .png extension
            is_working_copy: If the image being imported is the working copy of the project

        Returns:
            output_image:   A PIL.Image if image exists in bucket. Otherwise, None
        """

        if image_name[-4:] != '.png':
            print("ERROR (import_image_from_s3): %s must have '.png' extension" % image_name)
            return None

        try:
            if is_working_copy:
                location = "%s/image_projects/%s" % (self.username, image_name)
            else:
                location = "%s/image_projects/assets/%s" % (self.username, image_name)

            file_byte_string = self.s3_client.get_object(Bucket=BUCKET_NAME, Key=location)['Body'].read()

            return Image.open(BytesIO(file_byte_string)).convert('RGBA')

        except self.s3_client.exceptions.NoSuchKey as e:
            print("ERROR (import_image_from_s3): " + str(e))
            return None

    def upload_image_to_s3(self, input_image: Image,
                           image_name: str = "working_copy.png", is_working_copy: bool = True) -> str:
        """
        Args:
            input_image:  A PIL.Image
            image_name:   Name of the image (with the .png extension). Default is "working_copy.png"
            is_working_copy: If the image to be uploaded is the working copy of the project. Default is True

        Returns:
            url:    The URL to the file in the S3 bucket on success. Otherwise, will return
                    an appropriate error message
        """

        if image_name[-4:] != '.png':
            return "Missing \".png\" extension!"

        buffer = BytesIO()
        image = input_image.convert('RGBA')

        image.save(buffer, 'PNG')

        if is_working_copy:
            location = "%s/image_projects/%s" % (self.username, image_name)
        else:
            location = "%s/image_projects/assets/%s" % (self.username, image_name)

        self.s3_client.put_object(Body=buffer.getvalue(), Bucket=BUCKET_NAME, Key=location)
        url = "https://%s.s3.amazonaws.com/%s" % (BUCKET_NAME, location)

        return url
