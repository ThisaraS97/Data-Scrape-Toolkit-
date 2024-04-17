import pandas as pd

#This script reads the "reorder updated.xlsx" file and prints the number of unique values in the "ID" column.
# Load the CSV file into a DataFrame
df = pd.read_excel("reorder updated.xlsx")

# Check the unique count in the "ID" column
unique_count = df["ID"].nunique()

print("Number of unique values in the 'ID' column:", unique_count)
