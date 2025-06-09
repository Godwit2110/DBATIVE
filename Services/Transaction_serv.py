from sqlmodel import Session
from Domain.Entities.Transaction import Transaction
from Persistence.Transaction_repo import TransactionRepository

class TransactionService:
    def __init__(self, repo: TransactionRepository):
        self.repo = repo

    def create_transaction(self, session: Session, transaction: Transaction) -> Transaction:
        # You could add extra validation or logic here
        return self.repo.create_transaction(session, transaction)

    def get_transaction(self, session: Session, transaction_id: int) -> Transaction | None:
        return self.repo.get_transaction_by_id(session, transaction_id)

    def list_transactions(self, session: Session) -> list[Transaction]:
        return self.repo.list_all_transactions(session)

    def update_transaction(self, session: Session, transaction_id: int, data: Transaction) -> Transaction | None:
        # Possibly add business rules for editing transactions
        return self.repo.update_transaction(session, transaction_id, data)

    def delete_transaction(self, session: Session, transaction_id: int) -> bool:
        return self.repo.delete_transaction(session, transaction_id)