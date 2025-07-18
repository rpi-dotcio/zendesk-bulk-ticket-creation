**Directive: This is the master Product Requirements Document. It is the single source of truth for what this application must do. All development work must align with these requirements. Any changes must be approved and logged in `DECISION_LOG.md`.**

# 1. Introduction & Goal

## 1.1. Goal
The goal of this project is to develop a secure, robust, and reliable Python application that automates the creation of Zendesk tickets to track and manage the remediation of thousands of Windows 10 devices facing End-of-Life (EOL).

## 1.2. Background
RPI College uses Zendesk for all help desk and IT tickets. A large number of Windows 10 machines must be remediated before their EOL date. This application will replace the manual process of tracking these devices in a shared spreadsheet, moving the project's source of truth into Zendesk.

# 2. User Personas

*   **Systems Engineer (Project Lead):** Responsible for running the application, monitoring its output, managing the GitHub repository, and overseeing the project's success.
*   **IT Technician:** The end-user of the tickets created by this application. They will use the tickets to perform the remediation work on the assigned devices.

# 3. Features & Requirements

## 3.1. Core Functionality
*   **File Input:** The application must read and process both `.xlsx` and `.csv` file formats.
*   **Ticket Creation:** The application will create Zendesk tickets using the Zendesk API.
*   **Configuration:** All sensitive data (API tokens, email, subdomain) must be loaded from environment variables, not hardcoded.

## 3.2. Ticket Content Requirements
*   **Assignment:** All created tickets must be assigned to the "Windows EOL" group.
*   **Tagging:**
    *   Every ticket must be tagged with "windows10eol".
    *   The system must allow for the addition of other tags as determined by the discovery phase (e.g., "staff", "academic_area").
*   **Requestor Logic:**
    *   The ticket requestor must be set to the device's user if that user is an "Employee".
    *   If the user is not an "Employee" or is not listed, the requestor must be a designated shared mailbox (created by Mare).
    *   **Action Item:** The definition of "Employee" is determined by a mapping in the `idd_basic_status` sheet of the `Win 10 EOL Assets.xlsx` file.
*   **Initial Email:** An initial notification email (content specified in "WIN 10 EOL Plan.pdf") must be sent to the user if they are an "Employee".
*   **Comment Data:**
    *   The first comment of the ticket must contain all technical details from the source spreadsheet, formatted as a readable list.
    *   A file containing the spreadsheet's column definitions must be attached to each ticket.

## 3.3. Technical Requirements
*   **Language:** Python 3.
*   **Security:** The application must be built with security as a top priority. No credentials shall be exposed in the code or logs.
*   **Error Handling:** The application must implement exceptional error handling, including network issues and API errors. It should fail gracefully and provide clear error messages.
*   **Logging:** A robust logging system must be implemented to track every action, success, and failure. Logs should be detailed and easy to parse.
*   **API Interaction:**
    *   The application must gracefully handle Zendesk API rate limits by respecting `429` status codes and `Retry-After` headers.
    *   Ticket creation should be done asynchronously for performance.
    *   The application must verify the success of asynchronous jobs via the `job_statuses` endpoint.

## 3.4. Development & Operations
*   **Version Control:**
    *   A new GitHub repository will be created for the project under the `RPI DotCIO` organization.
    *   All code changes must be committed to GitHub with clear, descriptive messages.
*   **Code Quality:** All code must be thoroughly commented, with professional file headers explaining the purpose of each module.
*   **Testing:** The application must include a "test mode" that allows for the creation and subsequent deletion of a single test ticket to verify functionality without impacting real data.

# 4. Rollout Plan
*   **Phase 1 (Initial):** The application will first be run only for devices that are already past their EOL date, as identified by the "EOL" value in the "Is_EOL_Date" column of the spreadsheet.
*   **Subsequent Phases:** Further rollout plans will be determined after the successful completion of Phase 1.

# 5. Success Metrics
*   **100% Ticket Creation:** All devices in the target spreadsheet batch have a corresponding ticket created in Zendesk.
*   **Error-Free Logs:** The application's logs show no unhandled errors for the production runs.
*   **Data Verification:** A spot-check of created tickets confirms that all data (requestor, tags, comments, attachments) is accurate and matches the requirements.
*   **Technician Acceptance:** IT Technicians confirm that the tickets contain all the necessary information to perform their work.

# 6. Out of Scope
*   A graphical user interface (GUI) for the application.
*   Handling EOL projects for systems other than Windows 10.
*   Direct modification of the input spreadsheet.
*   Real-time monitoring of device status post-ticket-creation.
