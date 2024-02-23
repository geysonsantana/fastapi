from typing import ClassVar, List

from pydantic_settings import BaseSettings
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.decl_api import DeclarativeMeta


class Settings(BaseSettings):
        API_V1_STR: str = '/api/v1'
        DB_URL: str = 'postgresql+asyncpg://usuario:senha@localhost:5432/faculdade'
        DBBaseModel: ClassVar[DeclarativeMeta] = declarative_base()

        JWT_SECRET: str = 'OCbQlEN-2uNEh84UFCwLPPgubc-nJwJWWx0AwF9E6ZA'

        #Abaixo para gerar o token
        """
        import secrets
        token: str = secrets.token_urlsafe(32)
        """

        ALGORITHM: str = 'HS256'
        # 60 minutos * 24 horas * 7 dias
        ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7

        class Config:
            case_sensitive = True

settings: Settings = Settings()