from django.db.models import CharField
from .base_model import BaseModel


class MGadgetModel(BaseModel):
    '''
    ドラえもんひみつ道具
    '''
    
    name = CharField(max_length=8192)
    ruby = CharField(max_length=8192)
    desc = CharField(max_length=8192)
