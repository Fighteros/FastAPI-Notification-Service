from datetime import datetime, timedelta, timezone
from sqlalchemy.orm import Session

from .models import User

def seed_users(db: Session):
    """Seed the database with test users covering different reminder scenarios"""

    reference_time = datetime.now(timezone.utc)

    # Clear existing users
    db.query(User).delete()
    db.commit()

    # Test cases for reminders
    test_users = [
        # Case 1: Reminder due in 30 minutes (should be included in due-reminders)
        User(
            email="user1@example.com",
            full_name="User One",
            reminder_date=reference_time + timedelta(minutes=30),
            is_active=True
        ),

        # Case 2: Reminder due in 45 minutes (should be included in due-reminders)
        User(
            email="user2@example.com",
            full_name="User Two",
            reminder_date=reference_time + timedelta(minutes=45),
            is_active=True
        ),

        # Case 3: Reminder due in exactly 1 hour (should be included in due-reminders)
        User(
            email="user3@example.com",
            full_name="User Three",
            reminder_date=reference_time + timedelta(hours=1),
            is_active=True
        ),

        # Case 4: Reminder due in 1 hour and 1 second (should NOT be included)
        User(
            email="user4@example.com",
            full_name="User Four",
            reminder_date=reference_time + timedelta(hours=1, minutes=10),
            is_active=True
        ),

        # Case 5: Reminder due in 2 hours (should NOT be included)
        User(
            email="user5@example.com",
            full_name="User Five",
            reminder_date=reference_time + timedelta(hours=2),
            is_active=True
        ),

        # Case 6: Reminder due in 30 minutes but user is inactive (should NOT be included)
        User(
            email="user6@example.com",
            full_name="User Six",
            reminder_date=reference_time + timedelta(minutes=30),
            is_active=False
        ),

        # Case 7: Reminder was due 30 minutes ago (should NOT be included)
        User(
            email="user7@example.com",
            full_name="User Seven",
            reminder_date=reference_time - timedelta(minutes=30),
            is_active=True
        ),

        # Case 8: Reminder due exactly now (should NOT be included as per our logic)
        User(
            email="user8@example.com",
            full_name="User Eight",
            reminder_date=reference_time,
            is_active=True
        )
    ]

    # Add all users to the database
    for user in test_users:
        db.add(user)

    # Commit the changes
    db.commit()

    return len(test_users)