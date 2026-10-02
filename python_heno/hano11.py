cus_name=input("enter customer name:")
age=int(input("enter customer age:"))
monthly_salary=float(input("enter montly salary:"))
is_completed_kyc=input("customer has completed kyc (yes or no):")
if is_completed_kyc == "no":
    print("please complete your kyc.")
elif age >= 21 and monthly_salary>=30000:
    print("car loan provided.")
elif age>=21 or monthly_salary>=30000:
    print("under review.")
else:
    print("car loan rejected.")
    
#
customer_name=input("enter customer name:")
shopping_amount=float(input("enter shopping amount:"))
is_prime_member=input("the customer is a prime member (yes or no):")
is_payment_completed=input("payment is completed (yes or no):")
if is_payment_completed == "no":
    print("please complete your payment.")
elif shopping_amount>=50000 and is_prime_member =="yes":
    print("give a 15% discount has applied.")
elif shopping_amount>=5000 or is_prime_member =="yes":
    print("give a 5% discount has applied.")
else:
    print("no discount!")
    