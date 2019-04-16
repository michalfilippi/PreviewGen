import os
from pathlib import Path

from PIL import Image

from previewgen.previewgenerator import run


def prepare_structure(tmpdir, source_structure, destination_structure):
    source_dir = tmpdir.join('source/').mkdir()
    destination_dir = tmpdir.join('destination/').mkdir()

    source_photos = [(Path(source_dir.join(p)), w, h) for p, w, h in source_structure]
    destination_photos = [(Path(destination_dir.join(p)), w, h) for p, w, h in destination_structure]
    for path, width, height in source_photos + destination_photos:
        if not path.parent.exists():
            os.makedirs(path.parent)
        photo = Image.new(mode='RGB', size=(width, height), color=0)
        photo.save(path)

    return source_dir, destination_dir


def test_previewgenerator(tmpdir):
    source_structure = [
        ('img_1.jpg', 100, 100),
        ('img_2.jpg', 100, 100),
        ('sub_1/img_1_1.jpg', 100, 100)
    ]

    destination_structure = [
        ('img_1.jpg', 50, 50)
    ]

    source_dir, destination_dir = prepare_structure(tmpdir, source_structure, destination_structure)

    preview_config = {
        'max_width': 50,
        'max_height': 80,
        'quality': 20
    }

    scanner_config = {
        'source_dir': str(source_dir),
        'destination_dir': str(destination_dir)
    }

    run(scanner_config, preview_config)

    photo = Image.open(str(destination_dir.join('sub_1/img_1_1.jpg')))

    assert photo.width == 50
    assert photo.height == 50
