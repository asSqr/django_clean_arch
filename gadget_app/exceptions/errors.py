class BaseError(Exception):
    def __init__(self, message: str) -> None:
        self.__message = message
        super().__init__(message)
        
    @property
    def message(self) -> str:
        return self.__message
    

class ValidationError(BaseError):
    def __init__(self, cause: str) -> None:
        super().__init__(message=f'The request is invalid. {cause}')
        

class UnexpectedError(BaseError):
    def __init__(self, state: str) -> None:
        super().__init__(message=f'Unexpected error occurred. {state}')
