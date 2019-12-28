#!/usr/bin/env python3
#Ref: https://codereview.stackexchange.com/questions/201244/flatten-an-array-in-python

def flatten(input_array):
    result_array = []
    for element in input_array:
        if isinstance(element, int):
            result_array.append(element)
        elif isinstance(element, list):
            result_array += flatten(element)
    return result_array

#For tests: pytest es1.py
def test00():
    results = flatten([[[1,2,[3]],4]])
    assert results == [1, 2, 3, 4]

def test01():
    results = flatten([1, [2, 3, [4]], 5, [[6]]])
    assert results == [1, 2, 3, 4, 5, 6]


def test02():
    results = flatten([1, [2, 3, [4], []], [], 5, [[], [6]]])
    assert results == [1, 2, 3, 4, 5, 6]
    
def test03():
    results = flatten([[[[1,2],[3]],[4,5]]])
    assert results == [1, 2, 3, 4, 5]