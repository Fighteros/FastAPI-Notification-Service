
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

    @staticmethod
    async def send_multiple_notifications(tokens: list[str], notification: NotificationData) -> NotificationResponse:
        """
        Send notification to multiple devices

        Args:
            tokens: List of device tokens
            notification: Notification data

        Returns:
            NotificationResponse with success status and counts
        """
        try:
            message = messaging.MulticastMessage(
                notification=messaging.Notification(
                    title=notification.title,
                    body=notification.body
                ),
                data=notification.data or {},
                tokens=tokens
            )

            response = messaging.send_multicast(message)
            return NotificationResponse(
                success=True,
                success_count=response.success_count,
                failure_count=response.failure_count
            )
        except Exception as e:
            raise Exception(f"Failed to send notifications: {str(e)}")