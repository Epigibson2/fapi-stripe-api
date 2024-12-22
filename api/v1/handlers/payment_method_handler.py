from fastapi import APIRouter

payment_method_router = APIRouter()


@payment_method_router.get("/", summary="Get all Stripe payment methods", tags=["Payment-Method"])
async def get_all_payment_methods():
    # Logic to fetch all payment methods from Stripe
    return {"message": "All Stripe payment methods fetched successfully"}


@payment_method_router.get("/{payment_method_id}", summary="Get a Stripe payment method by ID",
                           tags=["Payment-Method"])
async def get_payment_method_by_id(payment_method_id: str):
    # Logic to fetch a payment method by ID from Stripe
    return {"message": f"Stripe payment method with ID {payment_method_id} fetched successfully"}


@payment_method_router.post("/", summary="Create a Stripe payment method", tags=["Payment-Method"])
async def create_payment_method():
    # Logic to create a new payment method on Stripe
    return {"message": "Stripe payment method created successfully"}


@payment_method_router.put("/{payment_method_id}", summary="Update a Stripe payment method",
                           tags=["Payment-Method"])
async def update_payment_method(payment_method_id: str):
    # Logic to update a payment method on Stripe
    return {"message": f"Stripe payment method with ID {payment_method_id} updated successfully"}


@payment_method_router.delete("/{payment_method_id}", summary="Delete a Stripe payment method",
                              tags=["Payment-Method"])
async def delete_payment_method(payment_method_id: str):
    # Logic to delete a payment method from Stripe
    return {"message": f"Stripe payment method with ID {payment_method_id} deleted successfully"}
