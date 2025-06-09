from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class Transaction(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    buyer_id: int = Field(foreign_key="user.id")
    seller_id: int = Field(foreign_key="user.id")
    product_id: int = Field(foreign_key="usedproduct.id")
    price_sold: float
    created_at: datetime = Field(default_factory=datetime.utcnow)