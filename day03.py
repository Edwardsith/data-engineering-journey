# Exercise 1

# number = int(input("Enter a number: "))

# for i in range(1, 11):
#     print(f"{number} x {i} = {number * i}")

# Exercise 2
# salaries = [32000, 75000, 120000, 45000, 98000]
# total = 0

# for i in salaries:
#     total = total + i

#     print(f"The total is: {total}")

secret_code = 42
guess = 0

while guess != secret_code:
    guess = int(input("Guess: "))
    if guess > secret_code:
        print("Too high")
    elif guess < secret_code:
        print("Too low")
    else:
        print("Correct!")
        break
