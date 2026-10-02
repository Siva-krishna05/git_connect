'''def f():
    print("Hi")

def g():
    return "Hi"'''
    
with open("attendance.txt","w") as f:
   print(f)
    

while True:
    print("\n===== Student Attendance System =====")
    print("1. Mark Attendance")
    print("2. View Attendance")
    print("3. Exit")
    try:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            name = input("Enter Student Name: ")
            attendance = input("Enter Attendance (Present/Absent): ")
            with open("attendance.txt", "a") as file:
                file.write(f"{name} - {attendance}\n")
            print("Attendance Saved Successfully!")
        elif choice == 2:
            try:
                with open("attendance.txt", "r") as file:
                    data = file.read()
                    if data:
                        print("\n----- Attendance Records -----")
                        print(data)
                    else:
                        print("No attendance records found.")
            except FileNotFoundError:
                print("attendance.txt file not found!")
        elif choice == 3:
            print("Exiting Program...")
            break
        else:
            print("Invalid Choice! Please enter 1, 2, or 3.")
    except ValueError:
        print("Please enter numbers only!")