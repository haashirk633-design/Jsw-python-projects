# hashir, 12525400
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

PATH = r"C:\Users\Dell\Downloads\jsw FINAL.REAL11.csv"

# Read CSV
df = pd.read_csv(PATH)

# Remove spaces in column names
df.columns = df.columns.str.strip()

# Convert Year column
df['Year'] = pd.to_datetime(df['Year'], format='%b-%y')
# Convert numeric columns
df['Equity Capital'] = pd.to_numeric(df['Equity Capital'], errors='coerce')

df['Reserves'] = (
    df['Reserves']
    .astype(str)
    .str.replace(',', '')
)

df['Reserves'] = pd.to_numeric(df['Reserves'], errors='coerce')

# Remove invalid rows
df = df.dropna()

# X-axis positions
x = np.arange(len(df))

# Create graph
plt.figure(figsize=(10,6))

plt.bar(x - 0.2,
        df['Equity Capital'],
        width=0.4,
        label='Equity Capital')

plt.bar(x + 0.2,
        df['Reserves'],
        width=0.4,
        label='Reserves')

# Labels
plt.xticks(x, df['Year'].dt.year)

plt.title('Equity Capital vs Reserves')
plt.xlabel('Year')
plt.ylabel('Amount')

plt.legend()

plt.tight_layout()
plt.show()