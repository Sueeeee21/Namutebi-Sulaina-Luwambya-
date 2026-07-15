# Mode                Meaning
# r                   read
# w                   write
# a                   append
# x                   create a new file
# rb                  read in binary mode
# wb                  write in binary mode
# ab                  append in binary mode

# file = open("student.txt", "r")

# file_content = file.read()
# print(file_content)

# file.close()

# with open("student.txt", "r") as file:
#     data = file.read()

# print(data)

# with open("report.txt", "w") as file:
#     file.write("I love Python programming\n")
#     file.write("I am becoming a data scientist")

# print("File created successfully")

#Open a csv file

import csv

# with open("students.csv", "r") as file:
#     reader = csv.reader(file)

#     for row in reader:
#         print(row)

# with open("students.csv", "a") as file:
#     append = csv.writer(file)
#     append.writerow(["24/U/0939", "Sulaina Namutebi", "Female", 21, "Python Programming", 80])

import json

student = {
    "name": "Sulaina Namutebi",
    "age": "24",
    "course": "Python Programming"
}

with open('student.json', 'w') as file:
    json.dump(student, file, indent=4)