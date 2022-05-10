from gadget_app.adapters.repositories import MGadgetRepository
from gadget_app.request_objects import ListMGadgetRequest
from gadget_app.response_objects import ListMGadgetResponse
from ..base_use_case import BaseUseCase


class ListMGadgetUseCase(BaseUseCase):
    def __init__(self, repo: MGadgetRepository):
        self._repo = repo
        
    def handle(self, request: ListMGadgetRequest) -> ListMGadgetResponse:
        mgadgets = self._repo.all()
        
        return ListMGadgetResponse(mgadgets)
