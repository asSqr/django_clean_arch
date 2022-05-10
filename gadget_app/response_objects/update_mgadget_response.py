from dataclasses import dataclass
from .base_response import BaseResponse
from typing import Dict, Any


@dataclass
class UpdateMGadgetResponse(BaseResponse):
    def to_json(self) -> Dict[str, Any]:
        return {}
