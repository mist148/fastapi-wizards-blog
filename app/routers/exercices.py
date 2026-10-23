from typing import Annotated, Literal

from fastapi import APIRouter, Path, Query, Request

from app.schemas.product import ProductCreate


router = APIRouter(tags=["exercices"])

@router.get("/products/new")
def newProduct() -> str:
    return "Nouveau produits"
    
@router.get("/products/{id}")
def show(id: Annotated[int, Path(ge=1)]) -> dict[str, str]:
    return {"message" : f"Produit n°{id}"}

@router.get("/search")
def search(q : Annotated[str , Query(min_length=3)], limit : Annotated[int , Query(le=50)] = 10 ) -> dict[str, str]:
    return {"message" : f"q : {q}, limit: {limit}"}

@router.get("/categories/{name}")
def categorie(name : str, country : Literal["en", "fr"] | None = None) -> dict[str, str]:
    return {"message" : f"name: {name}, country : {country or "non précisé"}"}

@router.post("/products",response_model=ProductCreate, status_code=201)
def product(product: ProductCreate) -> ProductCreate:
    return product

@router.get("/sizes/{size}")
def size(size: Literal["small", "medium", "large"]) -> dict[str, str]:
    return {"size" : size}

@router.get("/sessions/{uuid}")
def session(uuid: Annotated[str, Path(pattern="[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}")]) -> dict[str, str]:
    return {"message" : f"produit {uuid}"}

@router.get("/debug/{value}")
def debug(value: str,  request: Request) -> dict[str, str]:
    return {"message": f"valeur : {value} méthode : {request.method} url : {request.url} en-tête : {request.headers}"}