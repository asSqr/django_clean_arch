from abc import ABC
from typing import Dict, Any

from gadget_app.models import BaseModel


class BaseRepository(ABC):
    def __init__(self, model_class: BaseModel):
        raise NotImplementedError()

    def create(self, data: Dict[str, Any]) -> str:
        raise NotImplementedError()
