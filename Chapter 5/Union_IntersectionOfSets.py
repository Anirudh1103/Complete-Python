Table_0f_2 = {2,4,6,8,10,12,14,16,18,20}
Table_of_3 = {3,6,9,12,15,18,21,24,27,30}

#Union: Union operation will consider all the elements from the two sets and returns a single set.
#If there ais a an element common in both the sets it will consider the element only once
print("Union: ", Table_0f_2.union(Table_of_3))

#Intersection: Intersection operation will consider the common elements of set 1 which are in set 2
print("Intersection: ",Table_0f_2.intersection(Table_of_3))