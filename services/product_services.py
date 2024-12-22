from typing import Any

import stripe
from core.config import settings
from schemas.product_schemas import ProductCreate, ProductUpdate

stripe.api_key = settings.STRIPE_SECRET_KEY


class ProductServices:

    @staticmethod
    async def create_product(product_data: ProductCreate) -> dict[str, Any]:
        """
        Crea un producto en Stripe.

        :param product_data: Esquema para crear el producto.
        :return: Datos del producto creado.
        """
        product_object = product_data.model_dump(exclude_unset=True)
        product = stripe.Product.create(**product_object)
        return product

    @staticmethod
    async def update_product(product_id: str, product_data: ProductUpdate) -> dict[str, Any]:
        """
        Actualiza un producto en Stripe.

        :param product_id: ID del producto a actualizar.
        :param product_data: Nuevos datos (opcional).
        :return: Datos del producto actualizado.
        """
        # Filtra los campos que no son None
        update_data = product_data.model_dump(exclude_unset=True)

        if not update_data:
            raise ValueError("No hay datos válidos para actualizar el producto")

        product = stripe.Product.modify(
            product_id,
            **update_data
        )
        return product

    @staticmethod
    async def delete_product(product_id: str) -> dict[str, Any]:
        """
        Elimina un producto en Stripe.

        :param product_id: ID del producto a eliminar.
        :return: Datos del producto eliminado.
        """
        deleted_product = stripe.Product.delete(product_id)
        return deleted_product

    @staticmethod
    async def get_product_by_id(product_id: str) -> dict[str, Any]:
        """
        Obtiene un producto de Stripe por su ID.

        :param product_id: ID del producto.
        :return: Datos del producto.
        """
        product = stripe.Product.retrieve(product_id)
        return product

    @staticmethod
    async def list_products(active_only: bool = True, limit: int = 100) -> list[dict[str, Any]]:
        """
        Lista todos los productos de Stripe.

        :param active_only: Sí se debe filtrar por productos activos (opcional, por defecto True).
        :param limit: Número máximo de productos a obtener (opcional, por defecto 100).
        :return: Lista de productos.
        """
        products_response = stripe.Product.list(
            active=active_only,
            limit=limit
        )
        return products_response.get("data", [])
