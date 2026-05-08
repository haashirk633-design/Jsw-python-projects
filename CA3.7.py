# HASHIR , 12525400
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# File path
PATH = r"C:\Users\Dell\Downloads\jsw FINAL.REAL11.csv"

# Read CSV
df = pd.read_csv(PATH)

# Remove extra spaces in column names
df.columns = df.columns.str.strip()

# Print column names
print(df.columns)

# Convert numeric columns
columns = ['Fixed Assets', 'Investments', 'Borrowings',
           'Reserves', 'Total Liabilities']

for col in columns:
    df[col] = (
        df[col]
        .astype(str)
        .str.replace(',', '')
    )

    df[col] = pd.to_numeric(df[col], errors='coerce')

# Create heatmap
plt.figure(figsize=(8,6))

sns.heatmap(
    df[columns].corr(),
    annot=True,
    cmap='coolwarm',
    fmt='.2f'
)

plt.title('JSW Steel – Correlation Heatmap')

plt.tight_layout()

plt.show()