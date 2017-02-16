import matplotlib.pyplot as pyplot
from numpy import mean
import numpy as np
from scipy import stats


def confidence_interval(data, confidence=0.95):
    a = 1.0 * np.array(data)
    n = len(a)
    m, se = np.mean(a), stats.sem(a)
    h = se * stats.t.ppf((1 + confidence) / 2., n - 1)
    return m - h, m + h


file = open("arrival_service_times.csv", "r")

ia_times = []
service_times1 = []
service_times2 = []
delay_times1 = []
delay_times2 = []
departure_times1 = []
departure_times2 = []
arrival_times = []
total_times1 = []
total_times2 = []

for line in file:
    items = line.strip("\n").split(",")
    ia_times.append(float(items[0]))
    service_times1.append(float(items[1]))
    service_times2.append(float(items[2]))

arrival_times.append(0)
delay_times1.append(0)
delay_times2.append(0)
departure_times1.append(service_times1[0])
departure_times2.append(service_times2[0])
total_times1.append(departure_times1[0] - arrival_times[0])
total_times2.append(departure_times2[0] - arrival_times[0])

for i in range(1, 300):
    arrival_times.append(arrival_times[i - 1] + ia_times[i])

for i in range(1, 300):
    if arrival_times[i] < departure_times1[i - 1]:
        delay_times1.append(departure_times1[i - 1] - arrival_times[i])
    else:
        delay_times1.append(0)

    departure_times1.append(arrival_times[i] + delay_times1[i] + service_times1[i])
    total_times1.append(departure_times1[i] - arrival_times[i])

    if arrival_times[i] < departure_times2[i - 1]:
        delay_times2.append(departure_times2[i - 1] - arrival_times[i])
    else:
        delay_times2.append(0)

    departure_times2.append(arrival_times[i] + delay_times2[i] + service_times2[i])
    total_times2.append(departure_times2[i] - arrival_times[i])

server_utilization1 = (300 * mean(service_times1))/departure_times1[299]
server_utilization2 = (300 * mean(service_times2))/departure_times2[299]
print("Mean Wait time 1: ", mean(delay_times1))
print("Mean Wait time 2: ", mean(delay_times2))
print("Average Time in System 1: ", mean(total_times1))
print("95% CI for Time in System 1: ", confidence_interval(total_times1))
print("Average Time in System 2: ", mean(total_times2))
print("95% CI for Time in System 2: ", confidence_interval(total_times2))
print("Average Server Utilization 1", server_utilization1)
print("Average Server Utilization 2", server_utilization2)
print("Average Customers in Queue 1: ", (300/departure_times1[299])*mean(delay_times1))
print("Average Customers in Queue 2: ", (300/departure_times2[299])*mean(delay_times2))

print("Mean Inter-Arrival Time: ", mean(ia_times))
print("95% CI Inter-Arrival Times: ", confidence_interval(ia_times))
print("Mean Arrival Rate: ", 1/mean(ia_times))
pyplot.hist(ia_times, 30)
pyplot.title("Inter-Arrival Times")
pyplot.show()

print("Mean Service Time 1: ", mean(service_times1))
print("95% CI Service Times 1: ", confidence_interval(service_times1))
print("Mean Service Rate 1: ", 1/mean(service_times1))
pyplot.hist(service_times1, 30)
pyplot.title("Service Times 1")
pyplot.show()

print("Mean Service Time 2: ", mean(service_times2))
print("95% CI Service Times 2: ", confidence_interval(service_times2))
print("Mean Service Rate 2: ", 1/mean(service_times2))
pyplot.hist(service_times2, 30)
pyplot.title("Service Times 2")
pyplot.show()
