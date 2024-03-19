import numpy as np
import matplotlib.pyplot as plt

# Sample data: monthly sales and advertising spending
sales_data = np.array([100, 120, 130, 150, 160, 180, 200, 210, 220, 240, 250, 270])
advertising_data = np.array([50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160])

# Calculate the correlation coefficient between sales and advertising
correlation_coefficient = np.corrcoef(sales_data, advertising_data)[0, 1]

# Create a scatter plot of the data
plt.figure(figsize=(8, 6))
plt.scatter(advertising_data, sales_data, color='blue')
plt.title('Correlation between Sales and Advertising Spending')
plt.xlabel('Advertising Spending')
plt.ylabel('Sales')
plt.grid(True)
plt.show()

# Print the correlation coefficient
print("Correlation Coefficient between Sales and Advertising:", correlation_coefficient)
