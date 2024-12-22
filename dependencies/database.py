from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from core.config import settings



async def init_db():
    """
    Inicializa la conexión a la base de datos y configura los modelos de documentos.

    :return: None
    """
    client = AsyncIOMotorClient(settings.DATABASE_URL)

    await init_beanie(
        database=client[settings.DATABASE_NAME],
        document_models=[

        ],
    )
