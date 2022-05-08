import json

from django.http import HttpRequest, HttpResponse

from gadget_app.request_objects import (
    RetrieveMGadgetRequest,
    CreateMGadgetRequest,
)

from gadget_app.use_cases import (
    RetrieveMGadgetUseCase,
    CreateMGadgetUseCase,
)

from gadget_app.models import MGadgetModel
from ..repositories import MGadgetRepository
from .handlers import handle_success


def retrieve_mgadget(request: HttpRequest, id: str) -> HttpResponse:
    if request.method == 'GET':
        req = RetrieveMGadgetRequest(id)
        
        repo = MGadgetRepository(MGadgetModel)
        use_case = RetrieveMGadgetUseCase(repo)
        
        resp = use_case.handle(req)
        
        return handle_success(resp)


def create_mgadget(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        data = json.loads(request.body)
        
        req = CreateMGadgetRequest(**data)
        
        repo = MGadgetRepository(MGadgetModel)
        use_case = CreateMGadgetUseCase(repo)
        
        resp = use_case.handle(req)
        
        return handle_success(resp)
