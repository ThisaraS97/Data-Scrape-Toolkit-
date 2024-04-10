import pandas as pd

# Read the first Excel file
import_df = pd.read_excel("import_sample.xlsx")

# Read the second Excel file
live_df = pd.read_excel("live_sample.xlsx")

# Extract the 'LinkNameAddressLine1' column from the first file
import_column = import_df['Name']

# Check if any value in the 'LinkNameAddressLine1' column of the second file exists in the first file
for value in live_df['LinkNameAddressLine1']:
    if value in import_column.values:
        print(f"'{value}' exists in the first file.")
    else:
        print(f"'{value}' does not exist in the first file.")
