import pandas as pd
import sys
import os

def should_select(row):
    year = row['Year']
    cites = row['Cites']
    current_year = 2025
    age = current_year - year
    
    # Define thresholds based on publication year ranges
    if 7 <= age <= 10:  # Papers from 2015 to 2018
        return cites > 10
    elif 5 <= age <= 7:  # Papers from 2018 to 2020
        return cites > 7
    elif 3 <= age <= 5:  # Papers from 2020 to 2022
        return cites > 5
    elif 0 <= age <= 3:  # Papers from 2022 to 2025
        return cites > 0
    else:
        return False

def process_csv(input_file):
    # Read the CSV file
    df = pd.read_csv(input_file)

    # Select rows based on citation and year criteria
    selected_df = df[df.apply(should_select, axis=1)]

    # Columns to remove
    columns_to_remove = [
        "Abstract", "Age",
        "FullTextURL", "RelatedURL", "Publisher", "ArticleURL", "CitesURL",
        "QueryDate", "Type", "DOI", "ISSN", "CitationURL", "Volume", "Issue",
        "StartPage", "EndPage"
    ]

    # Drop specified columns, ignore if not present
    selected_df = selected_df.drop(columns=columns_to_remove, errors='ignore')

    # Identify and remove columns that are entirely empty (all NaN or all empty strings)
    empty_cols = [col for col in selected_df.columns if selected_df[col].isna().all() or (selected_df[col] == '').all()]
    selected_df = selected_df.drop(columns=empty_cols)

    # Sort: by Year descending, then Cites descending, then Title ascending
    selected_df = selected_df.sort_values(by=['Year', 'Cites', 'Title'], ascending=[False, False, True])

    return selected_df

def main():
    # Check if file name is provided
    if len(sys.argv) != 2:
        print("Usage: python main.py <input_csv_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = "processed.csv"

    # Check if input file exists
    if not os.path.exists(input_file):
        print(f"Error: Input file '{input_file}' does not exist.")
        sys.exit(1)

    # Process the CSV
    processed_df = process_csv(input_file)

    # Check if output file exists
    if os.path.exists(output_file):
        response = input(f"Output file '{output_file}' already exists. Do you want to overwrite it? (y/yes to overwrite, any other key to exit): ").strip().lower()
        if response not in ['y', 'yes']:
            print("Operation cancelled. Exiting without saving.")
            sys.exit(0)

    # Save to new CSV
    processed_df.to_csv(output_file, index=False)
    print(f"Processed data saved to '{output_file}'.")

if __name__ == "__main__":
    main()