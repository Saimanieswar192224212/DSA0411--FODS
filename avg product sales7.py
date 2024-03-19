import numpy as np

# Sample sales data (3x3 matrix)
sales_data = np.array([[100, 150, 200],
                       [120, 180, 220],
                       [90, 130, 170]])

# Step 1: Calculate total sales for each product (sum of sales for each column)
total_sales_per_product = np.sum(sales_data, axis=0)

# Step 2: Calculate average sales price for each product
num_sales_per_product = sales_data.shape[0]  # Number of sales for each product (assuming each row represents a sale)
average_price_per_product = total_sales_per_product / num_sales_per_product

# Step 3: Calculate overall average price (average of average prices of all products)
overall_average_price = np.mean(average_price_per_product)

print("Average price of all products sold in the past month:", overall_average_price)
