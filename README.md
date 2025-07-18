**Directive: This document is the single source of truth for the project's goals and high-level overview. It must be updated whenever the project's scope or objectives change.**

# Zendesk Bulk Ticket Creation for Windows 10 EOL

## Project Overview

This project is a Python application designed to automate the creation of Zendesk tickets for the Windows 10 End-of-Life (EOL) remediation project at RPI. It reads device and user data from a spreadsheet, processes it according to defined business rules, and creates tickets in Zendesk via their API.

## Goals

*   Automate the creation of thousands of Zendesk tickets.
*   Ensure data integrity by mapping spreadsheet data to controlled fields in Zendesk.
*   Provide robust logging and error handling for verification.
*   Handle API rate limits gracefully.
*   Securely manage API credentials.

## Source Code

[https://github.com/rpi-dotcio/zendesk-bulk-ticket-creation](https://github.com/rpi-dotcio/zendesk-bulk-ticket-creation)

## Project Status

**Current Phase:** Phase 2: Core Logic and Testing
**Next Step:** Implement Requestor Logic

## Setup and Usage

1.  **Prerequisites:**
    *   Python 3
    *   `requests` library (`pip install requests`)
    *   `pandas` and `openpyxl` for spreadsheet processing (`pip install pandas openpyxl`)

2.  **Configuration:**
    *   Set the following environment variables with your Zendesk API credentials:
        *   `ZENDESK_API_TOKEN`
        *   `ZENDESK_USER_EMAIL`: kittet@rpi.edu
        *   `ZENDESK_SUBDOMAIN`: rpi-dotcio

3.  **Running the application:**
    ```bash
    python main.py --file 'Win 10 EOL Assets.xlsx'
    ```