#booking movie tickets
customer_name = input("enter a customer name:")
age = int(input("enter a customer age:"))
ticket_price = float(input("enter the ticket price:"))
no_of_ticket = int(input("enter number of tickets:"))
total_amount = ticket_price * no_of_ticket
if age >= 60 or age < 12:
    discount = total_amount*0.20
    final_amount = total_amount-discount
    print("total Amount:",total_amount)
    print("after 20% discount applied!--->")
    print("final amount",final_amount)
else:
    print("total amount",total_amount)
    print("original amount")

#Online shopping
customer_name = input("enter a customer name:")
product_price = float(input("enter the product price:"))
quantity = int(input("enter a quantity:"))
is_coupon = input("do you have a coupon(True/False):") == True
total_amount = product_price * quantity
if total_amount > 2000 or is_coupon:
    discount = total_amount * 0.15
    final_amount = total_amount - discount
    print("give a 15% discount")
    print("final amount", final_amount)
else:
    print("total amount", total_amount)
    print("no discount")