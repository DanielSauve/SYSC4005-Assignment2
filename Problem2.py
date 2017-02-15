import random
import math

a = 5.0
b = a


def run_sim(trials):
    crosses = 0

    i = 0
    while i < trials:
        i += 1

        # generate random orientation of pin
        y = random.uniform(0, a)
        phi = random.uniform(0, math.pi / 2)

        # check if pin crosses a line
        if y <= b * math.sin(phi):
            crosses += 1

    # calcualte estimate for 1 / pi
    estimate = (a * crosses) / (2 * b * trials)

    c = 0.95
    interval = (a * (float(crosses) / (trials - 1)) * (1 - float(crosses) / trials)) / (
        2 * b * math.sqrt(trials * (1 - c)))
    lower = estimate - interval
    upper = estimate + interval

    # print results
    print("Actual: " + str(1 / math.pi) + ", Estimate: " + str(estimate) + ", [" + str(lower) + ", " + str(upper) + "]")


if __name__ == '__main__':
    run_sim(20)
    run_sim(100)
