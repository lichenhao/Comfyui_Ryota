import matplotlib.font_manager as fm
from PIL import ImageFont,Image,ImageDraw,ImageColor


font_cache ={}
font_names = []

def get_system_fonts():
    fonts = fm.findSystemFonts(fontpaths=None, fontext='ttf') 

    for font in fonts:
        font_name = fm.FontProperties(fname=font).get_name()
        font_names.append(font_name)
        font_cache[font_name] = font

get_system_fonts()


def draw(fname:str, text:str, fsize:int, fcolor:str, bcolor:str):

    font = ImageFont.truetype(font_cache[fname], fsize)

    left,top,width,height = font.getbbox(text)
    
    cvs = Image.new('RGBA', (width, height), color=ImageColor.getcolor(bcolor, 'RGBA'))
    draw = ImageDraw.Draw(cvs)

    draw.text((left, top), text, fill = ImageColor.getcolor(fcolor, "RGB"), font=font)
    
    cvs.save("demo.png")


draw(font_names[0],  "Hello world!!", 12, "#FFFFFF", "#00000000")


