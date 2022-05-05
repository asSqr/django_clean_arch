import logging
from dataclasses import asdict

from gadget_app.adapters.repositories import MGadgetRepository
from gadget_app.exceptions import UnexpectedError
from gadget_app.request_objects import CreateMGadgetRequest
from gadget_app.response_objects import CreateMGadgetResponse
from ..base_use_case import BaseUseCase


class CreateMGadgetUseCase(BaseUseCase):
    def __init__(self, repo: MGadgetRepository):
        self._repo = repo
        
    def handle(self, request: CreateMGadgetRequest) -> CreateMGadgetResponse:
        try:
            mgadget_id = self._repo.create(asdict(request))
        except Exception as e:
            logging.exception(e)
            
            raise UnexpectedError("Failed to create gadget.")
        
        return CreateMGadgetResponse(mgadget_id)
