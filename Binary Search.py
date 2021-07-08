import math

def BinarySearch(List,searchItem,Index):
    midpoint = (len(List)-1)/2
    midpoint = (int(math.ceil(midpoint))) #math.ceil is used instead of round() as decimals with .5 round down with round()
    itemValue = List[midpoint]
    
    #print(List) #Debugging
    #print("Start Index: " + str(Index)) #Debugging
    #print("Midpoint: " + str(midpoint)) #Debugging
    #print("Item Value: " + str(itemValue)) #Debugging
    
    if itemValue == searchItem:
        Index += midpoint
        return (Index)

    elif itemValue != searchItem and len(List) == 1:
        return ("Not in list")

    elif itemValue < searchItem:
        Index += midpoint+1 # +1 deals with python lists counting from 0
        
        #print("Large - alteredIndex: " + str(Index)) #Debugging
        
        return (BinarySearch(List[midpoint + 1: len(List)],searchItem,Index))
    
    elif itemValue > searchItem:
        return (BinarySearch(List[0:midpoint],searchItem,Index))

Sequence = [
2,
3,
4,
5,
6,
9,
10,
11,
12,
16,
21,
22,
25,
26,
27,
29,
33,
34,
37,
38,
39,
40,
41,
44,
47,
48,
49,
54,
56,
57,
67,
68,
69,
76,
78,
79,
80,
81,
82,
83,
86,
87,
89,
90,
91,
92,
94,
96,
98,
100,
]


searchItem = float(input("Enter the search item "))

print(BinarySearch(Sequence,searchItem,0))