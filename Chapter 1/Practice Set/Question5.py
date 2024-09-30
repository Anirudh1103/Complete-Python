#write a python program to print the contents of a directory using OS module 
import os
directory_path = 'D:\Programs\Python 2024\Chapter 1\Practice Set'
contents = os.listdir(directory_path)
for item in contents:
    print(item)