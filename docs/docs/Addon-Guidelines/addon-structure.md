---
layout: default
title: Addon Structure
parent: Addon Guidelines
nav_order: 2
---
# Addon Structure
{: .no_toc }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## bl_info

The `bl_info` is a python dictionary that must be included at the top of your addon directly below the imports. If your addon is a python module instead of a single .py file it needs to go inside the `__init__.py` file.

```python
bl_info = {
    "name": "My Addon", 
    "description": "Single line explaining what this script exactly does.",
    "author": "Matt. A",
    "version": (1, 0, 0),
    "blender": (2, 80, 0),
    "location": "View3D > Add > Mesh",
    "warning": "Beta Version",
    "wiki_url": "http://wiki.myAddon.com"
    "tracker_url": "http://wiki.myAddon.com/bugs",
    "category": "Add Mesh"
    }
```

---

### Breakdown

- `"name"` : This is the name that will be displayed in the add-ons menu, it should be similar to the name of the module/.py file. <br>
- `"description"` : A brief description of what the addon does. <br>
- `"author"` : List the authors by contribution. <br>
- `"version"` : Version number of your addon. <br>
- `"blender"` : Blender version number that the addon is intended to work on. <br>
- `"location"` : Where the UI can be located within blender (if applicable). <br>
- `"warning"` : Optional, adds a warning to the addons panel. <br>
- `"wiki_url"` : Link to your addons documentation or website. <br>
- `"tracker_url"` : Link to your addons bug tracker, or wherever users can report issues. <br>
- `"category"` : Addon category. Don't add your own category if at all possible, use an existing one.

---

## Registering Addons

Before an addon can be used in Blender, each command and user interface needs to be assigned a method to register and unregister it.

```python
Class HelloWorld():

    def execute(self, context):
        
        text = "Hello World"
        print(text)

        return {'FINISHED'}

def register():
    bpy.utils.register_class(HelloWorld)

def unregister():
    bpy.utils.unregister_class(HelloWorld)

if __name__ == "__main__":
    register()
```
---

If your addon is a python module as opposed to a .py file you can register every command in the `__init__` file rather than repeating the same code in every file.


```python
import HelloWorld
import ExampleCommand2

def register():
    """register"""
    for cls in (
        HelloWorld,
        ExampleCommand2
    ):
        bpy.utils.register_class(cls)


def unregister():
    """unregister"""
    for cls in (
        HelloWorld,
        ExampleCommand2
    ):
        bpy.utils.unregister_class(cls)
```
---

# Python Module Hierarchy

For larger addons you can package multiple files into a python module, this can include as many folders and sub-folders as you need. The only requirement is an `__init__.py` file in the root directory of the addon.

I try to organise each different type of file into it's own folder, for example, operators would go into an operators folder, UI files into a UI folder, images into an image folder etc. 

<img src="{{site.baseurl}}/assets/images/folder_structure_diagram.png">