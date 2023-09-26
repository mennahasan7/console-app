import json
from createproject import create_new_project
from viewprojects import view_all_projects
from editproject import edit_project
from deleteproject import delete_project
from searchproject import search_for_project

def menu(user_id):
    print("Please choose  : \n 1) Create new project \n 2) View projects \n 3) Edit project \n 4) Delete project \n 5) Search for project")
    choice = input("Type 1 or 2 or 3 or 4 or 5 : \n")

    if choice == "1":
        create_new_project(user_id)
        
    elif choice == "2":
        view_all_projects(user_id)
        
    elif choice == "3":
        edit_project(user_id)

    elif choice == "4":
        delete_project(user_id)
        
    elif choice == "5":
        search_for_project(user_id)
        
    else:
        print("\nPlease choose From menu")
     
