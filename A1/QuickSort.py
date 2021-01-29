#!/usr/bin/env python3

# QUICKSORT
# Worst Case - Theta(n^2)
# Average Case - Theta(nlogn)
import sys
import csv
import time
import math
import matplotlib.pyplot as plt

sys.setrecursionlimit(10**9)

Submission = True
InputFile = sys.argv[1]

# Storing Data as nested list, where key is element 0 of nested list
Data = dict()
with open(InputFile + '.csv', 'r') as csvfile:
    csv_reader = csv.reader(csvfile)
    for row in csv_reader:
        Data[int(row[0])] = list()
        for i in row[1:]:
            Data[int(row[0])].append(i)
Arr = list(Data)


def DetermineInputSizeList(Arr, buckets):
    InputSize = []
    i = int(len(Arr)/buckets)
    for idx, value in enumerate(Arr):
        if idx % i == 0 and idx != 0:
            InputSize.append(idx)
        if idx == len(Arr) - 1:
            InputSize.append(idx)
    return InputSize


def Partition(Arr, p, r):

    pivot = Arr[r]
    i = p - 1

    for j in range(p, r):
        if Arr[j] <= pivot:
            i += 1
            Arr[i], Arr[j] = Arr[j], Arr[i]
    # Swap Elements
    Arr[i+1], Arr[r] = Arr[r], Arr[i+1]
    return (i+1)  # Return element q


def QuickSort(Arr, p, r):

    if (p < r):
        q = Partition(Arr, p, r)
        QuickSort(Arr, p, q - 1)
        QuickSort(Arr, q + 1, r)


def TimeAlgorithm(Arr, InputSize, p, r):
    ExecTime = []
    for i in InputSize:
        StartTime = time.time()
        QuickSort(Arr[0:i], p, i-1)
        ExecTime.append(time.time() - StartTime)
    return ExecTime


def Graph(InputSize, ExecTime):
    plt.plot(InputSize, ExecTime)
    plt.ylabel('Execution Time (s)')
    plt.xlabel('Input Size (n)')
    plt.title('Algorithm RunTime as a Function of Input Size')
    plt.show()


p = 0
r = len(Arr) - 1

if Submission:  # Submission flag
    print(f'Running QuickSort on Input Size of {len(Arr)}')
    InputSize = DetermineInputSizeList(Arr, 5)
    ExecTime = TimeAlgorithm(Arr, InputSize, p, r)
    Graph(InputSize, ExecTime)
else:
    QuickSort(Arr, p, r)
    for i in Arr:
        Data[i].insert(0, i)
        print(Data[i])
    SortStatus = all(Arr[i] <= Arr[i+1]
                     for i in range(len(Arr)-1))  # Check if Sorted
    print(f'Is the Dataset Sorted: {SortStatus}')
