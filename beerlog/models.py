from datetime import datetime
from typing import Optional
from pydantic import validator
from sqlmodel import SQLModel, Field
from statistics import mean


class Beer(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, default=None)
    name: str
    style: str
    flavor: int
    image: int
    cost: int
    rate: int = 0

    created_at: datetime = Field(default_factory=datetime.now)

    @validator("flavor", "image", "cost")
    def validate_rantings(cls, v, field):
        if v < 1 or v > 10:
            raise RuntimeError(f"{field.name} must be between 0 and 5")
        return v

    @validator("rate", always=True)
    def calculate_rate(cls, v, values):
        rate = mean([values["flavor"], values["image"], values["cost"]])
        return int(rate)
