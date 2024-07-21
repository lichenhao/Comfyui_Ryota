from ..utils.Register import RegisterNode
from ..utils.Utils import pil2tensor
from PIL import Image,ImageFont,ImageDraw,ImageColor
import matplotlib.font_manager as fm
import logging
import os
# import textwrap

font_cache ={}
font_names = []

def get_system_fonts():
    fonts = fm.findSystemFonts(fontpaths=None, fontext='ttf') 

    for font in fonts:
        fp = fm.FontProperties(fname=font)
        font_name = f"{fp.get_family()} | {fp.get_style()} | {fp.get_name()} | {fp.get_weight()}"

        font_names.append(font_name)
        font_path = font_cache[font_name] = font
        logging.debug(f"get font {font_name} from {font_path}")

get_system_fonts()

@RegisterNode("RN Texts", )
class CombineTexts:
    
    RETURN_TYPES=("STRING",)

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "text1":("STRING", {"default": "","multiline": False,}),
                "text2":("STRING", {"default": "", "multiline": False,}),
                "seperator":("STRING",{"default":",","multiline":False,},),
            },
        }

    
    @classmethod
    def execute(self, text1:str, text2:str, seperator:str, ) -> str:

        t3 = []
        t3.extend(text1.split(seperator))
        t3.extend(text2.split(seperator))

        return (str.join(seperator, list(set(t3))),)
 

@RegisterNode("RN Texts")
class FontLoader:

    RETURN_TYPES=("STRING",)

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "mode":(["System", "Local"], {"default":"System"}),
                "font_name":(font_names, {"default":font_names[0], "multiline": False,}),
                # "local_name":(["n"],{"default": "", "multiline":False,}),
            },
        }
    

    @classmethod
    def execute(self, mode:str, font_name:str,) -> str:
        fpath = font_cache[font_name]
        logging.debug(f"get font path {fpath}")
        if (fpath is None):
            return Exception(f"RNText:Get font path by name`{font_name}` with mode `{mode}` failed")
        return {"ui":{"text": fpath}, "result":(fpath,)}


@RegisterNode("RN Texts")
class DrawText:

    RETURN_TYPES=("IMAGE",)

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "font":("STRING", {"default":"","forceInput":True,}),
                "text":("STRING", {"default":"", "multiline":True,}),
                "size":("INT", {"default": 12, "step": 1,}),
                "align":(["left","right","center"], {"default":"left"}),
                "color":("STRING", {"default":"#FFFFFF"}),
                "alpha":("INT", {"default": 255, "min": 0, "max": 255}),
                "space":("INT", {"default": 5, "min": 0}),
            
            },
        }
    
    @classmethod
    def execute(self, font:str, text:str, size:int, align:str, color:str, alpha:int, space:int):
        logging.debug(f"get font path `{font}`")
        
        if(os.path.exists(font) is False):
            return Exception(f"RNText:font file is not found {font}")
        font = ImageFont.truetype(font, size)

        left,top,width,height = font.getbbox(text)

        cvs = Image.new('RGBA', (width,height), color = (0,0,0,0))
        ctx = ImageDraw.Draw(cvs)

        ctx.text((0,0), text, fill = ImageColor.getcolor(color, 'RGB'), font = font, align=align, spacing=space,)

        cvs.putalpha(alpha=alpha)
        out = pil2tensor(cvs)

        return (out,)
