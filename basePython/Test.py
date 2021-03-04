# -*- coding:utf-8 -*-

"""
@version:
author:changshuai
@time: 2019/08/14
@file: encrypt_aar.py
@function: auto encrypt aar
"""
import requests
import re
import os
import shutil
from zipfile import ZipFile
import subprocess
import argparse

directory = os.path.dirname(os.path.abspath(__file__))


def move_so(src, dst):
    print("move-so from: ", src, " to: ", dst)
    if not os.path.exists(dst):
        os.makedirs(dst)
    shutil.move(src, dst)


def copy_file(src, dst):
    print("copy_file-so from: ", src, " to: ", dst)
    if not os.path.exists(dst):
        os.makedirs(dst)
    shutil.copyfile(src, dst)


def unzip_aar(src, aar_src_folder=None):
    dst_folder = src.split('.')[:-1]
    zip_file = '.'.join(dst_folder) + ".zip"
    os.rename(src, zip_file)
    if aar_src_folder is None:
        aar_src_folder = str(src).replace('.aar', '')
        if not os.path.exists(aar_src_folder):
            os.makedirs(aar_src_folder)
    with ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(aar_src_folder)

    return aar_src_folder, zip_file


def main(origin_src, keep):
    print("sdk_path: ", sdk_path, "isKeep: ", keep)
    dst_folder = origin_src.split('.')[:-1]
    v7a_file = '.'.join(dst_folder) + "_v7a.aar"
    v8a_file = '.'.join(dst_folder) + "_v8a.aar"
    copy_file(origin_src, v7a_file)
    copy_file(origin_src, v8a_file)

    v7a_aar_src_folder, v7a_zip_file = unzip_aar(v7a_file)
    v8a_aar_src_folder, v8a_zip_file = unzip_aar(v7a_file)


if __name__ == '__main__':
    version = os.getenv('VERSION_NAME', '3.2.0')
    build_name = os.getenv('BUILD_NUMBER', '19')

    default_sdk_name = "".join(["colivecore_v", version, ".", build_name, "_limitTime.aar"])
    default_sdk_path = os.path.join("release", "sdk", default_sdk_name)
    print("default_sdk_path: ", default_sdk_path)

    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--sdk", required=False, help="aar sdk to encrypt")
    parser.add_argument("-k", "--keep", required=False, default=False,
                        help="whether keep intermediary backup file, aar source folder")

    args = parser.parse_args()
    sdk_path = args.sdk
    is_keep = args.keep

    if sdk_path is None or len(sdk_path.strip()) == 0:
        sdk_path = default_sdk_path

    if not os.path.isabs(sdk_path):
        sdk_path = os.path.join(directory, sdk_path)

    if not os.path.exists(sdk_path):
        print("sdk not existed")
        exit(1)

    main(sdk_path, is_keep)
