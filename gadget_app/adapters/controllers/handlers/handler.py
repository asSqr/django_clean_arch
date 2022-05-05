from gadget_app.response_objects import BaseResponse
from django.http.response import JsonResponse
from dataclasses import asdict


def handle_success(resp: BaseResponse) -> JsonResponse:
    return JsonResponse(asdict(resp))


def handle_empty() -> JsonResponse:
    return JsonResponse({})
