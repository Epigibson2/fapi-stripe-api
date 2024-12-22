from datetime import datetime
from typing import Optional, Dict, Any
from beanie import Document
from pydantic import EmailStr, Field
from uuid import UUID, uuid4
from enum import Enum


class CustomerStatus(str, Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    DELINQUENT = "delinquent"


class Customer(Document):
    id: UUID = Field(default_factory=uuid4)
    email: EmailStr
    name: str
    stripe_customer_id: Optional[str] = None
    phone: Optional[str] = None
    status: CustomerStatus = CustomerStatus.ACTIVE
    metadata: Dict[str, Any] = Field(default_factory=dict)
    default_payment_method: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

    class Settings:
        name = "customers"
        indexes = [
            "email",
            "stripe_customer_id"
        ]
