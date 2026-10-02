student_name = input("enter student name:")
maths=int(input("enter math marks:"))
science=int(input("enter science marks:"))
english=int(input("enter english marks: "))
total_marks=maths+science+english
avg_marks=total_marks/3
attendance_percentage=float(input("enter attendance percentage:"))
sports_quota=input("is student belongs to sports quota (yes or no):")
if avg_marks >= 90 and attendance_percentage >= 85:
    print("100% Scholarship.")
elif avg_marks>=75 or sports_quota =="yes":
    print("50% scholarship.")
elif sports_quota =="no":
    print("No scholarship.")
else:
    print("Try again next year") 
    
print("\n ----student details----")
print("student name:", student_name)
print("total marks:", total_marks)
print("average:", avg_marks)