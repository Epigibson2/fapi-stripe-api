from fastapi import APIRouter, HTTPException, status

from schemas.customer_schemas import CustomerCreate, CustomerUpdate
from services.customer_services import CustomerServices

customer_router = APIRouter()


@customer_router.get("/", summary="Get all Stripe customers", tags=["Customer"])
async def get_all_customers():
    try:
        # Logic to fetch all customers from Stripe
        result = await CustomerServices.get_stripe_all_customers()
        return result
    except Exception as e:
        # Handle exceptions, e.g., log the error
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@customer_router.get("/{customer_email}", summary="Get a Stripe customer by ID", tags=["Customer"])
async def get_customer_by_email(customer_email: str):
    try:
        # Logic to fetch a customer by ID from Stripe
        result = await CustomerServices.get_stripe_customer_by_email(customer_email)
        return result
    except Exception as e:
        # Handle exceptions, e.g., log the error
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@customer_router.post("/", summary="Create a Stripe customer", tags=["Customer"])
async def create_customer(customer_data: CustomerCreate):
    try:
        result = await CustomerServices.create_stripe_customer(customer_data)
        return result
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@customer_router.put("/{customer_id}", summary="Update a Stripe customer", tags=["Customer"])
async def update_customer(customer_id: str, customer_data: CustomerUpdate):
    try:
        result = await CustomerServices.update_stripe_customer(customer_id, customer_data)
        return result
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@customer_router.delete("/{customer_id}", summary="Delete a Stripe customer", tags=["Customer"])
async def delete_customer(customer_id: str):
    try:
        await CustomerServices.delete_stripe_customer(customer_id)
        return {"message": "Customer deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
