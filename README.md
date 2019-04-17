# PreviewGen

PreviewGen is a tool for generating previews from photo galleries at source location. Previews are created in target location where the source structure is copied but images are replaced with compressed and resized copy. Basic idea is to provide a preview of a full size gallery with a reasonable size and quality.

## Instalation

PreviewGen is deployed to pypi and can be therefore easily installed using pip.

```sh
$ pip3 install previewgen
```

### Requirements

PreviewGen is written for Python >3.6. Necessary dependencies are listed in `requirements.txt` and can be installed using pip as follows.

```sh
$ pip3 install -r requirements.txt
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
  source_dir: /Users/mfilippi/pg-gallery/s
  destination_dir: /Users/mfilippi/pg-gallery/d

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

## Example

```sh
$ python --version
Python 3.7.1
```
```sh
$ pwd
/home/user/gallery
```
```sh
$ ls -lh
total 12K
-rw-rw-r-- 1 user user  187 Apr 17 11:27 conf.yaml
drwxrwxr-x 2 user user 4.0K Apr 17 11:42 preview
drwxrwxr-x 4 user user 4.0K Apr 17 11:34 original
```
```sh
$ du -hs original
112M    original
```
```sh
$ cat conf.yaml
scanner:
  source_dir: /home/user/gallery/original/
  destination_dir: /home/user/gallery/preview/

previewer:
  max_width: 800
  max_height: 800
  quality: 80

logger:
  level: INFO
```
```sh
$ ls -lhR original
original:
total 76M
-rwxr-xr-x 1 user user 7.7M Apr 17 11:24 PA280002.JPG
-rwxr-xr-x 1 user user 7.1M Apr 17 11:24 PA280005.JPG
-rwxr-xr-x 1 user user 7.9M Apr 17 11:24 PA280007.JPG
-rwxr-xr-x 1 user user 7.1M Apr 17 11:24 PA280008.JPG
-rwxr-xr-x 1 user user 7.8M Apr 17 11:24 PA280009.JPG
-rwxr-xr-x 1 user user 7.4M Apr 17 11:25 PA280045.JPG
-rwxr-xr-x 1 user user 7.5M Apr 17 11:25 PA280061.JPG
-rwxr-xr-x 1 user user 7.5M Apr 17 11:25 PA280069.JPG
-rwxr-xr-x 1 user user 8.2M Apr 17 11:25 PA280080.JPG
-rwxr-xr-x 1 user user 8.1M Apr 17 11:25 PA280091.JPG
drwxrwxr-x 3 user user 4.0K Apr 17 11:33 sub_1
drwxrwxr-x 2 user user 4.0K Apr 17 11:34 sub_3

original/sub_1:
total 15M
-rwxr-xr-x 1 user user 7.2M Apr 17 11:24 PA280012.JPG
-rwxr-xr-x 1 user user 7.6M Apr 17 11:24 PA280014.JPG
drwxrwxr-x 2 user user 4.0K Apr 17 11:34 sub_2

original/sub_1/sub_2:
total 7.5M
-rwxr-xr-x 1 user user 7.5M Apr 17 11:24 PA280024.JPG

