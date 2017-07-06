'''
Ask the user for a string and print out whether this string is a palindrome or not
The str() function converts values to a string form so they can be combined with other strings.
Created on Jul 5, 2017

@author: shikhadubey

'''

inp= raw_input("Enter a word!")
#inp= str(inp)
rev= inp[::-1]

print(rev)
if rev== inp:
    print ("Yayy! Palindrome")
else:
    print("Not a palindrome...")



'''
Slice notation "[a:b:c]" means "count in increments of c starting at a inclusive, up to b exclusive". 
If c is negative you count backwards, if omitted it is 1. 
If a is omitted then you start as far as possible in the direction you're counting from
 (so that's the start if c is positive and the end if negative). 
 If b is omitted then you end as far as possible in the direction you're counting to 
 (so that's the end if c is positive and the start if negative). 
If a or b is negative it's an offset from the end (-1 being the last character) instead of the start.
raw_input takes the input as string only so no use to convert the input to string by using str(inp))
inp[0::-1]---> will only give the first letter---> count backwards from index 0 as far as you can
inp[::-1]---> Start from the back (-1) till the end

'''