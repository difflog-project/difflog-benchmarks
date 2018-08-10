#!/usr/bin/env python

import numpy as np

def generate_initial(args):
    return []

def fill_map(arr, points):
    for point in points:
        temp = arr
        for x in point[:-1]:
            temp = temp[x]
        temp[point[-1]] = 1

def fill_relation(arr, points):
    arr += points

def main():
    arr = generate_initial((2,2))
    fill_relation(arr, [(0, 0), (1,1)])
    print arr

if __name__ == "__main__":
    main()
