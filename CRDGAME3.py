# cook your dish here
# cook your dish here
# Importing math for ceiling
import math 
# For each one of the test cases
for i in range(int(input())):
    # Split these two numbers
    cc, cr = map(int, input().split())
    # Divide these two by 9 and ceil them.
    ccA = math.ceil(cc/9.0)
    crA = math.ceil(cr/9.0)
    # If chef's is greater than morty's, print 1, followed by morty's.
    # So hence, 28 18 will become 1 and ceil(18/9), hence 1 2
    # The end is to make sure that there is a space between them
    if (ccA >= crA):
        print("1", end=" ")
        print(crA)
    # Similarly, if chef loses, then 14 24 would be 0 ceil(14/9), so 0 2.
    else:
        print("0", end=" ")
        print(ccA)
