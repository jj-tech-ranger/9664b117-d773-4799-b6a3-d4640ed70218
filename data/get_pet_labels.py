#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PROGRAMMER: Student
# DATE CREATED: 2026-09-29
# REVISED DATE:

import os

def get_pet_labels(image_dir):
    results_dic = {}
    filename_list = os.listdir(image_dir)

    for filename in filename_list:
        if filename.startswith('.'):
            continue
        lower_name = filename.lower()
        word_list = lower_name.split("_")
        pet_name = " ".join([word for word in word_list if word.isalpha()]).strip()

        if filename not in results_dic:
            results_dic[filename] = [pet_name]
        else:
            print(f"** Warning: Key={filename} already exists in results_dic with value={results_dic[filename]}")

    return results_dic
