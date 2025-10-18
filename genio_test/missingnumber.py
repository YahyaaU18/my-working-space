num_list = [1, 2, 3, 4, 5]

missing_list = [1, 2, 3, 5]

for num in num_list:
    if num not in missing_list:
        missing_number = num
        break

print(f"The missing number is: {missing_number}")