from abc import ABC, abstractmethod

from ..request_objects import BaseRequest
from ..response_objects import BaseResponse


class BaseUseCase(ABC):
    @abstractmethod
    def handle(self, request: BaseRequest) -> BaseResponse:
        raise NotImplementedError()
