#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PROGRAMMER: Student
# DATE CREATED: 2026-09-29
# REVISED DATE:

def print_results(results_dic, results_stats_dic, model, 
                  print_incorrect_dogs=False, print_incorrect_breed=False):
    """
    Prints summary results on the classification and displays any incorrectly 
    classified dogs or dog breeds if requested.
    """
    print(f"\n\n*** RESULTS SUMMARY FOR MODEL ARCHITECTURE: {model.upper()} ***")
    print(f"Total Number of Images       : {results_stats_dic['n_images']:3d}")
    print(f"Number of Dog Images         : {results_stats_dic['n_dogs_img']:3d}")
    print(f"Number of 'Not-a' Dog Images : {results_stats_dic['n_notdogs_img']:3d}")
    print("-" * 55)

    for key, value in results_stats_dic.items():
        if key.startswith('pct_'):
            label = key.replace('pct_', '% ').replace('_', ' ').title()
            print(f"{label:<30}: {value:6.2f}%")

    total_correct_species = results_stats_dic['n_correct_dogs'] + results_stats_dic['n_correct_notdogs']
    if print_incorrect_dogs and (total_correct_species != results_stats_dic['n_images']):
        print("\nINCORRECT Dog/Not-a-Dog Classifications:")
        for filename, data in results_dic.items():
            if sum(data[3:]) == 1:
                print(f"File: {filename:<25} | Truth: {data[0]:<20} | Predicted: {data[1]}")

    if print_incorrect_breed and (results_stats_dic['n_correct_dogs'] != results_stats_dic['n_correct_breed']):
        print("\nINCORRECT Dog Breed Classifications:")
        for filename, data in results_dic.items():
            if sum(data[3:]) == 2 and data[2] == 0:
                print(f"File: {filename:<25} | Truth: {data[0]:<20} | Predicted: {data[1]}")
