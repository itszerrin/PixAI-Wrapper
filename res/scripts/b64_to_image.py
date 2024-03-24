from PIL        import Image
from io         import BytesIO
import base64

def convert_b64_to_image(b64_string) -> Image:

    """
    Convert a base64 string to an image.
    
    :param b64_string: The base64 string to convert.
    
    :return: The image as a PIL.Image object.
    """

    # Decode base64 string to binary data
    binary_data: bytes = base64.b64decode(b64_string)

    # Open binary data as an image
    image: Image = Image.open(BytesIO(binary_data))

    return image