# Exercise 1 Skills list

skills = ["Python", "SQL", "Git"]

for i, skill in enumerate(skills):
    print(f"{i + 1}: {skill}")

skills.append("Docker")
print(skills)

# Exercise 2 Employee record

employee = {"name": "Tony", "role": "Junior data engineer", "salary": 32000}

print(f"{employee["name"]} is a {employee["role"]} earing {employee["salary"]}")

employee["salary"] = employee["salary"] * 1.1
employee["Years of experience"] = 1

for key, value in employee.items():
    print(f"{key}: {value}")


# Exercise 3 Team of employees

employees = [{"name": "Tony", "salary": 32000},
             {"name": "Sara", "salary": 75000},
             {"name": "Edward", "salary": 120000}
]

for person in employees:
    if person["salary"] >= 100000:
        print(f"{person["name"]}: high earner")
    elif person["salary"] >= 50000:
        print(f"{person["name"]}: mid range")
    else:
        print(f"{person["name"]}: entry level")