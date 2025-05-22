# 2. Write a function that will take a list and return sum of all numbers in the list.

def sum_list(numbers: list) -> int:
    total = 0
    for num in numbers:
        total += num
    return total

result = sum_list([10, 11, 12, 13, 14, 15])     # calling function and assigning return value to result
print(result)