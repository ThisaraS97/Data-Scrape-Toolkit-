import pandas as pd

# Read the Excel file into a DataFrame
file_path = "/content/contactlist.xlsx"
df = pd.read_excel(file_path)

# Define the range of rows where you want to remove duplicates
start_row = 2
end_row = 1610

# Count the number of duplicates before removal
num_duplicates_before = df.duplicated(subset='Link Name (Links)').sum()

# Remove duplicates in the specified range (L2:L1610), keeping the last occurrence
df.drop_duplicates(subset='Link Name (Links)', keep='last', inplace=True)

# Count the number of duplicates after removal
num_duplicates_after = num_duplicates_before - df.duplicated(subset='Link Name (Links)').sum()

# Define the file path to save the updated Excel file in Colab files
updated_file_path = "/content/Updated_Contact_List.xlsx"

# Write the DataFrame to the updated file path
df.to_excel(updated_file_path, index=False)

print(f"{num_duplicates_after} duplicates removed. Updated file saved successfully.")
