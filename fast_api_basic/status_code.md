# STATUS CODE
 - An HTTP Status Code is used to help the client (the user or submitting data to the server) to understand what happened on the server side application.
 - Ther are international standards on how a Client/Server should handle the resulr of a request.
 - It allows everyone who sends a request to understand what happened on the server side application [success/failure].
 - Common Status Code
    - 1xx - Informational Responses : Request Processing
    - 2xx - Success: Request Successfully Completed
    - 3xx - Redirection : Further Action Required to Complete the Request
    - 4xx - Client Errors : An error was caused by the client
    - 5xx - Server Errors : An error occurred on the server

## 2xx - Success
- **200 OK** : Request successful; returns data (GET) or confirms processing (POST, PUT, DELETE).
- **201 Created** : Request successful; a new resource has been created (POST).
- **204 No Content** : Request successful; no response body returned (commonly DELETE/PUT).

## 4xx - Client Errors
- **400 Bad Request** : Invalid request due to incorrect syntax or format.
- **401 Unauthorized** : Authentication required or failed.
- **403 Forbidden** : Authenticated but lacks permission to access the resource.
- **404 Not Found** : Resource or endpoint does not exist.
- **409 Conflict** : Conflict with current resource state (e.g., duplicate or version issue).
- **422 Unprocessable Entity** : Valid request format but fails validation rules.
- **429 Too Many Requests** : Rate limit exceeded; too many requests in a short time.

## 5xx - Server Errors
- **500 Internal Server Error** : Generic server failure.
- **502 Bad Gateway** : Invalid response from upstream server.
- **503 Service Unavailable** : Server overloaded or under maintenance.
- **504 Gateway Timeout** : Upstream server took too long to respond.
    