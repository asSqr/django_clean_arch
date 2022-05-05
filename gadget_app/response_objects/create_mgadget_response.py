from dataclasses import dataclass
from .base_response import BaseResponse


@dataclass
class CreateMGadgetResponse(BaseResponse):
    mgadget_id: str
