#7. Write a python function to remove a given word from a list ad strip it at the same time.
def rmWord(word,lst):
    lst.remove(word)
    print(lst)
    
lst = ["apple", "banana", "cherry", "date", "elderberry"]
rmWord("banana",lst)
