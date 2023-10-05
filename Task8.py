# Task1
import re


def validate_mobile_tel_number(number):
    try:
        result = re.match(r'[+]+\d+', number).group(0)
        if result == number and len(number) == 13:
            return True
        else:
            return False
    except AttributeError as e:
        print("Please provide valid value for tel number")


# Task2
def validate_home_tel_number(home_number):
    try:
        result = re.match(r'\d+', home_number).group(0)
        if result == home_number and len(home_number) == 7:
            return True
        else:
            return False
    except AttributeError as e:
        print("Please provide valid value for tel number")


# Task3

def validate_email(email):
    try:
        email_result = re.match(r'\w+[@]\w+[.]\w+', email).group(0)
        if email_result == email and 6 <= len(email) <= 20:
            return True
        else:
            return False
    except AttributeError as e:
        print("Please provide valid value for email")


# Task4
def validate_full_name(full_name):
    try:
        full_name_result = re.split(r'\s', full_name)
        for name in full_name_result:
            single_name_result = re.match(r'\w+', name).group(0)
            if single_name_result == name and 2 <= len(single_name_result) <= 20:
                return True
            else:
                return False
    except AttributeError as e:
        print("Please provide valid value for full name")


# Task5
def validate_password(password):
    try:
        password_result = re.match(r'^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*\W)(?!.* ).{8,16}$', password).group(0)
        if password_result == password:
            return True
        else:
            return False
    except AttributeError as e:
        print("Please provide valid value for password")


tel_number = '+380981234567'
tel_number2 = '123'
tel_number3 = 'dfsdfs'
result1 = validate_mobile_tel_number(tel_number)
print(result1)
result2 = validate_mobile_tel_number(tel_number2)
print(result2)
result3 = validate_mobile_tel_number(tel_number3)
print(result3)
tel_number4 = '4578035'
result4 = validate_home_tel_number(tel_number4)
print(result4)
user_email = 'test@gmail.com'
result5 = validate_email(user_email)
print(result5)
user_email2 = '123'
result6 = validate_email(user_email2)
print(result6)
user_full_name = 'Пупкин Василий Петрович'
result7 = validate_full_name(user_full_name)
print(result7)
user_password = 'Password5$'
result8 = validate_password(user_password)
print(result8)