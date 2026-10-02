emp_name=input("enter employee name:")
annual_salary=float(input("enter annual salary:"))
investment_amount=float(input("enter investment amount:"))
home_loan_intrest=float(input("enter home loan interest:"))
medical_insurance_premium=float(input("enter medical insurance premium:"))
total_deduction=investment_amount+home_loan_intrest+medical_insurance_premium
taxable_income=annual_salary-total_deduction
if taxable_income >= 1500000:
    tax_percent=30
    tax_amount=taxable_income*30/100
elif taxable_income >= 1000000 and taxable_income <= 1499999:
    tax_percent=20
    tax_amount=taxable_income*20/100
elif taxable_income >= 500000 and taxable_income <=999999:
    tax_percent=10
    tax_amount=taxable_income*10/100
else:
    tax_percent=0
    tax_amount=0
    print("No tax is applicable.")
if tax_amount>200000:
    category="high tax payers."
elif tax_amount>=50000 and tax_amount<=200000:
    category="medium tax payers."
else:
    category="low tax payers."
print("\n ======= TOTAL TAX DETAILS =======")
print("employee name:", emp_name)
print("annual salary:", annual_salary)
print("total deduction:", total_deduction)
print("taxable income:", taxable_income)
print("tax percentage:", tax_percent)
print("tax amount:", tax_amount)
print("tax payers category:", category)