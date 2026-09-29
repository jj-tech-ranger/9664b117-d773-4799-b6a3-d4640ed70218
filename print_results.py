#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def print_results(
    results_dic,
    results_stats_dic,
    model,
    print_incorrect_dogs=False,
    print_incorrect_breed=False,
):
    """Print summary metrics and optional misclassification details."""
    print(
        "\n\n*** Results Summary for CNN Model Architecture",
        model.upper(),
        "***",
    )
    print("{:20}: {:3d}".format("N Images", results_stats_dic["n_images"]))
    print("{:20}: {:3d}".format("N Dog Images", results_stats_dic["n_dogs_img"]))
    print(
        "{:20}: {:3d}".format(
            "N Not-Dog Images", results_stats_dic["n_notdogs_img"]
        )
    )

    print("\n")
    for key in (
        "pct_match",
        "pct_correct_dogs",
        "pct_correct_breed",
        "pct_correct_notdogs",
    ):
        print("{:20}: {:5.1f}".format(key, results_stats_dic[key]))

    if (
        print_incorrect_dogs
        and (
            results_stats_dic["n_correct_dogs"]
            + results_stats_dic["n_correct_notdogs"]
        )
        != results_stats_dic["n_images"]
    ):
        print("\nINCORRECT Dog/NOT Dog Assignments:")
        for key, value in results_dic.items():
            if value[3] != value[4]:
                print(
                    "Real: {:>26}   Classifier: {:>30}".format(
                        value[0], value[1]
                    )
                )

    if (
        print_incorrect_breed
        and results_stats_dic["n_correct_dogs"]
        != results_stats_dic["n_correct_breed"]
    ):
        print("\nINCORRECT Dog Breed Assignment:")
        for key, value in results_dic.items():
            if value[3] == 1 and value[4] == 1 and value[2] == 0:
                print(
                    "Real: {:>26}   Classifier: {:>30}".format(
                        value[0], value[1]
                    )
                )
