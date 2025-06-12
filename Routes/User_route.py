from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from Domain.Entities.User import User
from Services.User_serv import UserService
from Persistence.User_repo import UserRepository
from Persistence.database import get_session
from Domain.Models.User_view import UserView

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=User, status_code=201)
def create_user(user: User, session: Session = Depends(get_session)):
    service = UserService(UserRepository())
    return service.create_user(session, user)

@router.get("/{user_id}", response_model=UserView)
def get_user(user_id: int, session: Session = Depends(get_session)):
    service = UserService(UserRepository())
    user_view = service.get_user_view(session, user_id)
    if not user_view:
        raise HTTPException(status_code=404, detail="User not found")
    return user_view

@router.get("/", response_model=list[User])
def list_users(session: Session = Depends(get_session)):
    service = UserService(UserRepository())
    return service.list_users(session)

@router.put("/{user_id}", response_model=User)
def update_user(user_id: int, user: User, session: Session = Depends(get_session)):
    service = UserService(UserRepository())
    return service.update_user(session, user_id, user)

@router.delete("/{user_id}", status_code=204)
def delete_user(user_id: int, session: Session = Depends(get_session)):
    service = UserService(UserRepository())
    success = service.delete_user(session, user_id)
    return {"deleted": success}