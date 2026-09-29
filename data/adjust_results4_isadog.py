#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PROGRAMMER: Student
# DATE CREATED: 2026-09-29
# REVISED DATE:

def adjust_results4_isadog(results_dic, dogfile):
    dognames_dic = {}
    with open(dogfile, "r") as f:
        for line in f:
            dog_name = line.strip().lower()
            if dog_name and dog_name not in dognames_dic:
                dognames_dic[dog_name] = 1

    for filename, data in results_dic.items():
        pet_label = data[0]
        classifier_label = data[1]

        pet_is_dog = 1 if pet_label in dognames_dic else 0
        clf_terms = [t.strip() for t in classifier_label.split(",")]
        classifier_is_dog = 1 if (classifier_label in dognames_dic or any(term in dognames_dic for term in clf_terms)) else 0

        data.extend([pet_is_dog, classifier_is_dog])
