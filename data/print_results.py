#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/print_results.py
#
# PROGRAMMER: Jemimah Jemutai
# DATE CREATED: 2026-09-29
# REVISED DATE:
# PURPOSE: Print the final classification statistics and requested
#          misclassification details.

def print_results(results_dic, results_stats_dic, model,
                  print_incorrect_dogs=False, print_incorrect_breed=False):
    """
    Prints summary results on the classification and, when requested,
    incorrectly classified dogs and incorrectly classified dog breeds.

    Parameters:
      results_dic - Dictionary with key as image filename and value as a list:
                    [pet label, classifier label, match, pet_is_dog,
                     classifier_is_dog]
      results_stats_dic - Dictionary containing classification counts and
                          percentages.
      model - CNN architecture name: resnet, alexnet, or vgg.
      print_incorrect_dogs - Print dog/not-dog errors when True.
      print_incorrect_breed - Print dog breed errors when True.

    Returns:
      None
    """
    print("\n\n*** Results Summary for CNN Model Architecture",
          model.upper(), "***")
    print("{:20}: {:3d}".format(
        "N Images", results_stats_dic["n_images"]))
    print("{:20}: {:3d}".format(
        "N Dog Images", results_stats_dic["n_dogs_img"]))
    print("{:20}: {:3d}".format(
        "N Not-Dog Images", results_stats_dic["n_notdogs_img"]))

    print("\n")
    for key, value in results_stats_dic.items():
        if key.startswith("pct"):
            print("{:20}: {:5.1f}".format(key, value))

    # Print images where the classifier confused a dog with a non-dog,
    # or a non-dog with a dog.
    if (print_incorrect_dogs and
            ((results_stats_dic["n_correct_dogs"]
              + results_stats_dic["n_correct_notdogs"])
             != results_stats_dic["n_images"])):
        print("\nINCORRECT Dog/NOT Dog Assignments:")
        for key, value in results_dic.items():
            if value[3] != value[4]:
                print("Real: {:>26}   Classifier: {:>30}".format(
                    value[0], value[1]))

    # Print dog images for which the classifier identified a dog but
    # selected the wrong breed.
    if (print_incorrect_breed and
            results_stats_dic["n_correct_dogs"]
            != results_stats_dic["n_correct_breed"]):
        print("\nINCORRECT Dog Breed Assignment:")
        for key, value in results_dic.items():
            if value[3] == 1 and value[4] == 1 and value[2] == 0:
                print("Real: {:>26}   Classifier: {:>30}".format(
                    value[0], value[1]))
