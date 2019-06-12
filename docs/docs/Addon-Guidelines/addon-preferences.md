---
layout: default
title: Addon Preferences
parent: Addon Guidelines
nav_order: 3
---
# Addon Preferences
{: .no_toc }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Preferences

Addon preferences are properties that are set from the Add-ons tab, a common example is setting a directory path that is used in the addon. These preferences are saved along with other Blender preferences so they do not need to be re-entered by the user after a restart.

---

## Registering Preferences

Addon preferences are set in a class inheriting from `bpy.types.AddonPreferences`, the preferences are defined in the same manor as operator properties using `bpy.props`. The Add-ons menu UI for setting these preferences should also be defined within this class.

```python
class ExampleAddonPreferences(bpy.types.AddonPreferences):
    """Addon user settings"""

    bl_idname = "example_addon"
    
    save_dir: bpy.props.StringProperty(
    name="Save Directory", subtype='DIR_PATH')
    
    def draw(self, context):  # pylint: disable=unused-argument
        """Draw UI"""
    
        layout = self.layout
    
        row = layout.row()
        row.scale_y = 1.25
        row.prop(self, "save_dir")        

def register():
    bpy.utils.register_class(ExampleAddonPreferences)

def unregister():
    bpy.utils.unregister_class(ExampleAddonPreferences)

if __name__ == "__main__":
    register()
```

---

### Breakdown
`bl_idname:` This must be identical to the name of your addon, so either the name of the .py file or the name of the base folder if your addon is a package.

The UI will be drawn under the checkox to enable your addon in the Add-ons menu, this is where the user will be able to edit the preferences.

The preferences class is registered just like any other and can also be registered inside the `__init__.py` file if your addon has one.

---

## Accessing Addon Preferences

Addon preferences can be accessed through bpy.context.preferences.addons["addon_bl_idname"].preferences.

```python
def save_file_path():
	"""Get the path to save the file"""
	
	prefs = bpy.context.preferences.addons["example_addon"].preferences
	save_path = prefs.save_dir + "\test_file.fbx"
```
**IMPORTANT:** `bpy.context.preferences.addons["example_addon"].preferences` has to be used inside a function or method, it cannot be used directly under a class.