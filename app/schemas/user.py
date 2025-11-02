from pydantic import BaseModel



class UserCreate(BaseModel):
    phone_number: str
    password: str

