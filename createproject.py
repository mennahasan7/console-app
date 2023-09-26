import json
from datetime import datetime

def validate_date(date):
    try:
        return bool(datetime.strptime(date, '%d-%m-%Y')) 
    except ValueError:
        return False

projects_list=[]
def create_new_project(user_id):

    title = input("Enter project title : ")
    details = input("Enter project details : ")
    total_target = input("Enter project total target : ")
    start_date = input("Enter campaign start Date 'dd-mm-YYYY' : ")
    end_date = input("Enter campaign end Date 'dd-mm-YYYY' : ")
    

    while True :
        if validate_date(start_date) and validate_date(end_date):
            break
        else:
            print("Your data is invalid .. Please enter valid data :")
            start_date = input("Enter campaign start Date 'dd-mm-YYYY' : ")
            end_date = input("Enter campaign end Date 'dd-mm-YYYY' : ")


    validated_project_data = {'project_user_id': user_id,
                            'title': title, 
                            'details': details ,
                            'total_target': total_target,
                            'start_date': start_date,
                            'end_date': end_date}
        
    p = open("project_data.json", "r+")
    p_data =p.read()
    if p_data:
        old_project_data = json.loads(p_data)
        flagg = False
        for project in old_project_data:
            if title != project['title'] or project['project_user_id'] != user_id:
                break
        if not flagg:
                print("this project name is already exit .. please try another name")
                create_new_project(user_id) 
          
    else:
        old_project_data = []
        
    old_project_data.append(validated_project_data)
    new_project_data = json.dumps(old_project_data, indent=5)
    p.seek(0)
    p.write(new_project_data)
    p.close()  
    print('Project is created successfully')


