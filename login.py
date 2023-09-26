import json
from projectmenu import menu 

def login_user():

    print("Please enter user email and password to login.")
    email = input("Enter email: ")
    password = input ("Enter password: ")

    f = open("user_data.json", "r")
    f_data =f.read()
    if f_data:
        data = json.loads(f_data)
    else:
        data = []
        print("there is no users")
    f.close()  

    successful_login = False
    for user in data:
        if email == user['email']: 
            if password == user['password']:
                successful_login = True
                user_id = user['user_id']
                print("logged in successfully")
                repeat = True
                while repeat == True :
                    menu(user_id)        
                    print("Would you like to go back to project menu or exit ?")
                    again = input("Type menu or exit .\n")
                    if again == "exit":
                        repeat = False 
                        break 
                break
            
    if not successful_login:
        print("invalid data .. please try again")
        login_user()




