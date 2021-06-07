"""
Test numpy_financial functions
"""
import numpy_financial as npf

monthly_pmt = npf.pmt(0.085 / 12, 10 * 12, -1 * 100000)
print(f"The monthly payment on $100000 at 8.5% for 10 years is ${monthly_pmt:0,.2f}.")
