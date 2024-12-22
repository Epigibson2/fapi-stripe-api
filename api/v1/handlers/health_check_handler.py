from fastapi import APIRouter

health_check_router = APIRouter()


@health_check_router.get("/",  summary="Health Check", tags=["Health-Check"])
async def health_check():
    try:
        # Lógica de verificación de salud
        # Puedes realizar comprobaciones adicionales aquí
        return {"status": "Health from Stripe API is checked!"}
    except Exception as e:
        # Manejo de errores
        return {"status": "error", "message": str(e)}
