# <pep8-80 compliant>

"""__init__"""

import bpy

from .preferences import RizomUVBridgeAddonPreferences
from .operators.manual_bridge import ExportToRizom, ImportFromRizom
from .ui.bridge_panel import RizomUVPanel, RizomUVSettingsPanel,\
    RizomUVPanelProperties

bl_info = {  # pylint: disable=invalid-name
    "name": "RizomUV Bridge",
    "description": "Streamlined workflow between Blender and RizomUV.",
    "author": "MattA",
    "version": (1, 0, 0),
    "blender": (2, 80, 0),
    "category": "UV"
}


def register():
    """register operators and menus"""

    for cls in (
            RizomUVBridgeAddonPreferences,
            ExportToRizom,
            ImportFromRizom,
            RizomUVPanelProperties,
            RizomUVPanel,
            RizomUVSettingsPanel
    ):
        bpy.utils.register_class(cls)

    bpy.types.WindowManager.RizomUVPanelProperties = bpy.props.PointerProperty(
        type=RizomUVPanelProperties)


def unregister():
    """unregister operators and menus"""

    del bpy.types.WindowManager.RizomUVPanelProperties

    for cls in (
            RizomUVBridgeAddonPreferences,
            ExportToRizom,
            ImportFromRizom,
            RizomUVPanelProperties,
            RizomUVPanel,
            RizomUVSettingsPanel
    ):
        bpy.utils.unregister_class(cls)
