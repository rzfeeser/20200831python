#!/usr/bin/python3
"""RZFeeser || Alta3 Research
We have regularly updating datasets containing numbers of cars purchased per month. Current trackings on Tesla, Ford, Chevy"""

import json

import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt


# our data set lives in a file called carspurchased.json
# read in data set from carspurchased.json
with open("carspurchased.json", "r") as carfile:
    cardata = carfile.read()

# convert our cars string into a python list /dict
cardata = json.loads(cardata)

# our labels are months in a dictionary

labels = cardata.keys()


teslasales = []
chevysales = []
fordsales = []

for month in cardata:
    teslasales.append(cardata.get(month).get("tesla"))
    fordsales.append(cardata.get(month).get("ford"))
    chevysales.append(cardata.get(month).get("chevy"))



width = 0.35       # the width of the bars: can also be len(x) sequence

fig, ax = plt.subplots()

ax.bar(labels, teslasales, width, label='Men')
ax.bar(labels, chevysales, width, label='Chevy')
ax.bar(labels, fordsales, width, label='Ford')

ax.set_ylabel('Number of Sales')
ax.set_title('Sales of Vehicles within the United States per Month in 2020')
ax.legend()

plt.savefig("/home/student/mycode/graphing/secondgraph.png")
