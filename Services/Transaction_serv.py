from sqlmodel import Session
from Domain.Entities.Transaction import Transaction
from Persistence.Transaction_repo import TransactionRepository
from Domain.Models.Transaction_view import TransactionView

class TransactionService:
    def __init__(self, repo: TransactionRepository):
        self.repo = repo

    def to_view(self, tx_db: Transaction) -> TransactionView:
        if tx_db.id is None:
            raise ValueError("Transaction id cannot be None")
        return TransactionView(
            
            transaction_id=tx_db.id,
            buyer=tx_db.buyer_id,
            seller=tx_db.seller_id,
            total_paid=tx_db.price_sold
        )

    def get_transaction_view(self, session: Session, transaction_id: int) -> TransactionView | None:
        tx_db = self.repo.get_transaction_by_id(session, transaction_id)
        if not tx_db:
            return None
        return self.to_view(tx_db)
    
    def create_transaction(self, session: Session, transaction: Transaction) -> Transaction:
        # You could add extra validation or logic here
        return self.repo.create_transaction(session, transaction)

    def list_transactions(self, session: Session) -> list[Transaction]:
        return self.repo.list_all_transactions(session)

    def update_transaction(self, session: Session, transaction_id: int, data: Transaction) -> Transaction | None:
        # Possibly add business rules for editing transactions
        return self.repo.update_transaction(session, transaction_id, data)

    def delete_transaction(self, session: Session, transaction_id: int) -> bool:
        return self.repo.delete_transaction(session, transaction_id)