original/sub_3:
total 15M
-rwxr-xr-x 1 user user 7.2M Apr 17 11:24 PA280037.JPG
-rwxr-xr-x 1 user user 7.1M Apr 17 11:24 PA280038.JPG
```
```sh
$ preview-gen conf.yaml
INFO:previewgen.__main__:Config file "conf.yaml" read successfully.
INFO:previewgen.__main__:{'scanner': {'source_dir': '/home/user/gallery/original/', 'destination_dir': '/home/user/gallery/preview/'}, 'previewer': {'max_width': 800, 'max_height': 800, 'quality': 80}, 'logger': {'level': 'INFO'}}
INFO:previewgen.scanner:Found 15 photos in "/home/user/gallery/original".
INFO:root:Ignoring 0 hidden photos or photos under hidden subtree.
INFO:previewgen.previewer:Saving photo to "/home/user/gallery/preview/PA280005.JPG" with quality=80.
INFO:previewgen.previewer:Parent directory "/home/user/gallery/preview/sub_1" does not exist. Creating all missing directories.
INFO:previewgen.previewer:Saving photo to "/home/user/gallery/preview/sub_1/PA280014.JPG" with quality=80.
INFO:previewgen.previewer:Saving photo to "/home/user/gallery/preview/PA280002.JPG" with quality=80.
INFO:previewgen.previewer:Parent directory "/home/user/gallery/preview/sub_1/sub_2" does not exist. Creating all missing directories.
INFO:previewgen.previewer:Saving photo to "/home/user/gallery/preview/sub_1/sub_2/PA280024.JPG" with quality=80.
INFO:previewgen.previewer:Saving photo to "/home/user/gallery/preview/sub_1/PA280012.JPG" with quality=80.
INFO:previewgen.previewer:Saving photo to "/home/user/gallery/preview/PA280061.JPG" with quality=80.
INFO:previewgen.previewer:Saving photo to "/home/user/gallery/preview/PA280009.JPG" with quality=80.
INFO:previewgen.previewer:Saving photo to "/home/user/gallery/preview/PA280045.JPG" with quality=80.
INFO:previewgen.previewer:Saving photo to "/home/user/gallery/preview/PA280008.JPG" with quality=80.
INFO:previewgen.previewer:Parent directory "/home/user/gallery/preview/sub_3" does not exist. Creating all missing directories.
INFO:previewgen.previewer:Saving photo to "/home/user/gallery/preview/sub_3/PA280037.JPG" with quality=80.
INFO:previewgen.previewer:Saving photo to "/home/user/gallery/preview/PA280091.JPG" with quality=80.
INFO:previewgen.previewer:Saving photo to "/home/user/gallery/preview/PA280007.JPG" with quality=80.
INFO:previewgen.previewer:Saving photo to "/home/user/gallery/preview/PA280069.JPG" with quality=80.
INFO:previewgen.previewer:Saving photo to "/home/user/gallery/preview/sub_3/PA280038.JPG" with quality=80.
INFO:previewgen.previewer:Saving photo to "/home/user/gallery/preview/PA280080.JPG" with quality=80.
```
```sh
$ ls -lhR preview
preview:
total 784K
-rw-rw-r-- 1 user user  87K Apr 17 11:43 PA280002.JPG
-rw-rw-r-- 1 user user  86K Apr 17 11:43 PA280005.JPG
-rw-rw-r-- 1 user user  79K Apr 17 11:43 PA280007.JPG
-rw-rw-r-- 1 user user  78K Apr 17 11:43 PA280008.JPG
-rw-rw-r-- 1 user user  86K Apr 17 11:43 PA280009.JPG
-rw-rw-r-- 1 user user  76K Apr 17 11:43 PA280045.JPG
-rw-rw-r-- 1 user user  59K Apr 17 11:43 PA280061.JPG
-rw-rw-r-- 1 user user  67K Apr 17 11:43 PA280069.JPG
-rw-rw-r-- 1 user user  64K Apr 17 11:43 PA280080.JPG
-rw-rw-r-- 1 user user  83K Apr 17 11:43 PA280091.JPG
drwxrwxr-x 3 user user 4.0K Apr 17 11:43 sub_1
drwxrwxr-x 2 user user 4.0K Apr 17 11:43 sub_3

preview/sub_1:
total 196K
-rw-rw-r-- 1 user user  87K Apr 17 11:43 PA280012.JPG
-rw-rw-r-- 1 user user 102K Apr 17 11:43 PA280014.JPG
drwxrwxr-x 2 user user 4.0K Apr 17 11:43 sub_2

preview/sub_1/sub_2:
total 60K
-rw-rw-r-- 1 user user 60K Apr 17 11:43 PA280024.JPG

preview/sub_3:
total 128K
-rw-rw-r-- 1 user user 67K Apr 17 11:43 PA280037.JPG
-rw-rw-r-- 1 user user 59K Apr 17 11:43 PA280038.JPG
```
```sh
$ du -h preview
1.2M    preview
```

---

[![Build Status](https://travis-ci.com/userfilippi/PreviewGen.svg?branch=master)](https://travis-ci.com/userfilippi/PreviewGen)
