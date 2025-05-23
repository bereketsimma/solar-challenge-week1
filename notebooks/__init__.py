import pandas as pd

# Load the dataset
df = pd.read_csv('path_to_your_data.csv')
 
# Summary statistics
print(df.describe())

# Check for missing values
print(df.isna().sum())

# Detecting outliers (Z-score)
from scipy.stats import zscore
df['z_ghi'] = zscore(df['GHI'])
df_outliers = df[df['z_ghi'].abs() > 3]
print("Outliers in GHI:", df_outliers)


