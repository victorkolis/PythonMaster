# function_more_than_one_input.py

def greet(name, location):
    print(f"Hi {name}")
    input(f"What is it like in {location}? ")
    print(f"Nice! Someday I might visit {location}")


greet(name = "Victor", location = "São Paulo")
