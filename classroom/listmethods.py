alist = [45,78,21,68,29,43]
print(type(alist))

# slicing
print(alist[0])
print(alist[0:4])

# methods
# list.append(value) -- adding value at the end of the list
alist.append(92)
print("after appending:",alist)

# list.extend(list) - adding multipel values(list) at the end of the list 
alist.extend([53,27,49])
print("after extending :",alist)


#list.insert(where to insert,what to insert)
#list.insert(index,value)
alist.insert(1,200)
print("After inserting :",alist)

######## remove elments# 
# value should exist to remove from list
alist.remove(45)
print("AFter removing :",alist)

if 53 in alist:
    alist.remove(53)
else:
    print("not found")


# reversing values
alist.reverse()
print("After reversing :",alist)


# sorting in ascending
alist.sort()
print("After sorting ",alist)
alist.sort(reverse=True)  # soring in descending order
print("Descending order:",alist)












alist = [10,10,30,40,50,60,10,10,10,50,60]

firstpart = alist[:4]
secondpart = alist[4:]

# remove dups only from second part 
uniquesecondpart = []
for item in secondpart:
    if item not in uniquesecondpart:
        uniquesecondpart.append(item)

#final list
result = firstpart + secondpart
print(result)