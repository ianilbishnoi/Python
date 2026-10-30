#dictionary stores data as key-value pairs and is mutable
dict={"name":"Max","age":28,"city":"London"}
print(dict)

value= dict["city"]#gets the value of city
print(value)

dict["email"]="coolmax@xyz.com"#adds a new key-value pair
print(dict)

#pop() removes an item using its key
#popitem() removes the last inserted item

if "name" in dict:
     print(dict["name"])

#exception handling
try :
     print(dict["name"])
except:
    print("error")

for key, value in dict.items():#loops through each key-value pair
    print(key,value)

dict_cpy= dict#both variables refer to the same dictionary
print(dict_cpy)

dict_cpy["name"]="Daisy"
print(dict_cpy)
print(dict)#the original dictionary also changes

dict1 = {"name":"Max","age":28,"city":"London"}
dict2 = {"name":"Madiline","age":32,"city":"Berlin"}

dict1.update(dict2)#updates dict1 with values from dict2
print(dict1)

#numbers and tuples can be dictionary keys, but lists cannot
