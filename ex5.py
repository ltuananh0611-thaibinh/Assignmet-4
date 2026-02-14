def remove_uneven(numbers):
    even_numbers = []
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers

original_list = [67, 99, 456, 21, 60, 66, 77, 88]
new_list = remove_uneven(original_list)

print("Original list:", original_list)
print("Even numbers list:", new_list)
