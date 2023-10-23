from sqlalchemy.orm import Session
import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(username=user.username, password=user.password, isAdmin=user.isAdmin, balance=user.balance)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def create_transport(db: Session, transport: schemas.TransportCreate):
    db_transport = models.Transport(users_id=transport.users_id, canBeRented=transport.canBeRented,
                                    transportType=transport.transportType, model=transport.model, color=transport.color,
                                    identifier=transport.identifier, description=transport.description,
                                    latitude=transport.latitude, longitude=transport.longitude,
                                    minutePrice=transport.minutePrice, dayPrice=transport.dayPrice,
                                    radius=transport.radius)
    db.add(db_transport)
    db.commit()
    db.refresh(db_transport)
    return db_transport


def get_rents(db: Session, rentId: int):
    return db.query(models.Rent).filter(models.Rent.id == rentId).all()


def create_user_rent(db: Session, rent: schemas.RentCreate):
    db_rent = models.Rent(**rent.dict())
    db.add(db_rent)
    db.commit()
    db.refresh(db_rent)
    return db_rent
