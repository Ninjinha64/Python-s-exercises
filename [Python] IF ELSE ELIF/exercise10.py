loan = int(input("Enter the loan amount: "))
installments = int(input("Enter the number of installments: "))
monthly_payment = loan / installments

if loan > 200000:
    print("Loan denied.")
else:
    print("Loan approved.")
