#Long Ngu
#02/16/23
#Image Interface
#From users input of 2-Dimensional image of pixel and color to generate 3-Dimensional voxels.

#sources
#######################################################

#Math formula from Wolfram MathWorld#
#https://mathworld.wolfram.com/

#User Interface#
#https://developer.rhino3d.com/guides/rhinopython/eto-forms-python/

#Open Browser#
#https://discourse.mcneel.com/t/webbrowser-package-supported-on-macos/128401/11

#imports
#######################################################

##Import Rhino##
import rhinoscriptsyntax as rs
import Rhino
import Rhino.UI

##Import Bitmap##
import System.Drawing.Bitmap as Bitmap

##Import random##
import random

##Import script context#
from scriptcontext import escape_test
import scriptcontext

#Import system and url#
import System
import urllib
import shutil

##Import reload#
from imp import reload

##Import Eto##
import Eto.Drawing as drawing
import Eto.Forms as forms

##Import box tool##
from box_tool import center_box

##Import color tools##
import color_tools as ct
reload(ct)

##Import viewport tools##
import viewport_tools as vt
reload(vt)

##Import pixel transformation##
import pixel_transformation as pt
reload(pt)

##Import user interface##
import user_interface as ut
reload(ut)

##Giving object color##
def assign_material_color(object, color):
    rs.AddMaterialToObject(object)
    index = rs.ObjectMaterialIndex (object)
    rs.MaterialColor(index, color)

##Giving user instruction##
def instruction():
    dialog = ut.instruction_dialog();
    rc = dialog.ShowModal(Rhino.UI.RhinoEtoApp.MainWindow)

##Giving user instruction##
def instruction2():
    dialog = ut.instruction2_dialog();
    rc = dialog.ShowModal(Rhino.UI.RhinoEtoApp.MainWindow)

##Upload an image and select geometry##
def image_geometry():
    escape_test(True)
    
    instruction()
    
    #Open the browser to generate image.
    url = 'https://deepai.org/machine-learning-model/text2img'
    System.Diagnostics.Process.Start(url)
    
    instruction2()
    
    #Convert Ai image link to jpg.
    ai_url = rs.StringBox('Paste the link.')
    file_path = "test.jpg"
    urllib.urlretrieve(ai_url, file_path)
    
    img = Bitmap.FromFile(file_path)
    
    width = img.Width
    height = img.Height
    
    
    w_step = int(width/100)
    h_step = int(height/100)
    
    
    ##The script that will be using the dialog##
    dialog = ut.geometry_dialog();
    rc = dialog.ShowModal(Rhino.UI.RhinoEtoApp.MainWindow)
    if (rc):
        transform = dialog.get_t()
        dim_1 = int(dialog.get_d1())
        dim_2 = int(dialog.get_d2())
    
    """
    ##This creat the form from image##
    for i in range(0, width, w_step):
        x = i
        for j in range(0, height, h_step):
            y = j
            r, g, b, a = img.GetPixel(x, y)
            color= rs.CreateColor(r, g, b)
            location = (x, y, 0)
            rect = rs.AddRectangle(location, 10, 10)
            rectangle = rs.AddPlanarSrf(rect)
            assign_material_color(rectangle, color)
            rs.ObjectColor(rectangle, color)
            """
    ##This creat the form from image##
    for i in range(0, width, w_step):
        x = i
        for j in range(0, height, h_step):
            y = j
            r, g, b, a = img.GetPixel(x, y)
            
            if transform == 'Cone':
                x2, y2, z2 = pt.ai2_transform_pixel_z(r, g, b)
            if transform == 'Polar':
                x2, y2, z2 = pt.ai5_transform_pixel_z(r, g, b)
            if transform == 'Torus':
                x2, y2, z2 = pt.ai6_transform_pixel_z(r, g, b)
            if transform == 'Spherical':
                x2, y2, z2 = pt.ai4_transform_pixel_z(r, g, b)
            if transform == 'Radial':
                x2, y2, z2 = pt.ai3_transform_pixel_z(r, g, b)
            if transform == 'Octahedron':
                x2, y2, z2 = pt.octahedron_transform_pixel_z(r, g, b)
            if transform == 'Ai':
                x2, y2, z2 = pt.ai_transform_pixel_z(r, g, b)
                
            #creating a box
            color_2= rs.CreateColor(r, g, b)
            location_2 = (x2, y2, z2)
            size_box = random.uniform(dim_1,dim_2)
            box = center_box(location_2, size_box, size_box, size_box)
            assign_material_color(box, color_2)
            rs.ObjectColor(box, color_2)
            color= rs.CreateColor(r, g, b)
            location = (x, y, 0)
            rect = rs.AddRectangle(location, size_box, size_box)
            rectangle = rs.AddPlanarSrf(rect)
            assign_material_color(rectangle, color)
            rs.ObjectColor(rectangle, color)
            rs.DeleteObjects(rect)



##To start as blank or keep the previous object##
def clear_file():
    options_1 = ('Yes', 'No')
    if options_1:
        delete_1 = rs.ListBox(options_1, 'Would you like to delete all objects?')
        if delete_1 == "Yes":
            all_objects = rs.AllObjects()
            rs.DeleteObjects(all_objects)
        else:
            pass



##Allow user to save image or animtation##
def save_file():
    rs.EnableRedraw (True)
    view_port = "Port"
    dialog = ut.image_dialog();
    rc = dialog.ShowModal(Rhino.UI.RhinoEtoApp.MainWindow)
    print rc
    if (rc):
        rotate_right = int(dialog.get_rr())
        rotate_up = int(dialog.get_ru())
    vt.create_parallel_view(view_port, (800, 800))
    vt.set_axon_view (rotate_right, rotate_up, view_port)
    rs.ZoomExtents()
    vt.zoom_scale(.75, view_port)
    vt.set_display_mode (view_port, "Rendered")
    options_v = ('Yes', 'No')
    if options_v:
        like_view = rs.ListBox(options_v, 'Do you like the view?')
        if like_view == 'Yes':
            option_1 = ('Animation', 'Image', 'No')
            if option_1:
                save_1 = rs.ListBox(option_1, 'Would you like to save?')
                if save_1  == "Animation":
                    file_name = rs.StringBox('Please provide a file name.', None, 'File')
                    folder_name = file_name + " folder"
                    for i in range (30):
                        rs.Sleep(1)
                        vt.set_axon_view(1, 0, view_port)
                        animate_name = file_name + str("%04d"%i)
                        vt.capture_view(2, animate_name, folder_name)
                        
                elif save_1  == "Image":
                    file_name = rs.StringBox('Please provide a file name.', None, 'File')
                    folder_name = file_name + " folder"
                    vt.capture_view(2, file_name, folder_name)
                    options_again = ('Yes', 'No')
                    if options_again:
                        view_again = rs.ListBox(options_again, 'Would you like to save a different angle view?')
                        if view_again == 'Yes':
                            save_file()
                else:
                    pass
        if like_view == 'No':
            save_file()


#main
#######################################################
def main():
    
    rs.EnableRedraw(False)
    escape_test(True)
    clear_file()
    image_geometry()
    save_file()




#run program
#######################################################
main()


