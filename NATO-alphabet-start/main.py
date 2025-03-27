student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
import csv
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
with open("nato_phonetic_alphabet.csv", "r") as file:
    reader = csv.DictReader(file)
    nato_dict = {row["letter"].split():row["code"].split() for row in reader}


name = input("     ")


list_phoenic = [nato_dict[letter] for letter in name if letter in nato_dict]

