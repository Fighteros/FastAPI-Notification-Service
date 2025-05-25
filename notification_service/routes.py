from fastapi import APIRouter, HTTPException
from .models import NotificationRequest, NotificationResponse
from .services import NotificationService

router = APIRouter(prefix="/notifications", tags=["notifications"])

@router.post("/send", response_model=NotificationResponse)
async def send_notification(request: NotificationRequest):
    """
    Send notification to a single device
    """
    try:
        return await NotificationService.send_single_notification(
            token=request.token,
            notification=request.notification
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))