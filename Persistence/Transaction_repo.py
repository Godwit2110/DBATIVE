from sqlmodel import Session, select
from Domain.Entities.Transaction import Transaction

class TransactionRepository:
    def create_transaction(self, session: Session, transaction: Transaction) -> Transaction:
        session.add(transaction)
        session.commit()
        session.refresh(transaction)
        return transaction

    def get_transaction_by_id(self, session: Session, transaction_id: int) -> Transaction | None:
        statement = select(Transaction).where(Transaction.id == transaction_id)
        return session.exec(statement).first()

    def list_all_transactions(self, session: Session) -> list[Transaction]:
        statement = select(Transaction)
        return list(session.exec(statement).all())

    def update_transaction(self, session: Session, transaction_id: int, data: Transaction) -> Transaction | None:
        existing_transaction = self.get_transaction_by_id(session, transaction_id)
        if not existing_transaction:
            return None
        existing_transaction.buyer_id = data.buyer_id
        existing_transaction.seller_id = data.seller_id
        existing_transaction.product_id = data.product_id
        existing_transaction.price_sold = data.price_sold
        session.add(existing_transaction)
        session.commit()
        session.refresh(existing_transaction)
        return existing_transaction

    def delete_transaction(self, session: Session, transaction_id: int) -> bool:
        transaction = self.get_transaction_by_id(session, transaction_id)
        if not transaction:
            return False
        session.delete(transaction)
        session.commit()
        return True