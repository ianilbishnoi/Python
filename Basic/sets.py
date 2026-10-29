#sets
#sets store unique values and don't maintain a fixed order
#sets are mutable, but their elements must be hashable

names={"roger","syd"} # creating a set
names2={"roger", "luna"} #duplicate values are not allowed

intersect = names & names2 #gets the common elements
print(intersect)

mod = names | names2 #combines both sets without duplicates
print(mod)

dif = names-names2 #gets elements present in names but not names2
print(dif)

sup= names >names2 # checks if names is a proper superset of names2
print(sup)

print(list(names)) #converts the set into a list

#sets can be used to find common elements between collections
#duplicate values are removed when converting a collection to a set
