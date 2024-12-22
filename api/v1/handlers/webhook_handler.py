from fastapi import APIRouter, Request, HTTPException, status
from services.webhook_services import WebhookServices

webhook_router = APIRouter()


@webhook_router.post("/", summary="Stripe Webhook", tags=["Webhook"])
async def stripe_webhook(request: Request):
    try:
        # Procesa el webhook
        return await WebhookServices.handle_webhook(request)
    except Exception as e:
        # Handle exceptions, e.g., log the error
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))