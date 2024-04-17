import pandas as pd

def clean_phone_number(phone_number):
    """
    Clean the phone number by removing any symbols or letters.
    """
    return ''.join(filter(str.isdigit, str(phone_number)))

def process_excel(input_file, output_file):
    """
    Process the Excel file containing phone numbers.
    """
    # Read the Excel file
    df = pd.read_excel(input_file)

    # Clean the phone numbers
    df['Cleaned Mobile Number'] = df['Mobile No'].apply(clean_phone_number)

    # Write the cleaned data to a new Excel file
    df.to_excel(output_file, index=False)

    print("Processing complete. Cleaned data saved to", output_file)

# Example usage:
input_file_path = 'mobile number.xlsx'
output_file_path = 'cleaned_mobile_numbers.xlsx'

process_excel(input_file_path, output_file_path)
