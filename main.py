from typing import Annotated
from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel

from sqlalchemy.orm import Session
import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@app.get("/api/Account/SignIn")
async def read_account_signIn(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"token": token}


class User(BaseModel):
    username: str
    password: str
    isAdmin: bool
    balance: float


def fake_decode_token(token):
    return User(
        username=token + "fakedecoded", password="fakepassword", isAdmin=False, balance=0
    )


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    user = fake_decode_token(token)
    return user


@app.get("/api/Account/Me")
async def read_account_me(current_user: Annotated[User, Depends(get_current_user)]):
    return current_user


@app.post("/users/", response_model=schemas.User)
async def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=list[schemas.User])
async def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=schemas.User)
async def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.post("/api/Transport", response_model=schemas.Transport)
async def create_transport(transport: schemas.TransportCreate, db: Session = Depends(get_db)):
    return crud.create_transport(db=db, transport=transport)


@app.post("/api/Admin/Rent/", response_model=schemas.Rent)
async def create_rent_for_user(rent: schemas.RentCreate, db: Session = Depends(get_db)):
    return crud.create_user_rent(db=db, rent=rent)


@app.get("/api/Admin/Rent/{rentId}", response_model=list[schemas.Rent])
async def read_rents(rentId: int, db: Session = Depends(get_db)):
    rent = crud.get_rents(db, rentId=rentId)
    return rent


