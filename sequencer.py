import pandas
import os,glob
import functions
import numpy
import json

import time

DAYS = 30
flag = False

folder_path = 'Sequences/'
for filename in glob.glob(os.path.join(folder_path, '*.csv')):

    print("Working on:", filename)
    file = pandas.read_csv(filename).sort_values(by=['Date'])

    values = functions.normalize(file["Close"].values)
    size = len(values)

    # splits data in blocks of days=DAYS
    months = functions.splitData(functions.splitAllSequences(values, DAYS), DAYS)

    if flag == True:
        res = numpy.concatenate((res, months), axis=0)
    else:
        res = months
        flag = True

with open('data.txt', 'w') as outfile:
    seq = res.tolist()
    json.dump(seq, outfile)