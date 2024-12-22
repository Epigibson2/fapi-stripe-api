import stripe
from stripe import PaymentIntent, SetupIntent, Charge, Refund

from core.config import settings
from schemas.payment_schemas import (
    PaymentIntentCreate,
    SetupIntentCreate,
    ChargeCreate,
    RefundCreate,
)

# Configura tu clave secreta de Stripe
stripe.api_key = settings.STRIPE_SECRET_KEY


class PaymentServices:

    # ------------- PaymentIntent Services -------------

    @staticmethod
    async def create_payment_intent(payment_data: PaymentIntentCreate) -> PaymentIntent:
        """
        Crea un PaymentIntent en Stripe.

        :param payment_data: Datos del PaymentIntent a crear.
        :return: PaymentIntent creado.
        """
        payment_object = payment_data.model_dump(exclude_unset=True)
        payment_intent = stripe.PaymentIntent.create(**payment_object)
        return payment_intent

    @staticmethod
    async def retrieve_payment_intent(payment_intent_id: str) -> PaymentIntent:
        """
        Obtiene un PaymentIntent por su ID.

        :param payment_intent_id: ID del PaymentIntent.
        :return: Datos del PaymentIntent.
        """
        payment_intent = stripe.PaymentIntent.retrieve(payment_intent_id)
        return payment_intent

    # ------------- SetupIntent Services -------------

    @staticmethod
    async def create_setup_intent(setup_data: SetupIntentCreate) -> SetupIntent:
        """
        Crea un SetupIntent en Stripe.

        :param setup_data: Datos del SetupIntent a crear.
        :return: SetupIntent creado.
        """
        setup_object = setup_data.model_dump(exclude_unset=True)
        setup_intent = stripe.SetupIntent.create(**setup_object)
        return setup_intent

    @staticmethod
    async def retrieve_setup_intent(setup_intent_id: str) -> SetupIntent:
        """
        Obtiene un SetupIntent por su ID.

        :param setup_intent_id: ID del SetupIntent.
        :return: Datos del SetupIntent.
        """
        setup_intent = stripe.SetupIntent.retrieve(setup_intent_id)
        return setup_intent

    # ------------- Charge Services -------------

    @staticmethod
    async def create_charge(charge_data: ChargeCreate) -> Charge:
        """
        Crea un Charge en Stripe.

        :param charge_data: Datos del Charge a crear.
        :return: Charge creado.
        """
        charge_object = charge_data.model_dump(exclude_unset=True)
        charge = stripe.Charge.create(**charge_object)
        return charge

    @staticmethod
    async def retrieve_charge(charge_id: str) -> Charge:
        """
        Obtiene un Charge por su ID.

        :param charge_id: ID del Charge.
        :return: Datos del Charge.
        """
        charge = stripe.Charge.retrieve(charge_id)
        return charge

    # ------------- Refund Services -------------

    @staticmethod
    async def create_refund(refund_data: RefundCreate) -> Refund:
        """
        Crea un Refund en Stripe.

        :param refund_data: Datos del Refund a crear.
        :return: Refund creado.
        """
        refund_object = refund_data.model_dump(exclude_unset=True)
        refund = stripe.Refund.create(**refund_object)
        return refund

    @staticmethod
    async def retrieve_refund(refund_id: str) -> Refund:
        """
        Obtiene un Refund por su ID.

        :param refund_id: ID del Refund.
        :return: Datos del Refund.
        """
        refund = stripe.Refund.retrieve(refund_id)
        return refund
