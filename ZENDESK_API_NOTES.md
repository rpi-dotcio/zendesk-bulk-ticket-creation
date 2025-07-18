**Directive: This document is a reference for Zendesk API best practices. It should be updated with any new findings or relevant information discovered during development.**

# Zendesk API Notes

This document summarizes key findings and considerations from the provided Zendesk API documentation.

### Authentication

*   Authentication will be handled using an API token.
*   The credentials will be passed in the format: `{email_address}/token:{api_token}`.
*   For security, the API token will be stored in an environment variable (`ZENDESK_API_TOKEN`) and not hardcoded.

### Rate Limiting

*   The Zendesk API has strict rate limits. Bulk creation will certainly hit these limits.
*   The application must handle `429 Too Many Requests` HTTP status codes.
*   When a `429` is received, the `Retry-After` header indicates how many seconds to wait before retrying.
*   The core application logic will include a mechanism to `time.sleep()` for the specified duration upon receiving a `429`.

### Ticket Creation

*   **Asynchronous Creation:** To improve performance and avoid timeouts during bulk operations, tickets should be created asynchronously using the `?async=true` parameter. This will queue a background job in Zendesk.
*   **Bulk Creation:** The `tickets/create_many.json` endpoint can be used to create up to 100 tickets at a time. This is more efficient than creating them one by one.
*   **Custom Fields:** Custom fields must be created in Zendesk *before* they can be populated via the API. The `custom_fields` property in the ticket object takes an array of objects, each with an `id` and `value`.
*   **Attachments:** Files can be attached to tickets. This involves a two-step process:
    1.  Upload the file to get a token.
    2.  Use the token in the `uploads` property of the ticket comment when creating the ticket.
*   **Tags:** Tags can be added via the `tags` array property.

### User and Requester Management

*   A ticket `requester` can be set by providing a `requester` object with `name` and `email`.
*   If the email address doesn't exist, a new user profile will be created.
*   If the email exists, the existing user is associated with the ticket.

### Error Handling and Verification

*   **Update Collisions:** Zendesk has optimistic locking to prevent update collisions. While less critical for ticket *creation*, it's a good practice to be aware of.
*   **Job Status:** When using asynchronous creation, we must use the `job_statuses` endpoint to check if the creation job was successful.