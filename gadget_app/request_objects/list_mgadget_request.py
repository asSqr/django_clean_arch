from dataclasses import dataclass
# from ..exceptions import ValidationError
from .base_request import BaseRequest


@dataclass
class ListMGadgetRequest(BaseRequest):
    def __post_init__(self) -> None:
        pass
