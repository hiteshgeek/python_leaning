sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# result = [len(n) for n in sentence.split(" ")]
result = {n:len(n) for n in sentence.split(" ")}
print(result)

