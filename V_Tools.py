import bpy

def v_orgin(context): 
    try: 
        bpy.ops.view3d.snap_cursor_to_selected() 
        bpy.ops.object.editmode_toggle() 
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR') 
    except: print('Select Editmode first')

class addCubeSample(bpy.types.Operator): 
    bl_idname = 'mesh.add_cube_sample' 
    bl_label = 'Set Orgin' 
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        v_orgin(context)
        return {'FINISHED'}

class EXAMPLE_PT_panel(bpy.types.Panel):
    bl_label = "V_Tools" #    bl_label = "My own addon"
    bl_category ="V_Tools" #"Name of your tab"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):
        layout = self.layout

#        layout.label(text="Edge")
#        layout.operator("mesh.split_normals",text="Hard")
#        layout.operator("mesh.merge_normals",text="Soft")
        
        layout.label(text="Orgin")
        layout.operator("mesh.add_cube_sample")
        
        #row
        layout.label(text="Normals")
        row = layout.row()
        row.operator("mesh.split_normals",text="Hard")
        row.operator("mesh.merge_normals",text="Soft")
        
        layout.label(text="Loops")
        row = layout.row()
        row.operator("mesh.set_edge_flow",text="Flow")

classes = (EXAMPLE_PT_panel,addCubeSample)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()