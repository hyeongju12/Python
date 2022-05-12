#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp




with open("./Input/Letters/starting_letter.txt", 'r') as letter_file:
    letter = letter_file.readlines()

with open("./Input/Names/invited_names.txt", 'r') as name_file:
    names = name_file.readlines()

for name in names:
    for line in letter:
        line = line.replace("[name]", name)
        line = line.replace("\n", "")
        with open(f"./Output/ReadyToSend/{name}.txt", 'a') as file:
            file.write(line+'\n')

