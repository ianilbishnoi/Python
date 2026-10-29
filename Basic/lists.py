# LISTS
dogs=["roger","Syd", True] # a list can store different types of values

print("roger" in dogs) # checks if roger is present

# accessing items using index
print(dogs[2])

dogs[2]="Beau" # changing the value at index 2
dogs.append("judah") # adds one item at the end
dogs.extend(["judah",5]) # adds multiple items from another list
dogs+= ["Judah", 5] # another way to add items

print(dogs)

# accessing items from the list
print(dogs[-1]) # gets the last item
print(dogs[2:4]) # gets items from index 2 up to 3
print(dogs[-2:]) # gets the last two items
print(dogs[:3]) # gets items from the beginning up to index 2

print(len(dogs)) # counts the items in the list

dogs.remove("judah") # removes the first matching item
print(dogs)

dogs.insert(0,"Niko") # adds Niko at index 0
dogs[1:1]=["Test1","Test2"] # inserts two items at index 1

print(dogs)

dogs.sort() # sorts the list in place
print(dogs)

# sorted() returns a sorted list without changing the original

# list comprehension
nums = [1,2,3,4,5]

nums_power_2 =[n**2 for n in nums] # squares each number in the list
print(nums_power_2)
