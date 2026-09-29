#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse


def get_input_args():
    """Retrieve and parse the three command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Process pet image classifier command line arguments."
    )
    parser.add_argument(
        "--dir",
        type=str,
        default="pet_images/",
        help="Path to the folder of pet images.",
    )
    parser.add_argument(
        "--arch",
        type=str,
        default="vgg",
        help="CNN model architecture.",
    )
    parser.add_argument(
        "--dogfile",
        type=str,
        default="dognames.txt",
        help="File containing dog names.",
    )
    return parser.parse_args()
