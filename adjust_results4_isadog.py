#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def adjust_results4_isadog(results_dic, dogfile):
    """Append dog/not-dog flags for true and classifier labels."""
    with open(dogfile, "r") as infile:
        dog_names = {line.rstrip().lower() for line in infile if line.rstrip()}

    for key in results_dic:
        pet_label = results_dic[key][0].lower().strip()
        classifier_label = results_dic[key][1].lower().strip()

        pet_is_dog = 1 if pet_label in dog_names else 0
        classifier_is_dog = 1 if classifier_label in dog_names else 0

        results_dic[key].extend([pet_is_dog, classifier_is_dog])
