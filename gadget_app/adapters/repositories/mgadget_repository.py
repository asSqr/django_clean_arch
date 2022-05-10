from .base_repository import BaseRepository
from gadget_app.models import BaseModel
from typing import List, Dict, Any


class MGadgetRepository(BaseRepository):
    def __init__(self, model_class: BaseModel) -> None:
        self.model_class = model_class
        
    def get(self, id: str) -> BaseModel:
        return self.model_class.objects.get(id=id)
    
    def all(self) -> List[BaseModel]:
        return self.model_class.objects.all()

    def create(self, data: Dict[str, Any]) -> str:
        model = self.model_class(**data)
        
        model.save()
        
        return str(model.id)

    def update(self, data: Dict[str, Any]) -> None:
        model = self.model_class(**data)
        data.pop('id')
        self.model_class.objects.bulk_update([model], data.keys())
        
    def delete(self, id: str) -> None:
        model = self.model_class.objects.get(id=id)
        
        model.delete()
