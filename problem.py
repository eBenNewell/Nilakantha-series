#!/usr/bin/env python3
# Compute pi at any point in series
#def computer()
#    list1 = [1, 101, 201, 301, 401, 501, 601, 701, 801, 901]
#    pi = 0
#    change = 4 / ((i * 2) * ((i * 2) + 1) * ((i * 2) + 2))

def m(i):
    # define variables
    pi = 0
    operator = 1
    denominator = 1
    run = 0
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
        print(f"{run}        {round(pi, 4)}")
m(901)   