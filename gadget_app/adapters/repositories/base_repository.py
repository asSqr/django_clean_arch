from abc import ABC, abstractmethod
from typing import Dict, Any, Optional

from gadget_app.models import BaseModel


class BaseRepository(ABC):
    @abstractmethod
    def __init__(self, model_class: BaseModel):
        raise NotImplementedError()
    
    @abstractmethod
    def get(self, id: str) -> Optional[BaseModel]:
        raise NotImplementedError()

    @abstractmethod
    def create(self, data: Dict[str, Any]) -> str:
        raise NotImplementedError()
