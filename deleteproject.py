from viewprojects import view_all_projects
import json


def delete_project(user_id):
    view_all_projects(user_id)

    project_name = input("Enter project title you want to delete : ")

    d = open("project_data.json", "r+")
    d_data =d.read()
    if d_data:
        old_data = json.loads(d_data)
    else:
        old_data = []
        print("there is no projects to delete")
    dell = False
    for project in old_data:
        if project['title'] == project_name:
            dell = True
            d.seek(0)
            d.truncate()
            old_data.remove(project)
            new_data = json.dumps(old_data , indent=5)
            d.write(new_data)
            d.close()  
            print("Project successfully deleted")
            break
        
    if not dell:
        print("Invalid project title .. please enter another")
        delete_project(user_id) 
        
