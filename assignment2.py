# accept inputs from the user
car_price = float(input("enter car price: "))
insurance_amount = float(input("enter insurance amount: "))
down_payment = float(input("enter down payment: "))
# arithmetic operations
total_amount = car_price + insurance_amount
remaining_amount = total_amount - down_payment
half_amount = total_amount / 2
remainder = total_amount % 1000
whole_number = total_amount // 1000
# Comparison Operations
car_price_check = car_price > 2000000
down_payment_check = down_payment == 500000
remaining_amount_check = remaining_amount < 1500000
insurance_check = insurance_amount != 50000
total_amount_check = total_amount >= 2500000
# Display Results
print("--- BILL DETAILS ---")
print("total amount:", total_amount)
print("remaining amount:", remaining_amount)
print("half amount:", half_amount)
print("remainder when divided by 1000:", remainder)
print("whole number when divided by 1000:", whole_number)
print("--- COMPARISON RESULTS ---")
print("car price > 20,00,000 :", car_price_check)
print("down payment == 5,00,000 :", down_payment_check)
print("remaining amount < 15,00,000 :", remaining_amount_check)
print("insurance amount != 50,000 :", insurance_check)
print("total amount >= 25,00,000 :", total_amount_check)