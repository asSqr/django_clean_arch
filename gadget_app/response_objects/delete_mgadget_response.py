from dataclasses import dataclass
from .base_response import BaseResponse
from typing import Dict, Any


@dataclass
class DeleteMGadgetResponse(BaseResponse):
    def to_json(self) -> Dict[str, Any]:
        return {}
