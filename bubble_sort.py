import math, random, datetime

numbers = []

def bubbleSort(arr):
    for num in range(len(arr)-1,0,-1):
        for i in range(num):
            if arr[i] > arr[i+1]:
                placeholder = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = placeholder

def numberGen():
    for i in range(100):
        numbers.append(random.randint(0,10000))

print(datetime.datetime.now())
numberGen()

bubbleSort(numbers)
print(datetime.datetime.now())

print(numbers)
