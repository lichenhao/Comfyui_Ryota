from ..utils.Register import RegisterNode

@RegisterNode("Batch Concat", )
class BatchTexts:

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "text1":("STRING", {"default": "","multiline": False,}),
                "text2":("STRING", {"default": "", "multiline": False,}),
                "seperator":("STRING",{"default":",","multiline":False,},),
            }
        }
    RETURN_TYPES=("STRING",)
    
    @classmethod
    def execute(self, text1:str, text2:str, seperator:str, ) -> str:

        t3 = []
        t3.extend(text1.split(seperator))
        t3.extend(text2.split(seperator))

        return (str.join(seperator, list(set(t3))),)
 
