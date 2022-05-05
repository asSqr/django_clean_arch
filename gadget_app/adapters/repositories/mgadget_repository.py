from .base_repository import BaseRepository
from gadget_app.models import BaseModel
from typing import Dict, Any


class MGadgetRepository(BaseRepository):
    def __init__(self, model_class: BaseModel):
        self.model_class = model_class

    def create(self, data: Dict[str, Any]) -> str:
        model = self.model_class(**data)
        
        model.save()
        
        return str(model.id)
