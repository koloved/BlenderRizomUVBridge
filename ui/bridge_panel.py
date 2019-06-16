# <pep8-80 compliant>

"""RizomUV Bridge user-interface."""

import bpy
import os
import tempfile


class RizomUVPanel(bpy.types.Panel):
    """Main UI panel"""

    bl_idname = "PANEL_PT_RizomUVBridge"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "RizomUV"
    bl_context = "objectmode"
    bl_label = "Standard Bridge"

    def draw(self, context):
        """Draw the UI."""

        temp_file = tempfile.gettempdir() + os.sep + "rizom_temp.fbx"

        props = context.window_manager.RizomUVPanelProperties
        sel = bpy.context.active_object

        layout = self.layout

        # Import/Export
        box = layout.box()
        row = box.row(align=True)
        row.label(text="UV Operations:", icon='FILE')

        row = box.row(align=True)
        row.scale_y = 1.25
        if not os.path.exists(temp_file) or props.auto_uv is True:
            row.enabled = False
        row.operator("ruv.rizom_edit", text="Edit")

        row = box.row(align=True)
        row.scale_y = 1.25
        if not sel:
            row.enabled = False
        if props.auto_uv is True:
            export = "Export (Auto UV)"
        else:
            export = "Export"
        row.operator("ruv.rizom_export", text=export)

        row = box.row(align=True)
        row.scale_y = 1.25
        if not sel:
            row.enabled = False
        row.operator("ruv.rizom_import", text="Import")

        # Export Settings
        box = layout.box()
        row = box.row(align=True)
        row.label(text="Export Settings:")

        row = box.row(align=True)
        row.scale_y = 1.25
        row.prop(props, "script_run")

        row = box.row(align=True)
        row.scale_y = 1.25
        if props.script_run == 'NO_SCRIPT':
            row.enabled = False
        row.prop(props, "auto_uv")

        ###

        # Import Settings
        box = layout.box()
        row = box.row(align=True)
        row.label(text="Import Settings:")

        row = box.row(align=True)
        row.scale_y = 1.25
        row.prop(props, "seams")


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

        props = context.window_manager.RizomUVPanelProperties

        layout = self.layout
        box = layout.box()

        row = box.row(align=True)
        row.label(text="Viewport:", icon='SETTINGS')

        row = box.row(align=True)
        row.scale_y = 1.25
        row.prop(props, "image_path")

        ###

        layout = self.layout
        box = layout.box()

        row = box.row(align=True)
        row.label(text="Layout:", icon='SETTINGS')

        row = box.row(align=True)
        row.scale_y = 1.25
        row.prop(props, "shell_pad")

        row = box.row(align=True)
        row.scale_y = 1.25
        row.prop(props, "map_res")

        ###

        box = layout.box()
        row = box.row(align=True)
        row.label(text="Packing:", icon='SETTINGS')
        row = box.row(align=True)
        row.scale_y = 1.25
        row.prop(props, "pack_qual")
        row.prop(props, "mutations")
        row = box.row(align=True)
        row.scale_y = 1.25
        row.prop(props, "init_orient")
        row = box.row(align=True)
        row.scale_y = 1.25
        row.prop(props, "orient_step")


class RizomUVPanelProperties(bpy.types.PropertyGroup):
    """Properties that can be changed in panel"""

    # Export settings
    script_run_des = "Run a LUA script when Rizom launches."
    script_run: bpy.props.EnumProperty(
        name="Script", default='SHARP_EDGES', items=(
            ('NO_SCRIPT', "No Script",
             "Exports current UV layout in its present condition."),
            ('PELT', "Autoseams: Pelt",
             "Performs a quick auto unwrap using the pelt algorithm."),
            ('MOSAIC', "Autoseams: Mosaic",
             "Performs a quick auto unwrap using the mosaic algorithm."),
            ('SHARP_EDGES', "Autoseams: Sharp Edges",
             "Performs a quick auto unwrap using the sharp edges algorithm."),
            ('BOX', "Autoseams: Box",
             "Performs a quick auto unwrap using the box algorithm.")
        ), description=script_run_des
    )

    auto_uv_des = "Create an automatic uv map and return to blender"
    auto_uv: bpy.props.BoolProperty(name="Auto UV", default=False,
                                    description=auto_uv_des)

    # Import settings
    seams_des = ("Creates seams and sharp edges from UV"
                 " island boundaries after importing")
    seams: bpy.props.BoolProperty(name="Mark Seams", description=seams_des,
                                  default=True)

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
    orient_step: bpy.props.IntProperty(name="Step Angle", default=45,
                                       min=0, max=180, subtype='ANGLE',
                                       description=orient_step_des)

    mutations_des = ("Maximum number of trials to find best packing solution")
    mutations: bpy.props.IntProperty(name="Mutations", default=1,
                                     max=1000, min=0,
                                     description=mutations_des)

    pack_qual_des = "Resolution of the packing algorithm"
    pack_qual: bpy.props.IntProperty(name="Quality", default=200, max=1000,
                                     min=0, description=pack_qual_des)
