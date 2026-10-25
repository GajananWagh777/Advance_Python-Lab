import csv

student = [
    ["Hello I am Gajanan"],
    ["mit adt"],
    ["cse department"]
]

# Write data to CSV file
with open("student.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(student)
    

print("New file created: Hello1.txt")

# Read data from CSV file
with open("student.csv", "r") as file:
    lines = file.readlines()
print(lines)

# Print each line without \n
for line in lines:
    print(line.strip())
  
