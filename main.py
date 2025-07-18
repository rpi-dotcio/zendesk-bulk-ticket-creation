
"""
Zendesk Bulk Ticket Creation Tool

Directive: This is the main application file for the Windows 10 EOL project.
It reads data from the specified Excel file, processes it, and will eventually
create tickets in Zendesk.
"""

import argparse
import pandas as pd
import sys

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

def main():
    """Main function to drive the application."""
    parser = argparse.ArgumentParser(description="Zendesk Bulk Ticket Creation Tool for Win10 EOL.")
    parser.add_argument("--file", required=True, help="Path to the input Excel file (e.g., 'Win 10 EOL Assets.xlsx').")
    args = parser.parse_args()

    assets_df, employee_map_df = load_spreadsheet(args.file)

    if assets_df is not None and employee_map_df is not None:
        print("\n--- 'Assets' Sheet Head ---")
        print(assets_df.head())

        print("\n--- 'idp_Basic_Status' Sheet Head ---")
        print(employee_map_df.head())

        # Future phases will add processing logic here.
        print("\n--- Spreadsheet processing complete. ---")

if __name__ == "__main__":
    main()
