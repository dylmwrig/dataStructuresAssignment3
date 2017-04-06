#data structures assignment 3
#1) fill lists of lengths 100, 500, 1000, 2000, 5000, 8000, 10000 with random numbers
#   -umbers should be between 0 and 20000
#2) implement each of the following sorting algorithms on each list
#   -insertion sort, quick sort, heap sort, and merge sort
#   -use either recursive or iterative versions, given the choice, it's up to you
#   -use every sorting algorithm on each list
#3) obtain the execution time
#   -compare when the list is sorted vs unsorted
#graph comparing execution times

import random

#insertion sort
#given a 'key' to insert, read in each element individually and compare it to each list element, starting at the end
#if it is smaller than the 'key', copy the element in the position one to the right
#otherwise, put it one position to that element's right
def insertSort(toSort):
    sorted = []
    sorted.append(toSort[0])
    print(str(sorted[0]) + "yeah whatever")

    for i in range(1, len(toSort)):
        element = toSort[i]
        sorted.append(element)
        for j in range(len(sorted) - 1, -1, -1):
            if sorted[j] > element:
                sorted[j + 1] = sorted[j]
                break;

            else:
                sorted[j + 1] = element
                break;

    for i in range(0, len(sorted)):
        print (sorted[i])

#generate a list of given size filled with random numbers from 0 to 20000
def randGen(listSize):
    randList = []
    for i in range(listSize):
        randList.append(random.randint(0, 20000))
    return randList

def main():
    listToSort = randGen(20)
    for i in range(len(listToSort)):
        print(listToSort[i])
    print("now for sorting:")
    insertSort(listToSort)

if (__name__ == "__main__"):
    main()