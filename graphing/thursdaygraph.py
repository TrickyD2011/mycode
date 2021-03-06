#!/usr/bin/env python3
"""Imports"""
import matplotlib.pyplot as plt
import numpy as np
import pytest
import os.path
from os import path



def main():
    """Time to make a Pie Chart"""
    # Size of each slice:
    size = np.array([12, 35, 3, 50])
    # Label of each slice:
    mylabels = ["Perfect Slice", "Too Big", "Too Little", "The Rest of the Pie"]
    # makes slice come out
    myexplode = [0.2, 0, 0, 0]
    # Customize the pie
    plt.pie(size, labels = mylabels, explode = myexplode, shadow = True, startangle = 90)
    # Create a legend
    plt.legend(title = "The Right Amount of Pie:")
    # display/save the graph
    plt.savefig("/home/student/mycode/graphing/perfectpy.png")
    # copy of save
    plt.savefig("/home/student/static/perfectpy.png")

def test_print(su="successful"):
    print ("File exists: "+str(path.exists('/home/student/static/perfectpy.png')))
    return f"Print was {su}"
test_print()

def test_save():
    #testing if the file was saved
    assert test_print() == "Print was successful"

main()
