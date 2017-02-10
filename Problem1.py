import numpy
import matplotlib.pyplot as pyplot
from prettytable import PrettyTable
import math


def generate(x, y):
    return numpy.random.uniform(-x, x), numpy.random.uniform(-y, y)


def hit(x, y):
    return pow(x / 3, 2) + pow(y / 2, 2) <= 1


def confidence_interval(n, estimate, x, y):
    interval = 1.96 * (math.sqrt(estimate * (4 * x * y - estimate) / n))
    low = estimate - interval
    high = estimate + interval
    return [low, high]

maxX = 3
maxY = 2
start = 100
stop = 2000
step = 100
hits = 0
tests = range(start, stop + step, step)
table = {}
i = 0

for num in tests:
    while i < num:
        xCoord, yCoord = generate(maxX, maxY)
        if hit(xCoord, yCoord):
            hits += 1
        i += 1
    table[num] = hits

pretty = PrettyTable()
pretty.field_names = ["N", "Area", "95% CI"]
iterations = []
estimations = []
confidence_intervals = []
for num, j in table.items():
    area = (j/num)*2*maxX*2*maxY
    confidence = confidence_interval(num, area, maxX, maxY)
    iterations.append(num)
    estimations.append(area)
    confidence_intervals.append(confidence)
    pretty.add_row([num, area, confidence])

print(pretty)

pyplot.plot(iterations, estimations)
pyplot.plot(iterations, confidence_intervals, "--")
pyplot.show()

