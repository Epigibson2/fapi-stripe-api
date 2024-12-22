from fastapi import APIRouter, HTTPException, status

from schemas.product_schemas import ProductCreate, ProductUpdate
from services.product_services import ProductServices

product_router = APIRouter()


@product_router.get("/", summary="Get all Stripe Products", tags=["Product"])
async def get_all_products():
    try:
        result = await ProductServices.list_products()
        return result
    except Exception as e:
        # Handle exceptions, e.g., log the error
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@product_router.get("/{product_id}", summary="Get a Stripe Product by ID", tags=["Product"])
async def get_product_by_id(product_id: str):
    try:
        result = await ProductServices.get_product_by_id(product_id)
        return result
    except Exception as e:
        # Handle exceptions, e.g., log the error
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@product_router.post("/", summary="Create a Stripe Product", tags=["Product"])
async def create_product(product_data: ProductCreate):
    try:
        result = await ProductServices.create_product(product_data)
        return result
    except Exception as e:
        # Handle exceptions, e.g., log the error
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@product_router.put("/{product_id}", summary="Update a Stripe Product", tags=["Product"])
async def update_product(product_id: str, product_data: ProductUpdate):
    try:
        result = await ProductServices.update_product(product_id, product_data)
        return result
    except Exception as e:
        # Handle exceptions, e.g., log the error
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@product_router.delete("/{product_id}", summary="Delete a Stripe Product", tags=["Product"])
async def delete_product(product_id: str):
    try:
        result = await ProductServices.delete_product(product_id)
        return result
    except Exception as e:
        # Handle exceptions, e.g., log the error
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
