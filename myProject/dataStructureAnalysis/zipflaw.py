import dataStructureAnalysis.WordAnalysis as WA
import math
import matplotlib.pyplot as plt
import numpy as np

def ziplawtest():
    d = WA.make_word_analysis(open("../emma.txt"))
    max_length = 0
    for key in d:
        if d[key] > max_length:
            max_length = d[key]

    x = []
    y = []
    rank = 1
    for i in range(max_length, 0, -1):
        for key in d:
            if d[key] == i:
                print(key, d[key], math.log(d[key]))
                x.append(rank)
                y.append(d[key])
                rank += 1
    return x, y


class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def distance(self):
        return self.x**2 + self.y**2

    def distance_between_point(self, p):
        return (p.x - self.x)**2 + (p.y - self.y)**2


if __name__ == '__main__':
    x, y = ziplawtest()
    scale = "log"
    plt.xscale(scale)
    plt.yscale(scale)
    plt.plot(x ,y)
    plt.show()
