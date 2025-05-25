from firebase_admin import messaging
from .models import NotificationData, NotificationResponse

class NotificationService:
    """Service class for handling notification operations"""

    @staticmethod
    async def send_single_notification(token: str, notification: NotificationData) -> NotificationResponse:
        """
        Send notification to a single device

        Args:
            token: Device token
            notification: Notification data

        Returns:
            NotificationResponse with success status and message ID
        """
        try:
            message = messaging.Message(
                notification=messaging.Notification(
                    title=notification.title,
                    body=notification.body
                ),
                data=notification.data or {},
                token=token
            )

            response = messaging.send(message)
            return NotificationResponse(success=True, message_id=response)
        except Exception as e:
            raise Exception(f"Failed to send notification: {str(e)}")