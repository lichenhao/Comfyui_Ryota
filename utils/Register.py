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

# def RegisterSwitchNode(name:str, displayName:str, inputs:tuple):

#     @RegisterNode(name, displayName, "Switch Inputs")
#     class _:
#         RETURN_TYPES=ReverseTuples(inputs)
        
#         @classmethod        
#         def INPUT_TYPES(s):
#             types = {}
#             for input in inputs:
#                 types[SafeComfyName(input)]= (input,)
#             return {
#                 "required": types
#             }
#         @classmethod
#         def IS_CHANGED(s, *args):
#             return False
#         @classmethod        
#         def execute(s, *args):
#             return ReverseTuples(args)

# def RegisterSwitchNodeByTypesOnly(inputs:tuple):
#     displayName = f"Switch {' '.join(inputs).title()}"
#     name = displayName.replace(" ", "")
    
#     print(name, displayName)
#     return RegisterSwitchNode(name, displayName, inputs)