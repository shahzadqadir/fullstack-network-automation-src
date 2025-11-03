### Conditionals Exercises

1. We have a list of fruits: `fruits=["apple", "banana", "orange", "mango"]`. Ask the user to input the name of a fruit they are looking for. Check if the fruit is in the list. If it is, return the index of the fruit; otherwise, return `-1`.
2. Use the same list as in Question 1. This time, if you can't find the fruit in the list, **add it to the list** and print `"fruit not found but added now"`.
3. We have a dictionary of student names and grades:

```python
student_grades = {
    "bilal": [91.5, 87.99, 99.56],
    "mike": [89.00, 77.67, 99.99],
    "ambar": [71.77, 69.01, 88.8]
}
```

Ask the user for their name and try to find it in the `student_grades` dictionary. If you can find it, return the **average grades**. Otherwise, tell the user you can't find their grades, ask for 3 grades, add them to the dictionary, and also return their average.

**Note:** The formatting of the dictionary is broken across multiple lines for readability, which is acceptable in Python.

4. Take the user's name, check the time of day using the **`time`** module, and greet the user based on the time. If the current hour is less than 12, print `"Good morning, username"`.

```python
import time
current_hour = time.localtime().tm_hour
# This returns the current hour of the day (0-23).
```

##### Format Strings

From Python 3.6 on-wards, Python supports **f-strings** (formatted string literals), which allow you to easily pass variables into a string.

```python
username = "John Doe"
greeting = f"Welcome, {username}."

print(greeting)

# Output: Welcome, John Doe.

# The 'f' at the beginning of the string and the variable name within curly braces {} enable this feature.
```

### 
