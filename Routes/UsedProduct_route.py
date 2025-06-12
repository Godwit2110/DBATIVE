from fastapi import APIRouter, Depends, HTTPException
from Domain.Models.UsedProduct_view import UsedProductView
from sqlmodel import Session
from Domain.Entities.UsedProduct import UsedProduct
from Services.UsedProduct_serv import UsedProductService
from Persistence.UsedProduct_repo import UsedProductRepository
from Persistence.database import get_session

router = APIRouter(prefix="/usedproducts", tags=["Used Products"])

@router.post("/", response_model=UsedProduct, status_code=201)
def create_product(product: UsedProduct, session: Session = Depends(get_session)):
    service = UsedProductService(UsedProductRepository())
    return service.create_product(session, product)

@router.get("/{product_id}", response_model=UsedProductView)
def get_product(product_id: int, session: Session = Depends(get_session)):
    service = UsedProductService(UsedProductRepository())
    product_view = service.get_product_view(session, product_id)
    if not product_view:
        raise HTTPException(status_code=404, detail="Used product not found")
    return product_view

@router.get("/")
def list_products(limit: int = 10, offset: int = 0, session: Session = Depends(get_session)):
    service = UsedProductService(UsedProductRepository())
    products = service.list_products(session)
    return products[offset : offset + limit]

@router.put("/{product_id}", response_model=UsedProduct | None)
def update_product(product_id: int, product: UsedProduct, session: Session = Depends(get_session)):
    service = UsedProductService(UsedProductRepository())
    return service.update_product(session, product_id, product)

@router.delete("/{product_id}", status_code=204)
def delete_product(product_id: int, session: Session = Depends(get_session)):
    service = UsedProductService(UsedProductRepository())
    success = service.delete_product(session, product_id)
    return {"deleted": success}