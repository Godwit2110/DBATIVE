from pydantic import BaseModel

class TransactionView(BaseModel):
    transaction_id: int
    buyer: int
    seller: int
    total_paid: float
    # Example transformation or computed fields