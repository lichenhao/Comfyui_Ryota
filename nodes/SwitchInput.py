from ..utils.Register import RegisterNode
from ..utils.Utils import any

CATEGORY_NAME="Switch Inputs"

@RegisterNode(CATEGORY_NAME,returns=("CLIP","MODEL",))
class SwitchModelClip:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "MODEL":("MODEL",),
                "CLIP":("CLIP",),
            }
        }

    @classmethod
    def execute(self, MODEL, CLIP, ):
        return (CLIP,MODEL,)


@RegisterNode(CATEGORY_NAME, returns=(any,any,))
class SwitchAnyInputs:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "value1":(any,),
                "value2":(any,),
            }
        }
    
    @classmethod
    def execute(self, value1, value2, ):
        return (value2, value1, )


@RegisterNode("Reroute Inputs", returns=(any,any,))
class Reroute2:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "value1":(any,),
                "value2":(any,),
            }
        }

    @classmethod
    def execute(self, value1, value2,):
        return (value1,value2,)
    

@RegisterNode("Reroute Inputs", returns=(any,any,any,))
class Reroute3:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "value1":(any,),
                "value2":(any,),
                "value3":(any,),
            }
        }
    @classmethod
    def execute(self, value1, value2, value3,):
        return (value1,value2,value3,)
    

    
