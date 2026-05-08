# HASHIR, 12525400
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# File path
PATH = r"C:\Users\Dell\Downloads\jsw FINAL.REAL11.csv"

# Read CSV
df = pd.read_csv(PATH)

# Convert Year column properly
df['Year'] = pd.to_datetime(df['Year'], format='%y-%b')

# Convert numeric columns
cols = ['Borrowings', 'Total Liabilities']

for col in cols:
    df[col] = df[col].astype(str).str.replace(',', '')
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Convert TAD to string for hue
df['TAD'] = df['TAD'].astype(str)

# Plot
sns.lmplot(
    x='Borrowings',
    y='Total Liabilities',
    data=df,
    hue='TAD',
    palette='Set1'
)

plt.title('Borrowings vs Liabilities by TAD')

plt.show()