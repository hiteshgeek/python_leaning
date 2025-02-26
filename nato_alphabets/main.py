import pandas 

data = pandas.read_csv("nato_phonetic_alphabet.csv")

data_dict = {row.letter:row.code for index,row in data.iterrows()}

print(data_dict)