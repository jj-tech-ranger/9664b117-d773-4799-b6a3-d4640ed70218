#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

from classifier import classifier


def classify_images(images_dir, results_dic, model):
    """Classify each image and append the classifier label and match flag."""
    for key in results_dic:
        image_path = os.path.join(images_dir, key)

        classifier_label = classifier(image_path, model).lower().strip()
        pet_label = results_dic[key][0].lower().strip()

        classifier_terms = [term.strip() for term in classifier_label.split(",")]
        match = 1 if pet_label in classifier_terms else 0

        results_dic[key].extend([classifier_label, match])
