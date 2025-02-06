is_programmer = True

dictionary = {
    "name" : "Hitesh",
    "city" : "Bengaluru",
    "country" : "INDIA",
    123: "named key",
    is_programmer: "variable key"
}

# print(dictionary)
# print(dictionary["name"])
# print(dictionary[123])
# print(dictionary[True])
# print(dictionary["ads"]) #key error

#get keys
print("-----------------------")
print(f"keys : {dictionary.keys()}")

print("-----------------------")
for x in dictionary.keys():
    print(f"Key {x} = Value {dictionary[x]}")

#get values
print("-----------------------")
print(f"values : {dictionary.values()}")

print("-----------------------")
for x in dictionary.values():
    print(f"Value {x}")

#both key and values
print("-----------------------")
print(f"items : {dictionary.items()}")

print("-----------------------")
for key, value in dictionary.items():
    print(f"{key} = {value}")


#length of the dictionary
print("-----------------------")
print(f"length of dictionary : {len(dictionary)}")
#iterate dictionary
print("-----------------------")
for x in dictionary:
    print(x)

print("-----------------------")
fruits = {"orange" : 4, "apple": 2, "banana" : 10}

print(f"Max fruits : {max(fruits, key=fruits.get)}")
print(f"Min fruits : {min(fruits, key=fruits.get)}")

