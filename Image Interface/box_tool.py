#Long Ngu
#10/10/2022
#This program generate cube

import rhinoscriptsyntax as rs


def center_cube (center, radius):
    cx, cy, cz = center
    #print (cx, cy, cz)
    
    
   #lower points
    p1 = (cx - radius, cy - radius, cz - radius)
    p2 = (cx + radius, cy - radius, cz - radius)
    p3 = (cx + radius, cy + radius, cz - radius)
    p4 = (cx - radius, cy + radius, cz - radius)
    
    
       #upper points
    p5 = (cx - radius, cy - radius, cz + radius)
    p6 = (cx + radius, cy - radius, cz + radius)
    p7 = (cx + radius, cy + radius, cz + radius)
    p8 = (cx - radius, cy + radius, cz + radius)
    
    points = [p1, p2, p3, p4, p5, p6, p7, p8]
    box = rs.AddBox(points)
    return box
    #print(points)

def center_box (center, height, width, length):
    
    cx, cy, cz = center
    
    h = height/2 #z
    w = width/2 #x
    l = length/2 #y
    #print (cx, cy, cz)
    
    
   #lower points
    p1 = (cx - w, cy - l, cz - h)
    p2 = (cx + w, cy - l, cz - h)
    p3 = (cx + w, cy + l, cz - h)
    p4 = (cx - w, cy + l, cz - h)
    
    
       #upper points
    p5 = (cx - w, cy - l, cz + h)
    p6 = (cx + w, cy - l, cz + h)
    p7 = (cx + w, cy + l, cz + h)
    p8 = (cx - w, cy + l, cz + h)
    
    points = [p1, p2, p3, p4, p5, p6, p7, p8]
    box = rs.AddBox(points)
    return box
    #print(points)

#center_cube((0,0,10), 10)
#center_box ((0, 0, 0), 40, 60, 80)