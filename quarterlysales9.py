import numpy as np

# Sample sales data (assuming a 1D NumPy array with sales for each quarter)
sales_data = np.array([10000, 12000, 14000, 16000])  # Replace this with your actual sales data

# Step 1: Calculate total sales for the year
total_sales_year = np.sum(sales_data)

# Step 2: Calculate percentage increase in sales from Q1 to Q4
sales_q1 = sales_data[0]
sales_q4 = sales_data[-1]
percentage_increase = ((sales_q4 - sales_q1) / sales_q1) * 100

# Print the results
print("Total sales for the year:", total_sales_year)
print("Percentage increase in sales from Q1 to Q4:", percentage_increase)
