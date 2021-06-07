#Assignment2 Qiaofei Yan
import numpy_financial as npf
S_A = 100000
S_M_Y = 15
S_R = 0.0625
def S_Custom():
    global loan_amount,Loan_Months,Annual_Rate
    S_C = input('[S]ample or [C]ustom Report: ')
    if S_C.upper() == 'S':
        loan_amount = S_A
        Loan_Months = S_M_Y * 12
        Annual_Rate = S_R
    elif S_C.upper() =='C':
        Annual_Rate = C_R = float(input('Enter annual interest rate: '))
        loan_amount = C_A = int(input('Enter loan amount: '))
        while True:
            Loan_Months = C_M_Y = int(input('Enter number of years (between 3 and 30): '))
            if Loan_Months >= 3 and Loan_Months <= 30:
                Loan_Months = Loan_Months * 12
                M_Annual()
            else:
                print('Error.')
    else:
        print('Error. Enter [S]ample or [C]ustom.')
        S_Custom()
def M_Annual():
    global Title_M_A
    M_A = input('[M]onthly or [A]nnual Report:')
    if M_A.upper() == 'M':
        Title_M_A = 'Month'
        Heading()
    elif M_A.upper() == 'A':
        Title_M_A = 'Year'
        Heading()
    else:
        print('Error. Enter [M] or [A]')
        M_Annual()
def Heading():
    global monthly_pmt
    monthly_pmt = npf.pmt(Annual_Rate / 12,  Loan_Months, -1 * loan_amount)
    print('='*60)
    print(f'Loan amount:\t\t${loan_amount:>12,.2f}')
    print(f'Loan duration in months:{Loan_Months:>12}')
    print(f'nnual Interest Rate:\t{Annual_Rate:>12,.4f}%')
    print(f'Monthly Payment:\t${monthly_pmt:>12,.2f}')
    print('='*60)
    print(f'{Title_M_A}\tPrincipal\tInterest\tPayment')
    print('='*60)
    M_report()
def M_report():
    global loan_year
    loan_year = int(Loan_Months/12)
    Y1 = 1
    M1 = 0
    Interest_total = 0
    if Title_M_A == 'Month':
        #loan_year let the for loop run motiple times
        for i in range(loan_year):
                print(f'Year: {Y1}'.center(60, "-"))
                Y1 += 1
                print(f'{Title_M_A}\tPrincipal\tInterest\tPayment')
                for i in range(12):
                    M1 += 1
                    M_prin_partM1 = npf.ppmt(Annual_Rate / 12, M1, Loan_Months, -1 * loan_amount)
                    M_int_partM1 = npf.ipmt(Annual_Rate / 12, M1, Loan_Months, -1 * loan_amount)
                    Interest_total += M_int_partM1
                    print(f'{f"{M1:03}":>6} ${M_prin_partM1:>12,.2f} ${M_int_partM1:>12,.2f} ${monthly_pmt:>12,.2f}')
                    #end- of repot the month when principal exceeds interest payment
                    if M_prin_partM1 < M_int_partM1:
                        #when the principal exceeds print the month
                        exceeds_month_number= M1
        print("="*60)
        print(f"Total: ${loan_amount:>12,.2f} ${Interest_total:>12,.2f} ${loan_amount+Interest_total:>12,.2f}")
        print(f"Principal payment exceeds interest payment starting in month {exceeds_month_number+ 1}.")
    else:
        T_P_Total = 0
        T_I_Total = 0
        Y_2 = 1
        loan_duration_year = int(Loan_Months/12)
        for i in range(loan_duration_year):
            Y_principal = 0
            Y_interest = 0
            for i in range (12):
                M1 += 1
                prin_partM1 = npf.ppmt(Annual_Rate / 12, M1, Loan_Months, -1 * loan_amount)
                int_partM1 = npf.ipmt(Annual_Rate / 12, M1, Loan_Months, -1 * loan_amount)
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
def main():
    S_Custom()
    M_Annual()
    Heading()
main()