# for methods and functions .     . we use ()     Eg. print()   range()   str.upper()
# for indexing and accessing keys.. we use []     Eg. name[0]     alist[0]    book["chap1"]



book = { "chap1":10 , "chap2":20 ,"chap3":30 ,"chap1":1000 }
print(book)
# display individual value
print(book["chap1"]) # 10
print(book["chap2"]) # 20

if "chap100" in book:
    print(book["chap100"])

# create new key-value pairs
book["chap4"] = 40
book["chap5"] = 50
book["chap6"] = 60
print(book)

# display keys
print(book.keys()) 

# display values
print(book.values())

# display key-value pairts
print(book.items())



# delete key-value pair
book.pop("chap1") #chap1-10 will be remoed from dictionary
print("After pop operation :", book)

# delete random key-value
book.popitem()
print("After popitem operation :", book)
book.popitem()
print("After popitem operation :", book)
book.popitem()
print("After popitem operation :", book)


# combinee 2 dictionaries
book = {"chap1":10 ,"chap2":20}
newbook = {"chap3":30 ,"chap4":40}
finalbook = { **book ,**newbook}
print(finalbook)

book = { "chap1":10 , "chap2":20 ,"chap3":30 ,"chap1":1000 }
to_be_removed = ["chap1","chap2"]
for key in to_be_removed:
    book.pop(key)

print("after removing key-values :", book)


book = { "chap1":10 , "chap2":20 ,"chap3":30 ,"chap1":1000 }
# display keys
for key in book.keys():
    print(key)

for key in book:     # explicitly defining keys is not required
    print(key)

# dipslay values
for v in book.values():
    print(v)

# display key-value pairs
for key,value in book.items():
    print(key,value)

# validation
if "chap1" in book:
    print("key exists...!!!")