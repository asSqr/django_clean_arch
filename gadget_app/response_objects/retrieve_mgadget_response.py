from dataclasses import dataclass
from .base_response import BaseResponse
from gadget_app.models import MGadgetModel
from typing import Dict, Any


@dataclass
class RetrieveMGadgetResponse(BaseResponse):
    mgadget: MGadgetModel

    def to_json(self) -> Dict[str, Any]:
        return {
            'id': str(self.mgadget.id),
            'name': self.mgadget.name,
            'desc': self.mgadget.desc,
            'ruby': self.mgadget.ruby,
        }
