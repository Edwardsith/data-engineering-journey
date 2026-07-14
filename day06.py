# Exercise 1 - WRITING SKILLS TO A FILE

skills = ["Python", "SQL", "Git", "Docker"]

with open("skills.txt", "w") as file:
    for skill in skills:
        file.write(f"{skill}\n")

# Exercise 2 - READING IT BACK AND COUNTING LINES

def count_lines(filename):
    count = 0
    with open(filename, "r") as file:
        for line in file:
            count = count + 1
    return count

print(count_lines("skills.txt"))

# Exercise 3 - SAFE FILE READING

def read_file_safely(filename):
    try:
        with open(filename, "r") as file:
            print(file.read())
    except FileNotFoundError:
        print(f"{filename} not found")

read_file_safely("skills.txt")
read_file_safely("missing.txt")

