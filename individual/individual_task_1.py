#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == "__main__":
    A = list(map(int, input().split()))
    
    if len(A) != 10:
        print("Введите ровно 10 элементов!", file=sys.stderr)
        exit(1)
    
    cnt = 0
    max_index = -1
    for i, item in enumerate(A):
        if item % 3 == 0:
            cnt += 1
            max_index = i
    
    print(f"Число элементов, кратных 3: {cnt}")
    if max_index != -1:
        print(f"Наибольший индекс таких элементов: {max_index}")
