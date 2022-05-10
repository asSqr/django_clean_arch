from dataclasses import dataclass
from .base_response import BaseResponse
from gadget_app.models import MGadgetModel
from gadget_app.utils import mgadget_serialize
from typing import List, Dict, Any


@dataclass
class ListMGadgetResponse(BaseResponse):
    mgadgets: List[MGadgetModel]

    def to_json(self) -> Dict[str, Any]:
        return {
            'datas': [mgadget_serialize(mgadget) for mgadget in self.mgadgets]
        }
