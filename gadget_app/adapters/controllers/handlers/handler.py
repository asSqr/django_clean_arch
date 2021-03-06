from gadget_app.response_objects import BaseResponse
from django.http.response import JsonResponse


def handle_success(resp: BaseResponse) -> JsonResponse:
    return JsonResponse(resp.to_json())


def handle_empty() -> JsonResponse:
    return JsonResponse({})
