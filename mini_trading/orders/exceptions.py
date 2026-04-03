class KISError(Exception):
    pass

class AuthError(KISError):
    pass

class OrderError(KISError):
    def __init__(self, message: str, symbol: str = ""):
        super().__init__(message)
        self.symbol = symbol

class ConnectionError(KISError):
    pass