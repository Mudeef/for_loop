dict={1:"he",2:"Me",3:"He"}
dict.update({4:"She"})
print(dict)
dict["5"]="I"
print(dict)
dict.pop(1)
print(dict)
dict.popitem()
print()
del dict[2]
print(dict)
dict.clear()
print(dict)
print("=====================================================")

dict={1:"He",2:"She",3:"I"}
for i in dict.items():
    print(i)
for i in dict.keys():
    print(i)
for i in dict.values():
    print(i)