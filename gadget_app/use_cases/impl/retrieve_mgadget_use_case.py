from gadget_app.adapters.repositories import MGadgetRepository
from gadget_app.exceptions import UnexpectedError
from gadget_app.request_objects import RetrieveMGadgetRequest
from gadget_app.response_objects import RetrieveMGadgetResponse
from ..base_use_case import BaseUseCase


class RetrieveMGadgetUseCase(BaseUseCase):
    def __init__(self, repo: MGadgetRepository):
        self._repo = repo
        
    def handle(self, request: RetrieveMGadgetRequest) -> RetrieveMGadgetResponse:
        mgadget = self._repo.get(request.id)
        
        if mgadget is None:
            raise UnexpectedError("Failed to retrieve gadget.")
        
        return RetrieveMGadgetResponse(mgadget)