#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PROGRAMMER: Student
# DATE CREATED: 2026-09-29
# REVISED DATE:

import os
from classifier import classifier

def classify_images(images_dir, results_dic, model):
    for filename, data in results_dic.items():
        image_path = os.path.join(images_dir, filename)
        model_output = classifier(image_path, model).lower().strip()
        pet_label = data[0]
        model_terms = [term.strip() for term in model_output.split(",")]

        match = 1 if (pet_label in model_terms or pet_label in model_output) else 0
        data.extend([model_output, match])
