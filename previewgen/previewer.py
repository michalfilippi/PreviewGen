import logging
import os
from pathlib import Path

from PIL import Image

logger = logging.getLogger(__name__)

previewer_config_schema = {
    'max_width': int,
    'max_height': int,
    'quality': int
}


class Previewer:
    def __init__(self, max_width: int, max_height: int, quality: int):
        self.max_width = max_width
        self.max_height = max_height

        q_upper = 95
        q_lower = 0
        self.quality = max(min(quality, q_upper), q_lower)
        if self.quality != quality:
            logger.warning(f"Compression quality out of bounds ({q_lower}-{q_upper}). "
                           f"Setting quality to {self.quality}.")

    def resize(self, photo: Image) -> Image:
        resize_width = self.max_width / photo.width if self.max_width else 1
        resize_height = self.max_height / photo.height if self.max_height else 1
        resize_ratio = min(resize_width, resize_height)
        if resize_ratio >= 1:
            logger.debug(f"Skipping photo resizing due to resize_ratio >= 1 ({resize_ratio}).")
        else:
            new_size = (int(photo.width * resize_ratio), int(photo.height * resize_ratio))
            logger.debug(f"Compressing photo size from {photo.size} to {new_size} (ratio {resize_ratio}).")
            photo = photo.resize(new_size)
        return photo

    def save(self, photo: Image, destination: Path):
        parent = Path(destination.parent)
        if not parent.exists():
            logger.info(f"Parent directory \"{parent}\" does not exist. Creating all missing directories.")
            os.makedirs(parent)
        logger.info(f"Saving photo to \"{destination}\" with quality={self.quality}.")
        photo.save(destination, quality=self.quality)

    def save_resized(self, photo: Image, destination: Path):
        self.save(self.resize(photo), destination)
