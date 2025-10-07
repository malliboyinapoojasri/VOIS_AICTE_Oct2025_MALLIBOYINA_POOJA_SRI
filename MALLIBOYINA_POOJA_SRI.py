# 1️⃣ Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Display settings
pd.set_option('display.max_columns', None)

print("\n🚀 Airbnb Hotel Booking Analysis Project Started...\n")

# 2️⃣ Load Dataset
file_path = "1730285881-Airbnb_Open_Data.xlsx"
df = pd.read_excel(file_path)
print("✅ Dataset Loaded Successfully!\n")

# Show basic info
print("📊 Dataset Information:")
print(df.info())

print("\n🧾 First 5 Rows of Data:")
print(df.head())

# 3️⃣ Data Cleaning
print("\n🧹 Data Cleaning...")

# Remove duplicates
df.drop_duplicates(inplace=True)

# Handle missing values
df.fillna({
    'Name': 'Unknown',
    'country': 'Unknown',
    'price': df['price'].mean()
}, inplace=True)

# Convert dates if available
for col in df.columns:
    if 'date' in col.lower():
        df[col] = pd.to_datetime(df[col], errors='coerce')

print("✅ Missing values handled & data cleaned.\n")

# 4️⃣ Basic Dataset Overview
print("📈 Dataset Summary:")
print(df.describe())

# 5️⃣ Exploratory Data Analysis (EDA)

# Example 1: Top 10 most common room types
plt.figure(figsize=(8,5))
sns.countplot(data=df, x='room type', order=df['room type'].value_counts().index, palette='viridis')
plt.title('Most Common Room Types on Airbnb')
plt.xlabel('Room Type')
plt.ylabel('Count')
plt.tight_layout()
plt.show()

# Example 2: Average Price by Room Type
plt.figure(figsize=(8,5))
sns.barplot(data=df, x='room type', y='price', estimator=np.mean, ci=None, palette='coolwarm')
plt.title('Average Price by Room Type')
plt.xlabel('Room Type')
plt.ylabel('Average Price ($)')
plt.tight_layout()
plt.show()

# Example 3: Price Distribution
plt.figure(figsize=(8,5))
sns.histplot(df['price'], bins=50, kde=True)
plt.title('Price Distribution of Airbnb Listings')
plt.xlabel('Price ($)')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# Example 4: Correlation Heatmap
plt.figure(figsize=(10,6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='Blues')
plt.title('Correlation Between Numerical Features')
plt.tight_layout()
plt.show()

# Example 5: Top 10 Hosts by Listing Count
if 'host_name' in df.columns:
    top_hosts = df['host_name'].value_counts().head(10)
    plt.figure(figsize=(10,5))
    sns.barplot(x=top_hosts.values, y=top_hosts.index, palette='magma')
    plt.title('Top 10 Hosts by Number of Listings')
    plt.xlabel('Number of Listings')
    plt.ylabel('Host Name')
    plt.tight_layout()
    plt.show()

# 6️⃣ Insights and Results
print("\n📌 PROJECT INSIGHTS:")
print("1️⃣ Most common room type is:", df['room_type'].mode()[0])
print("2️⃣ Average Airbnb price is approximately: ${:.2f}".format(df['price'].mean()))
if 'country' in df.columns:
    print("3️⃣ Dataset contains listings from:", df['country'].nunique(), "countries.")

print("\n🎯 PROJECT COMPLETED SUCCESSFULLY!")
print("Now take 3 screenshots of your results and graphs for PPT.\n")

# End of Code
