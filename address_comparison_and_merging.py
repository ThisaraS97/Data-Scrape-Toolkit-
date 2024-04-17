import pandas as pd

# Read the first Excel file ("Updated Address")
updated_address_df = pd.read_excel("Updated Address.xlsx")

# Read the second Excel file ("docc")
docc_df = pd.read_excel("docc.xlsx")

# Merge the DataFrames on the combination of "Title" and "Address Title"
merged_df = pd.merge(updated_address_df, docc_df, on=["Title", "Address Title"], how="outer", suffixes=('_Updated_Address', '_docc'))

# Filter out rows where the address does not match
mismatched_addresses = merged_df[merged_df["Address_Updated_Address"] != merged_df["Address_docc"]]

# Display the mismatches
print("Mismatched Addresses:")
print(mismatched_addresses)

# Save the mismatched addresses to a new Excel file
mismatched_addresses.to_excel("mismatched_addresses.xlsx", index=False)
