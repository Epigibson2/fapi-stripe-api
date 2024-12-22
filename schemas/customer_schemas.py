from datetime import datetime
from typing import Optional, Dict, Any
from pydantic import BaseModel, EmailStr, Field
from uuid import UUID
from models.customer_model import CustomerStatus


# Base Schema with common attributes
class CustomerBase(BaseModel):
    email: EmailStr
    name: str
    phone: Optional[str] = None
    metadata: Dict[str, Any] = Field(default_factory=dict)


# Schema for creating a customer
class CustomerCreate(CustomerBase):
    pass


# Schema for updating a customer
class CustomerUpdate(BaseModel):
    email: Optional[EmailStr] = None
    name: Optional[str] = None
    phone: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    status: Optional[CustomerStatus] = None


# Schema for returning customer data
class CustomerResponse(CustomerBase):
    id: UUID
    stripe_customer_id: Optional[str]
    status: CustomerStatus
    default_payment_method: Optional[str]
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


# Schema for stripe-specific operations
class StripeCustomerCreate(BaseModel):
    customer_id: UUID
    stripe_payment_method_id: Optional[str] = None
    set_as_default: bool = False


# Schema for payment method operations
class PaymentMethodCreate(BaseModel):
    payment_method_id: str
    set_as_default: bool = False


class PaymentMethodResponse(BaseModel):
    id: str
    type: str
    card: Dict[str, Any]
    is_default: bool


# Schema for customer search/filter
class CustomerFilter(BaseModel):
    email: Optional[str] = None
    status: Optional[CustomerStatus] = None
    created_after: Optional[datetime] = None
    created_before: Optional[datetime] = None


# Schema for customer list response with pagination
class CustomerListResponse(BaseModel):
    items: list[CustomerResponse]
    total: int
    page: int
    size: int
    pages: int


# Schema for customer statistics
class CustomerStats(BaseModel):
    total_customers: int
    active_customers: int
    inactive_customers: int
    delinquent_customers: int
    customers_with_payment_method: int


# Schema for subscription-related operations
class CustomerSubscriptionCreate(BaseModel):
    price_id: str
    trial_period_days: Optional[int] = None
    metadata: Dict[str, Any] = Field(default_factory=dict)


# Schema for customer billing information
class CustomerBillingInfo(BaseModel):
    billing_email: Optional[EmailStr]
    billing_name: Optional[str]
    billing_phone: Optional[str]
    billing_address: Optional[Dict[str, Any]]
    tax_id: Optional[str]


# Schema for customer metadata update
class CustomerMetadataUpdate(BaseModel):
    metadata: Dict[str, Any]


# Schema for customer status update
class CustomerStatusUpdate(BaseModel):
    status: CustomerStatus
    reason: Optional[str] = None


# Schema for customer deletion
class CustomerDelete(BaseModel):
    permanent: bool = False
    reason: Optional[str] = None
