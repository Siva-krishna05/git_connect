student_name=input("enter student name:")
percentage_of_10th=int(input("enter your 10th percentage:"))
percentage_of_12th=int(input("enter your 12th percentage:"))
entrance_exam_marks=int(input("enter your entrance exam marks:"))
sports_quota=input("are you sport quota person? (yes/no):")
avg=(percentage_of_10th+percentage_of_12th) / 2
print("average percentage=",avg)

if avg >= 90 and entrance_exam_marks >= 90:
    print("Admission comfirmed.")
elif avg >= 80 and sports_quota == "yes":
    print("Admission comfirmed.")
elif avg >= 75 or entrance_exam_marks >= 80:
    print("Waiting list!")
else:
    print("Rejected...")