import math

def total(lst):
    return float(sum(lst))

def average(values):
    if any(values):
        return float(sum(values))/len(values)
    else:
        return math.nan

def median(values):
    values = sorted(values)
    if any(values):
        if len(values) % 2 != 0:
            return values[(len(values)-1)//2]
        else:
            return average([values[(len(values)//2)-1],values[len(values)//2]])
    else:
        raise ValueError


