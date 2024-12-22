import stripe
from fastapi import Request, HTTPException, status
from core.config import settings

# Configura tu clave secreta de Stripe y la clave del webhook
stripe.api_key = settings.STRIPE_SECRET_KEY
WEBHOOK_SECRET = settings.STRIPE_WEBHOOK_SECRET


class WebhookServices:

    @staticmethod
    async def handle_webhook(request: Request):
        """
        Maneja los eventos de webhook de Stripe.

        :param request: Objeto de solicitud (request) de FastAPI.
        :return: Respuesta con el manejo del evento.
        """
        try:
            # Obtén el payload del webhook
            payload = await request.body()

            # Verifica la firma del webhook usando la clave secreta
            sig_header = request.headers.get("Stripe-Signature")
            if not sig_header:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Firma de Stripe ausente"
                )

            # Construir el evento usando la clave secreta del webhook
            event = stripe.Webhook.construct_event(
                payload=payload,
                sig_header=sig_header,
                secret=WEBHOOK_SECRET
            )

        except ValueError as e:
            # Maneja errores en el cuerpo de la solicitud
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Payload inválido"
            )
        except stripe.error.SignatureVerificationError as e:
            # Maneja errores de verificación de firma
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Firma de webhook inválida"
            )

        # Procesa el evento
        return await WebhookServices.process_event(event)

    @staticmethod
    async def process_event(event: dict):
        """
        Procesa el evento del webhook.

        :param event: Evento del webhook.
        :return: Respuesta con el manejo del evento.
        """
        event_type = event.get("type")
        data = event.get("data", {}).get("object", {})

        # Diccionario de eventos y funciones asociadas
        event_handlers = {
            "payment_intent.succeeded": WebhookServices.handle_payment_intent_succeeded,
            "checkout.session.completed": WebhookServices.handle_checkout_session_completed,
            "customer.subscription.created": WebhookServices.handle_subscription_created,
            "product.updated": WebhookServices.handle_product_updated,
            "price.updated": WebhookServices.handle_price_updated,
            # Agrega aquí más eventos según sea necesario
        }

        # Llama a la función asociada al evento si existe
        handler = event_handlers.get(event_type)
        if handler:
            return await handler(data)
        else:
            return {"message": f"Evento {event_type} no manejado", "data": data}

    @staticmethod
    async def handle_payment_intent_succeeded(data: dict):
        """
        Maneja el evento 'payment_intent.succeeded'.
        """
        print(f"Pago exitoso: {data}")
        return {"message": "Pago exitoso procesado", "data": data}

    @staticmethod
    async def handle_checkout_session_completed(data: dict):
        """
        Maneja el evento 'checkout.session.completed'.
        """
        print(f"Sesión completada: {data}")
        return {"message": "Sesión de checkout completada", "data": data}

    @staticmethod
    async def handle_subscription_created(data: dict):
        """
        Maneja el evento 'customer.subscription.created'.
        """
        print(f"Suscripción creada: {data}")
        return {"message": "Suscripción creada correctamente", "data": data}

    @staticmethod
    async def handle_product_updated(data: dict):
        """
        Maneja el evento 'product.updated'.
        """
        print(f"Producto actualizado: {data}")
        return {"message": "Producto actualizado", "data": data}

    @staticmethod
    async def handle_price_updated(data: dict):
        """
        Maneja el evento 'price.updated'.
        """
        print(f"Precio actualizado: {data}")
        return {"message": "Precio actualizado", "data": data}
