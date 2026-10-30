#creating lists
myList = [1,2,3,4,5]
print(myList)

list3 =[]
print(list3)

#lists can store different data types
list2 = ["Orange","Banana", 5, True]
print(list2)

#accessing an item using its index
item = myList[1]
print(item)

#looping through a list
for i in myList:
    print(i)

#checking if an item exists in a list
if "Banana" in list2:
    print("Yes")
else:
    print("No")

#finding the number of items
print(len(myList))

#adding an item at the end
list2.append("lemon")
print(list2)

#inserting an item at a specific index
myList.insert(1,56)
print(myList)
