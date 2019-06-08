# <pep8-80 compliant>

"""RizomUV Bridge user-interface."""

import bpy


class RizomUVPanel(bpy.types.Panel):
    """Main UI panel"""

    bl_idname = "PANEL_PT_RizomUVBridge"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "RizomUV"
    bl_context = "objectmode"
    bl_label = "RizomUV Bridge"

    def draw(self, context):
        """Draw the UI."""

        win_manager = context.window_manager
        sel = bpy.context.active_object

        layout = self.layout
        box = layout.box()

        row = box.row(align=True)
        row.label(text="Startup Script:", icon='SCRIPT')
        row = box.row(align=True)
        row.scale_y = 1.25
        row.prop(win_manager.RizomUVPanelProperties, "script_run")

        box = layout.box()

        row = box.row(align=True)
        row.label(text="File Operations:", icon='FILE')

        row = box.row(align=True)
        row.scale_y = 1.25
        if not sel:
            row.enabled = False
        row.operator("ma.rizom_export", text="Export")

        row = box.row(align=True)
        row.scale_y = 1.25
        if not sel:
            row.enabled = False
        row.operator("ma.rizom_import", text="Import")

        row = box.row(align=True)
        row.scale_y = 1.25
        row.prop(win_manager.RizomUVPanelProperties, "image_path")


class RizomUVSettingsPanel(bpy.types.Panel):
    """Settings panel"""

    bl_idname = "PANEL_PT_RizomUVSettings"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "RizomUV"
    bl_context = "objectmode"
    bl_label = "RizomUV Settings"

    def draw(self, context):
        """Draw the UI."""

        win_manager = context.window_manager

        layout = self.layout
        box = layout.box()

        row = box.row(align=True)
        row.label(text="RizomUV Settings:", icon='SETTINGS')

        row = box.row(align=True)
        row.scale_y = 1.25
        row.prop(win_manager.RizomUVPanelProperties, "shell_pad")

        row = box.row(align=True)
        row.scale_y = 1.25
        row.prop(win_manager.RizomUVPanelProperties, "map_res")

        row = box.row(align=True)
        row.scale_y = 1.25
        row.prop(win_manager.RizomUVPanelProperties, "orient_step")

        row = box.row(align=True)
        row.scale_y = 1.25
        row.prop(win_manager.RizomUVPanelProperties, "init_orient")


class RizomUVPanelProperties(bpy.types.PropertyGroup):
    """Properties that can be changed in panel"""

    script_run_des = "Run a LUA script when Rizom launches"
    script_run: bpy.props.EnumProperty(
        name="", default='MOSAIC', items=(
            ('EDIT_UV', "No Script",
             "Exports current UV layout in its present condition."),
            ('SHARP_EDGES', "Sharp Edges Unwrap",
             "Performs a quick auto unwrap using the sharp edges algorithm."),
            ('MOSAIC', "Mosaic Unwrap",
             "Performs a quick auto unwrap using the mosaic algorithm.")
        ), description=script_run_des
    )

    # RizomUV settings
    shell_pad_des = "Pixel padding between each UV island"
    shell_pad: bpy.props.IntProperty(name="Island Padding", default=16, min=0,
                                     subtype='PIXEL', soft_max=32,
                                     description=shell_pad_des)

    map_res_des = "The horizontal resoultion of the texture map."
    map_res: bpy.props.IntProperty(name="Map Resolution", default=2048, min=0,
                                   subtype='PIXEL', description=map_res_des)

    image_path_des = "Texture to be loaded into RizomUV"
    image_path: bpy.props.StringProperty(name="", subtype='FILE_PATH',
                                         default="Texture Image (optional)",
                                         description=image_path_des)

    init_orient_des = "Pre-orient islands by bounding box before packing"
    init_orient: bpy.props.EnumProperty(
        name="", default='1', items=(
            ('0', "No Pre-Orientation",
             "Do not pre-orient islands."),
            ('1', "Horizontal Pre-Orientation",
             "Pre-orient islands horizontally."),
            ('2', "Vertical Pre-Orientation",
             "Pre-orient islands vertically.")
        ), description=init_orient_des
    )

    orient_step_des = "Step angle for finding best orientation while packing"
    orient_step: bpy.props.IntProperty(name="Step Angle", default=45, min=0,
                                       max=180, subtype='ANGLE')
