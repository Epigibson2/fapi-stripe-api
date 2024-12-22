from datetime import datetime
from enum import Enum
from typing import Optional
from pydantic import BaseModel, EmailStr, Field
from uuid import UUID, uuid4


class PaymentStatus(str, Enum):
    PENDING = "pending"
    SUCCEEDED = "succeeded"
    FAILED = "failed"
    REFUNDED = "refunded"


class StripeCustomer(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    email: EmailStr
    name: str
    stripe_customer_id: str
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
    is_active: bool = True

    class Config:
        from_attributes = True


class StripePayment(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    customer_id: UUID
    amount: int = Field(gt=0)  # Amount in cents
    currency: str = Field(max_length=3, default="usd")
    payment_intent_id: str
    payment_method_id: Optional[str]
    status: PaymentStatus = PaymentStatus.PENDING
    description: Optional[str]
    metadata: dict = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

    class Config:
        from_attributes = True


class StripeSubscription(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    customer_id: UUID
    stripe_subscription_id: str
    status: str
    current_period_start: datetime
    current_period_end: datetime
    cancel_at: Optional[datetime]
    canceled_at: Optional[datetime]
    trial_start: Optional[datetime]
    trial_end: Optional[datetime]
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

    class Config:
        from_attributes = True


# Optional: Create a payment request model
class CreatePaymentRequest(BaseModel):
    amount: int = Field(gt=0)
    currency: str = Field(max_length=3, default="mxn")
    customer_id: UUID
    payment_method_id: Optional[str]
    description: Optional[str]
    metadata: dict = Field(default_factory=dict)


# Optional: Create a subscription request model
class CreateSubscriptionRequest(BaseModel):
    customer_id: UUID
    price_id: str
    trial_period_days: Optional[int] = Field(None, ge=0)
    metadata: dict = Field(default_factory=dict)
