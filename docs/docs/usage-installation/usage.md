---
layout: default
title: Using The Bridge
parent: Usage & Installation
nav_order: 2
---
# Usage
{: .no_toc }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Panel Location

The RizomUV Bridge panel can be found in the 3D View Sidebar, the hotkey for the default "Blender" keymap to show the sidebar is **N**.

**Info:** The panel is only enabled in object mode.
{: .notice .notice-info}

---

---

## File Operations

### Exporting

Select one or more objects and click the **Export** button, RizomUV will open with your objects loaded and run a auto UV script (if you selected one).

#### Startup Script

These are scripts that will be automatically run when RizomUV opens, they automatically place seams and pack a quick UV map. This provides a good base to begin creating your final UV map.

**Warning:** Your UV map names must contain alphabetical and numerical characters only.
{: .notice .notice-warning}

**Warning:** Each object needs to have the same UV maps. For example, if the first object has two UV maps; map1 and map2, every object you are exporting should have those maps.
{: .notice .notice-warning}
---

### Importing

Select your objects and click the **Import** button, each UV set on your original objects will be updated.

**Warning:** The script uses name matching to transfer the UV maps so it is important that you do not change the names of your original objects between operations.
{: .notice .notice-warning}

---

### Texture Image Export

This field allows you to select a texture map that you can see in the RizomUV viewport and grid background. Once RizomUV opens you need to set your shading mode to **Viewport Texture Custom**, your texture will then be vvisible.

**Warning:** The file format must be one of: .tiff, .png, .jpg, .tga or .bmp
{: .notice .notice-warning}

---

---

## RizomUV Settings

This section of the UI allows you to choose some of the settings RizomUV loads up with, the settings are fairly self explanatory and have tooltips if you need them.
