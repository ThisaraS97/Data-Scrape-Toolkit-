import pandas as pd

# Read the two Excel files
file1 = "doc.xlsx"
file2 = "doc2.xlsx"

# Load Excel files into pandas dataframes
df1 = pd.read_excel(file1)
df2 = pd.read_excel(file2)

# Convert names to lowercase for case-insensitive matching
df1['Name_lower'] = df1['Name'].str.lower()
df2['Name_lower'] = df2['Name'].str.lower()

# Find duplicates based on lowercase names
duplicates = df1[df1['Name_lower'].isin(df2['Name_lower'])]

# Drop the lowercase name column
duplicates.drop(columns=['Name_lower'], inplace=True)

# Save duplicates to a new Excel file
output_file = "duplicates.xlsx"
duplicates.to_excel(output_file, index=False)

print("Duplicates saved to", output_file)
