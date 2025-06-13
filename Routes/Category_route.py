from fastapi import APIRouter, Depends, HTTPException
from Domain.Models.Category_view import CategoryView
from sqlmodel import Session
from Domain.Entities.Category import Category
from Services.Category_serv import CategoryService
from Persistence.Category_repo import CategoryRepository
from Persistence.database import get_session

router = APIRouter(prefix="/categories", tags=["Categories"])

@router.post("/", response_model=Category, status_code=201)
def create_category(category: Category, session: Session = Depends(get_session)):
    service = CategoryService(CategoryRepository())
    return service.create_category(session, category)

@router.get("/{category_id}", response_model=CategoryView)
def get_category(category_id: int, session: Session = Depends(get_session)):
    service = CategoryService(CategoryRepository())
    category_view = service.get_category_view(session, category_id)
    if not category_view:
        raise HTTPException(status_code=404, detail="Category not found")
    return category_view

@router.get("/", response_model=list[CategoryView])
def list_categories(
    limit: int = 10,
    offset: int = 0,
    session: Session = Depends(get_session)
):
    service = CategoryService(CategoryRepository())
    categories = service.list_categories(session)
    return [service.to_view(cat) for cat in categories][offset: offset + limit]

@router.put("/{category_id}", response_model=Category | None)
def update_category(category_id: int, category: Category, session: Session = Depends(get_session)):
    service = CategoryService(CategoryRepository())
    return service.update_category(session, category_id, category)

@router.delete("/{category_id}", status_code=204)
def delete_category(category_id: int, session: Session = Depends(get_session)):
    service = CategoryService(CategoryRepository())
    success = service.delete_category(session, category_id)
    return {"deleted": success}