#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()
    # print(names)

with open("./Input/Letters/starting_letter.txt") as invitation_letter:
    letter_content = invitation_letter.read()
    for name in names:
        striped_name = name.strip()
        new_letter = letter_content.replace(PLACEHOLDER, striped_name)
        with open(f"./Output/ReadyToSend/letter_for_{striped_name}.txt", mode="w") as output_file:
            output_file.write(new_letter)