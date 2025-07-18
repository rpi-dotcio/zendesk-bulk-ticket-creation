**Directive: This document is the single source of truth for the project's data structures. It must be updated if the source spreadsheet changes.**

# Data Dictionary for `Win 10 EOL Assets.xlsx`

This document describes the structure and purpose of the `Win 10 EOL Assets.xlsx` spreadsheet, which is the primary data source for this project.

## 1. Sheets Overview

The spreadsheet contains the following sheets:

*   **`Assets`**: The main data sheet containing one row per device to be remediated. This is the primary source for ticket creation.
*   **`idd_basic_status`**: A reference sheet that contains all unique values for the `idp_Basic_Status` column from the `Assets` sheet. It also contains a mapping that defines which statuses correspond to an "Employee".
*   **`IDP_Status`**: A reference sheet that contains all unique values for the more detailed `idp_Status` column from the `Assets` sheet.
*   **`Column Definitions`**: A sheet that provides definitions for each column header in the `Assets` sheet. The content of this sheet will be attached to each created ticket.

## 2. Key Data Mappings

### 2.1. Employee Status

*   **Source:** `idd_basic_status` sheet.
*   **Logic:** This sheet will be used to determine if a user associated with a device is an "Employee". The application will read this sheet to understand which `idp_Basic_Status` values signify that the user is an employee.
*   **Application:** This mapping is critical for the **Requestor Logic** defined in the `PRD.md`.

### 2.2. Department Area

*   **Source Columns:** `idp_Basic_Status` and `idp_Status` from the `Assets` sheet.
*   **Logic:** These columns will be used to populate the custom `DepartmentArea` field in Zendesk. A mapping will be implemented to reduce the number of unique values and ensure data consistency.
*   **Application:** This logic will be part of the ticket creation process.
