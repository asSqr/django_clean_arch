from dataclasses import dataclass
from .base_request import BaseRequest
from typing import Dict, Any


@dataclass
class UpdateMGadgetRequest(BaseRequest):
    data: Dict[str, Any]
    
    def __post_init__(self):
        pass
