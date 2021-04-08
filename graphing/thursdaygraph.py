#!/usr/bin/env python3
"""Imports"""
import matplotlib.pyplot as plt
import matplotlib
import numpy as np


"""Main Code"""


def main():
    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    y = np.array([12, 35, 3, 50])
    mylabels = ["Perfect Slice", "Too Big", "Too Little", "The Rest of the Pie"]
    # makes slice come out
    myexplode = [0.2, 0, 0, 0]
    # Customize the pie
    plt.pie(y, labels = mylabels, explode = myexplode, shadow = True, startangle = 90)
    # Create a legend
    plt.legend(title = "The Right Amount of Pie:")
    # display/save the graph
    plt.savefig("/home/student/mycode/graphing/perfectpy.png")
    # copy
    plt.savefig("/home/student/static/perfectpy.png")


main()
