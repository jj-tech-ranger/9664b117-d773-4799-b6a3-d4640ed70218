#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from time import time

from print_functions_for_lab_checks import *
from get_input_args import get_input_args
from get_pet_labels import get_pet_labels
from classify_images import classify_images
from adjust_results4_isadog import adjust_results4_isadog
from calculates_results_stats import calculates_results_stats
from print_results import print_results


def main():
    # Record the start time immediately before the first function call.
    start_time = time()

    in_arg = get_input_args()
    check_command_line_arguments(in_arg)

    results = get_pet_labels(in_arg.dir)
    check_creating_pet_image_labels(results)

    classify_images(in_arg.dir, results, in_arg.arch)
    check_classifying_images(results)

    adjust_results4_isadog(results, in_arg.dogfile)
    check_classifying_labels_as_dogs(results)

    results_stats = calculates_results_stats(results)
    check_calculating_results(results, results_stats)

    print_results(results, results_stats, in_arg.arch, True, True)

    # Record the end time immediately after print_results() finishes.
    end_time = time()

    tot_time = end_time - start_time
    hours = int(tot_time // 3600)
    minutes = int((tot_time % 3600) // 60)
    seconds = int(tot_time % 60)

    print(f"\n** Total Elapsed Runtime: {hours:02d}:{minutes:02d}:{seconds:02d}")


if __name__ == "__main__":
    main()
