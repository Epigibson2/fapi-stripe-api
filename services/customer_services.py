from __future__ import annotations

import stripe
from typing import Any
from core.config import settings
from schemas.customer_schemas import CustomerCreate, CustomerUpdate

# Configura tu clave secreta de Stripe
stripe.api_key = settings.STRIPE_SECRET_KEY


class CustomerServices:

    @staticmethod
    async def create_stripe_customer(customer_data: CustomerCreate):
        """
        Crea un cliente en Stripe sin interactuar con la base de datos.
        :param: CustomerCreate
        :return: Datos del cliente creado en Stripe.
        """
        # Crea un cliente en Stripe
        stripe_customer = stripe.Customer.create(
            email=customer_data.email,
            name=customer_data.name,
            phone=customer_data.phone,
            metadata=customer_data.metadata or {}
        )

        return {
            "short_response": {
                "id": stripe_customer["id"],
                "email": stripe_customer["email"],
                "name": stripe_customer["name"],
                "phone": stripe_customer.get("phone"),
                "metadata": stripe_customer["metadata"]
            },
            "full_response": stripe_customer,
            "message": "Customer created successfully"
        }

    @staticmethod
    async def get_stripe_all_customers() -> list[dict[str, Any]]:
        """
        Obtiene todos los clientes de Stripe.

        :return: Lista de clientes de Stripe.
        """
        # Obtiene la lista de clientes desde Stripe
        customers_response = stripe.Customer.list(limit=100)

        # Asegúrate de que 'data' esté presente y sea una lista
        customers = customers_response.get("data", [])
        if not isinstance(customers, list):
            raise ValueError("El campo 'data' no contiene una lista válida de clientes")

        # Procesa los clientes para obtener los datos necesarios
        processed_customers = []
        for customer in customers:
            processed_customers.append(customer)

        return processed_customers if len(processed_customers) > 0 else {
            "message": "No customers found"}

    @staticmethod
    async def get_stripe_customer_by_email(email: str) -> dict | None:
        """
        Obtiene un cliente en Stripe basado en su email.

        :param email: Email del cliente.
        :return: Datos del cliente si existe, None si no se encuentra.
        """
        # Obtiene la lista de clientes desde Stripe
        customers_response = stripe.Customer.list(limit=100)

        # Asegúrate de que 'data' esté presente y sea una lista
        customers = customers_response.get("data", [])
        if not isinstance(customers, list):
            raise ValueError("El campo 'data' no contiene una lista válida de clientes")

        # Busca el cliente por email
        for customer in customers:
            if customer.get("email") == email:  # Usa .get() para evitar KeyError
                return customer  # Retorna toda la data del cliente
        # Si no se encuentra el cliente, devuelve None
        return {"message": "Customer not found"}

    @staticmethod
    async def add_payment_method(
            stripe_customer_id: str,
            payment_method_id: str,
            set_as_default: bool = False
    ) -> dict[str, Any]:
        """
        Agrega un método de pago a un cliente en Stripe.

        :param stripe_customer_id: ID del cliente en Stripe.
        :param payment_method_id: ID del método de pago en Stripe.
        :param set_as_default: Si el método debe establecerse como predeterminado.
        :return: Datos del método de pago agregado.
        """
        payment_method = stripe.PaymentMethod.attach(
            payment_method_id,
            customer=stripe_customer_id
        )

        if set_as_default:
            stripe.Customer.modify(
                stripe_customer_id,
                invoice_settings={
                    "default_payment_method": payment_method_id
                }
            )

        return {
            "id": payment_method["id"],
            "type": payment_method["type"],
            "card": payment_method["card"],
            "is_default": set_as_default
        }

    @staticmethod
    async def update_stripe_customer(
            stripe_customer_id: str,
            customer_data: CustomerUpdate
    ):
        """
        Actualiza un cliente en Stripe.

        :param stripe_customer_id: ID del cliente en Stripe.
        :param customer_data: Datos a actualizar del cliente.
        :return: Datos actualizados del cliente.
        """

        # Filtra los campos que no son None
        update_data = customer_data.model_dump(exclude_unset=True)

        if not update_data:
            raise ValueError("No hay datos válidos para actualizar al cliente")

        # Actualiza el cliente en Stripe
        updated_customer = stripe.Customer.modify(
            stripe_customer_id,
            **update_data
        )
        return updated_customer

    @staticmethod
    async def delete_stripe_customer(stripe_customer_id: str) -> None:
        """
        Elimina un cliente en Stripe.

        :param stripe_customer_id: ID del cliente en Stripe.
        """
        stripe.Customer.delete(stripe_customer_id)

    @staticmethod
    async def get_payment_methods(
            stripe_customer_id: str
    ) -> list[dict[str, Any]]:
        """
        Obtiene la lista de métodos de pago de un cliente en Stripe.

        :param stripe_customer_id: ID del cliente en Stripe.
        :return: Lista de métodos de pago.
        """
        payment_methods_response = stripe.PaymentMethod.list(
            customer=stripe_customer_id,
            type="card"
        )

        # Obtiene la lista de métodos de pago
        payment_methods = payment_methods_response.get("data", [])

        # Validar que "data" es una lista
        if not isinstance(payment_methods, list):
            raise ValueError("El campo 'data' no contiene una lista válida")

            # Procesar y retornar los métodos de pago
        return [
            {
                "id": method.get("id"),
                "type": method.get("type"),
                "card": method.get("card", {})
            }
            for method in payment_methods
        ]

    @staticmethod
    async def create_subscription(
            stripe_customer_id: str,
            price_id: str,
            trial_period_days: int = None
    ) -> dict[str, Any]:
        """
        Crea una suscripción para un cliente en Stripe.

        :param stripe_customer_id: ID del cliente en Stripe.
        :param price_id: ID del precio del plan de suscripción.
        :param trial_period_days: Número de días de prueba gratuitos (opcional).
        :return: Datos de la suscripción creada.
        """
        subscription = stripe.Subscription.create(
            customer=stripe_customer_id,
            items=[{"price": price_id}],
            trial_period_days=trial_period_days
        )

        return {
            "id": subscription["id"],
            "status": subscription["status"],
            "items": subscription["items"]["data"]
        }
