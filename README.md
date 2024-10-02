# PixAI Realtime Image Generation Wrapper

**This is a collection of Python scripts. Together, they can take a prompt input and generates images from PixAI directly. This procedure does NOT cost you credits and you can use an alt too.**

Note: The **Realtime generation** feature is a compromise to not pay tokens but your images are of lesser quality.

---

## 1. Installation:

### 1.1 Copying the Git repository 
```bash
git clone https://github.com/Recentaly/PixAI-Wrapper.git
```

### 1.2 Entering the directory
```bash
cd PixAI-Wrapper
```

## 1.3 Installing Dependencies
```bash
pip install -r requirements.txt
```

## 2. Preparation

### 2.1 Create a Python file at root.

### 2.2 Importing required modules
```py
from res.scripts.generate_images    import get_image_batch
from res.scripts.get_jwt            import get_jwt
```

(Optional but recommended):
```py
from res.SaveConfig                 import SaveConfig
```

---

## 3. Saveconfig (optional)

### 3.1 Initialize the SaveConfig class in your code. Example:

When a `SaveConfig` object is passed to the API, the API automatically saves the images. There's an option to Save + Return too. To only return the images from the API, leave `SaveConfig` as `None` when calling `get_image_batch`. <br>

**Note: Automatically uses the .png file extension**

```py
# create a SaveConfig object
save_config = SaveConfig(
    save_dir="output/images",
    save_name="image",
    force_mkdir=True,
    additional_return_mode=False,
    separator="-"
)
```

- The `save_dir` (str) is a path to whatever directory you want the images to be saved at.
- `save_name` (str) is whatever you want the file(s) to be called.
- `force_mkdir` (bool) if the `save_dir` doesn't exist, forcibly create that directory if `force_mkdir` is True.
- `additional_return_mode` (bool) If true, also returns a `List` of images while also saving them at the specified directory.
- `separator` (str) The separator between the `save_name` and the Image's index.

For example, if I have this code and generated, let's say, 4 images..

```py
# create a SaveConfig object
save_config = SaveConfig(
    save_dir="output/images",
    save_name="generated-image",
    force_mkdir=True,
    additional_return_mode=False,
    separator="_"
)
```

The images would be saved like this:
```
generated-image_0.png
generated-image_1.png
generated-image_2.png
generated-image_3.png
```

---

## Getting the JWT

Here's example code to fetch your JWT.

```py
 jwt: str = get_jwt(
  email="<your pixai email here>",
  password="<your pixai password here>"
)
```

This will return a jwt of type string. Now you may actually use the function to gather the images

## 4. Fetching a batch of images

### 4.1 Compiling the parameters

To gather images, simply call the ``get_image_batch`` function after you've imported it.

Parameters:

- prompt: str = The prompt to generate the images from
- negative_prompt: str = The negative prompt to generate the image from
- size: tuple[int, int]: Width x Height of the image. it is generally recommended to keep this at 512x512 For speed and a higher chance of getting a result.
- __jwt: str = The JWT.
- _n: int = Number of images to generate | defaults to one
- _seed: int = The seed to generate the image with. Defaults to a None and lets PixAI decide.
- _saveConfig: SaveConfig = Optional SaveConfig if you want to save the images quickly and easily

Returns:

- if a `SaveConfig` is provided, and `_saveConfig.additional_return_mode` is true, it saves the images and returns a `List[Image]` object. Image is inherited from PIL.
- If `_saveConfig.additional_return_mode` is False, the API returns `None`
- If no `SaveConfig` is provided, it return `List[Image]` object. Image is inherited from PIL.

### 4.2 Calling the function

Below is an example of how to generate images of a dog. The negative prompt is one I found and is useful to generate high quality results.

```py
"""
The images automatically saved under 'output/images' as 'image-0.png'. The API didn't return anything because additional_return_mode is False.
"""

save_config = SaveConfig(
    save_dir="output/images",
    save_name="image",
    force_mkdir=True,
    additional_return_mode=False,
    separator="-"
)

image_outputs = get_image_batch(
    prompt="1dog. White. Fluffly. Looking at the camera.",
    negative_prompt="nsfw, lowres, (bad), text, error, fewer, extra, missing, worst quality, jpeg artifacts, low quality, watermark, unfinished, displeasing, oldest, early, chromatic aberration, signature, extra digits, artistic error, username, scan, abstract",
    size=(512, 512),
    _n=1,
    __jwt=__jwt,
    _saveConfig=save_config
)
```

### (4.3) Handling returned images

The Images are basic `Image` objects of the [Image](https://pillow.readthedocs.io/en/stable/reference/Image.html) module.

Output:

![Output_image_example_dog](https://i.imgur.com/msk40mQ.png)

---

## Example code:

```py
from res.scripts.get_jwt            import get_jwt
from res.scripts.generate_images    import get_image_batch
from res.SaveConfig                 import SaveConfig

# create a SaveConfig object
save_config = SaveConfig(
    save_dir="output/images",
    save_name="image",
    force_mkdir=True,
    additional_return_mode=True,
    separator="-"
)

if __name__ == '__main__':

    __jwt: str = get_jwt(
        email="xxxxxxxx", # input your actual email here
        password="xxxxxx" # input your actual password here
    )

    image_outputs = get_image_batch(
        prompt="1cat. Yellow. Aggressive. Angry. Hissing at the camera. Best quality. Masterpiece. Best anatomy. Open mouth.",
        negative_prompt="nsfw, lowres, (bad), text, error, fewer, extra, missing, worst quality, jpeg artifacts, low quality, watermark, unfinished, displeasing, oldest, early, chromatic aberration, signature, extra digits, artistic error, username, scan, abstract",
        size=(512, 512),
        _n=1,
        __jwt=__jwt,
        _saveConfig=save_config
    )

    # we can run the for loop because the API class is set to additionally return the images again 
    for image in image_outputs:
        image.show()
```

Output:

![Aggressive_cat_example](https://i.imgur.com/VOneDA2.png)

### Auto-claiming your daily credits

To auto-claim your daily credits, first import the code to claim credits

```py
from res.scripts.claim_credits      import claim_daily_credits
```

Then, call the `claim_daily_credits` function

```py
claim_daily_credits(
    jwt # you need your jwt from above
)
```

You will only get an error if something went wrong. It will tell you in the console if it was able to claim your daily credits or if you already claimed them.
