from gadget_app.adapters.repositories import MGadgetRepository
from gadget_app.exceptions import UnexpectedError
from gadget_app.request_objects import RetrieveMGadgetRequest
from gadget_app.response_objects import RetrieveMGadgetResponse
from ..base_use_case import BaseUseCase


class RetrieveMGadgetUseCase(BaseUseCase):
    def __init__(self, repo: MGadgetRepository) -> None:
        self._repo = repo
        
    def handle(self, request: RetrieveMGadgetRequest) -> RetrieveMGadgetResponse:
        mgadget = None
        
        try:
            mgadget = self._repo.get(request.id)
        except Exception:
            raise UnexpectedError("Failed to retrieve gadget.")
        
        return RetrieveMGadgetResponse(mgadget)
