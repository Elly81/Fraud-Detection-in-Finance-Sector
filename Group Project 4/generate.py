import pandas as pd

# Sample data for the Excel file
data = {
    'distance_from_home': [5.0, 2.5, 10.0],
    'distance_from_last_transaction': [1.0, 3.0, 4.0],
    'ratio_to_median_purchase_price': [0.8, 1.2, 0.5],
    'repeat_retailer': [1, 0, 1],
    'used_chip': [1, 0, 1],
    'used_pin_number': [1, 0, 0],
    'online_order': [0, 1, 1]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Define the file path
file_path = 'sample_transactions.xlsx'

# Save the DataFrame to an Excel file
df.to_excel(file_path, index=False)

print(f"Sample Excel file has been created: {file_path}")
