from .Store import NODE_CLASS_MAPPINGS,NODE_DISPLAY_NAME_MAPPINGS
from ..utils.Utils import Camelcase2Split#ReverseTuples,SafeComfyName

def RegisterNode(c:str = None, isOutNode:bool = False):

    def decorator(cls:object):
        name = cls.__name__            
        showName = Camelcase2Split(name)

        if (c != None):
            cls.CATEGORY =f"Ryota's Nodes/{c}"
        else:
            cls.CATEGORY =f"Ryota's Nodes"
        cls.FUNCTION = "execute"
        cls.OUTPUT_NODE = isOutNode
        
        NODE_CLASS_MAPPINGS[name]=cls
        NODE_DISPLAY_NAME_MAPPINGS[name]= showName
        print(f"Class {name} register to {cls.CATEGORY}/{showName} success")
    return decorator
