from viewprojects import view_all_projects
from createproject import validate_date
import json


def search_for_project(user_id):
    view_all_projects(user_id)

    project_date = input("Enter project date 'dd-mm-YYYY' : ")
    while True :
        if validate_date(project_date):
            break
        else:
            print("Your data is invalid .. Please enter valid data :")
            project_date = input("Enter project date 'dd-mm-YYYY' : ")

    s = open("project_data.json", "r")
    s_data =s.read()
    if s_data:
        data = json.loads(s_data)
    else:
        data = []
        print("there is no projects")
    s.close()  

    search = False
    for project in data:
        if project_date == project['start_date'] or project_date == project['end_date']:
            search = True
            print(project)
            break
    if not search :
        print("Invalid project date .. please try again")
        search_for_project(user_id)
       
       
       
       
            

