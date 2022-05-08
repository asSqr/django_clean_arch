from abc import ABC, abstractmethod

from gadget_app.adapters.repositories.base_repository import BaseRepository
from ..request_objects import BaseRequest
from ..response_objects import BaseResponse


class BaseUseCase(ABC):
    @abstractmethod
    def __init__(self, repo: BaseRepository):
        raise NotImplementedError()
    
    @abstractmethod
    def handle(self, request: BaseRequest) -> BaseResponse:
        raise NotImplementedError()
