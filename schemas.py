from pydantic import BaseModel


class SCarAdd(BaseModel):
    name: str
    carmodel: str
    number: str
    capacity: int

class SCar(SCarAdd):
    id: int