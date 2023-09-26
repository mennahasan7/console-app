import json
import re

def name_validation(name):
    while True:
        if name.isalpha():
            break
        else:
            print("Name must be only letters")
            name = input("Please enter another name: ")

def register_new_user(user_id):
    
    user_id += 1
    first_name = input("Enter user first name: ")
    name_validation(first_name)
   
    last_name = input("Enter user last name: ")
    name_validation(last_name)

    email = input("Enter user email: ")
    def validate_email(email):  
        if re.match(r"[^@]+@[^@]+\.[^@]+", email):  
            return True  
        return False

    while True:
        if validate_email(email):
            break
        else:
            email = input("Enter a valid user email: ")

    password = input("Enter user password consists of 8 numbers: ")
    confirm_password = input("Confirm password: ")
    while True:
        if len(password) == 8 and password.isdigit():
            if confirm_password == password:
                break
            else:
                print("Passwords don't match. please enter matching passwords.")
                
                password = input("Enter user password: ")
                confirm_password = input("Confirm password: ")
        else:
            print("Your password is invalid ")
            print("please enter a password of 8 numbers : ")
        
            password = input("Enter user password: ")
            confirm_password = input("Confirm password: ")


    phone_number = input("Enter user phone number: ")
    def validate_egy_phone_number(number):  
        if re.match(r"^(\+201|01|00201)[0-2,5]{1}[0-9]{8}", number):  
            return True  
        return False

    while True:
        if validate_egy_phone_number(phone_number):
            break
        else:
            phone_number = input("Please enter valid egyptian phone number: ")

    
    validated_user_data = {'user_id':user_id,
                        'first_name': first_name, 
                        'last_name': last_name, 
                        'email': email, 
                        'password': password,
                        'mobile_phone': phone_number}
      
    f = open("user_data.json", "r+")
    f_data =f.read()
    if f_data:
        old_data = json.loads(f_data)
        flagg = False
        for user in old_data:
            if email != user['email'] or user['mobile_phone'] != phone_number:
                break
        if not flagg:
                print("this user is already exit .. please try again")
                register_new_user(user_id)    
                
    else:
        old_data = []
    old_data.append(validated_user_data)
    
    new_data = json.dumps(old_data, indent=6)
    f.seek(0)
    f.write(new_data)
    f.close()  
    print('User is created successfully')
   

