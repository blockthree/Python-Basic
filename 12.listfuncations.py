
names = ["iyappan","deepak","vel","hari","prakash","gokul"]
print(names)
print(id(names))
print(names[0])
print(names[-1])
print(names[2:])
print(names[:3])
names.append("sarathi")
print(names)
v = names.count("iyappan")
print(v)
names.remove("iyappan")
print(names) #iyappan re
names.pop(1)
print(names) #vel index
names.insert(0,"iyappan")
print(names)
names.reverse()
print(names)

names.sort()
print(names)

names.clear()
print(names)