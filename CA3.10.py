# HASHIR, 12525400Z
import pandas as pd
import numpy as np

# File path
PATH = r"C:\Users\Dell\Downloads\jsw FINAL.REAL11.csv"

# Read CSV
df = pd.read_csv(PATH)

# Convert Year column
df['Year'] = pd.to_datetime(df['Year'], format='%y-%b')

# Convert numeric columns
cols = ['Borrowings', 'Total Assets']

for col in cols:
    df[col] = df[col].astype(str).str.replace(',', '')
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Remove missing values
df = df.dropna(subset=cols)

# Get values
x = df['Borrowings'].values
y = df['Total Assets'].values

# Correlation
r = np.corrcoef(x, y)[0, 1]

# Interpretation
if r > 0.7:
    print('Debt-driven growth – REVIEW leverage')
elif r > 0.4:
    print('Moderate link – MONITOR borrowings')
else:
    print('Healthy – assets not debt-dependent')

print(f'Correlation = {r:.3f}')