from sqlalchemy import select
from database import CarOrm, new_session
from schemas import SCar, SCarAdd

class CarRepository:
    @classmethod
    async def add_one(cls, data: SCarAdd) -> int:
        async with new_session() as session:
            car_dict = data.model_dump()

            car = CarOrm(**car_dict)
            session.add(car)
            await session.flush()
            await session.commit()
            
            return car.id

    @classmethod
    async def get_all(cls) -> list[SCar]:
        async with new_session() as session:
            query = select(CarOrm)
            result = await session.execute(query)
            car_models = result.scalars().all()
            car_schemas = [SCar.model_validate(car_model) for car_model in car_models]
            return car_schemas