import pandas as pd

# 1. Load dataset
df = pd.read_csv("C:/Users/rupal/OneDrive/Desktop/Labmentix Internship/4th project - Real Estate Investment Advisor (12 Dec 2025)/real_estate_project/data/india_housing_prices.csv")

# 2. Show first 5 rows
print("First 5 rows:")
print(df.head())

# 3. Check missing values
print("\nMissing values:")
print(df.isnull().sum())

# 4. Fill missing numerical values with median
for col in df.select_dtypes(include=['int64', 'float64']).columns:
    df[col] = df[col].fillna(df[col].median())

# 5. Fill missing text values with mode
for col in df.select_dtypes(include=['object']).columns:
    df[col] = df[col].fillna(df[col].mode()[0])

# 6. Remove duplicate rows
df = df.drop_duplicates()

# 7. Create new feature: Price per SqFt
df["Price_per_SqFt"] = df["Price_in_Lakhs"] * 100000 / df["Size_in_SqFt"]

# 8. Save cleaned data
df.to_csv("C:/Users/rupal/OneDrive/Desktop/Labmentix Internship/4th project - Real Estate Investment Advisor (12 Dec 2025)/real_estate_project/data/cleaned_data.csv", index=False)

print("\n✅ Data Cleaning Completed. Cleaned file saved.")