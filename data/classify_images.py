#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/classify_images.py
#
# PROGRAMMER: Jemimah Jemutai
# DATE CREATED: 2026-09-29
# REVISED DATE:
# PURPOSE: Classify each pet image and append the classifier label and
#          match flag to the results dictionary.

from classifier import classifier


def classify_images(images_dir, results_dic, model):
    """Create classifier labels and compare them with pet image labels.

    The classifier label is normalized to lowercase and stripped of leading
    and trailing whitespace.  The results dictionary is updated in place:
      index 0 = pet image label
      index 1 = classifier label
      index 2 = 1 if the labels match, otherwise 0
    """
    for key in results_dic:
        # The project supplies images_dir with a trailing slash by default.
        # Preserve that form for the required classifier(images_dir + key, ...)
        # call while also supporting a directory without a trailing slash.
        image_path = images_dir + key if images_dir.endswith("/") else images_dir + "/" + key

        model_label = classifier(image_path, model).lower().strip()
        pet_label = results_dic[key][0].lower().strip()

        # ImageNet can return several comma-separated names for one class.
        classifier_labels = [
            label.strip() for label in model_label.split(",")
        ]
        match = 1 if pet_label in classifier_labels else 0

        results_dic[key].extend([model_label, match])
