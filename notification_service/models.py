from pydantic import BaseModel
from typing import Optional, Dict

class NotificationData(BaseModel):
    """Model for notification data"""
    title: str
    body: str
    data: Optional[Dict[str, str]] = None

class NotificationRequest(BaseModel):
    """Model for single notification request"""
    token: str
    notification: NotificationData

class NotificationResponse(BaseModel):
    """Model for notification response"""
    success: bool
    message_id: Optional[str] = None
