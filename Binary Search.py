import math
import random

def BinarySearch(List,searchItem,Index):
    
    if len(List) == 0: #Catches index out of range errors for search items above or below the range of numbers in the list
        return ("Not in list")

    midpoint = math.floor((len(List)-1)/2) #-1 deals with python arrays starting from 0
    itemValue = List[midpoint]


    if itemValue == searchItem:
        Index += midpoint
        return (Index)

    elif itemValue != searchItem and len(List) == 1:
        return ("Not in list")

    elif itemValue < searchItem:
        Index += midpoint+1 # +1 deals with python lists counting from 0        
        return (BinarySearch(List[midpoint + 1: len(List)],searchItem,Index)) #Uses list slicing to remove the first half of the list
    
    elif itemValue > searchItem:
        return (BinarySearch(List[0:midpoint],searchItem,Index)) #Uses list slicing to remove the second half of the list

def SortedNumListGenerator(NoLoop,MaxRandNumber):
    
    def Quicksort (Sequence):
        #Lists  to append to
        SmallerThanPivot = []
        LargerThanPivot = []
        EqualToPivot = []
        
        if len(Sequence) <= 1: #End case for recursion, no more values to sort
            return(Sequence) #Ends recursion
        else:
            pivot = Sequence.pop(random.randint(0,len(Sequence)-1)) #Selects pivot randomly and removes it from the list (Would be better to use median of three)

            for i in Sequence: 
                
                if i > pivot: #Uses if statements to seperate smaller than pivot/equal to pivot and larger than pivot into different lists
                    LargerThanPivot.append(i)
                
                elif i < pivot:
                    SmallerThanPivot.append(i)
                
                elif i == pivot:
                    EqualToPivot.append(i)
            
            return (Quicksort(SmallerThanPivot) + [pivot] + EqualToPivot + Quicksort(LargerThanPivot)) #Uses recursion to do quicksort on the seperated lists
        
    Sequence = []

    for i in range(0,NoLoop):
        Sequence.append(random.randint(0,MaxRandNumber))
    
    Sequence = Quicksort(Sequence) #Sorts randomly generated list
    return Sequence
    

Sequence = SortedNumListGenerator(100,100)
print(Sequence)
searchItem = float(input("Enter the search item "))

print(BinarySearch(Sequence,searchItem,0))