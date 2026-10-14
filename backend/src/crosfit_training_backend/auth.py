import logging

import httpx
from jose import JWTError, jwt
from jose.exceptions import ExpiredSignatureError
from src.crosfit_training_backend.exceptions import AuthError
from src.crosfit_training_backend.settings import get_settings

settings = get_settings()
_jwks_cache: dict | None = None  # Cache used to verify ANY Keycloak token
logger = logging.getLogger(__name__)


async def _get_jwks() -> dict:
    global _jwks_cache
    if _jwks_cache is None:
        logger.debug("Fetching JWKS")
        async with httpx.AsyncClient(trust_env=False) as client:
            response = await client.get(settings.KEYCLOAK_JWKS_URL)
            response.raise_for_status()
            logger.debug("Successfully fetched JWKS from Keycloak")
            _jwks_cache = response.json()
    return _jwks_cache


async def decode_token(token: str) -> dict:
    try:
        jwks = await _get_jwks()
        payload = jwt.decode(
            token,
            jwks,
            algorithms=["RS256"],
            issuer=settings.KEYCLOAK_ISSUER,
            options={"verify_aud": False},
        )
        return payload
    except ExpiredSignatureError as exc:
        raise AuthError() from exc
    except JWTError as exc:
        logger.warning(f"Failed to decode token, due to a reason: {exc}")
        raise AuthError() from exc
