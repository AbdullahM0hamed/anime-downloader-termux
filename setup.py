#!/usr/bin/env python3

from setuptools import setup
from shutil import copyfile
import os
import subprocess

setup(
    name='anime-downloader-termux',
    version='0.1',
    scripts=['termux-anime'],
    install_requires=[
        'anime-downloader @ git+https://github.com/vn-ki/anime-downloader'
    ]
)

bin_dir = "/data/data/com.termux/files/home/bin"

try:
    os.makedirs(bin_dir)
except FileExistsError:
    if os.path.exists(f"{bin_dir}/termux-url-opener"):
        #For some reason, if user doesn't have termux-url-opener, it creates the one I want then runs again and copies that to termux-url-opener-2
        new = open("termux-url-opener").read()
        current = open(f"{bin_dir}/termux-url-opener").read()

        if current != new:
            os.rename(f"{bin_dir}/termux-url-opener", f"{bin_dir}/termux-url-opener-2")

copyfile("termux-url-opener", f"{bin_dir}/termux-url-opener")

app_not_installed = subprocess.getoutput("am startservice -a android.service.notification.NotificationListenerService com.termux.api | grep 'Error: Not found; no service started.'")
pkg_installed = subprocess.getoutput("pkg list-installed 2>&1 | grep termux-api")

if not pkg_installed:
    subprocess.getoutput("apt install -y termux-api")

if app_not_installed:
    subprocess.getoutput("am start -a android.intent.action.VIEW -d 'market://details?id=com.termux.api' com.android.vending")
