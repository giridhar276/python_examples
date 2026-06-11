#-17                                                -9    -8     -7   -6   -5    -4   -3     -2   -1
# p    y    t     h     o     n        p     r      o     g      r     a     m    m     i      n    g
# 0    1    2      3    4     5   6    7    8      9      10     11    12    13   14    15    16   17 

# string[start:stop:step]
name = "python programming"
# slicing
print(name[0])  #p
print(name[1])  # y
print(name[0:4])    #pyth
print(name[9:11])   #og
print(name[0:18])   # python programming
print(name[0:18:1]) # python programming
print(name[:])      # python programming
print(name[::])      # python programming
print(name[0:18:2])  #pto rgamn
print(name[-1])      #g
print(name[::-1])
print(name[-4:-1])
print(name[:-1])
print(name[-5:-3])
print(name[-1:-18:-2])



# string methods - string is immutable 
name = "python programming"
print(name.capitalize())
print(name.isupper())   # str.isupper() is just to validate
print(name.upper())     # str.upper() is used to display in upper
print(name)
print(name.islower())
print(name.lower())
print(name.startswith('p'))
print(name.startswith("z"))
print(name.endswith("m"))
print(name.endswith("g"))
print(name.count("p")) #2
print(name.replace("python","java"))  #java programming
print(name.isalpha())
print(name.isalnum())

print(name.title())
aname = "I love {} and {}" # template
print(aname.format("Bangalore","Hyderabad"))
print(aname.format("python","java"))
print(aname.format(1,2))
aname = " python     "
print(len(aname)) #12
print(aname.strip()) # remove whitespaces at both ends
print(len(aname.strip()))
print(len(aname.lstrip()))
print(len(aname.rstrip()))


# conditions 
if 1 < 2 :
    print("true")

# simple if
name  = "python programming"
if name.islower():
    print("string is lower")
    print("inside if")
    print("still inside if")

######## if-else
if name.startswith("p") :
    print("its python")
else:
    print("its someother language")

########## nested if 
name = input("Enter any language:")  
if name == "python":
    print("its python")
elif name == "java":
    print("its java")
elif name == "unix":
    print("its unix")
else:
    print("its tool based")

name = "python programming"
if len(name) == 18:
    print("its python programming")
else:
    print("its python")

if name.count('p') > 1:
    print("python programming")
else:
    print("python")

print("length of the string is " , len(name))


# for loop
# range(start,stop,step)
for val in range(1,10): # ascending order
    print(val)

for val in range(10,1,-1): # descending roeder
    print(val)

name = "python"
for char in name:
    print(char, end = " ")
print()
# display string in reverse order
for char in name[::-1]:
    print(char)


print(1,2) # 1 2
print(help(print))


#























# object - syntax
# object - slicing
# object - methods
# object - conditions 
# object - for loop