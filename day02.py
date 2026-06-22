score = 99

if score >= 80:
    print("Distinction")
elif score >= 60:
    print("Pass")
elif score >=40:
    print("Average")
else:
    print("Fail")


salaries = [32000, 55000, 41000, 28000, 67000, 39000]
count = 0

for salary in salaries:
    if salary > 40000:
        print(f"{salary} - above average")
        count = count + 1
    else:
        print(f"{salary} - below average")

print(f"above average count: {count}")


for i in range(1, 11):
    print(f"7 x {i} = {i*7}")
