print("1 --------------------------------------------------")

name = input('Hello, what is your name? ')
print(f'Hello, {name}. It is good to meet you.')

print("2 --------------------------------------------------")

# Prompting the user to enter a temperature in Celsius
celsius = float(input("Enter a temperature in Celsius: "))
# Converting Celsius to Fahrenheit
fahrenheit = (celsius * 9/5) + 32
# Displaying the temperature in Fahrenheit
print(f"{celsius}°C is equivalent to {fahrenheit}°F.")

print("3 --------------------------------------------------")

students = int(input('How many students? '))
group_size = int(input('Required group size? '))

num_groups = students // group_size
left_over = students % group_size

print(f"There will be {num_groups} groups with {left_over} students left over.")

print("4 --------------------------------------------------")

