import numpy as np
import matplotlib.pyplot as plt

# Mock dataset
years = [2015, 2016, 2017, 2018, 2019]
smoking_patients = [25, 30, 35, 40, 55]
lung_cancer_patients = [200, 220, 240, 260, 300]

# Calculate the correlation coefficient between smoking patients and lung cancer patients
correlation_coefficient = np.corrcoef(smoking_patients, lung_cancer_patients)[0, 1]

# Create a scatter plot of the data
plt.figure(figsize=(8, 6))
plt.scatter(smoking_patients, lung_cancer_patients, color='red')
plt.title('Correlation between Smoking Patients and Lung Cancer Patients')
plt.xlabel('Smoking Patients')
plt.ylabel('Lung Cancer Patients')
plt.grid(True)
plt.show()

# Print the correlation coefficient
print("Correlation Coefficient between Smoking Patients and Lung Cancer Patients:", correlation_coefficient)
