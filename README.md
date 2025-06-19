# 🖥️ IT Department Expense Analysis (Jan–Dec 2024)

This project simulates a real-world scenario for an **IT Analyst** tasked with analyzing and improving their department’s equipment and product management spending using Python and Excel.

## 📌 Project Overview

- Analyze IT spending using a Python script and Excel data from January to December 2024.
- Identify monthly and category-based costs.
- Automatically detect months that went over a $20,000/month budget.
- Generate insightful charts to visualize data trends.
- Offer strategic recommendations for cost-saving.

---

## 📂 What's Included

- `it_spending_2024.xlsx` — Simulated IT purchase data across all 12 months.
- `analyze_it_spending.py` — Python script to:
  - Load and process Excel data
  - Analyze spending by month and category
  - Identify top 5 most expensive items
  - Export 3 charts: Monthly Spend, Category Breakdown, Top Expenses
- PNG reports:
  - `monthly_spending.png`
  - `category_spending.png`
  - `top_expensive_items.png`

---

## 🔍 Key Questions from Management (with Answers)

### 📅 **Which months went over budget?**
> Based on the monthly spending chart, the following months exceeded the $20,000 limit:
**January, May, June, and July**

### 💸 **Which categories are the most expensive?**
> The top 5 categories are:
- Hardware
- Software
- Cloud Services
- Support Services
- Accessories

> The **most expensive** category is: **Support Services**

### 🔁 **Are there recurring costs we can negotiate or reduce?**
> It depends on what's most critical to the company's operations. 
To suggest cutbacks, leadership needs to clarify what tools/services are least essential.

### 🧾 **Which vendors or purchases could be consolidated?**
> One idea is to consolidate **Hardware and Accessories** since they fall under related purchases. 
Would that work for your strategy?

---

## 🎯 Department Goals

| Goal | Strategy |
|------|----------|
| 💰 Keep monthly spending under $20k | Identify and flag high-cost categories early each month |
| 🛠️ Plan for hardware-heavy months | Budget ahead for Q2/Q4 refresh cycles |
| 🧾 Suggest annual billing options | Consider annual licensing for software/cloud (often discounted) |
| 📊 Build dashboards by category | Maintain clean spreadsheets and tag items consistently |

---

## 📈 How This Helps

This system gives your IT department:

- A clear overview of monthly and annual financial performance
- Visual tools to present spending patterns
- Data-driven insights to back up cost-saving proposals
- A scalable script for ongoing use (just update the Excel sheet monthly)

---

## 💡 Want to Extend This?

- Export reports to PDF with embedded charts
- Build an interactive dashboard with Plotly or Dash
- Track vendor performance and delivery history
