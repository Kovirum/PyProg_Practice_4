#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == "__main__":
    G_populations = tuple(map(int, input("Введите численности населения (в млн. жителей) 28 государств: ").split()))
    G_squares = tuple(map(int, input("Введите площади 28 государств (в тыс. кв. км.): ").split()))
    A = int(input("Введите максимальную площадь \"маленького\" государства (в тыс. кв. км.): "))

    if len(G_populations) != 28:
        print("Вы должны ввести ровно 28 чисел населений государств!", file=sys.stderr)
        exit(1)
    if len(G_squares) != 28:
        print("Вы должны ввести ровно 28 площадей государств!", file=sys.stderr)
        exit(1)

    small_g_population = 0
    for i, item in enumerate(G_populations):
        if G_squares[i] <= A:
            small_g_population += item
    
    print(f"Общая численность населения в \"маленьких\" государствах: {small_g_population} млн. жителей")


    