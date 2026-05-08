# HASHIR , 12525400
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

PATH = r"C:\Users\Dell\Downloads\jsw FINAL.REAL11.csv"

# Read CSV
df = pd.read_csv(PATH)

# Print all column names
print(df.columns)

# Correct column names from CSV
cols = ['Fixed Assets', 'Investments']   # change if needed

# Convert to long format
df_m = df[cols].melt(var_name='Type', value_name='Value')

# Create boxplot
sns.boxplot(x='Type', y='Value', data=df_m, palette='Set2')

plt.title('Fixed Assets vs Investments')
plt.show()