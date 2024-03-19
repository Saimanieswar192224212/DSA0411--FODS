import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Sample dataset
data = {
    'Age': [25, 30, 35, 40, 45],
    'Salary': [50000, 60000, 70000, 80000, 90000]
}

# Create a DataFrame from the sample dataset
df = pd.DataFrame(data)

# Calculate correlation matrix
correlation_matrix = df.corr()

# Calculate covariance matrix
covariance_matrix = df.cov()

# Plot correlation heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)
plt.title('Correlation Plot of Age and Salary')
plt.show()

# Print correlation matrix and covariance matrix
print("Correlation Matrix:")
print(correlation_matrix)
print("\nCovariance Matrix:")
print(covariance_matrix)
