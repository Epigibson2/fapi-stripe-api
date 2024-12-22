import stripe
from stripe import PaymentMethod

from core.config import settings
from schemas.payment_method_schemas import (
    PaymentMethodCreate,
    PaymentMethodAttach,
    PaymentMethodDetach,
)

# Configura tu clave secreta de Stripe
stripe.api_key = settings.STRIPE_SECRET_KEY


class PaymentMethodServices:

    @staticmethod
    async def create_payment_method(payment_data: PaymentMethodCreate) -> PaymentMethod:
        """
        Crea un método de pago en Stripe.

        :param payment_data: Datos del método de pago a crear.
        :return: Método de pago creado.
        """
        payment_method_object = payment_data.model_dump(exclude_unset=True)
        payment_method = stripe.PaymentMethod.create(**payment_method_object)
        return payment_method

    @staticmethod
    async def attach_payment_method(attach_data: PaymentMethodAttach) -> PaymentMethod:
        """
        Adjunta un método de pago a un cliente.

        :param attach_data: Datos del método de pago y cliente.
        :return: Método de pago adjuntado.
        """
        payment_method = stripe.PaymentMethod.attach(
            attach_data.payment_method_id,
            customer=attach_data.customer
        )
        return payment_method

    @staticmethod
    async def detach_payment_method(detach_data: PaymentMethodDetach) -> PaymentMethod:
        """
        Desasocia un método de pago.

        :param detach_data: Datos del método de pago a desasociar.
        :return: Método de pago desasociado.
        """
        payment_method = stripe.PaymentMethod.detach(detach_data.payment_method_id)
        return payment_method

    @staticmethod
    async def retrieve_payment_method(payment_method_id: str) -> PaymentMethod:
        """
        Obtiene un método de pago por su ID.

        :param payment_method_id: ID del método de pago.
        :return: Método de pago encontrado.
        """
        payment_method = stripe.PaymentMethod.retrieve(payment_method_id)
        return payment_method

    @staticmethod
    async def list_payment_methods(customer: str, type: str = "card") -> PaymentMethod:
        """
        Lista los métodos de pago de un cliente.

        :param customer: ID del cliente.
        :param type: Tipo de método de pago (por defecto 'card').
        :return: Lista de métodos de pago.
        """
        payment_methods = stripe.PaymentMethod.list(customer=customer, type=type)
        return payment_methods["data"]
