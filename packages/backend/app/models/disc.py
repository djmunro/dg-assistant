from pydantic import BaseModel


class DiscCreate(BaseModel):
    name: str


class DiscRead(BaseModel):
    id: int
    name: str
