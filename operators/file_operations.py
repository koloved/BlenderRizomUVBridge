# <pep8-80 compliant>

"""Manual export and import to and from RizomUV."""

import os
import subprocess
import tempfile
import bpy
import rizomuv_bridge.ma_utils.utils as mutil
import rizomuv_bridge.ma_utils.lua_functions as lua

TEMP_PATH = tempfile.gettempdir() + os.sep + "rizom_temp.fbx"


class ExportToRizom(bpy.types.Operator):
    """Send the UVs to RizomUV."""

    bl_description = "Export objects to a temp file and open it in RizomUV"
    bl_idname = "ma.rizom_export"
    bl_label = "Export (RizomUV)"
    bl_options = {'REGISTER', 'INTERNAL'}

    @staticmethod
    def export_file(context):
        """Export the file."""

        act_obj = bpy.context.active_object
        sel_objs = mutil.get_sel_meshes()
        out_objs = []

        for obj in sel_objs:
            new_obj = obj.copy()
            new_obj.name = obj.name + "_rizom"
            bpy.context.scene.collection.objects.link(new_obj)
            out_objs.append(new_obj)

        bpy.ops.object.select_all(action='DESELECT')

        for obj in out_objs:
            bpy.data.objects[obj.name].select_set(True)

        bpy.ops.export_scene.fbx(
            filepath=TEMP_PATH, use_selection=True, global_scale=1.0,
            object_types={'MESH'}, use_mesh_edges=False, bake_anim=False,
            axis_forward='-Z', axis_up='Y'
        )

        bpy.ops.object.delete(use_global=False, confirm=False)

        for obj in sel_objs:
            bpy.data.objects[obj.name].select_set(True)

        context.view_layer.objects.active = act_obj

        script = lua.write_script()
        prefs = bpy.context.preferences.addons["rizomuv_bridge"].preferences
        exe = prefs.rizomuv_path

        subprocess.Popen([exe, TEMP_PATH, '-cfi' + script])

    def execute(self, context):  # pylint: disable=unused-argument
        """Operator execution code."""

        self.export_file(context)

        return {'FINISHED'}


class ImportFromRizom(bpy.types.Operator):
    """Get the UVs from RizomUV."""

    bl_description = "Import UVs from RizomUV"
    bl_idname = "ma.rizom_import"
    bl_label = "Import (RizomUV)"
    bl_options = {'REGISTER', 'UNDO', 'INTERNAL'}

    @staticmethod
    def import_file(context):
        """Import the file, transfer the UVs and delete imported objects."""

        act_obj = bpy.context.active_object
        sel_objs = mutil.get_sel_meshes()

        bpy.ops.import_scene.fbx(filepath=TEMP_PATH)

        bpy.ops.object.select_all(action='DESELECT')

        for obj in sel_objs:
            import_obj = bpy.data.objects[obj.name + "_rizom"]
            bpy.data.objects[obj.name].select_set(True)
            context.view_layer.objects.active = import_obj
            bpy.ops.object.join_uvs()
            bpy.ops.object.select_all(action='DESELECT')
            bpy.data.objects[obj.name + "_rizom"].select_set(True)
            bpy.ops.object.delete(use_global=False, confirm=False)

        for obj in sel_objs:
            bpy.data.objects[obj.name].select_set(True)

        context.view_layer.objects.active = act_obj

    def execute(self, context):
        """Operator execution code."""

        self.import_file(context)

        return {'FINISHED'}
