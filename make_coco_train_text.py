#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created Date: March 25. 2021
Author: Dae Jong Jin 
Description: make train.txt file about COCO

@example
python3 make_coco_train_text.py --make_train $(directory path)
python3 make_coco_train_text.py -mt ~/Documents/output
'''

import os
import natsort
import argparse

def make_coco_train_file(*input):

    help_str="""
    example
    img_path = '/home/djjin/Test/merge/labels_class_5/'
    """
    if len(input) != 1:
        print(help_str)
        return

    path = input[0] + "/"

    file_list = os.listdir(path)
    natsorted_files = natsort.natsorted(file_list, reverse=False)
    result_list = []

    for file in natsorted_files:
        if file.endswith(".txt"):
            with open(path+file, "r") as f:
                lines = f.readlines()

            with open(path+file, "w") as f:
                test = str(file)
                for line in lines:
                    data = line.split()
                    if data[0] != "None":
                        print(' '.join(data) )
                        f.write(' '.join(data) + '\n')
                result_list.append(str(test).replace('txt','jpg'))
            
    for file in natsorted_files:
        if file.endswith(".txt"):
            with open(path+file, "r") as f:
                lines = f.readlines()
                if len(lines) == 0:
                    os.remove(path+file)
                    os.remove(path+file.replace('txt','jpg'))

    with open(path+'../train.txt', 'w') as train_file:
        for file in result_list:
            train_file.write(path+file + "\n") 

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="convert coco annotation to yolo")
    parser.add_argument(
        '-mt', '--make_train', type=str, required=False, nargs='+',
        help='--make_train input_path'
    )

    args = parser.parse_args()
    input_list = args.make_train
    make_coco_train_file(*input_list)
