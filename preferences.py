"""Addon user preferences in addon menu"""

import bpy


class RizomUVBridgeAddonPreferences(bpy.types.AddonPreferences):
    """Addon user settings"""

    bl_idname = "rizomuv_bridge"

    rizomuv_path: bpy.props.StringProperty(
        name="Rizom Path", subtype='FILE_PATH',
        default=R"C:\Program Files\Rizom Lab\RizomUV VS RS 2018.0\rizomuv.exe")

    def draw(self, context):  # pylint: disable=unused-argument
        """Draw UI"""

        #props = bpy.context.preferences.addons["rizomuv_bridge"].preferences

        layout = self.layout

        row = layout.row()
        row.scale_y = 1.25
        row.prop(self, "rizomuv_path")
