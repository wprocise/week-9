import pandas as pd

## Exercise 1
"""
Build python class called 'GroupEstimate' taking categorical data and corresponding 
continuous values, and determines which group a new observation falls into, and 
predicts an estimate value based on the data provided.
"""
# Part 1: Define a class 'GroupEstimate' that accepts an 'estimate' argument, which can be either "mean" or "median".
class GroupEstimate(object):
    def __init__(self, estimate):
        if estimate not in ["mean", "median"]:
            raise ValueError("Estimate must be either 'mean' or 'median'")


