# filepath: c:\Users\alvar\Documents\GitHub\DBATIVE\Domain\Entities\transaction.py
from sqlmodel import SQLModel, Field
from typing import Optional

class Transaction(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    buyer_id: int = Field(foreign_key="user.id")
    seller_id: int = Field(foreign_key="user.id")
    product_id: int = Field(foreign_key="usedproduct.id")
    price_sold: float