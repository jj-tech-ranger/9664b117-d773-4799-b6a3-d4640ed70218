#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def calculates_results_stats(results_dic):
    """Calculate classification counts and percentages."""
    results_stats_dic = {}

    n_images = len(results_dic)
    n_dogs_img = 0
    n_notdogs_img = 0
    n_match = 0
    n_correct_dogs = 0
    n_correct_notdogs = 0
    n_correct_breed = 0

    for key in results_dic:
        match = results_dic[key][2]
        pet_is_dog = results_dic[key][3]
        classifier_is_dog = results_dic[key][4]

        if match == 1:
            n_match += 1

        if pet_is_dog == 1:
            n_dogs_img += 1
            if classifier_is_dog == 1:
                n_correct_dogs += 1
            if match == 1:
                n_correct_breed += 1
        else:
            n_notdogs_img += 1
            if classifier_is_dog == 0:
                n_correct_notdogs += 1

    results_stats_dic["n_images"] = n_images
    results_stats_dic["n_dogs_img"] = n_dogs_img
    results_stats_dic["n_notdogs_img"] = n_notdogs_img
    results_stats_dic["n_match"] = n_match
    results_stats_dic["n_correct_dogs"] = n_correct_dogs
    results_stats_dic["n_correct_notdogs"] = n_correct_notdogs
    results_stats_dic["n_correct_breed"] = n_correct_breed

    results_stats_dic["pct_match"] = (
        (n_match / n_images) * 100.0 if n_images > 0 else 0.0
    )
    results_stats_dic["pct_correct_dogs"] = (
        (n_correct_dogs / n_dogs_img) * 100.0 if n_dogs_img > 0 else 0.0
    )
    results_stats_dic["pct_correct_breed"] = (
        (n_correct_breed / n_dogs_img) * 100.0 if n_dogs_img > 0 else 0.0
    )
    results_stats_dic["pct_correct_notdogs"] = (
        (n_correct_notdogs / n_notdogs_img) * 100.0
        if n_notdogs_img > 0
        else 0.0
    )

    return results_stats_dic
