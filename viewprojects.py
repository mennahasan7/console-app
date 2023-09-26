import json

def view_all_projects(user_id):

    p = open("project_data.json", "r")
    p_data =p.read()
    if p_data:
        projects_data = json.loads(p_data)
    else:
        projects_data = []
        print("there is no projects to display")

    p.close() 

    flagg = False
    for user in projects_data:
        if user_id == user['project_user_id']:
            flagg = True
            print(projects_data) 
            break
    if not flagg:
        print("invalid user id .. please try again")
        view_all_projects(user_id)


