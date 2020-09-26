#!/usr/bin/env python3

def m(i):
    # define variables
    pi = 0
    operator = 1
    denominator = 1
    run = 0
    list1 = [1, 101, 201, 301, 401, 501, 601, 701, 801, 901]
    answ = []
    while run < i:
        pi = pi + (4 * operator * (1 / denominator))
        # incrases the denominator by 2 each run.
        denominator += 2
        # sets the operator back and forth between positive and negative each run.
        if operator == -1:
            operator = 1
        else:
            operator = -1
        run += 1
        #print(f"{run}        {format(pi, ".4f")}")
        answ.append((run, format(pi, ".4f")))
    for item in list1:
        # item - 1 because lists start at 0 in python instead of 1
        print(f"{answ[item - 1][0]}            {answ[item - 1][1]}")
m(901)