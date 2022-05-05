from dataclasses import dataclass
from ..exceptions import ValidationError
from .base_request import BaseRequest


@dataclass
class CreateMGadgetRequest(BaseRequest):
    name: str
    desc: str
    ruby: str
    
    def __post__init__(self):
        if not self.name:
            raise ValidationError('gadget name is required.')
        
        if not self.desc:
            raise ValidationError('gadget name is required.')
        
        if not self.ruby:
            raise ValidationError('gadget name is required.')