from gadget_app.models import MGadgetModel
from typing import Dict, Any


def mgadget_serialize(mgadget: MGadgetModel) -> Dict[str, Any]:
    return {
        'id': str(mgadget.id),
        'name': mgadget.name,
        'desc': mgadget.desc,
        'ruby': mgadget.ruby,
    }
