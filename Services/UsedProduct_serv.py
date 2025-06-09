from sqlmodel import Session
from Domain.Entities.UsedProduct import UsedProduct
from Persistence.UsedProduct_repo import UsedProductRepository

class UsedProductService:
    def __init__(self, repo: UsedProductRepository):
        self.repo = repo

    def create_product(self, session: Session, product: UsedProduct) -> UsedProduct:
        # Example of applying a slight discount based on age before saving
        adjusted_price = self._calculate_discounted_price(product)
        product.price = adjusted_price
        return self.repo.create_used_product(session, product)

    def _calculate_discounted_price(self, product: UsedProduct) -> float:
        # Suppose every 12 months reduces price by 20%
        discount_steps = product.age_in_months // 12
        discount_factor = 1 - (0.2 * discount_steps)
        discounted_price = product.price * max(discount_factor, 0.0)
        return discounted_price

    def get_product(self, session: Session, product_id: int) -> UsedProduct | None:
        return self.repo.get_used_product_by_id(session, product_id)

    def list_products(self, session: Session) -> list[UsedProduct]:
        return self.repo.list_all_used_products(session)

    def update_product(self, session: Session, product_id: int, data: UsedProduct) -> UsedProduct | None:
        # Optionally recalculate discounted price when updating
        data.price = self._calculate_discounted_price(data)
        return self.repo.update_used_product(session, product_id, data)

    def delete_product(self, session: Session, product_id: int) -> bool:
        return self.repo.delete_used_product(session, product_id)