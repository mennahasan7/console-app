from viewprojects import view_all_projects
import json


def edit_project(user_id):
    view_all_projects(user_id)

    project_name = input("Enter project title you want to edit : ")

    pj = open('project_data.json', 'r+')
    pj_data =pj.read()
    project_data = json.loads(pj_data)
    
    validated_title = False
    for project in project_data:
        if project['title'] == project_name:
            validated_title = True
            print(project)
            
            key_name = input("Please enter the name of key you want to edit : ")
            validated_key = False
            for key in project:
                if key == key_name:
                    validated_key = True
                    key_value = input("Please enter the key new value : ")
                    project[key] = key_value
                    project_data.append(project)
                    new_project_data = json.dumps(project_data , indent=5)
                    pj.seek(0)
                    pj.write(new_project_data)
                    pj.close()
                    print("Project successfully updated")
                    break
            if validated_key:
                break
            else:
                print("Invalid key name .. please enter another")
                edit_project(user_id)                       
    
    if not validated_title:
                print("Invalid project title .. please enter another")
                edit_project(user_id)                              
            

