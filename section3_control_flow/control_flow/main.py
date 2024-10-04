from datetime import datetime
# if statements

print("#" * 20)
print("Hello there, welcome to Bocil's University")
print("Register form below there\n")
fname = input("Fill your first name: ")
lname = input("Fill your last name: ")
age = int(input('Fill your age: '))
year_birth = int(input('Fill year of birth: '))
is_age_valid = datetime.now().year - age != year_birth
message = ""

if(is_age_valid):
    message = "Your age and birth year is not valid"
else:
    message = 'Ok welcome'

print('\n')
print("*" * 10 + " " + "SUMMARY" + " " + "*" * 10) 
print(f'First Name: {fname}')
print(f'Last Name: {lname}')
print(f'Age: {age}')
print(f'Birth Year: {year_birth}')
print(f'System message: {message}')
print("*" * 10 + ("*" * len(" SUMMARY ")) + "*" * 10) 
print('\n')

print("#" * 20)
