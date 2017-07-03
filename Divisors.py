'''

Create a program that asks the user for a number and then prints 
out a list of all the divisors of that number.
 (If you don’t know what a divisor is, it is a number that divides evenly into another number. 
 For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
 
Created on Jul 1, 2017

@author: shikhadubey
'''

number= int(input("Please choose a number to divide: "))
listdivisor= list(range(1, number+1))
divisorlist= []  #defines an empty list, {} is an dictionary

for i in listdivisor: 
    if number%i== 0: 
        divisorlist.append(i)
        
print("The list of divisors are :"), divisorlist


''' 
To create a list of numbers from 2 to 10, just use the following code:

  x = range(2, 11)
Then the variable x will contain the list [2, 3, 4, 5, 6, 7, 8, 9, 10].
 Note that the second number in the range() function is not included in the original list.
 Loop can also be used to create the list
 '''
