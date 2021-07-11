import math
import random
#To work on alphanumeric text, to compare two values turn strings into array of numbers that relate to the letter and compare the numerical values to find if one value is greater than the other

def BinarySearch(List,searchItem,Index):
    if len(List) == 0:
        return ("Not in list")
    
    midpoint = (len(List)-1)/2
    midpoint = (int(math.ceil(midpoint))) #math.ceil is used instead of round() as decimals with .5 round down with round()
    itemValue = List[midpoint]


    if itemValue == searchItem:
        Index += midpoint
        return (Index)

    elif itemValue != searchItem and len(List) == 1:
        return ("Not in list")

    elif itemValue < searchItem:
        Index += midpoint+1 # +1 deals with python lists counting from 0        
        return (BinarySearch(List[midpoint + 1: len(List)],searchItem,Index))
    
    elif itemValue > searchItem:
        return (BinarySearch(List[0:midpoint],searchItem,Index))

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
                
                if i > pivot: #Uses if statements to seperate smaller than pivot/equal to pivot and larger than pivot into list
                    LargerThanPivot.append(i)
                
                elif i < pivot:
                    SmallerThanPivot.append(i)
                
                elif i == pivot:
                    EqualToPivot.append(i)
            
            return (Quicksort(SmallerThanPivot) + [pivot] + EqualToPivot + Quicksort(LargerThanPivot)) #Uses recursion to do quicksort on the seperated lists
        
    Sequence = []

    for i in range(0,NoLoop):
        Sequence.append(random.randint(0,MaxRandNumber))
    
    Sequence = Quicksort(Sequence)
    return Sequence
    
Sequence = SortedNumListGenerator(100,100)
print(Sequence)
searchItem = float(input("Enter the search item "))

print(BinarySearch(Sequence,searchItem,0))