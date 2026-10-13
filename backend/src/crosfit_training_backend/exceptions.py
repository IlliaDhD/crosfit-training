class AppError(Exception):
    status_code = 400
    error_message = "An error occurred while processing the request"


class AuthError(AppError):
    status_code = 401
    error_message = "Invalid credentials"
