import pandas as pd

# 1. Dataset Load
df = pd.read_csv('internship_data.csv')

# 2. Duplicate Removal
df = df.drop_duplicates()

# 3. Handle Missing Values in Duration
# Agar duration missing hai to median duration (3 months) se fill karein
median_duration = df['Internship_Duration_Months'].median()
df['Internship_Duration_Months'] = df['Internship_Duration_Months'].fillna(median_duration)

# 4. Handle Outliers
# Agar koi 12 mahino se zyada ki internship daal raha hai (e.g., 24), wo outlier hai
# Hum 12 mahino se zyada walo ko hata denge ya cap kar denge
df = df[df['Internship_Duration_Months'] <= 12]

# 5. Standardize Major
df['Major'] = df['Major'].str.upper()

print("--- Successfully Cleaned Internship Data ---")
print(df)