from ..utils.Register import RegisterNode#, RegisterSwitchNode, RegisterSwitchNodeByTypesOnly
from ..utils.Utils import any

@RegisterNode("Switch Inputs",)
class SwitchModelClip:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "MODEL":("MODEL",),
                "CLIP":("CLIP",),
            }
        }
    RETURN_TYPES=("CLIP","MODEL",)
    
    @classmethod
    def execute(self, MODEL, CLIP, ):
        return (CLIP,MODEL,)


@RegisterNode("Switch Inputs",)
class SwitchAnyInputs:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "value1":(any,),
                "value2":(any,),
            }
        }
    RETURN_TYPES=(any,any,)
    
    @classmethod
    def execute(self, value1, value2, ):
        return (value2, value1, )


@RegisterNode("Reroute Inputs",)
class Reroute2:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "value1":(any,),
                "value2":(any,),
            }
        }
    RETURN_TYPES=(any,any,)
    @classmethod
    def execute(self, value1, value2,):
        return (value1,value2,)
    

@RegisterNode("Reroute Inputs",)
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
    RETURN_TYPES=(any,any,any,)
    @classmethod
    def execute(self, value1, value2, value3,):
        return (value1,value2,value3,)
    

    
