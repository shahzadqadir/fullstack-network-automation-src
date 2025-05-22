# 3. Write a function that takes a number and returns its factorial

def factorial(number: int) -> int:
    total = 1
    for i in range(number, 0, -1):
        total *= i
    return total

result = factorial(10)
print(result)

"""
Explaination: 
We are using range in reverse order by specifing step to -1, we start from number provided and multiply it with total which is initalized as 1
We keep doing it and decreasing number by 1 until we reach 1 as 0 is not included (end is not included).
"""