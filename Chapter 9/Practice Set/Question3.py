# 3. Write a program to generate multiplication tables from 2 to 20 and write it to the
# different files. Place these files in a folder for a 13 – year old.
import os
def generateMultiplicationTables(n):
    s = ""
    for i in range(1, 11):
        s+=(f"{n} X {i} = {n*i}\n")
    return s

def saveFile(fileName,table):
    with open(f"tables/table{fileName}.txt", "w") as f:
        f.write(generateMultiplicationTables(table))
for i in range(2,21):
    table = generateMultiplicationTables(i)
    saveFile(f"{i}",table)