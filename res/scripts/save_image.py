from PIL import Image

def save_image(image: Image, path: str) -> None:

    """
    Save an image to a file.
    
    :param image: The image to save.
    :param path: The path to save the image to.
    """

    image.save(path, "PNG")