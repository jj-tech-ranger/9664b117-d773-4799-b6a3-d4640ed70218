#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os


def get_pet_labels(image_dir):
    """Create pet labels from image filenames."""
    results_dic = {}

    for filename in os.listdir(image_dir):
        if filename.startswith("."):
            continue

        segments = filename.split("_")
        label_parts = [segment for segment in segments if segment.isalpha()]
        pet_label = " ".join(label_parts).lower().strip()

        if filename not in results_dic:
            results_dic[filename] = [pet_label]
        else:
            print(f"** Warning: Duplicate file exists in directory: {filename}")

    return results_dic
