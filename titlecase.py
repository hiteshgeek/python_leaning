def convertToTitleCase(str):
    words = str.split()

    title_case_string = [word[0].upper() + word[1:].lower() if word else '' for word in words]
    return ' '.join(title_case_string)


print(convertToTitleCase("hIteSh VaghelA"))
print(convertToTitleCase("hEllO WoRLD"))
