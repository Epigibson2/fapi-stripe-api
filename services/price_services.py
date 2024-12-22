import stripe
from typing import Any

from core.config import settings
from schemas.price_schemas import PriceCreate, PriceUpdate

# Configura tu clave secreta de Stripe
stripe.api_key = settings.STRIPE_SECRET_KEY


class PriceServices:

    @staticmethod
    async def create_price(price_data: PriceCreate) -> dict[str, Any]:
        """
        Crea un precio en Stripe.

        :param price_data: Esquema PriceCreate con los datos del precio.
        :return: Datos del precio creado en Stripe.
        """
        # Convierte el esquema en un diccionario y envía los datos a Stripe
        price_object = price_data.model_dump(exclude_unset=True)
        price = stripe.Price.create(**price_object)
        return price

    @staticmethod
    async def update_price(price_id: str, price_data: PriceUpdate) -> dict[str, Any]:
        """
        Actualiza un precio en Stripe.

        :param price_id: ID del precio a actualizar.
        :param price_data: Esquema PriceUpdate con los datos a actualizar.
        :return: Datos del precio actualizado en Stripe.
        """
        # Convierte el esquema en un diccionario y envía los datos a Stripe
        update_data = price_data.model_dump(exclude_unset=True)
        if not update_data:
            raise ValueError("No hay datos válidos para actualizar el precio")
        updated_price = stripe.Price.modify(price_id, **update_data)
        return updated_price

    @staticmethod
    async def delete_price(price_id: str) -> dict[str, Any]:
        """
        Elimina un precio en Stripe.

        :param price_id: ID del precio a eliminar.
        :return: Datos del precio eliminado.
        """
        deleted_price = stripe.Price.modify(price_id, active=False)
        return deleted_price

    @staticmethod
    async def get_price_by_id(price_id: str) -> dict[str, Any]:
        """
        Obtiene un precio de Stripe por su ID.

        :param price_id: ID del precio.
        :return: Datos del precio.
        """
        price = stripe.Price.retrieve(price_id)
        return price

    @staticmethod
    async def list_prices(product_id: str = None, active_only: bool = True, limit: int = 100) -> list[dict[str, Any]]:
        """
        Lista los precios de Stripe.

        :param product_id: ID del producto relacionado (opcional).
        :param active_only: Filtra solo precios activos (opcional).
        :param limit: Número máximo de precios a obtener (opcional).
        :return: Lista de precios.
        """
        prices_response = stripe.Price.list(
            product=product_id,
            active=active_only,
            limit=limit
        )
        return prices_response.get("data", [])
