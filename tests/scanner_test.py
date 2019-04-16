import previewgen.scanner as scanner


def prepare_structure(tmpdir, source_structure, destination_structure):
    source_dir = tmpdir.join('source/').mkdir()
    destination_dir = tmpdir.join('destination/').mkdir()

    source_paths = [source_dir.join(p) for p in source_structure]
    destination_paths = [destination_dir.join(p) for p in destination_structure]
    for path in source_paths + destination_paths:
        path.write('', ensure=True)

    return source_dir, destination_dir


def test_scanner(tmpdir):
    source_structure = [
        'img_1.jpg',
        'img_2.jpg',
        'img_3.jpg',
        'sub_1/img_1_1.jpg',
        'sub_1/img_1_2.jpg',
        'sub_1/img_1_3.jpg',
        'sub_2/sub_3/img_2_3_1.jpg',
        'sub_2/sub_3/img_2_3_4.jpg',
        'sub_2/sub_3/img_2_3_5.jpg',
        'sub_2/sub_3/img_2_3_6.jpg',
        'sub_3/.hidden/img_1.jpg',
        '.hidden/img_1.jpg'
    ]

    destination_structure = [
        'img_3.jpg',
        'sub_1/img_1_1.jpg'
    ]

    source_dir, destination_dir = prepare_structure(tmpdir, source_structure, destination_structure)

    scanner.logger.setLevel('DEBUG')
    s = scanner.Scanner(source_dir, destination_dir, False)

    source_images = s._scan_source()
    assert len(source_images) == len(source_structure)

    relative_paths = s._relative_paths(source_images)
    assert {str(p) for p in relative_paths} == set(source_structure)

    relative_without_hidden = s._ignore_hidden(relative_paths)
    assert len(relative_without_hidden) == len(source_structure) - 2

    pairs = s._pair_files(relative_without_hidden)

    filtered_paths = s._filter_existing(pairs)
    assert len(filtered_paths) == len(relative_without_hidden) - len(destination_structure)

    assert len(s.run()) == len(source_structure) - len(destination_structure)
