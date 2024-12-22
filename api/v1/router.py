from fastapi import APIRouter

from api.v1.handlers import customer_handler
from api.v1.handlers import payment_handler
from api.v1.handlers import payment_method_handler
from api.v1.handlers import price_handler
from api.v1.handlers import product_handler
from api.v1.handlers import subscription_handler
from api.v1.handlers import webhook_handler
from api.v1.handlers import health_check_handler

router = APIRouter()

router.include_router(customer_handler.customer_router, prefix="/customer", tags=["Customer"])
router.include_router(payment_handler.payment_router, prefix="/payment", tags=["Payment"])
router.include_router(payment_method_handler.payment_method_router, prefix="/payment-method",
                      tags=["Payment-Method"])
router.include_router(price_handler.price_router, prefix="/price", tags=["Price"])
router.include_router(product_handler.product_router, prefix="/product", tags=["Product"])
router.include_router(subscription_handler.subscription_router, prefix="/subscription",
                      tags=["Subscription"])
router.include_router(webhook_handler.webhook_router, prefix="/webhook", tags=["Webhook"])
router.include_router(health_check_handler.health_check_router, prefix="/health-check",
                      tags=["Health-Check"])

