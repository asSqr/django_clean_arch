from abc import ABC
from dataclasses import dataclass
from typing import Dict, Any


@dataclass
class BaseResponse(ABC):
    def to_json(self) -> Dict[str, Any]:
        raise NotImplementedError()
