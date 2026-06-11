
aset = {10,10,20,20,20,30,30,30}
print(aset)

bset = {30,30,30,30,40,40,40,50}
print(bset)

# add value to set
aset.add(10)
print(aset)
aset.add(40)
print(aset)

# union
print(aset.union(bset)) # {10,20,30,40,50}

#intersection
print(aset.intersection(bset)) # {30}

#difference
print(aset.difference(bset))  # {10,20,30} - {30,40,50} = {10,20}