from .Store import NODE_CLASS_MAPPINGS,NODE_DISPLAY_NAME_MAPPINGS
from ..utils.Utils import Camelcase2Split#ReverseTuples,SafeComfyName

def RegisterNode(category:str = None, isOutNode:bool = False, returns:tuple = None):

    def decorator(cls:object):
        name = cls.__name__            
        showName = Camelcase2Split(name)

        if (category is not None):
            cls.CATEGORY =f"Ryota's Nodes/{category}"
        else:
            cls.CATEGORY =f"Ryota's Nodes"
        if (returns is not None):
            cls.RETURN_TYPES = returns
        
        cls.FUNCTION = "execute"
        cls.OUTPUT_NODE = isOutNode
        
        NODE_CLASS_MAPPINGS[name]=cls
        NODE_DISPLAY_NAME_MAPPINGS[name]= showName
        print(f"Class {name} register to {cls.CATEGORY}/{showName} success")
    return decorator
