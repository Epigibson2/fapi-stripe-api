from pydantic import BaseModel
from typing import Any


class PriceBase(BaseModel):
    """
    Base schema para precios con atributos comunes.
    """
    unit_amount: int
    currency: str
    recurring: dict[str, Any] = None
    metadata: dict[str, Any] = None
    product: str  # ID del producto relacionado


class PriceCreate(PriceBase):
    """
    Schema para crear un precio.
    """
    nickname: str = None
    tax_behavior: str = None  # Puede ser 'inclusive', 'exclusive', o 'unspecified'


class PriceUpdate(BaseModel):
    """
    Schema para actualizar un precio.
    """
    active: bool = None
    nickname: str = None
    metadata: dict[str, Any] = None


class PriceResponse(PriceBase):
    """
    Schema para retornar los datos de un precio.
    """
    id: str
    active: bool
    created: int
    updated: int = None
    nickname: str = None
    tax_behavior: str = None

    class Config:
        from_attributes = True


class PriceListResponse(BaseModel):
    """
    Schema para la lista de precios.
    """
    items: list[PriceResponse]
    total: int
    has_more: bool
    object: str = "list"
