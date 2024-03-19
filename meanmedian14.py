import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats

# Sample data
data = {
    'age': [25, 38, 46, 55, 28, 50, 38, 60, 71, 37, 55, 35, 25, 29, 31, 44, 18, 64],
    '%fat': [20, 25, 30, 28, 18, 33, 22, 35, 40, 26, 36, 23, 19, 21, 24, 32, 17, 38]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Calculate mean, median, and standard deviation
mean_age = df['age'].mean()
median_age = df['age'].median()
std_dev_age = df['age'].std()

mean_fat = df['%fat'].mean()
median_fat = df['%fat'].median()
std_dev_fat = df['%fat'].std()

# Draw boxplots
plt.figure(figsize=(10, 6))
df.boxplot(column=['age', '%fat'])
plt.title('Boxplots for Age and %Fat')
plt.ylabel('Value')
plt.show()

# Draw scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(df['age'], df['%fat'])
plt.title('Scatter Plot: Age vs %Fat')
plt.xlabel('Age')
plt.ylabel('%Fat')
plt.grid(True)
plt.show()

# Draw Q-Q plot
plt.figure(figsize=(8, 6))
stats.probplot(df['age'], dist="norm", plot=plt)
plt.title('Q-Q Plot: Age')
plt.xlabel('Theoretical Quantiles')
plt.ylabel('Sample Quantiles')
plt.grid(True)
plt.show()

plt.figure(figsize=(8, 6))
stats.probplot(df['%fat'], dist="norm", plot=plt)
plt.title('Q-Q Plot: %Fat')
plt.xlabel('Theoretical Quantiles')
plt.ylabel('Sample Quantiles')
plt.grid(True)
plt.show()

# Print the calculated statistics
print("Age Statistics:")
print("Mean:", mean_age)
print("Median:", median_age)
print("Standard Deviation:", std_dev_age)
print("\n%Fat Statistics:")
print("Mean:", mean_fat)
print("Median:", median_fat)
print("Standard Deviation:", std_dev_fat)
