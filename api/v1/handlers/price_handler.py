from fastapi import APIRouter, HTTPException, status

from schemas.price_schemas import PriceCreate, PriceUpdate
from services.price_services import PriceServices

price_router = APIRouter()


@price_router.get("/", summary="Get all Stripe prices.", tags=["Price"])
async def get_all_prices():
    try:
        # Llama al servicio para obtener todos los precios
        result = await PriceServices.list_prices()
        return result
    except Exception as e:
        # Handle exceptions, e.g., log the error
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@price_router.get("/{price_id}", summary="Get a Stripe price by ID", tags=["Price"])
async def get_price_by_id(price_id: str):
    try:
        # Llama al servicio para obtener un precio por ID
        result = await PriceServices.get_price_by_id(price_id)
        return result
    except Exception as e:
        # Handle exceptions, e.g., log the error
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@price_router.post("/", summary="Create a Stripe price", tags=["Price"])
async def create_price(price_data: PriceCreate):
    try:
        # Llama al servicio para crear un precio
        result = await PriceServices.create_price(price_data)
        return result
    except Exception as e:
        # Handle exceptions, e.g., log the error
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@price_router.put("/{price_id}", summary="Update a Stripe price", tags=["Price"])
async def update_price(price_id: str, price_data: PriceUpdate):
    try:
        # Llama al servicio para actualizar un precio
        result = await PriceServices.update_price(price_id, price_data)
        return result
    except Exception as e:
        # Handle exceptions, e.g., log the error
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@price_router.delete("/{price_id}", summary="Delete a Stripe price", tags=["Price"])
async def delete_price(price_id: str):
    try:
        # Llama al servicio para eliminar un precio
        result = await PriceServices.delete_price(price_id)
        return result
    except Exception as e:
        # Handle exceptions, e.g., log the error
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
