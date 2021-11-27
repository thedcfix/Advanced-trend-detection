import numpy as np

round_n = 6

def variance(sequence):
    try:
        var = np.var(sequence)
    except:
        var = np.NaN
    
    return round(var, round_n)

def max(sequence):
    try:
        max = np.amax(sequence)
    except:
        max = np.NAN
    
    return round(max, round_n)

def min(sequence):
    try:
        min = np.amin(sequence)
    except:
        min = np.NAN
    
    return round(min, round_n)

def average(sequence):
    try:
        avg = np.mean(sequence)
    except:
        avg = np.NAN
    
    return round(avg, round_n)

def maxDelta(sequence):
    try:
        maxD = max(sequence) - min(sequence)
    except:
        maxD = np.NAN
    
    return round(maxD, round_n)

def deltaSequence(sequence):
    try:
        deltaS = sequence[-1] - sequence[0]
    except:
        deltaS = np.NAN
    
    return round(deltaS, round_n)

def growth(sequence):
    try:
        growth = (sequence[-1] - sequence[0]) / sequence[0] * 100
    except:
        growth = np.NAN
    
    return round(growth, round_n)

def maxGrowth(sequence):
    try:
        if(min(sequence) > 0):
            maxGrowth = (maxDelta(sequence) / min(sequence)) * 100
        else:
            maxGrowth = np.NAN
    except:
        maxGrowth = np.NAN
    
    return round(maxGrowth, round_n)