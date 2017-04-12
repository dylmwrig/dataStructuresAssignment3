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
import timeit #time the execution of each sorting algorithm

#insertion sort
#given a 'key' to insert, read in each element individually and compare it to each list element, starting at the end
#if it is smaller than the 'key', copy the element in the position one to the right
#otherwise, put it one position to that element's right
def insertSort(toSort):
    sorted = []
    sorted.append(toSort[0]) #adding the first element will logically result in an ordered list

    for i in range(1, len(toSort)):
        element = toSort[i]
        sorted.append(element)
        #start at length - 2 to account for the element we just inserted
        for j in range(len(sorted) - 2, -1, -1):
            if sorted[j] > element:
                sorted[j + 1] = sorted[j]

            else:
                sorted[j + 1] = element
                break;

            if j == 0: #if the final inserted element is smaller than everything else, place it as the 0th element
                sorted[j] = element

def quickSortBlastoff(toSort, start, end):
    if start < end:
        pivot = quickSort(toSort, start, end)
        quickSortBlastoff(toSort, start, pivot - 1)
        quickSortBlastoff(toSort, pivot + 1, end)

#quick sort
#divide and conquer algorithm with worst case n^2 and average case nlogn
#
#select an element in the array known as the 'pivot'
#sort so that each element to the left is less than or equal to the pivot, each to the right is greater than
#recursively quick sort each sub array to the left and right of the pivot
def quickSort(toSort, lowIndex, highIndex):
    pivotIndex = highIndex
    highIndex -= 1

    #keep an index for lower elements and an index for higher
    #start the low side on the left, start the high side on the right, one to the left of the pivot
    #if you find an element larger than the pivot on the low side, move through the higher elements
    #until an element smaller than the pivot is found. Then, swap these elements
    #finally, when the low and high indexes meet each other in the middle, swap the larger one with the pivot

    keepGoing = True
    while keepGoing:
        #print("At the top of while, low then high index: " + str(lowIndex) + " " + str(highIndex))
        #changed it so that it's while the lowIndex is strictly less than the highIndex, rather than less than or equal to
        #this fixes the recursion issue/issue when the pivot is the largest element
        while lowIndex < highIndex and toSort[lowIndex] <= toSort[pivotIndex]:
            lowIndex += 1

        while highIndex > lowIndex and toSort[highIndex] >= toSort[pivotIndex]:
            highIndex -= 1

        #is this conditional even necessary?
        if lowIndex < highIndex:
            temp = toSort[lowIndex]
            toSort[lowIndex] = toSort[highIndex]
            toSort[highIndex] = temp
            lowIndex += 1
            highIndex -= 1

        else:
            keepGoing = False

    #swap the pivot to be in the middle where it belongs
    temp = toSort[pivotIndex]
    toSort[pivotIndex] = toSort[lowIndex]
    toSort[lowIndex] = temp
    pivotIndex = lowIndex

    return pivotIndex

#make sure the root element is the largest
#if i is the index,
#the left child of any element is 2i + 1, the right is 2i + 2
#pass in the "largest" element, initialized to be the root when this function is first called
#pass in the array size as this will "change" as the max is deleted
def heapify(toSort, largest, arrSize):
    root = largest
    left = 2 * largest + 1
    right = 2 * largest + 2
    #if the index is not less than the size of the array, the child does not exist
    if left < arrSize and toSort[left] > toSort[largest]:
        largest = left

    if right < arrSize and toSort[right] > toSort[largest]:
        largest = right

    #if the root is not the largest element, swap to make it so
    if root != largest:
        temp = toSort[root]
        toSort[root] = toSort[largest]
        toSort[largest] = temp
        heapify(toSort, largest, arrSize)

#heapify from the bottom up, starting at the last element up to the root
def buildHeap(toSort):
    for i in range(len(toSort) - 1, -1, -1):
        heapify(toSort, i, len(toSort))

