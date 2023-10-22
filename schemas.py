from pydantic import BaseModel


class RentBase(BaseModel):
    pass


class RentCreate(RentBase):
    color: str
    timeStart: str
    timeEnd: str
    priceOfUnit: float
    priceType: str
    finalPrice: str
    owner_id_users: int
    owner_id_transports: int


class Rent(RentBase):
    rent_user_id: int
    rent_transports_id: int

    class Config:
        from_attributes = True


class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    username: str
    password: str
    isAdmin: bool
    balance: float


class User(UserBase):
    id: int
    rents_users: list[Rent] = []

    class Config:
        from_attributes = True


class TransportBase(BaseModel):
    pass


class TransportCreate(UserBase):
    users_id: int
    canBeRented: str
    transportType: str
    model: str
    color: str
    identifier: str
    description: str
    latitude: float
    longitude: float
    minutePrice: float
    dayPrice: float
    radius: float


class Transport(UserBase):
    id: int
    rents_users: list[Rent] = []

    class Config:
        from_attributes = True
