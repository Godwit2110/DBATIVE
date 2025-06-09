from sqlmodel import Session, select
from Domain.Entities.Category import Category

class CategoryRepository:
    def create_category(self, session: Session, category: Category) -> Category:
        session.add(category)
        session.commit()
        session.refresh(category)
        return category

    def get_category_by_id(self, session: Session, category_id: int) -> Category | None:
        statement = select(Category).where(Category.id == category_id)
        return session.exec(statement).first()

    def list_all_categories(self, session: Session) -> list[Category]:
        statement = select(Category)
        return list(session.exec(statement).all())

    def update_category(self, session: Session, category_id: int, data: Category) -> Category | None:
        existing_category = self.get_category_by_id(session, category_id)
        if not existing_category:
            return None
        existing_category.name = data.name
        existing_category.description = data.description
        existing_category.slug = data.slug
        existing_category.parent_id = data.parent_id
        session.add(existing_category)
        session.commit()
        session.refresh(existing_category)
        return existing_category

    def delete_category(self, session: Session, category_id: int) -> bool:
        category = self.get_category_by_id(session, category_id)
        if not category:
            return False
        session.delete(category)
        session.commit()
        return True