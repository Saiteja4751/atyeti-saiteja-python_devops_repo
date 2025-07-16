import pandas as pd

# Load the CSV file
def filter_function():
    df = pd.read_csv("~/ip_files/summer.csv")

    # Filter rows with Year between 1949 and 1990 and Gender == 'Men'
    filtered_df = df[(df['Year'] >= 1949) & (df['Year'] <= 1990) & (df['Gender'] == 'Men')]

    # Show the first few rows (optional)
    print(filtered_df.head())

    # Save the filtered data to a new CSV file (optional)
    filtered_df.to_csv("~/op_files/updated_filter_data.csv")