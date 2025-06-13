from fastapi import APIRouter, Depends, HTTPException
from Domain.Models.Transaction_view import TransactionView
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

@router.get("/{transaction_id}", response_model=TransactionView)
def get_transaction(transaction_id: int, session: Session = Depends(get_session)):
    service = TransactionService(TransactionRepository())
    transaction_view = service.get_transaction_view(session, transaction_id)
    if not transaction_view:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return transaction_view

@router.get("/", response_model=list[TransactionView])
def list_transactions(limit: int = 10, offset: int = 0, session: Session = Depends(get_session)):
    service = TransactionService(TransactionRepository())
    all_txs = service.list_transactions(session)
    return [service.to_view(tx) for tx in all_txs][offset : offset + limit]

@router.put("/{transaction_id}", response_model=Transaction | None)
def update_transaction(transaction_id: int, transaction: Transaction, session: Session = Depends(get_session)):
    service = TransactionService(TransactionRepository())
    return service.update_transaction(session, transaction_id, transaction)

@router.delete("/{transaction_id}", status_code=204)
def delete_transaction(transaction_id: int, session: Session = Depends(get_session)):
    service = TransactionService(TransactionRepository())
    success = service.delete_transaction(session, transaction_id)
    return {"deleted": success}