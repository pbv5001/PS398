import csv
import random
import math
import pvhw3
import time

test=[]
sample=[]
test_stooge=[]
test_comb=[]
test_quick=[]
start=[]
stooge_times=[]
comb_times=[]
quick_times=[]
test_stooge_temp=[]
test_quick_temp=[]
test_comb_temp=[]


#Choose specified random samples of specified size ranging from integers 0 to 1000


def random_ints(samples, sizes, lower=0, upper=999):
	for x in range(10, sizes): #picks numbers of samples
		for y in range(0, samples):
			test= [random.randrange(lower,upper+1) for i in range(x)] #pick a sample of size sizes for each sample in samples
			sample.append([test])
		




"""
#quick test of program; these seem to work		

random_ints(5,15) #5 lists of 10 to 15 integers 1-999 to test if sorting functions work
print sample

#create three identical lists of samples for testing

test_stooge=sample
test_comb=sample
test_quick=sample

for item in test_stooge:
	pvhw3.stoogesort(test_stooge[item])
print test_stooge
	
for item in test_comb:	
	pvhw3.combsort(test_comb[item])
print test_comb
	
for item in test_quick:
	pvhw3.quicksort(test_quick[item])
print test_quick


#collect times
"""


random_ints(1,999)
	
test_stooge=sample 
test_comb=sample
test_quick=sample


for x in range(0,999):
	test_stooge_temp= test_stooge[x]
	start= time.clock()
	pvhw3.stoogesort(test_stooge_temp[0])
	stooge_times.append(time.clock()- start)

for x in range(0,999):
	test_comb_temp= test_comb[x]
	start = time.clock()
	pvhw3.combsort(test_comb_temp[0])
	comb_times.append(time.clock()- start)
	

for x in range(0,999):
	test_quick_temp=test_quick[x]
	start = time.clock()
	pvhw3.quicksort(test_quick_temp[0])
	quick_times.append(time.clock()- start)	

	
#print times to CSV	
csvWriter = csv.writer(open('times.csv', 'wb'))

for i in range(0,999):
  csvWriter.writerow([stooge_times[i], comb_times[i], quick_times[i]])


