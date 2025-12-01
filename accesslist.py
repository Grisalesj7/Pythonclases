#Change List
mylist = ['apple', 'banana', 'cherry']
mylist[0] = 'kiwi'
print(mylist[1])

#Access List
mylist = ['apple', 'banana', 'cherry']
print(mylist[-1])

#Add list
mylist = ['apple', 'banana', 'cherry']
mylist.insert(0, 'orange')
print(mylist[1])

#Remove list
mylist = ["apple", "banana", "cherry"]
del mylist[0]
print(mylist)

#Loop List
mylist = ["apple", "banana", "cherry"]
i = 0
while i < len(mylist):
  print(mylist[i])
  i = i + 1

#list
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

#Sort list
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

#Copy list
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

#Join list
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

