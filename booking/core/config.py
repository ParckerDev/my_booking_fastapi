from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    db_url = "postgresql+asyncpg://MtkServiceUser:MtkServicePassword@localhost/booking_service_fa"



settings = Settings()