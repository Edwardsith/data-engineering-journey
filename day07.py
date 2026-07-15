employees = [
    {"name": "Tony", "salary": 32000},
    {"name": "Sara", "salary": 75000},
    {"name": "Edward", "salary": 120000},
    {"name": "Naledi", "salary": 45000},
    {"name": "Micheal", "salary": 98000}
    ]

def classify_salary(salary):
        if salary >= 100000:
            return "High earner"
        elif salary >= 50000:
            return "Mid range"
        else:
            return "Entry level"

def build_report(employees):
    report_lines = []
    for person in employees:
        label = classify_salary(person["salary"])
        line = f"{person["name"]}: R{person["salary"]} ({label})"
        report_lines.append(line)
    return report_lines

report = build_report(employees)

with open("report.txt", "w") as file:
    for line in report:
        file.write(f"{line}\n")

def read_file_safely(filename):
    try:
        with open(filename, "r") as file:
            print(file.read())

    except FileNotFoundError:
        print(f"{filename} not found.")


read_file_safely("report.txt")



    
     