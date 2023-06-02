from sqlalchemy.orm import Session
from models import User
import schemas
import bcrypt


def get_user(db : Session, user_id : int):
    return db.query(User).filter(User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def create_user(db: Session, user: schemas.UserCreate):
    salt = bcrypt.gensalt(rounds=15)
    hashed_pass = bcrypt.hashpw(user.password.encode("utf-8"), salt=salt)
    db_user = User(email=user.email, password=hashed_pass.decode("utf-8"))
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
