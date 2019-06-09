# <pep8-80 compliant>

"""LUA Script functions for RizomUV operations."""

import tempfile
import os
import bpy

TEMP_PATH = tempfile.gettempdir() + os.sep + "rizom_temp.fbx"
TEMP_PATH = '/'.join(TEMP_PATH.split('\\'))


def script_paths(key):
    """Dictionary of LUA scripts

    returns:
        str: The Path of the specified script

    """

    bridge_path = os.path.abspath(os.path.dirname(__file__))\
        .replace("ma_utils", "lua_scripts\\")

    scripts_dic = {
        'EDIT_UV': bridge_path + "blank.lua",
        'SHARP_EDGES': bridge_path + "sharp_edge_algorithm.lua",
        'MOSAIC': bridge_path + "mosaic_algorithm.lua",
        'CONSTRUCT': bridge_path + "py_construct.lua"
    }

    script = scripts_dic[key]

    return script


def script_strings():
    """Strings used to construct LUA scripts.

    returns:
        list: A list of strings that can be used in LUA scripts

    """

    props = bpy.data.window_managers["WinMan"].RizomUVPanelProperties

    shell_padding = ("ZomIslandGroups({Mode='SetGroupsProperties',"
                     " WorkingSet='Visible', MergingPolicy=8322,"
                     " GroupPaths={ 'RootGroup' },"
                     " Properties={Pack={SpacingSize="
                     + str(props.shell_pad/props.map_res) + "}}})")

    tile_padding = ("ZomIslandGroups({Mode='SetGroupsProperties',"
                    " WorkingSet='Visible', MergingPolicy=8322,"
                    " GroupPaths={ 'RootGroup' },"
                    " Properties={Pack={MarginSize="
                    + str(props.shell_pad/props.map_res) + "}}})")

    map_res = ("ZomSet({Path='Prefs.PackOptions.MapResolution',"
               " Value=" + str(props.map_res) + "})")

    orient_step = ("ZomIslandGroups"
                   "({Mode='SetGroupsProperties', WorkingSet='Visible',"
                   " MergingPolicy=8322, GroupPaths={ 'RootGroup' },"
                   " Properties={Pack={Rotate={Step="
                   + str(props.orient_step) + "}}}})")

    preorient = ("ZomIslandGroups({Mode='SetGroupsProperties',"
                 " WorkingSet='Visible', MergingPolicy=8322, GroupPaths="
                 "{ 'RootGroup' }, Properties={Pack={Rotate={Mode="
                 + props.init_orient + "}}}})")

    image = ("ZomLoadUserTexture("'"' + props.image_path + '"'")")

    if image.lower().endswith((".tiff", ".png", ".jpg", ".tga", ".bmp")):
        image = '/'.join(image.split('\\'))

    else:
        image = ""

    return [shell_padding, tile_padding, map_res, orient_step, preorient,
            image]


def save_file():
    """Function to save the file as a precaution

    returns:
        str: LUA script to overwrite the imported fbx file

    """

    file_save = ("ZomSave({File={Path=" + '"' + TEMP_PATH + '"' + ","
                 "UVWProps=true, FBX={UseUVSetNames=true}},"
                 " __UpdateUIObjFileName=true})")

    return file_save


def write_script():
    """Construct the final lua script to be loaded on startup.

    returns:
        str: The Path of the resulting script

    """

    props = bpy.data.window_managers["WinMan"].RizomUVPanelProperties

    strings = script_strings()
    save = save_file()

    preset_script = script_paths(props.script_run)
    lua_preset = open(preset_script, "r")
    preset_content = lua_preset.read()
    lua_preset.close()

    final_script = script_paths('CONSTRUCT')
    lua_final = open(final_script, "w")
    lua_final.truncate(0)

    for string in strings:
        lua_final.write(" ".join([string]))

    lua_final.write(" ".join([preset_content, save]))

    lua_final.close()

    return final_script
