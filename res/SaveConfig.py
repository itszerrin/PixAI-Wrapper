from dataclasses import dataclass

@dataclass
class SaveConfig():

    def __init__(self, save_dir: str, save_name: str, force_mkdir: bool = False, additional_return_mode: bool = False, separator: str = "-") -> None:

        """
        Configuration class for saving images. Automatically uses .png as the file extension.
        
        :param save_dir: The directory to save the images to.
        :param save_name: The name to save the images as.
        :param force_mkdir: Whether or not to force the creation of the save directory if it doesn't exist.
        :param additional_return_mode: Whether or not to return the image as well as save it.
        :param separator: The separator to use between the save_name and the index."""

        self.save_dir: str = save_dir
        self.save_name: str = save_name
        self.force_mkdir: bool = force_mkdir
        self.additional_return_mode: bool = additional_return_mode
        self.separator: str = separator
    
    def _validate(self) -> None:

        """
        Validate the SaveConfig object.
        """

        if not isinstance(self.save_dir, str):
            raise ValueError("The save_dir parameter must be a string.")
        if not isinstance(self.save_name, str):
            raise ValueError("The save_name parameter must be a string.")
        if not isinstance(self.force_mkdir, bool):
            raise ValueError("The force_mkdir parameter must be a boolean.")
        if not isinstance(self.additional_return_mode, bool):
            raise ValueError("The additional_return_mode parameter must be a boolean.")
        if not isinstance(self.separator, str):
            raise ValueError("The separator parameter must be a string.")