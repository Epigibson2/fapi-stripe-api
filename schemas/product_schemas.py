from pydantic import BaseModel
from typing import Any


class ProductBase(BaseModel):
    """
    Base schema con los atributos comunes de los productos.
    """
    name: str
    description: str = None
    metadata: dict[str, Any] = None


class ProductCreate(ProductBase):
    """
    Schema para crear un producto.
    """
    pass


class ProductUpdate(BaseModel):
    """
    Schema para actualizar un producto.
    """
    name: str = None
    description: str = None
    metadata: dict[str, Any] = None


class ProductResponse(ProductBase):
    """
    Schema para retornar la respuesta de un producto.
    """
    id: str
    active: bool
    created: int
    updated: int = None
    metadata: dict[str, Any]

    class Config:
        from_attributes = True


class ProductListResponse(BaseModel):
    """
    Schema para la lista de productos.
    """
    items: list[ProductResponse]
    total: int
    has_more: bool
    object: str = "list"
