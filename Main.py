import Student_Registration 
import Student_Details
import Student_Search
import json

Students=[]

path=fr"F:\Student-Record-Management-System\Student-Records\StudentsData.json"

print("**  Student Record Management System **")

def Menu():

    print("Press 1 - Student Registration.")
    print("Press 2 - Student Details.")
    print("Press 3 - Student Search.")
    print("Press 4 - Exit.")
    UserInput()


def UserInput():
    user_data=int(input("Enter your choice :"))
    Management(user_data)

def Management(choice):
    if(choice==1):
   
        flag=0

        while flag==0:

            data=Student_Registration.Registration()
            Students.append(data)
            
            MyData=json.dumps(Students,indent=4)
            with open(path,"w") as file:
                file.write(MyData)

            print("")
            print("Press 1 - Add more students ")
            print("Press 0 - exit ")
            print("")

            choice=int(input("Enter choice :"))

            if choice==0:
                flag=1
        Menu()
       
    elif(choice==2):
        Result=Student_Details.Details(path)
        print(Result)
        Menu()

    elif(choice==3):
        Student_Search.Searching()
        Menu()

    elif(choice==4):
        print(" Thank you for visiting us !")
        exit()

    else:
        print("Please enter valid choice !\n")
        
        Menu()

Menu()
