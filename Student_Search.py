import json 
import Validation

path=fr"F:\Student-Record-Management-System\Student-Records\StudentsData.json"

with open(path,"r") as file:
    data = json.load(file)

def Searching():
    print("")
    print("Press 1 - Search Student by contact")
    print("Press 2 - Search Student by qualification")
    print("")

    choice=Validation.get_valid_number("Enter your choice :")

    if choice==1:
        choice="contact"
        userVal = Validation.get_valid_contact("Enter your contact:- ")
        for listdata in data:
            for key,value in listdata.items():
                if str(value).lower()== str(userVal).lower():
                    return listdata
    elif choice==2:
      Qualification_search()

    else:
        print("Enter valid choice")



def Qualification_search():
    choice="qualification"
    print("Press 1 - Search by Qualification name : ")
    print("Press 2 - Search by Qualification year : ")
    userVal=int(input("Enter your choice : "))
    
    if userVal==1:
        userVal="qualificaton_name"
        StudentCh=input("Enter Student qualification name :")
    elif userVal==2:
        userVal="qualificaton_year"
        StudentCh=input("Enter Student qualification year :")
    else:
        print("Enter valid choice!")
    
    for listdata in data:
        for key,value in listdata.items():
            if key==choice:
                for q in value:
                    if q[f"{userVal}"]==StudentCh:
                        pretty_data = json.dumps(listdata, indent=4)
                        print(pretty_data)