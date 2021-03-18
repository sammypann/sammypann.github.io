import csv

def make_data_point(line, header):
    output = {}
    for index, header_item in enumerate(header):
        output[header_item] = line[index]
    return output

with open("denver-1.nov.csv") as inf:
    reader = csv.reader(inf)
    header = next(reader)
    all_data = []
    for line in reader:
        all_data.append(make_data_point(line, header))

import numpy as np
import pandas as pd

policeDF = pd.read_csv("denver-1.nov.csv")
policeDF

policeDFCrossTab = pd.crosstab(policeDF["date"],policeDF["arrest_made"])
policeDFCrossTab
policeDFCrossTab.mean(axis = 0) 