from abc import ABC, abstractmethod

from ..request_objects import CreateMGadgetRequest
from ..response_objects import CreateMGadgetResponse


class CreateMGadgetUseCase(ABC):
    @abstractmethod
    def handle(self, request: CreateMGadgetRequest) -> CreateMGadgetResponse:
        raise NotImplementedError()
