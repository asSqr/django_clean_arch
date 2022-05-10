from abc import ABC, abstractmethod
from typing import List, Dict, Any

from gadget_app.models import BaseModel


class BaseRepository(ABC):
    @abstractmethod
    def __init__(self, model_class: BaseModel) -> None:
        raise NotImplementedError()
    
    @abstractmethod
    def get(self, id: str) -> BaseModel:
        raise NotImplementedError()
    
    @abstractmethod
    def all(self) -> List[BaseModel]:
        raise NotImplementedError()

    @abstractmethod
    def create(self, data: Dict[str, Any]) -> str:
        raise NotImplementedError()
    
    @abstractmethod
    def update(self, data: Dict[str, Any]) -> None:
        raise NotImplementedError()
    
    @abstractmethod
    def delete(self, id: str) -> None:
        raise NotImplementedError()
