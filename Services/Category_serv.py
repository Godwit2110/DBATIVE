from sqlmodel import Session
from Domain.Entities.Category import Category
from Persistence.Category_repo import CategoryRepository
from Domain.Models.Category_view import CategoryView

class CategoryService:
    def __init__(self, repo: CategoryRepository):
        self.repo = repo

    def to_view(self, category_db: Category) -> CategoryView:
        if category_db.id is None:
            raise ValueError("Category id cannot be None")
        return CategoryView(
            category_id=category_db.id,
            label=category_db.name
        )

    def get_category_view(self, session: Session, category_id: int) -> CategoryView | None:
        category_db = self.repo.get_category_by_id(session, category_id)
        if not category_db:
            return None
        return self.to_view(category_db)

    def create_category(self, session: Session, category: Category) -> Category:
        # Could auto-generate slug if missing
        if not category.slug:
            category.slug = category.name.lower().replace(" ", "-")
        return self.repo.create_category(session, category)

    def list_categories(self, session: Session) -> list[Category]:
        return self.repo.list_all_categories(session)

    def update_category(self, session: Session, category_id: int, data: Category) -> Category | None:
        # Could ensure slug uniqueness or handle collisions here
        return self.repo.update_category(session, category_id, data)

    def delete_category(self, session: Session, category_id: int) -> bool:
        return self.repo.delete_category(session, category_id)