from sqlmodel import SQLModel, Field
from typing import Optional

class UsedProduct(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: str
    age_in_months: int
    price: float