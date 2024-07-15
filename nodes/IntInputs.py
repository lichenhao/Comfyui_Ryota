from ..utils.Register import RegisterNode

@RegisterNode("Inputs", )
class IntInputs:

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "int1":("INT", {"default": 0,"min": 0,"step":1}),
                "int2":("INT", {"default": 0, "min": 0,"step":1}),
            }
        }
    RETURN_TYPES=("INT","INT",)
    
    @classmethod
    def execute(self, int1:int, int2:int, ):
        return (int1,int2,)
 
