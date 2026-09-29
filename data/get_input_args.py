#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PROGRAMMER: Student
# DATE CREATED: 2026-09-29
# REVISED DATE:

import argparse

def get_input_args():
    parser = argparse.ArgumentParser(description="Command-line arguments for pet image classification.")
    parser.add_argument('--dir', type=str, default='pet_images/', help='Path to images folder')
    parser.add_argument('--arch', type=str, default='vgg', choices=['vgg', 'alexnet', 'resnet'], help='CNN model architecture')
    parser.add_argument('--dogfile', type=str, default='dognames.txt', help='File with list of dog names')
    return parser.parse_args()
