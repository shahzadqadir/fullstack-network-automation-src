# Problem
# 
# Write a function which takes a name with default set to empty string, 
# if user supplies a name, function prints "Hello, xxx" where xxx is the name provided by user. 
# If no name is provided, function just prints "Hello, World!".


def greeting(name: str=""):
    if name:
        print(f"Hello, {name}")
    else:
        print("Hello, World!")

greeting()  
greeting("Duncan Lockwood")