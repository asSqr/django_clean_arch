from django.http import HttpResponse
from typing import Optional


def optional_or(acc: Optional[HttpResponse], resp: Optional[HttpResponse]) -> Optional[HttpResponse]:
    if acc is not None:
        return acc
    
    return resp
