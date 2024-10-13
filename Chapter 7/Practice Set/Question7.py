# 7. Write a program to print the following star pattern.
#   *
#  ***
# ***** 
# for n = 3
n = 4
count = 1
spaces = n-1
for i in range(1,n+1):
    print(" "*(n-i),"*" * count)
    count += 2
    
