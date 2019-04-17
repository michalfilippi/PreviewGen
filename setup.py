import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="previewgen",
    version="1.3",
    author="Michal Filippi",
    author_email="michal.filippi@gmail.com",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/michalfilippi/PreviewGen",
    packages=setuptools.find_packages(),
    install_requires = [
        'PyYAML>=5.1',
        'Pillow>=6.0.0',
        'schema>=0.7.0'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'preview-gen = previewgen.__main__:main'
        ]
    }
)
