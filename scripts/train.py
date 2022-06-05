#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
import os
import shutil
import kaggle
import time

SUBMISSION_DIR = 'submission'
METADATA_FILE = 'scripts/kernel-metadata.json'


def main(notebook_path):
    if not os.path.exists(notebook_path):
        print(f'File {notebook_path} does not exist.')
        return

    if os.path.exists(SUBMISSION_DIR):
        shutil.rmtree(SUBMISSION_DIR)
    
    if 'pytorch' in notebook_path:
        METADATA_FILE = 'scripts/kernel-metadata-pytorch.json'

    os.mkdir(SUBMISSION_DIR)
    shutil.copy(METADATA_FILE, os.path.join(SUBMISSION_DIR, 'kernel-metadata.json'))
    shutil.copy(notebook_path, os.path.join(SUBMISSION_DIR, 'train.ipynb'))
    kaggle.api.kernels_push(SUBMISSION_DIR)
    shutil.rmtree(SUBMISSION_DIR)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('notebook_path')
    args = parser.parse_args()

    main(**vars(args))
