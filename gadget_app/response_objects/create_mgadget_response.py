from dataclasses import dataclass, asdict
from .base_response import BaseResponse
from typing import Dict, Any


@dataclass
class CreateMGadgetResponse(BaseResponse):
    mgadget_id: str
    
    def to_json(self) -> Dict[str, Any]:
        return asdict(self)
