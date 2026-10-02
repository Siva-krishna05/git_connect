#create a program that accepts emp name,department salary.
# save the details into emp.txt 
# salary should be numeric handle invalid salary input using exception handle
with open("employee.txt","w") as f:
    print(f)
while True:
    try:
        name=input("enter emp name:")
        department=input("enter department:")
        emp_salary=int(input("enter employee salary:"))
        
        with open("employee.txt","a") as f:
            f.write(f"\n name:{name}, department:{department}, emp_salary:{emp_salary}")
            
        print("employee records saved successfully.")
        
    except ValueError:
        print("invalid salary, please enter a numeric value only.")
            
    except Exception as siva:
        print("error:", siva)
            
    finally:
         choice=input("do you want to add another employee name (yes/no):").lower()
            
         if choice=="no":
            print("thank you...")            
    break