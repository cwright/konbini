import bpy

def cube(x=0,y=0,z=0,rotx=0,roty=0,rotz=0,scale=1, name="Cube"):
    bpy.ops.mesh.primitive_cube_add(location=(x,y,z), rotation=(rotx,roty,rotz))
    bpy.context.active_object.name = name

def circle(x=0,y=0,z=0,rotx=0,roty=0,rotz=0,width=1,height=1, name="Circle"):
    bpy.ops.mesh.primitive_circle_add(location=(x,y,z), rotation=(rotx,roty,rotz))
    bpy.context.active_object.name = name

def rect(x=0,y=0,z=0,rotx=0,roty=0,rotz=0,width=1,height=1,name="Plane"):
    bpy.ops.mesh.primitive_plane_add(location=(x,y,z), rotation=(rotx,roty,rotz))
    bpy.context.active_object.scale = [width,height,1]
    bpy.context.active_object.name = name

def text(text="konbini!",x=0,y=0,z=0,rotx=0,roty=0,rotz=0,size=1,character_spacing=1,line_spacing=1,name="Text"):
    bpy.ops.object.text_add(enter_editmode=True, location=(x,y,z), rotation=(rotx,roty,rotz))
    bpy.ops.font.delete()
    bpy.ops.font.text_insert(text=text)
    bpy.ops.object.editmode_toggle()
    bpy.context.object.data.space_character = character_spacing
    bpy.context.object.data.space_line = line_spacing
    

#standard setup. cam on top so x and z behave like you would expect 
bpy.data.objects["Camera"].location = (0,0,10)
bpy.data.objects["Camera"].rotation_euler = [0,0,0]
bpy.ops.object.select_pattern(pattern="Cube")
bpy.ops.object.delete()



#cube()
#text("bar",0,2,character_spacing = 3)
