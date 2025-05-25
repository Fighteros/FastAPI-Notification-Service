from fastapi import FastAPI

from notification_service.routes import router
from notification_service.config import initialize_firebase


# Initialize FastAPI app
app = FastAPI(
    title="Notification Service",
    description="A standalone notification service using FastAPI and Firebase Cloud Messaging",
    version="1.0.0"
)

# Initialize Firebase
initialize_firebase()

# Include routers
app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
