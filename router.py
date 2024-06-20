from fastapi import APIRouter, Depends 
from typing import Optional, Annotated
from pydantic import BaseModel

from repository import CarRepository
from schemas import SCar, SCarAdd

router = APIRouter(
    prefix="/cars",
    tags=["Машины"]
)

@router.post("")
async def add_car(
    car: Annotated[SCarAdd, Depends()], 
):
    car_id = await CarRepository.add_one(car)
    return {"ok": True, "car_id": car_id}

@router.get("")
async def get_all_cars() -> list[SCar]:
    cars = await CarRepository.get_all()
    return cars