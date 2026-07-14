# Exercise 1 

def calculate_raise(salary, percent):
    return salary * (1 + percent/100)

print(calculate_raise(32000, 10))
print(calculate_raise(75000, 5))

# Exercise 2

def classify_salary(salary):
    if salary >= 100000:
        return "high earner"
    elif salary >= 50000:
        return "mid level"
    else:
        return "entry level"
    
employees = [{"name": "Tony", "salary": 32000},
             {"name": "Sara", "salary": 75000},
             {"name": "Edward", "salary": 120000}
]

for person in employees:
    range = classify_salary(person["salary"])
    print(f"{person["name"]}: {range}")


# Exercise 3

def extract_data():
    return [
        {"name": "Tony", "salary": 32000},
        {"name": "Sara", "salary": 75000},
        {"name": "Edward", "salary": 120000}
    ]

def transform_data(employees):
    total = 0
    for person in employees:
        total = total + person["salary"]
    return total 

def load_data(total):
    print(f"Total payroll: {total}")



