from pathlib import Path

from PIL import Image

import previewgen.previewer as previewer


def test_previewer_resize():
    p = previewer.Previewer(50, 50, 10)

    size = (100, 200)

    photo = Image.new(mode='RGB', size=size, color=0)
    resized_photo = p.resize(photo)

    assert resized_photo.width == 25
    assert resized_photo.height == 50


def test_previewer(tmpdir):
    p = previewer.Previewer(50, 50, 10)

    destination = Path(tmpdir.join('destination_img.jpg'))
    size = (100, 200)
    photo = Image.new(mode='RGB', size=size, color=0)

    p.save_resized(photo, destination)

    loaded_photo = Image.open(destination)

    assert loaded_photo.width == 25
    assert loaded_photo.height == 50
