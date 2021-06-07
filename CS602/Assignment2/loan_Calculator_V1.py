"""
Assignment2
Name:Qiaofei Yan
"""

import numpy_financial as npf
#def the simple variable
loan_amount_s = 100000
loan_year_s = 15
An_rate_s = 0.0625

#user preferences
print("Welcome to the CS 602 Loan Calculator.")
while True:
    SC = input("[S]ample or [C]ustom Report: ")
    #set the input equl to s then run sample
    if SC.upper() == 'S':
        #set the goal value
        loan_amount = loan_amount_s
        loan_duration_months = loan_year_s * 12
        annual_interest_rate = An_rate_s
        #the monthley payment function
        break

    #set the input equal to c then run custom
    elif SC.upper() == 'C':
        annual_interest_rate = float(input('Enter annual interest rate: '))
        loan_amount = int(input('Enter loan amount: '))
        while True:
            loan_duration_months = int(input('Enter number of years (between 3 and 30): '))
            #def range of the input
            if loan_duration_months >= 3 and loan_duration_months <= 30:
                loan_duration_months = loan_duration_months * 12
                break
            else:
                print('error')
        #break the second while true loop
        break
    else:
        print("Error. Enter [S]ample or [C]ustom.")
while True:
    #set the summary load heading and input
    MA = input("[M]onthly or [A]nnual Report: ")
    if MA.upper() == 'M':
        MA = 'Month'
        break
    elif MA.upper() == 'A':
        MA = 'Year'
        break
    else:
        print("Error. Enter [M] or [A]:")
#output
monthly_pmt = npf.pmt(annual_interest_rate / 12,  loan_duration_months, -1 * loan_amount)
print('='*60)
print(f'Loan amount:\t\t${loan_amount:>12,.2f}')
print(f'Loan duration in months:{loan_duration_months:>12}')
print(f'nnual Interest Rate:\t{annual_interest_rate:>12,.4f}%')
print(f'Monthly Payment:\t${monthly_pmt:>12,.2f}')
print('='*60)
print(f'{MA}\tPrincipal\tInterest\tPayment')
print('='*60)

loan_year = int(loan_duration_months/12)
Y1 = 1
M1 = 0
Interest_total = 0
if MA == 'Month':
    #loan_year let the for loop run motiple times
    for i in range(loan_year):
            print(f'Year: {Y1}'.center(60, "-"))
            Y1 += 1
            print(f'{MA}\tPrincipal\tInterest\tPayment')
            for i in range(12):
                M1 += 1
                M_prin_partM1 = npf.ppmt(annual_interest_rate / 12, M1, loan_duration_months, -1 * loan_amount)
                M_int_partM1 = npf.ipmt(annual_interest_rate / 12, M1, loan_duration_months, -1 * loan_amount)
                Interest_total += M_int_partM1
                print(f'{f"{M1:03}":>6} ${M_prin_partM1:>12,.2f} ${M_int_partM1:>12,.2f} ${monthly_pmt:>12,.2f}')
                #end- of repot the month when principal exceeds interest payment
                if M_prin_partM1 < M_int_partM1:
                    #when the principal exceeds print the month
                    exceeds_month_number= M1
    print("="*60)
    print(f"Total: ${loan_amount:>12,.2f} ${Interest_total:>12,.2f} ${loan_amount+Interest_total:>12,.2f}")
    print(f"Principal payment exceeds interest payment starting in month {exceeds_month_number+ 1}.")
#year_report
else:

    T_P_Total = 0
    T_I_Total = 0
    Y_2 = 1
    loan_duration_year = int(loan_duration_months/12)
    for i in range(loan_duration_year):
        Y_principal = 0
        Y_interest = 0
        for i in range (12):
            M1 += 1
            prin_partM1 = npf.ppmt(annual_interest_rate / 12, M1, loan_duration_months, -1 * loan_amount)
            int_partM1 = npf.ipmt(annual_interest_rate / 12, M1, loan_duration_months, -1 * loan_amount)
            Interest_total += int_partM1
            Y_principal += prin_partM1
            Y_interest += int_partM1
            if prin_partM1 < int_partM1:
                exceeds_month_number= M1
        T_P_Total += Y_principal
        T_I_Total += Y_interest
        print(f'{f"{Y1:03}":>5}  ${Y_principal:>12,.2f}  ${Y_interest:>12,.2f}   ${monthly_pmt * 12:>12,.2f}')
        Y_2 +=1
        if Y_2 == 11:
            print()
            Y_2 = 1
        Y1 += 1
    print('='*60)
    print(f"Total: $ {T_P_Total:>12,.2f} ${T_I_Total:>12,.2f}   ${monthly_pmt*loan_duration_year*12:>12,.2f}")
    print(f"Principal payment exceeds interest payment starting in month {exceeds_month_number+ 1}.")
    