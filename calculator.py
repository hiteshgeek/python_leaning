def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def devide(x,y):
    return x/y

operations = {
    "+" : add,
    "-": subtract,
    "*" : multiply,
    "/" : devide
}

choice = input("Choose operation [+,-,*,/] : ")

number1 = input("Enter number 1 : ")
number2 = input("Enter number 2 : ")

number1 = float(number1)
number2 = float(number2)

result = operations[choice](number1, number2)

print(f"Result is : {result}")