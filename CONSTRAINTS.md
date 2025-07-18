**Directive: This document is the definitive source for all project constraints. Any changes to these constraints must be approved and documented here.**

# Project Constraints and Requirements

This document outlines the specific constraints and requirements for the project as defined by the user.

### General

*   **Language:** Python
*   **Input:** `.xlsx` and `.csv` files.
*   **Security:** The application must be "extremely secure". API tokens must not be hardcoded.
*   **Logging:** The application needs "professionally/expertly logged" output with a "robust logging system".
*   **Error Handling:** Must use "exceptional error handling and exception handling".
*   **Code Quality:** Code must be well-commented, with clear file headers that "explain everything fully".

### Ticket Creation Logic

*   **Group:** Tickets will be assigned to the "Windows EOL" group.
*   **Tags:**
    *   All tickets must have the "windows10eol" tag.
    *   The application should be able to assign other tags as needed. A discovery step is required to determine what other tags should be assigned.
*   **Requestor:**
    *   If a user is listed for a device and is an "Employee", set them as the requestor.
    *   The definition of "Employee" needs to be clarified with the business team.
    *   If the user is not an employee or no user is listed, the requestor should be set to a shared mailbox (created by Mare).
*   **Initial Message to User:**
    *   If the requestor is an "Employee", an initial email should be sent.
    *   The content of this email is defined in the "WIN 10 EOL Plan.pdf".
*   **Comment Data:**
    *   All technical details from the spreadsheet should be included in the first comment of the ticket, formatted as a list for readability.
    *   The column definition sheet from the spreadsheet should be included as a ticket attachment.

### Development and Deployment

*   **Phased Approach:** The project should not be done "all in one-shot". A slow, methodical, and professional approach is required.
*   **GitHub:**
    *   The project must be stored in the `RPI DotCIO` GitHub repository.
    *   A new repository should be created for this project.
    *   Every major change must be documented and committed to GitHub for version control and rollback capabilities.
*   **Testing:**
    *   The application must have a test mode to create and then remove test tickets for verification.

### Rollout

*   The initial rollout will target only the tickets that are already past their EOL date, as specified in the "Is_EOL_Date" column of the spreadsheet.