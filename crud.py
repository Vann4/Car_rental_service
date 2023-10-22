from sqlalchemy.orm import Session
import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    # fake_hashed_password = user.password + "notreallyhashed" , hashed_password=fake_hashed_password
    db_user = models.User(username=user.username, password=user.password, isAdmin=user.isAdmin, balance=user.balance)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_rents(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Rent).offset(skip).limit(limit).all()


def create_user_rent(db: Session, rent: schemas.RentCreate, user_id: int):
    db_rent = models.Rent(**rent.dict(), rent_user_id=user_id)
    db.add(db_rent)
    db.commit()
    db.refresh(db_rent)
    return db_rent