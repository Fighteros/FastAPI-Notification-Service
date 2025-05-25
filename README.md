# FastAPI Notification Service

A standalone notification service built with FastAPI and Firebase Cloud Messaging (FCM) that can be integrated into any existing system.

## Project Structure

```
notification_service/
├── __init__.py          # Package initialization
├── config.py           # Configuration and Firebase setup
├── models.py           # Pydantic models for request/response
├── routes.py           # API endpoints
└── services.py         # Business logic for notifications
```

## Features

- Send notifications to individual devices
- Support for notification title, body, and additional data
- Easy integration with existing systems
- RESTful API endpoints
- Modular and maintainable code structure

## Setup

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Set up Firebase:

   - Create a Firebase project in the Firebase Console
   - Generate a new private key from Project Settings > Service Accounts
   - Create a `.env` file with your Firebase credentials:

     ```

     ```

3. Run the service:

```bash
uvicorn app:app --reload
```

## API Endpoints

### Send Notification

```http
POST /notifications/send
Content-Type: application/json

{
    "token": "device_token",
    "notification": {
        "title": "Notification Title",
        "body": "Notification Body",
        "data": {
            "key1": "value1",
            "key2": "value2"
        }
    }
}
```

## Integration

To integrate this service into your existing system:

1. Make HTTP requests to the notification endpoint from your application
2. Store device tokens in your database
3. Call the endpoint when you need to send notifications

## Error Handling

The service includes error handling for:

- Invalid Firebase credentials
- Invalid device tokens
- Network issues
- Invalid request payload

## Security

- Keep your Firebase credentials secure
- Use environment variables for sensitive information
- Consider implementing authentication for the API endpoints in production

## Development

To run the service in development mode with auto-reload:

```bash
uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

## Production Deployment

For production deployment:

1. Set up proper authentication
2. Use a production-grade ASGI server
3. Configure proper logging
4. Set up monitoring
5. Use environment variables for configuration
