import pandas as pd

# Load your Excel file into a pandas DataFrame
df = pd.read_excel("test.xlsx")

# Specify the column name you want to calculate unique items for
column_name = "ID"

# Count unique items while skipping duplicates
unique_counts = df[~df.duplicated(subset=[column_name])][column_name].value_counts()

# Create a new DataFrame from the unique counts
output_df = pd.DataFrame({"Unique Item": unique_counts.index, "Count": unique_counts.values})

# Specify the path for the new Excel file
output_file = "output.xlsx"

# Write the DataFrame to a new Excel file
output_df.to_excel(output_file, index=False)

print(f"Output saved to {output_file}")
