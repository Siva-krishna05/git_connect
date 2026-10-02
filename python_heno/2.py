customer_name=input("enter customer name:")
rice_price=float(input("enter rice price:"))
oil_price=float(input("enter oil price:"))
milk_price=int(input("enter milk price:"))

total_bill=rice_price+oil_price+milk_price

is_premium=input("is customer a premium member(yes/no):")
has_coupon=input("do you have coupon(yes/no):")

discount=0

if total_bill>=5000 and is_premium =="yes":
    discount=total_bill*0.20
    print("give a 20% discount!")
elif total_bill>=3000 or has_coupon =="no":
    discount=total_bill*0.10
    print("give a 10% discount.")
elif total_bill<=2000 and is_premium =="no":
    print("become a premium member to get better offers.")
else:
    discount=0
final_amount=total_bill-discount

print("\n ----bill details----")
print("customer name:", customer_name)
print("total bill:", total_bill)
print("discount:", discount)
print("final amount:", final_amount)