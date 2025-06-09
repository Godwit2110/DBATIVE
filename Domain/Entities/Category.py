from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List

class Category(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: str
    slug: str = Field(unique=True)
    parent_id: Optional[int] = Field(default=None, foreign_key="category.id")

    subcategories: List["Category"] = Relationship(
        back_populates="parent",
        sa_relationship_kwargs={"cascade": "all, delete-orphan"}
    )

    parent: Optional["Category"] = Relationship(back_populates="subcategories")