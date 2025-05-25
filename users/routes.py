from datetime import datetime, timedelta, timezone
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List


from db.database import get_db
from .models import User as UserModel
from .schemas import User
from .service import UserService

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/", response_model=List[User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Get all users with optional pagination"""
    users = UserService.get_users(db, skip=skip, limit=limit)
    return users

@router.get("/due-reminders", response_model=List[User])
def read_users_with_due_reminders(db: Session = Depends(get_db)):
    """Get users who need to be reminded (reminder_date is within the next hour)"""

    current_time = datetime.now(timezone.utc)
    one_hour_later = current_time + timedelta(hours=1)

    print(f"current_time: {current_time.isoformat()}")
    print(f"one_hour_later: {one_hour_later.isoformat()}")


    users = db.query(UserModel).filter(
        UserModel.reminder_date .isnot(None),
         UserModel.reminder_date > current_time,
        UserModel.reminder_date <= one_hour_later,
        UserModel.is_active.is_(True)
    ).order_by(UserModel.reminder_date.asc()).all()

    return users
