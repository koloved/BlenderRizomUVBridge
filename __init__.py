# <pep8-80 compliant>

"""__init__"""

import bpy

from .preferences import RizomUVBridgeAddonPreferences
from .operators.manual_operations import ExportToRizom, ImportFromRizom
from .ui.bridge_panel import RizomUVPanel, RizomUVSettingsPanel,\
    RizomUVPanelProperties

bl_info = {  # pylint: disable=invalid-name
    "name": "RizomUV Bridge",
    "description": "Streamlined workflow between Blender and RizomUV.",
    "author": "MattA",
    "version": (0, 2, 1),
    "blender": (2, 80, 0),
    "location": "View3D > Sidebar",
    "wiki_url": "https://mattashpole.github.io/BlenderRizomUVBridge/",
    "tracker_url": "https://github.com/MattAshpole/BlenderRizomUVBridge/issues",
    "category": "UV"
}

CLASSES = [RizomUVBridgeAddonPreferences,
           ExportToRizom,
           ImportFromRizom,
           RizomUVPanelProperties,
           RizomUVPanel,
           RizomUVSettingsPanel]


def register():
    """register operators and menus"""

    for cls in CLASSES:
        bpy.utils.register_class(cls)

    bpy.types.WindowManager.RizomUVPanelProperties = bpy.props.PointerProperty(
        type=RizomUVPanelProperties)


def unregister():
    """unregister operators and menus"""

    del bpy.types.WindowManager.RizomUVPanelProperties

    for cls in CLASSES:
        bpy.utils.unregister_class(cls)
