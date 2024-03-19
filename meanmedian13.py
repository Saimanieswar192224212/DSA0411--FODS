import numpy as np
from scipy import stats

# Sample purchase amounts (replace with your actual data)
purchase_amounts = np.array([50, 60, 70, 80, 90, 100, 90, 80, 70, 60, 50, 50, 50, 60, 60])

# Calculate the mean (average) purchase amount
mean_purchase_amount = np.mean(purchase_amounts)

# Identify the mode of the purchase amounts
mode_result = stats.mode(purchase_amounts)
if isinstance(mode_result.mode, np.ndarray):
    mode_purchase_amount = mode_result.mode[0]
else:
    mode_purchase_amount = mode_result.mode

# Print the results
print("Mean (Average) Purchase Amount:", mean_purchase_amount)
print("Mode of Purchase Amounts:", mode_purchase_amount)
