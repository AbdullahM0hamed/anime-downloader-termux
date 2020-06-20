#!/usr/bin/env python3

from setuptools import setup

setup(
    name='anime-downloader-termux',
    version='0.1',
    scripts=['termux-anime'],
    install_requires=[
        'anime-downloader @ git+https://github.com/vn-ki/anime-downloader'
    ]
)
