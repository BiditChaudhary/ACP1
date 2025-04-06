name = input("Enter student name: ")
intro = input("Enter their introduction (like fav subject): ")

filename = "Student_data.txt"

f = open(filename, "r")
lines = f.readlines()
f.close()

lines = [f"{name}: {intro}\n" if line.startswith(name + ":") else line for line in lines]

if not any(line.startswith(name + ":") for line in lines):
    lines.append(f"{name}: {intro}\n")

f = open(filename, "w")
f.writelines(lines)
f.close()

print("Student info updated successfully!")