import math

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

    elif StringComparison(searchItem,itemValue) == True:
        Index += midpoint+1 # +1 deals with python lists counting from 0        
        return (BinarySearch(List[midpoint + 1: len(List)],searchItem,Index)) #Uses list slicing to remove the first half of the list
    
    elif StringComparison(searchItem,itemValue) == False:
        return (BinarySearch(List[0:midpoint],searchItem,Index)) #Uses list slicing to remove the second half of the list

def StringComparison(Item1, Item2):
    def CompareinLoop(SmallerItem):
        for i in range(0,len(SmallerItem)):
            if Item1[i] > Item2[i]:
                return True
            if Item1[i] < Item2[i]:
                return False
        return False
    
    def StringToListToAscii(String):
        List = list(String)
        for i in range(0,len(List)):
            List[i] = ord(List[i])
        return List
    
    Item1 = StringToListToAscii(Item1)
    Item2 = StringToListToAscii(Item2)
    if len(Item1) >= len(Item2):
        return CompareinLoop(Item2)
    else:
        return CompareinLoop(Item1)



List = ["Ali", "Bob", "Canver", "David", "Eve", "Frankenstein", "Gobble", "Harvard", "Ivan", "Jacob","Jen","Ken", "Larry","Parminder","Yvonne","Zendaya"]

print(List)
Item = input("Enter the search item ")

print(BinarySearch(List,Item,0))

