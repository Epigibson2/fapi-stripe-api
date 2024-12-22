from __future__ import annotations

from pydantic import BaseModel, Field
from typing import Annotated


class PaymentBase(BaseModel):
    """
    Base schema para pagos con atributos comunes.
    """
    amount: Annotated[int, Field(gt=0, description="Monto en la unidad más pequeña de la moneda.")]
    currency: str = Field(..., min_length=3, max_length=3, description="Código de moneda (ej: "
                                                                       "'usd').")
    description: str | None = Field(None, description="Descripción del pago.")
    metadata: dict[str, str] | None = Field(None, description="Metadatos adicionales.")


class PaymentIntentCreate(PaymentBase):
    """
    Schema para crear un PaymentIntent.
    """
    payment_method: str = Field(..., description="ID del método de pago.")
    confirm: bool = Field(default=True, description="Confirma automáticamente el PaymentIntent.")
    customer: str | None = Field(None, description="ID del cliente.")
    receipt_email: str | None = Field(None, description="Correo para el recibo.")


class PaymentIntentResponse(PaymentBase):
    """
    Schema para la respuesta de un PaymentIntent.
    """
    id: str = Field(..., description="ID del PaymentIntent.")
    status: str = Field(..., description="Estado del PaymentIntent.")
    created: int = Field(..., description="Timestamp de creación.")
    client_secret: str | None = Field(None, description="Secreto del cliente para confirmar "
                                                        "el pago.")
    receipt_url: str | None = Field(None, description="URL del recibo.")


class SetupIntentCreate(BaseModel):
    """
    Schema para crear un SetupIntent.
    """
    payment_method: str = Field(..., description="ID del método de pago.")
    customer: str | None = Field(None, description="ID del cliente.")
    usage: str = Field(..., description="Uso del SetupIntent ('on_session' o 'off_session').")
    metadata: dict[str, str] | None = Field(None, description="Metadatos adicionales.")


class SetupIntentResponse(BaseModel):
    """
    Schema para la respuesta de un SetupIntent.
    """
    id: str = Field(..., description="ID del SetupIntent.")
    status: str = Field(..., description="Estado del SetupIntent.")
    created: int = Field(..., description="Timestamp de creación.")
    client_secret: str = Field(..., description="Secreto del cliente para confirmar el setup.")
    payment_method: str | None = Field(None, description="ID del método de pago asociado.")


class ChargeCreate(PaymentBase):
    """
    Schema para crear un Charge.
    """
    source: str = Field(..., description="ID del token o fuente del pago.")
    customer: str | None = Field(None, description="ID del cliente (opcional).")


class ChargeResponse(PaymentBase):
    """
    Schema para la respuesta de un Charge.
    """
    id: str = Field(..., description="ID del Charge.")
    status: str = Field(..., description="Estado del Charge.")
    created: int = Field(..., description="Timestamp de creación.")
    receipt_url: str | None = Field(None, description="URL del recibo.")


class RefundCreate(BaseModel):
    """
    Schema para crear un Refund.
    """
    charge: str = Field(..., description="ID del Charge a reembolsar.")
    amount: int | None = Field(None, gt=0, description="Monto a reembolsar.")
    reason: str | None = Field(None, description="Razón del reembolso ('duplicate', "
                                                 "'fraudulent', o 'requested_by_customer').")
    metadata: dict[str, str] | None = Field(None, description="Metadatos adicionales.")


class RefundResponse(BaseModel):
    """
    Schema para la respuesta de un Refund.
    """
    id: str = Field(..., description="ID del Refund.")
    status: str = Field(..., description="Estado del Refund.")
    amount: int = Field(..., gt=0, description="Monto reembolsado.")
    created: int = Field(..., description="Timestamp de creación.")
    charge: str = Field(..., description="ID del Charge asociado.")
    reason: str | None = Field(None, description="Razón del reembolso.")
