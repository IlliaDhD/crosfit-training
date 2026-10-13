# Authorization

# _bearer = HTTPBearer()


# async def get_current_user(
#    credentials: HTTPAuthorizationCredentials = Depends(_bearer),
# ) -> KeycloakUser:
#    payload = await decode_token(credentials.credentials)
#    try:
#        return KeycloakUser.model_validate(payload)
#    except Exception:  # raises when token do not provide valid payload
#        raise AuthError()


