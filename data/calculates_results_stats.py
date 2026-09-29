#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PROGRAMMER: Student
# DATE CREATED: 2026-09-29
# REVISED DATE:

def calculates_results_stats(results_dic):
    results_stats = {
        'n_images': len(results_dic),
        'n_dogs_img': 0,
        'n_notdogs_img': 0,
        'n_match': 0,
        'n_correct_dogs': 0,
        'n_correct_notdogs': 0,
        'n_correct_breed': 0
    }

    for data in results_dic.values():
        match_flag = data[2]
        pet_is_dog = data[3]
        clf_is_dog = data[4]

        if match_flag == 1:
            results_stats['n_match'] += 1

        if pet_is_dog == 1:
            results_stats['n_dogs_img'] += 1
            if clf_is_dog == 1:
                results_stats['n_correct_dogs'] += 1
            if match_flag == 1:
                results_stats['n_correct_breed'] += 1
        else:
            if clf_is_dog == 0:
                results_stats['n_correct_notdogs'] += 1

    results_stats['n_notdogs_img'] = results_stats['n_images'] - results_stats['n_dogs_img']
    n_imgs = results_stats['n_images']
    n_dogs = results_stats['n_dogs_img']
    n_notdogs = results_stats['n_notdogs_img']

    results_stats['pct_match'] = (results_stats['n_match'] / n_imgs) * 100.0 if n_imgs > 0 else 0.0
    results_stats['pct_correct_dogs'] = (results_stats['n_correct_dogs'] / n_dogs) * 100.0 if n_dogs > 0 else 0.0
    results_stats['pct_correct_breed'] = (results_stats['n_correct_breed'] / n_dogs) * 100.0 if n_dogs > 0 else 0.0
    results_stats['pct_correct_notdogs'] = (results_stats['n_correct_notdogs'] / n_notdogs) * 100.0 if n_notdogs > 0 else 0.0

    return results_stats
