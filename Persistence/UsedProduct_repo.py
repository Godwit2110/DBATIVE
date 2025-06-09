from sqlmodel import Session, select
from Domain.Entities.UsedProduct import UsedProduct

class UsedProductRepository:
    def create_used_product(self, session: Session, product: UsedProduct) -> UsedProduct:
        session.add(product)
        session.commit()
        session.refresh(product)
        return product

    def get_used_product_by_id(self, session: Session, product_id: int) -> UsedProduct|None:
        statement = select(UsedProduct).where(UsedProduct.id == product_id)
        result = session.exec(statement).first()
        return result

    def list_all_used_products(self, session: Session) -> list[UsedProduct]:
        statement = select(UsedProduct)
        result = session.exec(statement).all()
        return list(result)

    def update_used_product(self, session: Session, product_id: int, new_data: UsedProduct) -> UsedProduct|None:
        product = self.get_used_product_by_id(session, product_id)
        if not product:
            return None
        
        product.name = new_data.name
        product.description = new_data.description
        product.age_in_months = new_data.age_in_months
        product.price = new_data.price

        session.add(product)
        session.commit()
        session.refresh(product)
        return product

    def delete_used_product(self, session: Session, product_id: int) -> bool:
        product = self.get_used_product_by_id(session, product_id)
        if not product:
            return False
        
        session.delete(product)
        session.commit()
        return True