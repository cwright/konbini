import bpy
import inspect
from functools import wraps
from pprint import pprint
from console_python import replace_help
import console_python



def cube(x=0,y=0,z=0,rotx=0,roty=0,rotz=0,scale=1, name="Cube"):
    bpy.ops.mesh.primitive_cube_add(location=(x,y,z), rotation=(rotx,roty,rotz))
    bpy.context.active_object.name = name
    return bpy.context.active_object

def circle(x=0,y=0,z=0,rotx=0,roty=0,rotz=0,width=1,height=1, name="Circle"):
    bpy.ops.mesh.primitive_circle_add(location=(x,y,z), rotation=(rotx,roty,rotz))
    bpy.context.active_object.name = name
    return bpy.context.active_object

def rect(x=0,y=0,z=0,rotx=0,roty=0,rotz=0,width=1,height=1,name="Plane"):
    bpy.ops.mesh.primitive_plane_add(location=(x,y,z), rotation=(rotx,roty,rotz))
    bpy.context.active_object.scale = [width,height,1]
    bpy.context.active_object.name = name
    return bpy.context.active_object

def text(text="konbini!",x=0,y=0,z=0,rotx=0,roty=0,rotz=0,size=1,character_spacing=1,line_spacing=1,name="Text"):
    bpy.ops.object.text_add(enter_editmode=True, location=(x,y,z), rotation=(rotx,roty,rotz))
    bpy.ops.font.delete()
    bpy.ops.font.text_insert(text=text)
    bpy.ops.object.editmode_toggle()
    bpy.context.object.data.space_character = character_spacing
    bpy.context.object.data.space_line = line_spacing
    return bpy.context.active_object

def setup():
#standard setup. cam on top so x and y behave like you would expect 
    bpy.data.objects["Camera"].location = (0,0,10)
    bpy.data.objects["Camera"].rotation_euler = [0,0,0]
    bpy.ops.object.select_pattern(pattern="Cube")
    bpy.ops.object.delete()



@wraps(replace_help)
def custom_convenience(namspace):
    """Add custom convenience definitions."""
    replace_help(namspace)
    namspace["setup"]= setup
    namspace["rect"] = rect
    namspace["circle"] = circle
    namspace["cube"] = cube
    namspace["text"] = text
    

def register():
    console_python.replace_help = custom_convenience

def unregister():
    console_python.replace_help = replace_help
