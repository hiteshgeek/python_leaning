# check single charatcer and make new list
fruits = ["Apple", "Mango", "Banana", "Watermelon"]

newlist = [x for x in fruits if 'a' in x]

print(f"Original list : "+", ".join(fruits))
print(f"New list containing 'a' : "+", ".join(newlist))

# check multiple charatcers and make new list
letters = ['a', 'e']

newlist = [x for x in fruits if all(letter in x.lower() for letter in letters)]

print(f"New list containing 'a' 'e': "+", ".join(newlist))

# newlist = [
#     fruit
#     for fruit in fruits 
#     if 'a' in fruit.lower()
#     if 'e' in fruit.lower()
# ]

newlist = [
    fruit
    for fruit in fruits 
    if all( letter in fruit.lower() for letter in letters)
]

print(f"New list containing 'a' 'e' with multiple conditions: "+", ".join(newlist))

numbers = [0,1,2,3,4,5,6,7,8,9]
evens = [num for num in numbers if num % 2 == 0]

print(f"Even numbers : "+", ".join(map(str,evens)))

odds = [num for num in range(0,11) if num%2 == 1]

print(f"Odd numbers : "+", ".join(map(str,odds)))

odds = [num for num in range(5,len(numbers)) if num%2 == 1]

print(f"Odd numbers : "+", ".join(map(str,odds)))

list_from_numbers = list(range(10))

print(f"List from numbers : "+", ".join(map(str,list_from_numbers)))

list_from_comprehention = [i for i in range(10)]

print(f"List from comprehention : "+", ".join(map(str, list_from_comprehention)))

matrix = [[1,2,3], [4,5,6], [7,8,9]]
flattened_list = [
    column 
    for row in matrix
    for column in row
] 

print(f"Flattened list : "+" ".join(map(str,flattened_list)))
