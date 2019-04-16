import logging

from PIL import Image

from .scanner import Scanner
from .previewer import Previewer

logger = logging.getLogger(__name__)


def run(scanner_conf, previewer_conf):
    scanner = Scanner(**scanner_conf)
    previewer = Previewer(**previewer_conf)

    for source, destination in scanner.run():
        photo = Image.open(source)
        previewer.save_resized(photo, destination)
