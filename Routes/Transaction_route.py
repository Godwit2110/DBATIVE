from fastapi import APIRouter, Depends
from sqlmodel import Session
from Domain.Entities.Transaction import Transaction
from Services.Transaction_serv import TransactionService
from Persistence.Transaction_repo import TransactionRepository
from Persistence.database import get_session

router = APIRouter(prefix="/transactions", tags=["Transactions"])

@router.post("/", response_model=Transaction, status_code=201)
def create_transaction(transaction: Transaction, session: Session = Depends(get_session)):
    service = TransactionService(TransactionRepository())
    return service.create_transaction(session, transaction)

@router.get("/{transaction_id}", response_model=Transaction | None)
def get_transaction(transaction_id: int, session: Session = Depends(get_session)):
    service = TransactionService(TransactionRepository())
    return service.get_transaction(session, transaction_id)

@router.get("/", response_model=list[Transaction])
def list_transactions(session: Session = Depends(get_session)):
    service = TransactionService(TransactionRepository())
    return service.list_transactions(session)

@router.put("/{transaction_id}", response_model=Transaction | None)
def update_transaction(transaction_id: int, transaction: Transaction, session: Session = Depends(get_session)):
    service = TransactionService(TransactionRepository())
    return service.update_transaction(session, transaction_id, transaction)

@router.delete("/{transaction_id}", status_code=204)
def delete_transaction(transaction_id: int, session: Session = Depends(get_session)):
    service = TransactionService(TransactionRepository())
    success = service.delete_transaction(session, transaction_id)
    return {"deleted": success}