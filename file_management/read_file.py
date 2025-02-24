#file = open('names.txt')
with open('names.txt', mode='r') as file:
    content = file.read()
    print(f"{content}")
    # file.write("Hitesh\n")
    # file.write("Monali\n")
    # file.write("Abhimanyu\n")
    #file.close()