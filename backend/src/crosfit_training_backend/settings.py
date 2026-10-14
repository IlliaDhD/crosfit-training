from dataclasses import dataclass
from os import getenv


@dataclass(frozen=True)
class Settings:
    LOG_LEVEL: str

    # Keycloak
    KEYCLOAK_URL: str
    KEYCLOAK_REALM: str
    KEYCLOAK_CLIENT_ID: str
    KEYCLOAK_ADMIN_ROLE: str

    @property
    def KEYCLOAK_JWKS_URL(self) -> str:
        return (
            f"{self.KEYCLOAK_URL}/realms/{self.KEYCLOAK_REALM}"
            "/protocol/openid-connect/certs"
        )

    @property
    def KEYCLOAK_ISSUER(self) -> str:
        return f"{self.KEYCLOAK_URL}/realms/{self.KEYCLOAK_REALM}"


_settings: Settings | None = None


def get_settings() -> Settings:
    global _settings

    if _settings is None:
        _settings = Settings(
            LOG_LEVEL=getenv("LOG_LEVEL"),
            KEYCLOAK_URL=getenv("KEYCLOAK_URL"),
            KEYCLOAK_REALM=getenv("KEYCLOAK_REALM"),
            KEYCLOAK_CLIENT_ID=getenv("KEYCLOAK_CLIENT_ID"),
            KEYCLOAK_ADMIN_ROLE=getenv("KEYCLOAK_ADMIN_ROLE_NAME"),
        )

    return _settings
