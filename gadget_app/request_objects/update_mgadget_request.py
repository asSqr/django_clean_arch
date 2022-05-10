from dataclasses import dataclass
from .base_request import BaseRequest
from gadget_app.exceptions import ValidationError
from typing import Dict, Any


@dataclass
class UpdateMGadgetRequest(BaseRequest):
    data: Dict[str, Any]
    id: str
    
    def __post_init__(self) -> None:
        if 'id' in self.data and self.id != self.data['id']:
            raise ValidationError("Invalid id.")
