import json

from gadget_app.request_objects import CreateMGadgetRequest
from ..repositories import MGadgetRepository
from gadget_app.use_cases import CreateMGadgetUseCase
from .handlers import handle_success

from django.views.decorators.csrf import ensure_csrf_cookie


@ensure_csrf_cookie
def create_mgadget(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        
        req = CreateMGadgetRequest(**data)
        
        repo = MGadgetRepository(data)
        use_case = CreateMGadgetUseCase(repo)
        
        resp = use_case.handle(req)
        
        return handle_success(resp)
