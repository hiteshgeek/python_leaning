

with open("file1.txt") as f1:
    numbers1 = [int(num) for num in f1.read().splitlines()]


with open("file2.txt") as f2:
    numbers2 = [int(num) for num in f2.read().splitlines()]
    
result = [n for n in numbers1 if n in numbers2]


print(result)