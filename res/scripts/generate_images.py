from .b64_to_image      import convert_b64_to_image
from .randomness        import number_between
from .save_image        import save_image
from ..SaveConfig       import SaveConfig
from .user_id           import get_user_id

from typing             import Tuple, List
from fake_useragent     import UserAgent
import requests
import logging
import os

# logging config
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_image_batch(prompt: str, negative_prompt: str, size: Tuple[int, int], __jwt: str, _n: int = 1, _seed: int | None = None, _saveConfig: SaveConfig | None = None) -> List | None:

    """
    Get an image from the PixAI API using the provided prompt and negative prompt.
    :param prompt: The prompt to generate the image from.
    :param negative_prompt: The negative prompt to generate the image from.
    :param size: The size of the image to generate. (width, height). 512x512 is recommended for availability.
    :param __jwt: The JWT token to authenticate with the PixAI API.
    :param _n: The number of images to generate. (optional)
    :param _seed: The seed to use for the image generation. (optional)
    :param _saveConfig: The SaveConfig object to save the images with. If None, it returns and doesn't save (optional)

    :return: A list of images as PIL.Image objects if _saveConfig is None, otherwise return if _saveConfig.additional_return_mode is True. Otherwise, None.
    """

    __headers = {
        "Host": "inference.pixai.art",
        "User-Agent": f"{UserAgent().random}",
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Authorization": f"Bearer {__jwt}",
        "Content-Type": "application/json",
        "Content-Length": f"{number_between(1, 100)}",
        "Origin": "https://pixai.art",
        "Connection": "keep-alive",
        "Referer": "https://pixai.art/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "TE": "trailers"
    }

    __payload = {
        "height": size[1],
        "width": size[0],
        "negative_prompt": f"{negative_prompt}",
        "prompt": f"{prompt}",
        "num_outputs": _n,
        "user_id": f"{get_user_id(__jwt)}",
    }

    # add a seed if provided and not None
    if _seed:   __payload["seed"] = _seed;  logging.info(f"Found seed {_seed}")

    logging.info(f"Generating {_n} image(s)..")
    response = requests.post("https://inference.pixai.art/lcm/v1/text2image", json=__payload, headers=__headers)
    response.raise_for_status()

    logging.info(f"Successfully generated {_n} image(s).")

    # try validating the saveConfig object

    # if a SaveConfig object is provided, save the images
    if _saveConfig:

        logging.info("SaveConfig object provided. Validating..")

        # validate the saveConfig object
        _saveConfig._validate()

        logging.info("SaveConfig object validated.")

        # create the save directory if it doesn't exist
        if not os.path.exists(_saveConfig.save_dir):

            logging.info(f"The directory {_saveConfig.save_dir} does not exist.")

            # if force_mkdir is True, create the directory
            if _saveConfig.force_mkdir:

                logging.info(f"Creating directory {_saveConfig.save_dir}..")
                os.makedirs(_saveConfig.save_dir, exist_ok=True)
            
            # if force_mkdir is False, raise an error
            else:
                raise FileNotFoundError(f"The directory {_saveConfig.save_dir} does not exist.")
            
        # save the images
        for image in response.json()["data"]:

            logging.info(f"Saving image {_saveConfig.save_name}{_saveConfig.separator}{response.json()['data'].index(image)}.png..")
            save_image(convert_b64_to_image(image["b64_image"]), f"{_saveConfig.save_dir}/{_saveConfig.save_name}{_saveConfig.separator}{response.json()['data'].index(image)}.png")

        # if additional_return_mode is True, return the images
        if _saveConfig.additional_return_mode:
            _outputs: List = []
    
            for image in response.json()["data"]:
                _outputs.append(convert_b64_to_image(image["b64_image"]))

            return _outputs
        
        # if additional_return_mode is False, return None
        return None
    
    # if no SaveConfig object is provided, return the images
    logging.info("No SaveConfig object provided. Returning images..")
    _outputs: List = []

    for image in response.json()["data"]:
        _outputs.append(convert_b64_to_image(image["b64_image"]))
    return _outputs
            
