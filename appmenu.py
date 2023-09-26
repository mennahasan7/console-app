from registeration import *
from login import login_user
import json

def app():
    print("Please choose  : \n 1) Registration \n 2) Login")
    choice = input("Type 1 or 2 : \n")

    if choice == "1":
        list=[]
        reg = open("user_data.json")
        reg_data =reg.read()
        if reg_data:
            data = json.loads(reg_data)
            last_index= len(data)-1
            last_user = data[last_index]
            user_id = last_user['user_id']
        else:
            user_id = 0
        reg.close()
        register_new_user(user_id)

    elif choice == "2":
        login_user()
        
    else:
        print("Please choose From menu")

repeat = True
while repeat == True :
    app()        
    print("Would you like to go back to menu or exit ?")
    again = input("Type menu or exit .\n")
    if again == "exit":
        repeat = False
        break