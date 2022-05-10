import logging

from gadget_app.adapters.repositories import MGadgetRepository
from gadget_app.exceptions import UnexpectedError
from gadget_app.request_objects import UpdateMGadgetRequest
from gadget_app.response_objects import UpdateMGadgetResponse
from ..base_use_case import BaseUseCase


class UpdateMGadgetUseCase(BaseUseCase):
    def __init__(self, repo: MGadgetRepository) -> None:
        self._repo = repo
        
    def handle(self, request: UpdateMGadgetRequest) -> UpdateMGadgetResponse:
        try:
            self._repo.update(request.data)
        except Exception as e:
            logging.exception(e)
            
            raise UnexpectedError("Failed to update gadget.")
        
        return UpdateMGadgetResponse()
