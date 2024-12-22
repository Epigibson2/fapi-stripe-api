from __future__ import annotations
from pydantic import BaseModel, Field


class PaymentMethodBase(BaseModel):
    """
    Base schema para métodos de pago con atributos comunes.
    """
    type: str = Field(..., description="Tipo de método de pago (ej. 'card').")
    metadata: dict[str, str] | None = Field(None, description="Metadatos adicionales para el "
                                                              "método de pago.")


class PaymentMethodCreate(PaymentMethodBase):
    """
    Schema para crear un método de pago.
    """
    card: dict[str, str] = Field(
        ...,
        description="Datos de la tarjeta (e.g., 'number', 'exp_month', 'exp_year', 'cvc')."
    )


class PaymentMethodAttach(BaseModel):
    """
    Schema para adjuntar un método de pago a un cliente.
    """
    payment_method_id: str = Field(..., description="ID del método de pago.")
    customer: str = Field(..., description="ID del cliente al que se adjunta el método de pago.")


class PaymentMethodDetach(BaseModel):
    """
    Schema para desasociar un método de pago.
    """
    payment_method_id: str = Field(..., description="ID del método de pago a desasociar.")


class PaymentMethodResponse(PaymentMethodBase):
    """
    Schema para la respuesta de un método de pago.
    """
    id: str = Field(..., description="ID del método de pago.")
    created: int = Field(..., description="Fecha de creación en formato timestamp.")
    customer: str | None = Field(None, description="ID del cliente asociado al método de pago.")
    card: dict[str, str] | None = Field(None, description="Detalles de la tarjeta.")
