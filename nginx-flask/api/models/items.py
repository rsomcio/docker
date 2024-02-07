from pydantic import BaseModel


class Item(BaseModel):
    seq: int = None
    name: str
    email: str
    username: str = None
    address: str = None
    phone: str = None
