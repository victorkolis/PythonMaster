# functions_with_output.py

# return - keyword

import subprocess

def format_name(f_name, l_name):
    full_name = f"{f_name} {l_name}"
    return full_name.title()

first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
subprocess.call("clear")

full_name = format_name(first_name,last_name)
print(full_name)
