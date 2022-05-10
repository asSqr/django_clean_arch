from dataclasses import dataclass
from .base_request import BaseRequest


@dataclass
class DeleteMGadgetRequest(BaseRequest):
    id: str
    
    def __post_init__(self) -> None:
        pass
