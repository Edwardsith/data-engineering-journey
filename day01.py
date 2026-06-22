name = "Edward"
age = 30
rate = 150.00
print(f"Hi, my name is {name}. I am {age} years old, and my hourly rate is {rate}.")

hours_worked = 45
hourly_rate = 150.00

if hours_worked > 40: 
    print(f"Total pay: {(40*hourly_rate)+((hours_worked-40)*hourly_rate*1.5)}")
else: 
    print(f"Total pay: {(hours_worked*hourly_rate)}")

