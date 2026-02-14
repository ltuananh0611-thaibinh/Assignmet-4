numbers = []

while True:
    user_input = input("Enter a number (press Enter to quit): ")

    if user_input == "":
        break

    try:
        number = float(user_input)
        numbers.append(number)
    except ValueError:
        print("Please enter a valid number!")

numbers.sort(reverse=True)

print("\nFive greatest numbers:")
for num in numbers[:5]:
    print(num)
