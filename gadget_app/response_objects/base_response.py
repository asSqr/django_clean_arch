from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Dict, Any


@dataclass
class BaseResponse(ABC):
    @abstractmethod
    def to_json(self) -> Dict[str, Any]:
        raise NotImplementedError()
