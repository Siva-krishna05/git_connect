#checking fee balance
sem1 = int(input("enter your 1st sem fee:"))
sem2 = int(input("enter your 2nd sem fee:"))
sem3 = int(input("enter your 3rd sem fee:"))
sem4 = int(input("enter your 4th sem fee:"))
sem5 = int(input("enter your 5th sem fee:"))
sem6 = int(input("enter your 6th sem fee:"))
total_sem_fees = sem1+sem2+sem3+sem4+sem5+sem6
paid = 75000
balance = total_sem_fees-paid
print("remaining balance",balance)
