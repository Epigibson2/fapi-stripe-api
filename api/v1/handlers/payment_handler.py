from fastapi import APIRouter, HTTPException, status
from schemas.payment_schemas import PaymentIntentCreate, ChargeCreate, SetupIntentCreate, \
    RefundCreate
from services.payment_services import PaymentServices

payment_router = APIRouter()


# STRIPE PAYMENT INTENT SERVICES

@payment_router.post("/payment-intent", summary="Create Stripe Payment Intent", tags=["Payment"])
async def create_payment_intent(payment_data: PaymentIntentCreate):
    try:
        result = await PaymentServices.create_payment_intent(payment_data)
        return result
    except Exception as e:
        # Handle exceptions, e.g., log the error
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@payment_router.get("/payment-intent/{payment_intent_id}", summary="Get Stripe Payment Intent",
                    tags=["Payment"])
async def retrieve_payment_intent(payment_intent_id: str):
    try:
        result = await PaymentServices.retrieve_payment_intent(payment_intent_id)
        return result
    except Exception as e:
        # Handle exceptions, e.g., log the error
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


# STRIPE SETUP INTENT SERVICES

@payment_router.post("/setup-intent", summary="Create Setup Intent", tags=["Payment"])
async def create_setup_intent(payment_data: SetupIntentCreate):
    try:
        result = await PaymentServices.create_payment_intent(payment_data)
        return result
    except Exception as e:
        # Handle exceptions, e.g., log the error
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@payment_router.get("/setup-intent/{setup_intent_id}", summary="Get Stripe Setup Intent",
                    tags=["Payment"])
async def retrieve_setup_intent(setup_intent_id: str):
    try:
        result = await PaymentServices.retrieve_setup_intent(setup_intent_id)
        return result
    except Exception as e:
        # Handle exceptions, e.g., log the error
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


# STRIPE SETUP CHARGE SERVICES


@payment_router.post("/charge", summary="Create Stripe Charge", tags=["Payment"])
async def create_charge(charge_data: ChargeCreate):
    try:
        result = await PaymentServices.create_charge(charge_data)
        return result
    except Exception as e:
        # Handle exceptions, e.g., log the error
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@payment_router.get("/charge/{charge_id}", summary="Get Stripe Charge",
                    tags=["Payment"])
async def retrieve_charge(charge_id: str):
    try:
        result = await PaymentServices.retrieve_charge(charge_id)
        return result
    except Exception as e:
        # Handle exceptions, e.g., log the error
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


# STRIPE SETUP REFUND SERVICES


@payment_router.post("/refund", summary="Create Stripe Refund", tags=["Payment"])
async def create_refund(refund_data: RefundCreate):
    try:
        result = await PaymentServices.create_refund(refund_data)
        return result
    except Exception as e:
        # Handle exceptions, e.g., log the error
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@payment_router.get("/refund/{refund_id}", summary="Get Stripe Refund",
                    tags=["Payment"])
async def retrieve_refund(refund_id: str):
    try:
        result = await PaymentServices.retrieve_refund(refund_id)
        return result
    except Exception as e:
        # Handle exceptions, e.g., log the error
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
