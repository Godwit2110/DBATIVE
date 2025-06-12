from pydantic import BaseModel

class UsedProductView(BaseModel):
    product_id: int
    item_name: str
    cost: float
    months_old: int
    # Example transformation from "price" -> "cost", "age_in_months" -> "months_old"