#heap sort
#use priority heap to sort in nlogn time, worst case 2NlogN - O(N)
#-build priority heap from input, O(n), then deleteMin N times to generate sequence in sorted order
#
#recall the heap requirement that the parent must be larger than the children
#take advantage of this property: swap the final child element with the root element, which will
#by this property be the largest element; now, deleteMin to cut off the final child because it is
#in the proper order. Now, re-heapify the heap by bubbling the largest elements to the top
def heapSort(toSort):
    buildHeap(toSort)
    for i in range(len(toSort) - 1, -1, -1):
        temp = toSort[0]
        toSort[0] = toSort[i]
        toSort[i] = temp
        heapify(toSort, 0, i)

#merge sort
#divide and conquer algorithm similar to quickSort, NlogN worst case
#split the input array into to sub arrays
#iterate through each sorted subarray, called L and R; if the element in L is smaller, place it in
#the output array. Same goes for the reverse
#do this until one of the arrays is empty; when this happens, empty the other array into the output
def mergeSort(toSort):
    if len(toSort) == 1: #base case: the list has been decomposed to being one element
        return

    mid = int(len(toSort) / 2)
    left = toSort[:mid]
    right = toSort[mid:len(toSort)]
    mergeSort(left) #sort the left and right halves until they are one element
    mergeSort(right)
    merge(left, right, toSort) #sort each subarray back until you have the final, sorted array

#called by mergeSort
#pass in the right and left subarrays, in addition to the complete array we're sorting
def merge(left, right, output):
    leftIndex, rightIndex, outIndex = 0, 0, 0
    while leftIndex < len(left) and rightIndex < len(right):
        #move elements from each subarray into the output array based on which is smaller
        if left[leftIndex] <= right[rightIndex]:
            output[outIndex] = left[leftIndex]
            leftIndex += 1
            outIndex += 1
        else:
            output[outIndex] = right[rightIndex]
            rightIndex += 1
            outIndex += 1

    #one array will be empty before the other, so only one of these will execute
    #empty the other array into the output
    while leftIndex < len(left):
        output[outIndex] = left[leftIndex]
        leftIndex += 1
        outIndex += 1
    while rightIndex < len(right):
        output[outIndex] = right[rightIndex]
        rightIndex += 1
        outIndex += 1

#TODO
#do not allow for duplicate values
#generate a list of given size filled with random numbers from 0 to 20000
def randGen(listSize):
    randList = []
    randNum = 0
    for i in range(listSize):
        newRand = True
        #continue generating random numbers if the number is already in the list
        while newRand:
            randNum = random.randint(0, 20000)
            if randNum not in randList:
                newRand = False

        randList.append(randNum)
    return randList

#return an ordered list for finding best case execution time for each sorting algorithm
def orderedList(listSize):
    ordered = []
    for i in range(listSize):
        ordered.append(i)
    return ordered

def main():
    output = open("output.txt", "w")
    listSize = [100, 500, 1000, 2000, 5000, 8000, 10000] #generate lists of these sizes when finding running time
    for i in range (len(listSize)):
        unordered = randGen(listSize[i])
        ordered = orderedList(listSize[i])
        output.write("Insert sort running time\n")
        start = timeit.default_timer()
        insertSort(unordered)
        stop = timeit.default_timer()
        output.write("unordered: " + str(stop - start) + "\n")
        start = timeit.default_timer()
        insertSort(ordered)
        stop = timeit.default_timer()
        output.write("ordered: " + str(stop - start) + "\n")

        output.write("Heap sort running time\n")
        start = timeit.default_timer()
        heapSort(unordered)
        stop = timeit.default_timer()
        output.write("unordered: " + str(stop - start) + "\n")
        start = timeit.default_timer()
        heapSort(ordered)
        stop = timeit.default_timer()
        output.write("ordered: " + str(stop - start) + "\n")

        output.write("Merge sort running time\n")
        start = timeit.default_timer()
        mergeSort(unordered)
        stop = timeit.default_timer()
        output.write("unordered: " + str(stop - start) + "\n")
        start = timeit.default_timer()
        mergeSort(ordered)
        stop = timeit.default_timer()
        output.write("ordered: " + str(stop - start) + "\n")
        output.write("\n\n\n")

if (__name__ == "__main__"):
    main()