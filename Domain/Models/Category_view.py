from pydantic import BaseModel

class CategoryView(BaseModel):
    category_id: int
    label: str
    # Example transformation: rename "name" to "label"