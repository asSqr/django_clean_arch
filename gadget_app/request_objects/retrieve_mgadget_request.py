from dataclasses import dataclass
# from ..exceptions import ValidationError
from .base_request import BaseRequest


@dataclass
class RetrieveMGadgetRequest(BaseRequest):
    id: str
    
    def __post_init__(self):
        pass
