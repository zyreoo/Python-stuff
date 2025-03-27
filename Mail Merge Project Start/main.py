

with open("Input/Names/invited_names.txt", "r") as file:
    names_list = file.read().splitlines()


word_to_replcae = "[nume]"

for name in names_list:
    with open("Input/Letters/starting_letter.txt", "r") as file:
        place_holder = file.read()


    updated_content = place_holder.replace(word_to_replcae, name)

    with open(f"Input/Letters/starting_letter_{name}.txt", "w") as file:
        file.write(updated_content)

    

