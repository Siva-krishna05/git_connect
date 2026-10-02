'''username=input("enter a username:")
pwd=input("enter a pwd:")
if username=="admin" and pwd == "asdfghjkl;":
    print("login successful")
else:
    print("invalid login")

customername = input("enter user name:")
pizzaprice = float(input("enter pizza prize:"))
quantity = int(input("enter quantity:"))
is_member = input("are you a member?(True/False):")
total = pizzaprice * quantity
if total >= 1000 and is_member:
    discount = total * 0.10
    final_bill = total - discount
    print("/n 10% discount applied")
else:
    final_bill = total
    print("/nNo discount applied")
    '''
'''numbers=[1,2,3,4,5,6]
for number in numbers:
    numbers.remove(number)
print(numbers)'''

'''while True:
    num=int(input("enter a number:"))
    if num%2==0:
        print("even")
        continue
    else:
        print("odd")
    break'''
    
def generate_bill_summary(bill_amount_str, tip_percent):
    # Step 1: convert the bill amount string to a decimal number
    bill = float(bill_amount_str)

    # Step 2: compute the tip and the total
    tip = bill * tip_percent / 100
    total = bill + tip

    # Step 3: build and return the three-line f-string summary
    return f"Bill amount: {bill}\nTip: {tip}\nTotal: {total}"


if __name__ == "__main__":
    print(generate_bill_summary("1000", 15))
