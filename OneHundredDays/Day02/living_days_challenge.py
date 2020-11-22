# This software objective is to print one's got left if they were to live till their 90's

age = int(input("What is your current age?'\n"))
age_verifier = 90
if(age < age_verifier):
    age_verifier -= age
    days = age_verifier * 365
    weeks = age_verifier * 52
    months = age_verifier * 12
    
    print(f"You have {days} days, {weeks} weeks and {months} months left.")
else:
    print("Kudos! You've already lived much!!")