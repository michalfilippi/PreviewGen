# PreviewGen

PreviewGen is a tool for generating previews from photo galleries at source location. Previews are created in target location where the source structure is copied but images are replaced with compressed and resized copy. Basic idea is to provide a preview of a full size gallery with a reasonable size and quality.

## Instalation

PreviewGen is deployed to pypi and can be therefore easily installed using pip.

```sh
$ pip install previewgen
```

## Usage

After installation preview-gen command should be available from command line.

```sh
$ preview-gen
usage: preview-gen [-h] config_file
```

### Config file

```yaml
# example config file conf.yaml

scanner:
  source_dir: /Users/mfilippi/pg-test/s
  destination_dir: /Users/mfilippi/pg-test/d

previewer:
  max_width: 1000
  max_height: 1000
  quality: 80

# optional logger config
logger:
  # posible levels can be found at https://docs.python.org/3/library/logging.html#levels
  level: DEBUG
```

In the same directory the tool can be executed using `$ preview-gen conf.yaml`.

---

[![Build Status](https://travis-ci.com/michalfilippi/PreviewGen.svg?branch=master)](https://travis-ci.com/michalfilippi/PreviewGen)
