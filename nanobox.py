import os
import subprocess
import logging
from urllib import request

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class NanoBox:
    def __init__(self):
        self.patch_directory = "C:\\NanoBox\\Patches"
        if not os.path.exists(self.patch_directory):
            os.makedirs(self.patch_directory)
        logging.info("Initialized NanoBox with patch directory: %s", self.patch_directory)

    def download_patch(self, url):
        try:
            file_name = os.path.join(self.patch_directory, url.split('/')[-1])
            logging.info("Downloading patch from %s", url)
            request.urlretrieve(url, file_name)
            logging.info("Downloaded patch to %s", file_name)
            return file_name
        except Exception as e:
            logging.error("Failed to download patch: %s", e)
            return None

    def apply_patch(self, file_path):
        try:
            logging.info("Applying patch from %s", file_path)
            subprocess.run(["wusa.exe", file_path, "/quiet", "/norestart"], check=True)
            logging.info("Patch applied successfully")
        except subprocess.CalledProcessError as e:
            logging.error("Failed to apply patch: %s", e)

    def list_patches(self):
        try:
            patches = os.listdir(self.patch_directory)
            logging.info("Available patches: %s", patches)
            return patches
        except Exception as e:
            logging.error("Failed to list patches: %s", e)
            return []

    def clean_patches(self):
        try:
            for file in os.listdir(self.patch_directory):
                file_path = os.path.join(self.patch_directory, file)
                os.remove(file_path)
                logging.info("Removed patch file: %s", file_path)
            logging.info("All patches removed from %s", self.patch_directory)
        except Exception as e:
            logging.error("Failed to clean patches: %s", e)

# Example Usage
if __name__ == "__main__":
    nanobox = NanoBox()
    patch_url = "http://example.com/patch.msu"
    patch_file = nanobox.download_patch(patch_url)
    if patch_file:
        nanobox.apply_patch(patch_file)
    nanobox.list_patches()
    nanobox.clean_patches()