import rhinoscriptsyntax as rs
import color_tools as ct
import math
from math import radians
from math import sin
from math import cos
from math import tan
from math import atan
from math import pi
from math import acos
from math import atan2
from math import exp

def radial_transform_pixel(r, g, b):
    h, s, v = ct.rgb_to_hsv(r, g, b)
    rad_angle = radians(h)
    x = cos(rad_angle)*s
    y = sin(rad_angle)*s
    z = v
    return x, y, z
    
def spherical_transform_pixel(r, g, b):
    h, s, v = ct.rgb_to_hsv(r, g, b)
    rad_angle_h = radians(h)
    rad_angle_v = radians(h/0.05)
    x = cos(rad_angle_h) * sin(rad_angle_v)*s
    y = sin(rad_angle_h) * sin(rad_angle_v)*s
    z = cos(rad_angle_v) * s
    return x, y, z

def torus_transform_pixel(r, g, b):
    h, s, v = ct.rgb_to_hsv(r, g, b)
    rad_angle_h = radians(h)
    rad_angle_v = radians (h/0.005)
    i = sin(rad_angle_v)
    j = cos(rad_angle_h)*s
    p = cos(rad_angle_v)
    k = sin (rad_angle_h)
    q = 2 + j
    x = q * p
    y = q * i 
    z = k * s
    return x, y, z

def polar_transform_pixel(r, g, b):
    h, s, v = ct.rgb_to_hsv(r, g, b)
    rad_angle = h*(pi/50)
    x = cos(rad_angle)*s
    y = sin(rad_angle)*s
    z = sin(rad_angle)*v
    point = (x, y, z)
    polar = rs.Polar(point, rad_angle, z)
    return polar
    
def cone_transform_pixel (r, g, b):
    h, s, v = ct.rgb_to_hsv(r, g, b)
    rad_angle_h = radians(h)
    i = v-0.5
    j = i/(v+0.01)
    p = j * s
    x = cos(rad_angle_h) * p
    y = sin(rad_angle_h) * p
    z = v
    return x, y, z


##When z is 0##
def ai_transform_pixel (r, g, b):
    h, s, v = ct.rgb_to_hsv(r, g, b)
    x1, y1, z1 = torus_transform_pixel(r, g, b)
    x2, y2, z2 = polar_transform_pixel(r, g, b)
    x = x1 + x2
    y = y1 + y2
    z = 0
    return x, y, z

def octahedron_transform_pixel(r, g, b):
    h, s, v = ct.rgb_to_hsv(r, g, b)
    x = math.sqrt(2) * s * (math.cos(math.radians(h)) - math.sin(math.radians(h)))
    y = math.sqrt(2) * s * (math.cos(math.radians(h)) + math.sin(math.radians(h)))
    z = 0
    return x, y, z

def ai2_transform_pixel(r, g, b):
    h, s, v = ct.rgb_to_hsv(r, g, b)
    x1, y1, z1 = torus_transform_pixel(r, g, b)
    x2, y2, z2 = cone_transform_pixel(r, g, b)
    x = x1 + x2
    y = y1 + y2
    z = 0 
    return x, y, z

def ai3_transform_pixel(r, g, b):
    h, s, v = ct.rgb_to_hsv(r, g, b)
    x1, y1, z1 = spherical_transform_pixel(r, g, b)
    x2, y2, z2 = octahedron_transform_pixel(r, g, b)
    x = x1 + x2
    y = y1 + y2
    z = 0
    return x, y, z

def ai4_transform_pixel(r, g, b):
    h, s, v = ct.rgb_to_hsv(r, g, b)
    x1, y1, z1 = radial_transform_pixel(r, g, b)
    x2, y2, z2 = octahedron_transform_pixel(r, g, b)
    x = x1 + x2
    y = y1 + y2
    z = 0
    return x, y, z

def ai5_transform_pixel(r, g, b):
    h, s, v = ct.rgb_to_hsv(r, g, b)
    x1, y1, z1 = polar_transform_pixel(r, g, b)
    x2, y2, z2 = octahedron_transform_pixel(r, g, b)
    x = x1 + x2
    y = y1 + y2
    z = 0
    return x, y, z

def ai6_transform_pixel(r, g, b):
    h, s, v = ct.rgb_to_hsv(r, g, b)
    x1, y1, z1 = torus_transform_pixel(r, g, b)
    x2, y2, z2 = torus_transform_pixel(r, g, b)
    x = x1 + x2
    y = y1 + y2
    z = 0
    return x, y, z



##There is a z value##
def octahedron_transform_pixel_z(r, g, b):
    h, s, v = ct.rgb_to_hsv(r, g, b)
    x = math.sqrt(2) * s * (math.cos(math.radians(h)) - math.sin(math.radians(h)))
    y = math.sqrt(2) * s * (math.cos(math.radians(h)) + math.sin(math.radians(h)))
    z = v - 0.5
    return x, y, z

def ai_transform_pixel_z(r, g, b):
    h, s, v = ct.rgb_to_hsv(r, g, b)
    x1, y1, z1 = torus_transform_pixel(r, g, b)
    x2, y2, z2 = polar_transform_pixel(r, g, b)
    x = x1 + x2
    y = y1 + y2
    z = z1 + z2 
    return x, y, z

def ai2_transform_pixel_z(r, g, b):
    h, s, v = ct.rgb_to_hsv(r, g, b)
    x1, y1, z1 = torus_transform_pixel(r, g, b)
    x2, y2, z2 = cone_transform_pixel(r, g, b)
    x = x1 + x2
    y = y1 + y2
    z = z1 + z2 
    return x, y, z

def ai3_transform_pixel_z(r, g, b):
    h, s, v = ct.rgb_to_hsv(r, g, b)
    x1, y1, z1 = spherical_transform_pixel(r, g, b)
    x2, y2, z2 = octahedron_transform_pixel(r, g, b)
    x = x1 + x2
    y = y1 + y2
    z = z1 + z2
    return x, y, z

def ai4_transform_pixel_z(r, g, b):
    h, s, v = ct.rgb_to_hsv(r, g, b)
    x1, y1, z1 = radial_transform_pixel(r, g, b)
    x2, y2, z2 = octahedron_transform_pixel(r, g, b)
    x = x1 + x2
    y = y1 + y2
    z = z1 + z2 
    return x, y, z
    
def ai5_transform_pixel_z(r, g, b):
    h, s, v = ct.rgb_to_hsv(r, g, b)
    x1, y1, z1 = polar_transform_pixel(r, g, b)
    x2, y2, z2 = octahedron_transform_pixel(r, g, b)
    x = x1 + x2
    y = y1 + y2
    z = z1 + z2 
    return x, y, z
    
def ai6_transform_pixel_z(r, g, b):
    h, s, v = ct.rgb_to_hsv(r, g, b)
    x1, y1, z1 = torus_transform_pixel(r, g, b)
    x2, y2, z2 = torus_transform_pixel(r, g, b)
    x = x1 + x2
    y = y1 + y2
    z = z1 + z2 
    return x, y, z

