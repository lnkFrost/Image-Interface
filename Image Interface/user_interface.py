import rhinoscriptsyntax as rs
import scriptcontext
import Rhino.UI
import Eto.Drawing as drawing
import Eto.Forms as forms
import Eto
from scriptcontext import escape_test


##Instruction dialog class##
class instruction_dialog(forms.Dialog[bool]):
    
    escape_test(True)
    
    # Dialog box Class initializer
    
    def __init__(self):

        # Initialize dialog box
        self.Title = 'Instruction'
        self.Padding = drawing.Padding(10)
        self.Resizable = False
        
        
        
        # Create controls for the dialog
        self.s1_label = forms.Label(Text = '1. The script would open an ai in the browser.')
        self.s2_label = forms.Label(Text = '2. Create an image through the ai text to image.')
        # Create the default button
        self.DefaultButton = forms.Button(Text = 'OK')
        self.DefaultButton.Click += self.on_ok_button_click
        
        
        
        
        
        
        # Create a table layout and add all the controls
        
        layout = forms.DynamicLayout()
        layout.Spacing = drawing.Size(5, 5)
        layout.AddRow('Please follow the steps:')
        layout.AddRow(self.s1_label)
        layout.AddRow(self.s2_label)
        layout.AddRow(self.DefaultButton)
        
        
        
        # Set the dialog content
        self.Content = layout
        
    
    
    # OK button click handler
    def on_ok_button_click(self, sender, e):
            self.Close(True)
    ## End of Dialog Class ##

##Instruction dialog class##
class instruction2_dialog(forms.Dialog[bool]):
    
    escape_test(True)
    
    # Dialog box Class initializer
    
    def __init__(self):

        # Initialize dialog box
        self.Title = 'Instruction'
        self.Padding = drawing.Padding(10)
        self.Resizable = False
        
        
        
        # Create controls for the dialog
        self.s3_label = forms.Label(Text = '3. Right click on the image.')
        self.s4_label = forms.Label(Text = '4. Select copy image link/address.')
        self.s5_label = forms.Label(Text = '5. Paste the link in the following pop-up window:')
        
        # Create the default button
        self.DefaultButton = forms.Button(Text = 'OK')
        self.DefaultButton.Click += self.on_ok_button_click
        
        
        
        
        
        
        # Create a table layout and add all the controls
        
        layout = forms.DynamicLayout()
        layout.Spacing = drawing.Size(5, 5)
        layout.AddRow('Please follow the steps:')
        layout.AddRow(self.s3_label)
        layout.AddRow(self.s4_label)
        layout.AddRow(self.s5_label)
        layout.AddRow(self.DefaultButton)
        
        
        
        # Set the dialog content
        self.Content = layout
        
    
    
    # OK button click handler
    def on_ok_button_click(self, sender, e):
            self.Close(True)
    ## End of Dialog Class ##

##Geometry dialog class##
class geometry_dialog(forms.Dialog[bool]):
    
    escape_test(True)
    
    # Dialog box Class initializer
    
    def __init__(self):

        # Initialize dialog box
        self.Title = 'Form'
        self.Padding = drawing.Padding(10)
        self.Resizable = False
        
        
        #Create Combobox
        self.t_label = forms.Label(Text = 'Transformation:')
        self.t_combobox = forms.ComboBox()
        self.t_combobox.DataStore = [None,'Cone', 'Polar', 'Torus', 'Spherical', 'Radial','Octahedron','Ai']
        
        self.t_combobox.SelectedIndex = 0
        
        # Create controls for the dialog
        self.d1_label = forms.Label(Text = 'Please enter a radius for the voxels (1-15):')
        self.d1_textbox = forms.TextBox(Text = None)
        self.d2_label = forms.Label(Text = 'Pleae enter a second radius for the voxels (1-15):')
        self.d2_textbox = forms.TextBox(Text = None)
        
        
        
        # Create the default button
        self.DefaultButton = forms.Button(Text = 'OK')
        self.DefaultButton.Click += self.on_ok_button_click
        
        
        
        # Create the abort button
        self.AbortButton = forms.Button(Text = 'Cancel')
        self.AbortButton.Click += self.on_close_button_click
        
        
        
        # Create a table layout and add all the controls
        
        layout = forms.DynamicLayout()
        layout.Spacing = drawing.Size(5, 5)
        layout.AddRow('Please provide the transformation and dimensions.:')
        layout.AddRow(self.t_label, self.t_combobox)
        layout.AddRow(self.d1_label, self.d1_textbox)
        layout.AddRow(self.d2_label, self.d2_textbox)
        layout.AddRow(self.DefaultButton, self.AbortButton)
        
        
        
        # Set the dialog content
        self.Content = layout
        
    
    # Start of the class functions
    # Get the value of the textbox
    
    def get_t(self):
        return self.t_combobox.Text
    
    def get_d1(self):
        return self.d1_textbox.Text
    
    def get_d2(self):
        return self.d2_textbox.Text
    
    
    # Close button click handler
    
    def on_close_button_click(self, sender, e):
        self.t_combobox.Text = ""
        self.Close(False)
        self.d1_textbox.Text = ""
        self.Close(False)
        self.d2_textbox.Text = ""
        self.Close(False)


    # OK button click handler
    def on_ok_button_click(self, sender, e):
        if self.t_combobox.Text == "":
            self.Close(False)
        elif self.d1_textbox.Text == "":
            self.Close(False)
        elif self.d2_textbox.Text == "":
            self.Close(False)
        else:
            self.Close(True)
    ## End of Dialog Class ##

##Image dialog class##
class image_dialog(forms.Dialog[bool]):
    
    escape_test(True)
    
    # Dialog box Class initializer
    
    def __init__(self):

        # Initialize dialog box
        self.Title = 'Image'
        self.Padding = drawing.Padding(10)
        self.Resizable = False
        
        
        # Create controls for the dialog
        self.rr_label = forms.Label(Text = 'Please provide a degree to rotate right and left:')
        self.rr_textbox = forms.TextBox(Text = None)
        self.ru_label = forms.Label(Text = 'Please provide a degree to rotate up and down:')
        self.ru_textbox = forms.TextBox(Text = None)
        
        
        
        # Create the default button
        self.DefaultButton = forms.Button(Text = 'OK')
        self.DefaultButton.Click += self.on_ok_button_click
        
        
        
        # Create the abort button
        self.AbortButton = forms.Button(Text = 'Cancel')
        self.AbortButton.Click += self.on_close_button_click
        
        
        
        # Create a table layout and add all the controls
        
        layout = forms.DynamicLayout()
        layout.Spacing = drawing.Size(5, 5)
        layout.AddRow('Please angle for view port.:')
        layout.AddRow(self.rr_label, self.rr_textbox)
        layout.AddRow(self.ru_label, self.ru_textbox)
        layout.AddRow(self.DefaultButton, self.AbortButton)
        
        
        
        # Set the dialog content
        self.Content = layout
        
    
    # Start of the class functions
    # Get the value of the textbox
    
    
    def get_rr(self):
        return self.rr_textbox.Text
    
    def get_ru(self):
        return self.ru_textbox.Text
    
    
    # Close button click handler
    
    def on_close_button_click(self, sender, e):
        self.rr_textbox.Text = ""
        self.Close(False)
        self.ru_textbox.Text = ""
        self.Close(False)


    # OK button click handler
    def on_ok_button_click(self, sender, e):
        if self.rr_textbox.Text == "":
            self.Close(False)
        elif self.ru_textbox.Text == "":
            self.Close(False)
        else:
            self.Close(True)
    ## End of Dialog Class ##
    


