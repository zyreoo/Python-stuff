
import random

name  = "Simone" 

new_list = [letter for letter in name]



new_range = [n*2 for n in range(1,5)]



names = ["caroline", "eleanor", "david"]


new_names = [name.upper() for name in names]

print(new_names)

list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
numbers = [int(string) for string in list_of_strings]
print(numbers)

result = []
with open("fisier1.txt", "r") as file:
        data = file.read().split()
        list_data = list(map(int, data)) 
with open("fisier2.txt", "r") as file:
        data2 = file.read().split()
        list_data2 = list(map(int, data2))  


result = [num for num in list_data if num in list_data2]

student_1 = {student:random.randint(1,100) for student in names}


student_dict = {student:score for (student, score) in student_1.items() if score >= 50}


print(student_dict)
print(student_1)


weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}

weather_f = {day:(temperature *9/5)+32 for (day, temperature) in weather_c.items()}

print(weather_f)