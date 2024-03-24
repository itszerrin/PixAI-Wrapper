# PixAI Realtime Image Generation Wrapper

**This is a collection of Python scripts. Together, they can take a prompt input and gather a pre-generated image from PixAI directly.**

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

## Getting the JWT

Here's example code to fetch your JWT.

```py
 jwt: str = get_jwt(
  email="<your email here>",
  password="<your password here>"
)
```

This will 

