#!/usr/bin/python
def pos_min(elements, i, j):
    pmin = i
    for k in range(i,j):
        if elements[k] < elements[pmin]:
            pmin = k

    return pmin

def swap(elements, i, j):
    aux = elements[i]
    elements[i] = elements[j]
    elements[j] = aux

def k_selection(elements, k):
    n = len(elements)
    for i in range(n):
        swap(elements, i, pos_min(elements, i, n))

    return elements[k]
