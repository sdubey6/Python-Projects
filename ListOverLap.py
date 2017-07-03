'''

Take two lists, say for example these two:

    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are common between the lists 
(without duplicates). 
Make sure your program works on two lists of different sizes.
Created on Jul 1, 2017

@author: shikhadubey
'''
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
overlaplist= []
i= len(a)-1

for x in range(0, i):
    if a[x] in b:
        overlaplist.append(a[x])
 
set1= list(set(overlaplist))        
print(set1)  ##It will give this result if you just do print(overlaplist):[1, 1, 2, 3, 5, 8, 13]
''' If you dont want the 1 to come two times?, use the set function...
But if only set(overlaplist) is used, it will give output as set(1,2,3,5 .....)
Therfore, enclose that set is a list again
Reason????
Dont know
'''        