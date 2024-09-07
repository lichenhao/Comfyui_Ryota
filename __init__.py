from .nodes import RNTexts,SwitchInput
from .utils.Store import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS

WEB_DIRECTORY="./web"

MANIFEST ={
    "name": "Ryota's Nodes",
    "version":(1,0,1),
    "author": "Ryota",
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS',"WEB_DIRECTORY"]