import rhinoscriptsyntax as rs
import color_tools as ct
import math
from imp import reload
from math import radians
from math import sin
from math import cos
from math import tan
from math import atan
from math import pi
from math import acos
from math import atan2
from math import exp
import pixel_transformation as pt
reload(pt)





def pink(r, g, b):
    if r >= 248 and g >= 127 and g <= 190 and b >= 180 and b <= 220:
        x2, y2, 0 = pt.ai_transform_pixel (r, g, b)
    else :
        x2, y2, z2 = pt.ai_transform_pixel(r, g, b)
    return x2, y2, z2
    
print pink()