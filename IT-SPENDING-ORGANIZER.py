#IMPORTING TO GO OVER THE EXCEL SPREAD SHEET FOR SPENDING

import openpyxl
from openpyxl.styles.builtins import total

#-------------------------

#Step1: I will be loading the excel file/spreadsheet

wb = openpyxl.load_workbook('it_spending_2024.xlsx')
sheet = wb.active  #This will assume the data is in the first sheet

print(sheet)

#------------------------------------------------------
#Step2: Intialize a dictionary to hold all monthly costs.
#------------------------------------------------------

monthly_costs = {}

#------------------------------------------------------

#Step3: I want to loop through all the rows now to accumulate the monthly spending
#------------------------------------------------------

for row in range(2, sheet.max_row + 1): #We're skipping the header row
    month = sheet[f'A{row}'].value
    cost = float(sheet[f'D{row}'].value)


    #Now i will be adding the cost to the appropriate month

    monthly_costs.setdefault(month, 0) # Looks for the key value of the month exists if no it will add 0 to its value.
    monthly_costs[month] += cost  #ADDS COSTS TO THE CURRENT MONTH VALUE TO THE OTHER MONTHS IN THE LIST DICTIONARY.

#------------------------------------------------------
#Step4: I will be printing th summary with the over under budget indication in which my boss asked.
#------------------------------------------------------

print("Monthly Spending Summary (2024)")
print("-" * 40)
total = 0

for month in sorted(monthly_costs.keys(), key = lambda m: "JanFebMarAprMayJunJulAugSepOctNovDec".index(m[:3])):
    cost = monthly_costs[month]
    total += cost
    status = "under" if cost <= 20000 else "Over"
    print(f"{month:>3}: ${cost:,.2f} {status}")


#------------------------------------------------------

#Step5 : i will be printing the total spending for the year

print(f"\nTotal Yearly Spent: ${total:,.2f}")
