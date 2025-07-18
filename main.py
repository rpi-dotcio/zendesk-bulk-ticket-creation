"""
Zendesk Bulk Ticket Creation Tool

Directive: This is the main application file for the Windows 10 EOL project.
It reads data from the specified Excel file, processes it, and will eventually
create tickets in Zendesk.
"""

import argparse
import pandas as pd
import sys
import numpy as np

def load_spreadsheet(file_path):
    """
    Loads the necessary sheets from the specified Excel file.

    Args:
        file_path (str): The path to the .xlsx file.

    Returns:
        tuple: A tuple containing the assets_df and employee_map_df DataFrames,
               or (None, None) if an error occurs.
    """
    print(f"--- Loading Spreadsheet: {file_path} ---")
    try:
        # Read the specific sheets into pandas DataFrames
        assets_df = pd.read_excel(file_path, sheet_name='Assets')
        employee_map_df = pd.read_excel(file_path, sheet_name='idp_Basic_Status')
        print("Successfully loaded 'Assets' and 'idp_Basic_Status' sheets.")
        return assets_df, employee_map_df
    except FileNotFoundError:
        print(f"Error: The file was not found at {file_path}", file=sys.stderr)
        return None, None
    except Exception as e:
        # Catches other potential errors like missing sheets
        print(f"An error occurred while reading the Excel file: {e}", file=sys.stderr)
        return None, None

def create_employee_map(employee_map_df):
    """
    Creates a mapping from idp_Basic_Status to a boolean is_employee flag.

    Args:
        employee_map_df (pd.DataFrame): The DataFrame from the 'idp_Basic_Status' sheet.

    Returns:
        dict: A dictionary mapping the status to a boolean.
    """
    print("\n--- Creating Employee Status Map ---")
    # The second column (Unnamed: 1) contains the 'Employee' flag.
    # We fill NaN values with False to ensure every status has a boolean.
    employee_map_df['is_employee'] = employee_map_df.iloc[:, 1].apply(lambda x: x == 'Employee')
    # The first column (0) contains the status name.
    employee_map = pd.Series(employee_map_df.is_employee.values, index=employee_map_df.iloc[:, 0]).to_dict()
    print("Employee map created successfully.")
    return employee_map

def main():
    """Main function to drive the application."""
    parser = argparse.ArgumentParser(description="Zendesk Bulk Ticket Creation Tool for Win10 EOL.")
    parser.add_argument("--file", required=True, help="Path to the input Excel file (e.g., 'Win 10 EOL Assets.xlsx').")
    args = parser.parse_args()

    assets_df, employee_map_df = load_spreadsheet(args.file)

    if assets_df is not None and employee_map_df is not None:
        print("\n--- Data Summary for 'idp_Basic_Status' column ---")
        total_rows = len(assets_df)
        non_empty_rows = assets_df['idp_Basic_Status'].notna().sum()
        empty_rows = total_rows - non_empty_rows
        percentage_filled = (non_empty_rows / total_rows) * 100 if total_rows > 0 else 0

        print(f"Total rows in Assets sheet: {total_rows}")
        print(f"Rows with a value in 'idp_Basic_Status': {non_empty_rows}")
        print(f"Rows without a value in 'idp_Basic_Status': {empty_rows}")
        print(f"Percentage of rows with a value: {percentage_filled:.2f}%")

        employee_map = create_employee_map(employee_map_df)

        # Apply the mapping to the Assets DataFrame
        assets_df['is_employee'] = assets_df['idp_Basic_Status'].map(employee_map)

        print("\n--- Assets DataFrame Columns ---")
        for col in assets_df.columns:
            print(f"- {col}")

        # Future phases will add processing logic here.
        print("\n--- Spreadsheet processing complete. ---")

if __name__ == "__main__":
    main()