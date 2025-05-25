from sqlalchemy.orm import Session
from typing import List

from .models import User

class UserService:
    @staticmethod
    def get_users(db: Session, skip: int = 0, limit: int = 100) -> List[User]:
        return db.query(User).offset(skip).limit(limit).all()