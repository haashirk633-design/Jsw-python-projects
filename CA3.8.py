# hashir, 12525400
import pandas as pd
import matplotlib.pyplot as plt

# File path
PATH = r'C:\Users\Dell\Downloads\jsw FINAL.REAL11.csv'

# Read CSV
df = pd.read_csv(PATH)

# Convert Year column
df['Year'] = pd.to_datetime(df['Year'], format='%y-%b')

# Columns used in pie chart
labels = ['Fixed Assets', 'CWIP', 'Investments', 'Other Assets']

# Remove commas and convert to numeric
for col in labels:
    df[col] = df[col].astype(str).str.replace(',', '')
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Get latest row
latest = df.iloc[-1]

# Values for pie chart
values = [latest[col] for col in labels]

# Plot pie chart
plt.figure(figsize=(8, 8))

plt.pie(
    values,
    labels=labels,
    autopct='%1.1f%%',
    startangle=140
)

plt.title(f'Asset Mix – {latest["Year"].year}')

plt.show()


