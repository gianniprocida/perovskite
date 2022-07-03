#Return a list with the n smallest elements from the dataset defined by iterable
import heapq
def smallestvalues(iterable):
    return heapq.nsmallest(3,iterable)


#Return a list with the n smallest elements from the dataset defined by iterable
def largestvalues(iterable):
    return heapq.nlargest(3,iterable)

def strtofloat(iterable):
    return [float(i) for i in iterable]

# Concatenate lists of lists 
def concatenate_lists(iterable1,iterable2):
    conc=[]
    for i in range(len(iterable1)):
        for j in range(len(iterable2)):
            if i!=j:
                continue
            if i==j:
                conc.append(iterable1[i]+iterable2[j])
    return conc

