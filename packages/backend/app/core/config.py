from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class Config(BaseSettings):
    app_name: str = "dg-assistant"
    debug: bool = False

    # Primary configuration: provide either database_uri OR individual components
    database_uri: str = ""

    # Alternative: Database connection parameters (used if database_uri is not provided)
    db_user: str = ""
    db_password: str = ""
    db_name: str = ""
    db_host: str = "localhost"
    db_port: int = 5432

    @property
    def database_url(self) -> str:
        """Get the database URL. Uses database_uri if provided, otherwise constructs from components."""
        if self.database_uri:
            return self.database_uri
        return f"postgresql://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"


config = Config()
