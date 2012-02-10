import random
import math
import timeit

def combsort(test_comb_temp): #Improvement of bubble sort via the use of a wider "gap" between compared elements (ie compares the 1st and 8th term as opposed to first and second term in bubblesort; gap is shrunk over time; this method eliminates "turtles" ie small values at end of set by quickly bringing them to beginning as opposed to through a series of single comparisons. This method becomes bubble sort over time. Speed is O n log n
	gap = len(test_comb_temp)
	swaps = True 
	while gap > 1 or swaps: #when gap becomes 1, the program is essentially the same as a bubble sort
		gap = max(1, int(gap / 1.3)) #recommended gap size of about 1.3 as most efficient; this command sets the max to be the greatest integer of size of previous gap/ 1.3, or 1. 
		swaps = False
		for i in range(len(test_comb_temp) - gap): #sets examination space to begin comparing first and gap-length element
			j = i+gap #this for loop tells the program to examine two numbers in list separated by gap size
			if test_comb_temp[i] > test_comb_temp[j]: #comparison and swap components
				test_comb_temp[i], test_comb_temp[j] = test_comb_temp[j], test_comb_temp[i]
				swaps = True
	return test_comb_temp
	
	
	
def stoogesort(test_stooge_temp, i=0, j=None): #stooge sort is an O n^2.7 method that was deliberately designed to be inefficient by  
	if j is None:
		j = len(test_stooge_temp) - 1
	if test_stooge_temp[j] < test_stooge_temp[i]: 
		test_stooge_temp[i], test_stooge_temp[j] = test_stooge_temp[j], test_stooge_temp[i] #swaps items
	if j - i > 1:
		t = (j - i + 1) // 3
		stoogesort(test_stooge_temp, i  , j-t)  #sorts first 2/3 of list
		stoogesort(test_stooge_temp, i+t, j  ) #sorts second 2/3
		stoogesort(test_stooge_temp, i  , j-t) #sorts first 2/3 of list again
	return test_stooge_temp

def quicksort(test_quick_temp): #quick sort algorithm selects a "pivot" point and divides list by that point sub
	if test_quick_temp == []: 
		return []
	else:
		pivot = test_quick_temp[0]
		lesser = quicksort([x for x in test_quick_temp[1:] if x < pivot])
		greater = quicksort([x for x in test_quick_temp[1:] if x >= pivot])
		test_quick_temp= lesser + [pivot] + greater
		return test_quick_temp
