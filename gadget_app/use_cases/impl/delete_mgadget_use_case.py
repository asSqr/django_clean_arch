from gadget_app.adapters.repositories import MGadgetRepository
from gadget_app.exceptions import UnexpectedError
from gadget_app.request_objects import DeleteMGadgetRequest
from gadget_app.response_objects import DeleteMGadgetResponse
from ..base_use_case import BaseUseCase


class DeleteMGadgetUseCase(BaseUseCase):
    def __init__(self, repo: MGadgetRepository) -> None:
        self._repo = repo
        
    def handle(self, request: DeleteMGadgetRequest) -> DeleteMGadgetResponse:
        try:
            self._repo.delete(request.id)
        except Exception:
            raise UnexpectedError('Failed to delete gadget.')
        
        return DeleteMGadgetResponse()
