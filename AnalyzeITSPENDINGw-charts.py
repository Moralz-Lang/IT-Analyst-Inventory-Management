import openpyxl
import matplotlib.pyplot as plt
from collections import defaultdict

from unicodedata import category

#Loading workbook

wb = openpyxl.load_workbook('it_spending_2024.xlsx')
sheet = wb.active


#I will be intializing Data Containers

monthly_costs = defaultdict(float) # Floating numbers to get an exact of what was spent
category_totals = defaultdict(float)

all_expenses = []  # Putting inside a list for all expenses

#Now i am processing rows

for row in range(2, sheet.max_row + 1): #the first month january starts in the 2nd row
    month = sheet[f'A{row}'].value
    category = sheet[f'B{row}'].value
    item = sheet[f'C{row}'].value
    cost = float(sheet[f'D{row}'].value)

    monthly_costs[month] += cost
    category_totals[category] += cost
    all_expenses.append((item, cost))



#TODO: MAKE CHARTS OF THE MONTHLY SPENDING, THE CATEGORIES, AND TOP 5 EXPENSES------------


#--------------------------------------------------------
# Top 5 Most expensive Items ----------------------------
top_expenses = sorted(all_expenses, key=lambda x: x[1], reverse=True)[:5]

print(top_expenses)

#---------------------------------Chart 1: Monthly Spending Bar Chart ---------------

months = list (monthly_costs.keys())  #This extracts month names
values = [monthly_costs[m] for m in months] #Gets corresponding costs for each month

plt.figure(figsize = (10, 5))  #Creates wide figure
plt.bar(months, values, color = 'skyblue') #Creates a bar chart of spending per month
plt.title("Monthly IT Spending (2024)") #This add the tile to the bar chart.
plt.ylabel("Cost ($)")  # Adds a y-axis labeled cost.
plt.axhline(y = 20000, color = 'red', linestyle ='--', label = 'Budget Limit ($20,000)') #This will draw a red dashed budget line
plt.legend() #Shows legend for the budget line
plt.tight_layout() #Makes sure it fits the layout to avoid cutoff.
plt.savefig("monthly_spendingchart.png") #Saves the chart as a png file
plt.close() #This closes the chart.
#-------------Chart 2: Pie-Chart-For-Each-Category-Spending-Percentage---------------------------------

labels = list(category_totals.keys()) #This gets list of category names from category totals keys not the value.
sizes = [category_totals[cat] for cat in labels] #Gets total spending for each category dollar amount spent for that certain category[cat]
plt.figure(figsize = (6, 6)) #This creates a square figure for a pie chart.
plt.pie(sizes, labels = labels, autopct = '%1.1f%%', startangle = 140) #This plots pie chart for percentages.
plt.title("Spending By Category") #This adds a title
plt.tight_layout() #This auto-adjusts layout to avoid cutoff.
#plt.show() #UNCOMMENT THIS IF YOU WOULD LIVE TO SEE IN IDE
plt.savefig("Category_Spending_PieChart.png")#Saves the pie chart.
plt.close() #Closes the piechart.

#-----------The-TOP-5-MOST-Expensive-Items------------------------------------------------------------

items =[item for item, _ in top_expenses] #Gets items from top 5 expenses. (e.g _ represents ignoring the cost section)
costs = [cost for _, cost in top_expenses] #GETS THE COST VALUES ONLY (e.g _ represents ignoring the items section)



plt.figure(figsize = (8, 4)) #Creates horizontal figure
plt.barh(items, costs, color = 'Purple') #Creates Horizontal bar Chart with a purple color.
plt.title("The Top 5 Most Expensive Items") #Adds Chart Title.
plt.xlabel("Cost ($)") #Labels the x-axis as cost.
plt.tight_layout() #Basically adjusts the chart layout so that it fits.
#plt.show()
plt.savefig("Top-5-Most-expensive-Items.png")
plt.close()