import pandas as pd

# Load a CSV file containing numeric and non-numeric data
def load_data(file_path):
        try:
            data = pd.read_csv(file_path)
            return data
        except exception as e:
            print("failed to")
        
        

# Process data: Clean and normalize a specific column
def process_data(data):

    print(f'input\n{data}')
    # Convert 'values' column to numeric, forcing non-numeric data to NaN
    try:
        data['values'] = pd.to_numeric(data['values'], errors='coerce')
    except TypeError:
        print(f'list of data`s values\n{data['values']}')
    # Drop missing or NaN values from the 'values' column
    cleaned_data = data.dropna(subset=['values'])
    print(f'data after cleanning is\n{cleaned_data}')
    # Normalize the 'values' column
    max_value = cleaned_data['values'].max()
    print(f'max value is\n{max_value}')
    return cleaned_data['values'] / max_value 

# Main function to run the data pipeline
def main():
    file_path = 'data.csv'  # Example file path
    data = load_data(file_path)
    normalized_values = process_data(data)
    print(normalized_values)

if __name__ == '__main__':
# Run the main function
    main()
