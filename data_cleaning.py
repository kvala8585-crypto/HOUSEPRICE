import pandas as pd
import os

# Path
base_path = r"C:\Users\kavi vala\Desktop\HOUSEPRICE"
data_path = os.path.join(base_path, "data", "Housing.csv")

# Load data
df = pd.read_csv(data_path)

# -------------------------
# Data Cleaning
# -------------------------

# Check missing values
df.drop_duplicates(inplace=True)

# Convert categorical columns to numeric
binary_cols = [
    'mainroad', 'guestroom', 'basement',
    'hotwaterheating', 'airconditioning',
    'prefarea'
]

for col in binary_cols:
    df[col] = df[col].map({'yes': 1, 'no': 0})

# Furnishing status encoding
df['furnishingstatus'] = df['furnishingstatus'].map({
    'unfurnished': 0,
    'semi-furnished': 1,
    'furnished': 2
})

# -------------------------
# Feature Engineering
# -------------------------

# Price per square feet
df['price_per_sqft'] = df['price'] / df['area']

# Total rooms
df['total_rooms'] = df['bedrooms'] + df['bathrooms']

# Save cleaned data
clean_path = os.path.join(base_path, "data", "housing_cleaned.csv")
df.to_csv(clean_path, index=False)

print("✅ Data Cleaning Completed Successfully")
print("✅ Cleaned file saved as housing_cleaned.csv")
