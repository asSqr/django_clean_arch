import json

from gadget_app.request_objects import CreateMGadgetRequest
from gadget_app.models import MGadgetModel
from ..repositories import MGadgetRepository
from gadget_app.use_cases import CreateMGadgetUseCase
from .handlers import handle_success


def create_mgadget(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        
        req = CreateMGadgetRequest(**data)
        
        repo = MGadgetRepository(MGadgetModel)
        use_case = CreateMGadgetUseCase(repo)
        
        resp = use_case.handle(req)
        
        return handle_success(resp)
