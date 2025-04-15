import Validation
def Registration():

    Qualificaton=[] 
    studentDict={}


    studentDict['id']=Validation.get_valid_number("Enter student id :- ")
    studentDict['name']=Validation.get_valid_name("Enter student name :- ")
    studentDict['email']=input("Enter student email :- ")
    studentDict['contact']=Validation.get_valid_contact("Enter student contact :- ")
    studentDict['address']=input("Enter student address :- ")

    flag=0

    while flag==0:

        qualificatonDict={}

        qualificatonDict['qualificaton_name']=input("Enter student qualification name:- ")
        # qualificatonDict['qualificaton_year']=int(input("Enter student qualification year:- "))
        qualificatonDict['qualificaton_year']=input("Enter student qualification year:- ")

        Qualificaton.append(qualificatonDict)

        studentDict["qualification"]=Qualificaton

        print("")
        print("Press 1 - Add more qualification ")
        print("Press 0 - exit ")
        print("")

        choice=int(input("Enter your choice :"))

        if choice==0:
            flag=1

    return studentDict