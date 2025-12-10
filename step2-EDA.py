import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned data
df = pd.read_csv("C:/Users/rupal/OneDrive/Desktop/Labmentix Internship/4th project - Real Estate Investment Advisor (12 Dec 2025)/real_estate_project/data/cleaned_data.csv")

# 1. Dataset info
print("\nDataset Info:")
print(df.info())

# 2. Dataset summary
print("\nDataset Summary:")
print(df.describe())

# 3. Price Distribution
plt.figure()
sns.histplot(df["Price_in_Lakhs"], bins=30)
plt.title("Price Distribution")
plt.show()

# 4. Size vs Price
plt.figure()
sns.scatterplot(x=df["Size_in_SqFt"], y=df["Price_in_Lakhs"])
plt.title("Size vs Price")
plt.show()

# 5. Property type count
plt.figure()
sns.countplot(x=df["Property_Type"])
plt.xticks(rotation=45)
plt.title("Property Type Count")
plt.show()

# 6. Correlation Heatmap
numeric_data = df.select_dtypes(include=['int64', 'float64'])
plt.figure()
sns.heatmap(numeric_data.corr())
plt.title("Correlation Heatmap")
plt.show()
