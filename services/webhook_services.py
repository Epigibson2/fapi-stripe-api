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

        # Manejo de eventos específicos
        if event_type == "payment_intent.succeeded":
            return {"message": "Pago exitoso procesado", "data": data}

        elif event_type == "invoice.payment_succeeded":
            return {"message": "Pago de factura exitoso", "data": data}

        elif event_type == "customer.subscription.created":
            return {"message": "Suscripción creada", "data": data}

        elif event_type == "product.updated":
            return {"message": "Producto actualizado", "data": data}

        elif event_type == "price.updated":
            return {"message": "Precio actualizado", "data": data}

        else:
            # Otros eventos no manejados específicamente
            return {"message": f"Evento {event_type} no manejado", "data": data}
