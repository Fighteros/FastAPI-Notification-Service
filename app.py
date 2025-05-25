from fastapi import FastAPI
from notification_service.routes import router as notification_router
from notification_service.config import initialize_firebase
from users.routes import router as user_router
from db.database import engine, Base

# Create database tables
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI(
    title="User Management and Notification Service",
    description="A service that combines user management with notification capabilities",
    version="1.0.0"
)

# Initialize Firebase
initialize_firebase()

# Include routers
app.include_router(user_router)
app.include_router(notification_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
