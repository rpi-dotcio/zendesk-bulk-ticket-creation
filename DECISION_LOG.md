**Directive: This document logs all significant project decisions. Each entry must include the date, the decision made, and the rationale.**

# Decision Log

### 2025-07-18

*   **Decision:** Created a set of markdown files (`README.md`, `PLAN.md`, `ZENDESK_API_NOTES.md`, `CONSTRAINTS.md`, `DECISION_LOG.md`) to serve as a living documentation for the project.
*   **Rationale:** To ensure clarity, continuity, and a single source of truth for all project stakeholders and developers (human or AI). This will help maintain project velocity and prevent knowledge gaps.

*   **Decision:** Corrected the sheet name for the employee status mapping from `idd_basic_status` to `idp_Basic_Status`.
*   **Rationale:** The script failed to find the sheet, and an inspection of the Excel file revealed the correct name. This highlights the importance of verifying data source details.