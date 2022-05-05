import logging

from adapters.repositories import MGadgetRepository
from exceptions import UnexpectedError
from request_objects import CreateMGadgetRequest
from response_objects import CreateMGadgetResponse
from ..create_mgadget_use_case import CreateMGadgetUseCase


class CreateMGadgetUseCaseImpl(CreateMGadgetUseCase):
    def __init__(self, repo: MGadgetRepository):
        self._repo = repo
        
    def handle(self, request: CreateMGadgetRequest) -> CreateMGadgetResponse:
        try:
            mgadget_id = self._repo.create(request.asdict())
        except Exception as e:
            logging.exception(e)
            
            raise UnexpectedError("Failed to create gadget.")
        
        return CreateMGadgetResponse(mgadget_id)
