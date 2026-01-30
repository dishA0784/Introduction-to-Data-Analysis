import pandas as pd

# ---------------------------------
# Day 1: Load the dataset
# ---------------------------------
df = pd.read_csv("sales_data.csv")

# ---------------------------------
# Day 2: Explore the data
# ---------------------------------
print("🔍 DATA OVERVIEW")
print("Shape of dataset:", df.shape)
print("\nColumn Names:")
print(df.columns)
print("\nData Types:")
print(df.dtypes)

# ---------------------------------
# Day 3: Clean the data
# ---------------------------------

# Check missing values
print("\nMissing Values Before Cleaning:")
print(df.isnull().sum())

# Fill missing numeric values with 0
df['Quantity'].fillna(0, inplace=True)
df['Price'].fillna(0, inplace=True)

# Recalculate Total_Sales if missing
df['Total_Sales'].fillna(df['Quantity'] * df['Price'], inplace=True)

# Remove duplicate rows
df.drop_duplicates(inplace=True)

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# ---------------------------------
# Day 4: Analyze Sales
# ---------------------------------

# Metric 1: Total Sales Revenue
total_revenue = df['Total_Sales'].sum()

# Metric 2: Best-Selling Product (by revenue)
best_selling_product = (
    df.groupby('Product')['Total_Sales']
    .sum()
    .sort_values(ascending=False)
    .idxmax()
)

# Metric 3: Average Order Value
average_order_value = df['Total_Sales'].mean()

# Metric 4: Total Quantity Sold
total_quantity_sold = df['Quantity'].sum()

# Metric 5: Revenue by Region
revenue_by_region = df.groupby('Region')['Total_Sales'].sum()

# ---------------------------------
# Day 5: Create Report Output
# ---------------------------------

print("\n📊 SALES ANALYSIS REPORT")
print("-" * 40)
print(f"Total Revenue: ₹{total_revenue:,.2f}")
print(f"Best-Selling Product: {best_selling_product}")
print(f"Average Order Value: ₹{average_order_value:,.2f}")
print(f"Total Quantity Sold: {total_quantity_sold}")

print("\n📍 Revenue by Region:")
print(revenue_by_region)
