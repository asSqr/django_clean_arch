import json

from django.http import HttpRequest, HttpResponse
from gadget_app.exceptions.errors import ValidationError

from gadget_app.request_objects import (
    RetrieveMGadgetRequest,
    ListMGadgetRequest,
    CreateMGadgetRequest,
    UpdateMGadgetRequest,
    DeleteMGadgetRequest,
)

from gadget_app.use_cases import (
    RetrieveMGadgetUseCase,
    ListMGadgetUseCase,
    CreateMGadgetUseCase,
    UpdateMGadgetUseCase,
    DeleteMGadgetUseCase,
)

from gadget_app.models import MGadgetModel
from gadget_app.utils import optional_or
from ..repositories import MGadgetRepository
from .handlers import handle_success


def mgadget_id_handler(request: HttpRequest, id: str) -> HttpResponse:
    resp = None
    
    resp = optional_or(resp, retrieve_mgadget(request, id))
    resp = optional_or(resp, update_mgadget(request, id))
    resp = optional_or(resp, delete_mgadget(request, id))
    
    return resp
    
    
def mgadget_handler(request: HttpRequest) -> HttpResponse:
    resp = None
    
    resp = optional_or(resp, list_mgadget(request))
    resp = optional_or(resp, create_mgadget(request))
    
    return resp


def retrieve_mgadget(request: HttpRequest, id: str) -> HttpResponse:
    if request.method == 'GET':
        req = RetrieveMGadgetRequest(id)
        
        repo = MGadgetRepository(MGadgetModel)
        use_case = RetrieveMGadgetUseCase(repo)
        
        resp = use_case.handle(req)
        
        return handle_success(resp)
    
    
def list_mgadget(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        req = ListMGadgetRequest()
        
        repo = MGadgetRepository(MGadgetModel)
        use_case = ListMGadgetUseCase(repo)
        
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
    
    
def update_mgadget(request: HttpRequest, id: str) -> HttpResponse:
    if request.method == 'PUT' or request.method == 'PATCH':
        data = json.loads(request.body)
        
        if 'id' in data and id != data['id']:
            raise ValidationError("Invalid id.")
        
        data['id'] = id
        
        req = UpdateMGadgetRequest(data)
        
        repo = MGadgetRepository(MGadgetModel)
        use_case = UpdateMGadgetUseCase(repo)
        
        resp = use_case.handle(req)
        
        return handle_success(resp)


def delete_mgadget(request: HttpRequest, id: str) -> HttpResponse:
    if request.method == 'DELETE':
        req = DeleteMGadgetRequest(id)
        
        repo = MGadgetRepository(MGadgetModel)
        use_case = DeleteMGadgetUseCase(repo)
        
        resp = use_case.handle(req)
        
        return handle_success(resp)
